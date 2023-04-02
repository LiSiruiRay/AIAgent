# Ray
# Created By: 2023-04-01
# Description: 

import os
import sys

# print("Python executable:", sys.executable)

import openai
from flask import Flask, redirect, render_template, request, url_for, json, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

all_plans = []


@app.route("/", methods=("GET", "POST"))
def index():
    global all_plans
    if request.method == "POST":
        days = request.form["days"]
        budget = request.form["budget"]
        from_l = request.form["fromlocation"]
        to_l = request.form["tolocation"]
        # print("-----------------------Days: ", days, ", budge: ", budget, ", from: ", from_l, ", to: ", to_l)

        # showing = str(days2) + ";;;'" + str(budget) + "---" + from_l + "000" + to_l
        # pr = generate_prompt(from_l, to_l, days, budget, "excited")
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=pr,
        #     temperature=0.6,
        #     max_tokens=800
        # )

        plan1 = """{
            "day1": {
                "location": "New York",
                "what to do": "Take a helicopter ride to Liberty State Park in New Jersey",
                "cost": {
                    "flight": 500,
                    "activity": 0,
                    "hotel": 200,
                    "transportation": 0,
                    "food": 50
                }
            },
            "day2": {
                "location": "New Jersey",
                "what to do": "Go on an exciting adventure at Six Flags Great Adventure",
                "cost": {
                    "flight": 0,
                    "activity": 200,
                    "hotel": 0,
                    "transportation": 0,
                    "food": 50
                }
            }
        }"""

        plan2 = """{
            "day1": {
                "location": "Jersey City",
                "what to do": "Take a helicopter ride to Liberty State Park in New Jersey",
                "cost": {
                    "flight": 500,
                    "activity": 0,
                    "hotel": 200,
                    "transportation": 0,
                    "food": 50
                }
            },
            "day2": {
                "location": "New Jersey",
                "what to do": "Go on an exciting adventure at Six Flags Great Adventure",
                "cost": {
                    "flight": 0,
                    "activity": 200,
                    "hotel": 0,
                    "transportation": 0,
                    "food": 50
                }
            }
        }"""

        plan3 = """{
            "day1": {
                "location": "Newark",
                "what to do": "Take a helicopter ride to Liberty State Park in New Jersey",
                "cost": {
                    "flight": 500,
                    "activity": 0,
                    "hotel": 200,
                    "transportation": 0,
                    "food": 50
                }
            },
            "day2": {
                "location": "New Jersey",
                "what to do": "Go on an exciting adventure at Six Flags Great Adventure",
                "cost": {
                    "flight": 0,
                    "activity": 200,
                    "hotel": 0,
                    "transportation": 0,
                    "food": 50
                }
            }
        }"""
        budget = int(budget)
        budgets = [budget * 0.75, budget, budget * 1.25]
        plans = ["", "", ""]

        # for i in range(3):
        #     plans[i] = openai.Completion.create(
        #         model="text-davinci-003",
        #         prompt=generate_prompt(from_l, to_l, days, budgets[i], "excited"),
        #         temperature=0.6,
        #         max_tokens=800
        #     )
        plans[0] = plan1
        plans[1] = plan2
        plans[2] = plan3
        all_plans = {"plan1": json.loads(plans[0]), "plan2": json.loads(plans[1]), "plan3": json.loads(plans[2])}
        # return render_template("plan_card.html", result=response.choices[0].text)
        d_serialzed = json.dumps(all_plans)
        print(type(d_serialzed))
        d_jsonified = jsonify(all_plans)
        return render_template("plan_card.html", data=all_plans)
        # return jsonify(all_plans)

    # result = request.args.get("result")
    # return render_template("index.html", result=result)
    return render_template("index.html")


@app.route('/card-details', methods=['POST'])
def card_details():
    card_id = request.form['card_id']
    # Do something with the card identifier, e.g. query the database for more details
    # print(all_plans)
    plan = all_plans[card_id]
    # print("------", all_plans[card_id])
    return render_template("card_detail.html", data=plan)


# def return_to_otherpage():


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
def generate_prompt(location_from, location_to, days, budget, theme="relax"):
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

    formate_prompt = "Give in the form of json file: \{\'day\': \{which day}, 'location': \{location from you}, 'what to do': \{what to do}, 'cost': \{cost details}}. Give me a " + str(
        days) + " day plane from " + location_from + " to " + location_to + ", with " + str(
        budget) + " dollar budget, including the transportation, flight, hotel. Generate the plan based on the theme of " + theme
    first_sentence = "The following conversation is bewtween a travel agent and a person who wants to travel, the travel agent will give a plan that meet the requirement for location, price, and day length. The price must the precise with customer's budget."
    templates = f"""{first_sentence}
    
    customer: {input1}
    agent: {output1}
    customer: {input2}
    agent: {output2}
    customer: {formate_prompt}
    agent: """
    return templates
