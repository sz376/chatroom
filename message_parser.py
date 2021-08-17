from validator_collection import validators, checkers
import requests

KEY_USER = "name"
KEY_PFP = "pfp"
KEY_LINK = "link"
KEY_IMAGE = "image"
KEY_MESSAGE = "message"


def checkUrl(path):
    return checkers.is_url(path)


def checkImage(path):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    if checkUrl(path):
        r = requests.head(path)
        if r.headers["content-type"] in image_formats:
            return True
    return False


def parsedata(data):
    res = {}
    res["name"] = data["user"]
    res["pfp"] = data["pfp"]
    res["link"] = ""
    res["image"] = "../static/placeholder.png"
    res["message"] = data["message"]

    if checkImage(data["message"]):
        res["image"] = data["message"]
        res["message"] = ""
        return res

    elif checkUrl(data["message"]):
        res["link"] = data["message"]
        res["message"] = ""
        return res

    else:
        return res


"""
data = {'user': 'LebronJames', 'pfp': 'https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png', 'link': '', 'image': 'https://www.bostonmagazine.com/wp-content/uploads/sites/2/2019/09/goat-hyde-park-t.jpg', 'message': ''}
print(parsedata(data))
"""
