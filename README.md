# chit chat

This is a chatroom deployed on heroku. There is a bot in residency that will take commands and return various information. Current commands include: !!about, !!help, !!translate, !!pokemon, !!weather. Type !!help in the chat to learn more.

# Setup
 1. Install your stuff!    
  a) `npm install`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `npm install -g webpack`    
  e) `npm install --save-dev webpack`    
  f) `npm install socket.io-client --save`    
  g) `pip install requests`
  h) `pip install validator-collection`
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install` :warning: :warning: :warning:    
2. If you already have psql set up, **SKIP THE REST OF THE STEPS AND JUST DO THE FOLLOWING COMMAND**:   
`sudo service postgresql start`    
  
### Getting PSQL to work with Python  
  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo /usr/local/bin/pip install --upgrade pip`  
3. Get psycopg2: `sudo /usr/local/bin/pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`    
  
### Setting up PSQL  
  
1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
    Enter yes to all prompts.    
2. Initialize PSQL database: `sudo service postgresql initdb`    
3. Start PSQL: `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER`    
    :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
5. Make a new database: `sudo -u postgres createdb $USER`    
        :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
6. Make sure your user shows up:    
    a) `psql`    
    b) `\du` look for ec2-user as a user    
    c) `\l` look for ec2-user as a database    
7. Make a new user:    
    a) `psql` (if you already quit out of psql)    
### REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.   
    b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!  
        `create user [some_username_here] superuser password '[some_unique_new_password_here]';`    
    c) `\q` to quit out of sql    
8. `cd` into `chatroom` and make a new file called `sql.env` and add `SQL_USER=` and `SQL_PASSWORD=` in it  
9. Fill in those values with the values you put in 7. b)  

### Set up DB  

0. `sudo service postgresql start` and `cd ~/environment/lect12 && python`  
1. In the python interactive shell, run:  
	`import models`  
	`models.db.create_all()`  
	`models.db.session.commit()`  

### Keys

1. Open the sql.env file.
2. Add the following:
```
DATABASE_URI='TODO'
USER='TODO'
OPEN_WEATHER_KEY='TODO'
```
3. Use your `SQL_USER` and `SQL_PASSWORD` to create your DATABASE_URI it should be formatted like this: 
```
DATABASE_URI='postgresql://{SQL_USER}:{SQL_PASSWORD}@localhost/postgres'
```
4. Create an account at [https://openweathermap.org/api](https://openweathermap.org/api) to create a free acount to obtain your "OPEN_WEATHER_KEY"
5. USER can just be your preferred screenname.
  
### Enabling read/write from SQLAlchemy  
There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!  
5. Run the code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)    

# Usage
There is currently no OAuth implemented so usernames are currently set to an input.<br>
Check out the heroku page at [https://fast-thicket-75469.herokuapp.com/](https://fast-thicket-75469.herokuapp.com/)

# Issues
One of the earliest issues with this project was figuring out how to create a table in psql. The issue was remedied by watching old lecture videos and realizing that I needed to start the python shell terminal in order to create the database. It goes to show that sometimes its better to follow along with your own code than to simply watch and forget. <br>
A second issue was figuring out how to match messages with the user that sent the message. I wanted a way for users to make a custom username for themselves and have it display along with their message. In the end the only thing I could do is try and follow the same logic as the messages themselves and fortunally it worked out well with trial and error using indexing techniques. <br>
A third issue was getting the bot text to output with a different style than a human user. Since the issue is so specific, theres no good documentation online pertaining to this. I literally had to guess what it might look like and just trial and errored my way to a solution. I feel like there might be a better way than just hardcoding my bot and and then scanning user list for its presence but for now it works. <br>
A fourth issue was working with an API, specifically the [PokeAPI](https://pokeapi.co/). The usage is to pull the flavor text for a user inputed pokemon but for some odd reason, there are odd random formatting characters in the json object, therefore it is difficult to return the data in a readable string. I tried all the classic methods such as .replace and .strip but none of it worked. In the end, the only way that worked for me is to take each individual character and parse them to make sure there is no formatting characters and then append it to a new string. <br>
The last major issue was figuring out why PSQL was giving me an error, specifically a "peer authentication failed for user" error when I tried to push the database to heroku. This issue was fixed when I rewatched a lecture video that showed the pg_hba.conf in the repo root folder is not the one I need to edit inorder to get permission to push.<br>
A major issue with milestone two is a new user's data overriding a previous user's data. If given more time, I would restructure my client side Button.jsx file to fix this issue.
I had trouble understanding how to use mocking to test the SOCKETIO module and therefore was not able to produce any sort of mocked tests. In a way, I overestimated the difficulty of mocking based on the homework. If given more time, I would probably attend an office hour to ask about mocking.

# Improvements
The one obvious improvement would be to allow users to log into the chat room with OAuth. The next milestone will require this. The best method is to follow the lect12 video where Sresht goes over how to implement Google OAuth.<br>
Something I wanted to implement was the ability for users to upload an image into the chat. I believe it is possible to do this with socketio and writing the image file onto a dedicated folder in the server. I would need to use the fs library to do filewrite. However, I believe it would be easy to implement images if a user posts an image link in the chat. I would simply search for the ".jpg" extention in a message and simply alter the formatting display if I find it. <br>
~~The last thing I want to do to improve my code is moving some functions and methods into their own module. I think the readability of the code, especially the chat bot methods can be better suited if it was in their own file. I would simply copy and paste all the bot commands that I have already written into a method in a chatbox class and then call it when the server receives a new message from the client.~~ <br>
I think another improvement is allowing other users see when someone is typing in the chat window. I think a way to achieve this is by using the lodash library's debounce function, which will delay an action for a specified amount of time. For example, if a user is typing, it'll continually reset the delay. When the user stops typing, the delay runs out and triggers the action.. By adding an onChange handler on my message box, I should be able to implement a typing indicator. <br>

# Testing
I chose to test the chatbot client specifically because I feel as though API dependencies are the most susesible to unannounced change and errors. (such as when Google updated their JSON response format). I had trouble understanding how to use mocking to test the SOCKETIO module and therefore was not able to produce any sort of mocked tests. In a way, I overestimated the difficulty of mocking based on the homework. If given more time, I would probably attend an office hour to ask about mocking.
