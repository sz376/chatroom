import funtranslate_parser
import openweather_parser
import funtranslate_parser
import pokemon_parser


def chatbot(command):
    response = []

    if "!!about" in command:
        temp = "Welcome to Shuo's chat room. This chat was built as a project for CS490 using python and ReactJS. Shuo is my dad and I love him very much. Type !!help in the chat to see the commands you can use."
        response.append(temp)

    elif "!!help" in command:
        temp = "Type !!about to learn about me! Type !!translate followed by some text to translate text into Yoda speak! (eg !!translate I have a bad feeling about this.) Type !!pokemon followed by a pokemon's name to see the flavor text for that pokemon!(eg !!pokemon pikachu) Type !!weather followed by your city to get the temperature in your city. (eg !!weather Chicago)"
        response.append(temp)

    elif "!!translate" in command:
        text = command[11:]
        temp = funtranslate_parser.funtranslate(text)
        response.append(temp)

    elif "!!pokemon" in command:
        pokename = command[10:]
        temp = pokemon_parser.pokefacts(pokename)
        response.append(temp)

    elif "!!weather" in command:
        city = command[9:]
        temp = (
            "The current temperature in"
            + city
            + " is "
            + str(openweather_parser.temperature(city))
            + " degrees Celcius."
        )
        response.append(temp)

    elif "!!" in command:
        oops = command[2:]
        temp = (
            "Oops! "
            + oops
            + " is not a valid command! Type !!help to see a list of valid commands!"
        )
        response.append(temp)

    return response
