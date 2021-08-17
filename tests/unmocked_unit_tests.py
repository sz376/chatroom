"""
    This file tests chatbot commands and the message parser.
"""

import unittest
from dotenv import load_dotenv
import os
from os.path import join, dirname
import sys

sys.path.insert(0, "/home/ec2-user/environment/project2-m3-sz376")
import chatbot_parser
import message_parser


KEY_INPUT = "input"
KEY_EXPECTED = "expected"
USER_INPUT = "user"
PFP_INPUT = "pfp"
LINK_INPUT = "link"
IMAGE_INPUT = "image"
MESSAGE_INPUT = "message"
EXPECTED_LINK = "expected link"
EXPECTED_IMAGE = "expected image"
EXPECTED_MESSAGE = "expected message"

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)


class MessageParserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                USER_INPUT: "LebronJames",
                PFP_INPUT: "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png",
                LINK_INPUT: "",
                IMAGE_INPUT: "",
                MESSAGE_INPUT: "https://www.bostonmagazine.com/wp-content/uploads/sites/2/2019/09/goat-hyde-park-t.jpg",
                EXPECTED_LINK: "",
                EXPECTED_IMAGE: "https://www.bostonmagazine.com/wp-content/uploads/sites/2/2019/09/goat-hyde-park-t.jpg",
                EXPECTED_MESSAGE: "",
            },
            {
                USER_INPUT: "MICHAEL_JORDAN",
                PFP_INPUT: "https://stats.nba.com/media/players/230x185/893.png",
                LINK_INPUT: "",
                IMAGE_INPUT: "",
                MESSAGE_INPUT: "https://clutchpoints.com/michael-jordan-is-still-the-goat-sorry-but-im-not-sorry-lebron-james/",
                EXPECTED_LINK: "https://clutchpoints.com/michael-jordan-is-still-the-goat-sorry-but-im-not-sorry-lebron-james/",
                EXPECTED_IMAGE: "../static/placeholder.png",
                EXPECTED_MESSAGE: "",
            },
            {
                USER_INPUT: "KB24",
                PFP_INPUT: "https://lanthorn.com/wp-content/uploads/2020/01/LAL_Bryant_Kobe-900x506.jpg",
                LINK_INPUT: "",
                IMAGE_INPUT: "",
                MESSAGE_INPUT: "MAMBA",
                EXPECTED_LINK: "",
                EXPECTED_IMAGE: "../static/placeholder.png",
                EXPECTED_MESSAGE: "MAMBA",
            },
        ]

    def test_get_chat_success(self):
        for test_case in self.success_test_params:
            test_data = {}
            test_data["user"] = test_case[USER_INPUT]
            test_data["pfp"] = test_case[PFP_INPUT]
            test_data["link"] = test_case[LINK_INPUT]
            test_data["image"] = test_case[IMAGE_INPUT]
            test_data["message"] = test_case[MESSAGE_INPUT]
            expectedlink = test_case[EXPECTED_LINK]
            expectedimage = test_case[EXPECTED_IMAGE]
            expectedmessage = test_case[EXPECTED_MESSAGE]
            parsed_data = message_parser.parsedata(test_data)
            self.assertEqual(parsed_data["link"], expectedlink)
            self.assertEqual(parsed_data["image"], expectedimage)
            self.assertEqual(parsed_data["message"], expectedmessage)


class ChatbotQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: "Welcome to Shuo's chat room. This chat was built as a project for CS490 using python and ReactJS. Shuo is my dad and I love him very much. Type !!help in the chat to see the commands you can use.",
            },
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: "Type !!about to learn about me! Type !!translate followed by some text to translate text into Yoda speak! (eg !!translate I have a bad feeling about this.) Type !!pokemon followed by a pokemon's name to see the flavor text for that pokemon!(eg !!pokemon pikachu) Type !!weather followed by your city to get the temperature in your city. (eg !!weather Chicago)",
            },
            {
                KEY_INPUT: "!!pokemon pikachu",
                KEY_EXPECTED: "When it smashes its opponents with its bolt- shaped tail, it delivers a surge of electricity equivalent to a lightning strike.",
            },
            {
                KEY_INPUT: "!!asdasd",
                KEY_EXPECTED: "Oops! asdasd is not a valid command! Type !!help to see a list of valid commands!",
            },
            {
                KEY_INPUT: "!!translate Hi, my name is John",
                KEY_EXPECTED: "Hi,John,  my name is",
            },
        ]

        self.fail_test_params = [
            {KEY_INPUT: "!!about", KEY_EXPECTED: ""},
            {KEY_INPUT: "!!help", KEY_EXPECTED: ""},
            {KEY_INPUT: "!!pokemon pikachu", KEY_EXPECTED: ""},
            {KEY_INPUT: "!!pokemon slowking", KEY_EXPECTED: ""},
            {KEY_INPUT: "!!weather chicago", KEY_EXPECTED: ""},
            {KEY_INPUT: "!!translate I love new york", KEY_EXPECTED: ""},
        ]

    def test_get_chat_success(self):
        for test_case in self.success_test_params:
            parsed_message = chatbot_parser.chatbot(test_case[KEY_INPUT])
            expected = test_case[KEY_EXPECTED]
            for line in parsed_message:
                self.assertEqual(line, expected)

    def test_get_chat_fail(self):
        for test_case in self.fail_test_params:
            parsed_message = chatbot_parser.chatbot(test_case[KEY_INPUT])
            expected = test_case[KEY_EXPECTED]
            for line in parsed_message:
                self.assertNotEqual(line, expected)


if __name__ == "__main__":
    unittest.main()
