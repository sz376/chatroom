# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models
import chatbot_parser
import message_parser

MESSAGES_RECEIVED_CHANNEL = "messages received"
USER_RECEIVED_CHANNEL = "user received"
current_users = 0

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

sql_user = os.environ["SQL_USER"]
sql_pwd = os.environ["SQL_PASSWORD"]
dbuser = os.environ["USER"]

database_uri = os.environ["DATABASE_URL"]

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.create_all()
db.session.commit()


def emit_all_messages(channel):

    all_users = [db_user.user for db_user in db.session.query(models.Chat).all()]

    all_messages = [
        db_message.message for db_message in db.session.query(models.Chat).all()
    ]

    all_pfp = [db_pfp.pfp for db_pfp in db.session.query(models.Chat).all()]

    all_links = [db_link.link for db_link in db.session.query(models.Chat).all()]

    all_images = [db_image.image for db_image in db.session.query(models.Chat).all()]

    global current_users

    socketio.emit(
        channel,
        {
            "allUsers": all_users,
            "allMessages": all_messages,
            "allPfp": all_pfp,
            "allLinks": all_links,
            "allImages": all_images,
            "currentUsers": current_users,
        },
    )


@socketio.on("new google user")
def on_new_google_user(data):
    print("Got an event for new google user input with data:", data)
    print(data["name"])
    print(data["email"])
    print(data["pfp"])
    print("sending " + data["name"] + " " + data["pfp"])
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    socketio.emit(USER_RECEIVED_CHANNEL, {"username": data["name"], "pfp": data["pfp"]})


@socketio.on("connect")
def on_connect():
    print("Someone connected!")
    global current_users
    current_users += 1
    socketio.emit("connected", {"test": "Connected"})
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@socketio.on("disconnect")
def on_disconnect():
    global current_users
    current_users -= 1
    print("Someone disconnected!")
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@socketio.on("new message input")
def on_new_address(data):
    print("Got an event for new message input with data:", data)
    parsed = message_parser.parsedata(data)
    db.session.add(
        models.Chat(
            parsed["name"],
            parsed["pfp"],
            parsed["message"],
            parsed["link"],
            parsed["image"],
        )
    )
    db.session.commit()
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    for line in chatbot_parser.chatbot(data["message"]):
        db.session.add(
            models.Chat(
                "zs-bot", "../static/zsbot.jpg", line, "", "../static/placeholder.png"
            )
        )
        db.session.commit()
        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)


@app.route("/")
def login():
    return flask.render_template("index.html")


if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
