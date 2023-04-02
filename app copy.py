# Ray
# Created By: 2023-04-01
# Description: 

import os
import sys
print("Python executable:", sys.executable)


import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # days = request.form["days"]
        location_from = request.form["travel_from"]
        location_to = request.form["travel_to"]
        # result1 = str(days) + location_from + "--" +location_to
        # print(result1)
        result1 = location_from + "--" +location_to
        print(result1)
        # print(animal)
        # print(type(animal))
        # prompt = generate_prompt(animal)
        # prompt = generate_prompt("New York", "Japan", 7, 5000, "excited")
        # print(prompt)
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt("New York", "New Jersey", 2, 3000, "excited"),
        #     temperature=0.6,
        #     max_tokens=300
        # )
        # print(response.choices[0].text)
        return redirect(url_for("index", result=result1))

    result = request.args.get("result")
    return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )

# Ray
# Created By: 2023-04-01
# Description: 
def generate_prompt(location_from, location_to, days, budget, theme = "relax"):
    """function for generating prompts for GPT

    Args:
        location_from (str): where user go to vacation
        location_to (str): destination, might be a country, or any certain places
        days (int): how long is the trip
        budget (int): budget for the trip
        theme (str, optional): the theme of the trip. Defaults to "relax".
    """
    input1 = "Give in the form of json file: \{'day': \{which day}, 'location': \{location from you}, 'what to do': \{what to do}, 'cost': \{cost details}}. Give me a 7 day plane from Los Angeles to China, with 5000 dollar budget, including the transportation, flight, hotel."
    output1 = """{
        "day1": {
            "location": "Los Angeles",
            "what to do": "Fly to Beijing",
            "cost": {
                "flight": 400,
                "activity": 100,
                "hotel": 0,
                "transportation": 50,
                "food": 50
            }
        },
        "day2": {
            "location": "Beijing",
            "what to do": "Explore the Summer Palace",
            "cost": {
                "flight": 0,
                "activity": 100,
                "hotel": 100,
                "transportation": 0,
                "food": 30
            }
        },
        "day3": {
            "location": "Beijing",
            "what to do": "Visit the Great Wall",
            "cost": {
                "flight": 0,
                "activity": 0,
                "hotel": 0,
                "transportation": 30,
                "food": 20
            }
        },
        "day4": {
            "location": "Beijing",
            "what to do": "Explore the Forbidden City",
            "cost": {
                "flight": 0,
                "activity": 0,
                "hotel": 0,
                "transportation": 20,
                "food": 30
            }
        },
        "day5": {
            "location": "Beijing",
            "what to do": "Visit the Temple of Heaven",
            "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 20
            }
        },
        "day6": {
            "location": "Beijing",
            "what to do": "Visit the Lama Temple",
            "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 0,
                "food": 20
            }
        },
        "day7": {
            "location": "Beijing",
            "what to do": "Fly back to Los Angeles",
            "cost": {
                "flight": 500,
                "activity": 0,
                "hotel": 0,
                "transportation": 50,
                "food": 50
            }
        }
    }

    """
    input2 = "Give in the form of json file: \{'day': \{which day}, 'location': \{location from you}, 'what to do': \{what to do}, 'cost': \{cost details}}. Give me a 5 day plane from New York to California, with 5000 dollar budget, including the transportation, flight, hotel."
    output2 = """{
    "day1": {
        "location": "New York",
        "what to do": "Fly to Los Angeles",
        "cost": {
            "flight": 300,
            "activity": 50,
            "hotel": 100,
            "transportation": 0,
            "food": 50
        }
    },
    "day2": {
        "location": "Los Angeles",
        "what to do": "Visit Santa Monica Beach and go for a relaxing walk on the pier",
        "cost": {
            "flight": 0,
            "activity": 0,
            "hotel": 100,
            "transportation": 0,
            "food": 50
        }
    },
    "day3": {
        "location": "Los Angeles",
        "what to do": "Spend a day exploring Griffith Park and the Griffith Observatory",
        "cost": {
            "flight": 0,
            "activity": 20,
            "hotel": 0,
            "transportation": 0,
            "food": 40
        }
    },
    "day4": {
        "location": "Los Angeles",
        "what to do": "Visit the Getty Center for some art and culture",
        "cost": {
            "flight": 0,
            "activity": 20,
            "hotel": 0,
            "transportation": 0,
            "food": 40
        }
    },
    "day5": {
        "location": "Los Angeles",
        "what to do": "Fly back to New York",
        "cost": {
            "flight": 300,
            "activity": 0,
            "hotel": 0,
            "transportation": 0,
            "food": 0
        }
    }
}

"""

    formate_prompt = "Give in the form of json file: \{\'day\': \{which day}, 'location': \{location from you}, 'what to do': \{what to do}, 'cost': \{cost details}}. Give me a " + str(days) + " day plane from " + location_from + " to " + location_to +", with "+ str(budget) + " dollar budget, including the transportation, flight, hotel. Generate the plan based on the theme of " + theme
    first_sentence = "The following conversation is bewtween a travel agent and a person who wants to travel, the travel agent will give a plan that meet the requirement for location, price, and day length. The price must the precise with customer's budget."
    templates = f"""{first_sentence}
    
    customer: {input1}
    agent: {output1}
    customer: {input2}
    agent: {output2}
    customer: {formate_prompt}
    agent: """
    return templates
