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
days = 0
budget = 0
from_l = ""
to_l = ""


@app.route("/", methods=("GET", "POST"))
def index():
    global all_plans
    global days
    global budget
    global from_l
    global to_l
    headers = request.headers
    print(headers)
    print("0000", request.args)
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
                "what to do": "Fly to Tokyo.",
                "cost": {
                "flight": 800,
                "activity": 0,
                "hotel": 100,
                "transportation": 30,
                "food": 50
                }
                },
                "day2": {
                "location": "Tokyo",
                "what to do": "Visit the Tsukiji Fish Market, the Meiji Shrine, and the Tokyo Tower.",
                "cost": {
                "flight": 0,
                "activity": 100,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day3": {
                "location": "Tokyo",
                "what to do": "Go shopping in Harajuku and Shibuya, and visit the Tokyo National Museum.",
                "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day4": {
                "location": "Kyoto",
                "what to do": "Take the bullet train to Kyoto. Visit the Kiyomizu-dera Temple, the Fushimi Inari Shrine, and have dinner at a traditional Kyoto restaurant.",
                "cost": {
                "flight": 150,
                "activity": 100,
                "hotel": 100,
                "transportation": 50,
                "food": 20
                }
                },
                "day5": {
                "location": "Kyoto",
                "what to do": "Visit the Kinkaku-ji Temple, the Gion district, and have lunch at a traditional tea house.",
                "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day6": {
                "location": "Osaka",
                "what to do": "Take the train to Osaka. Visit the Osaka Castle, the Dotonbori district, and have dinner at a local restaurant.",
                "cost": {
                "flight": 50,
                "activity": 100,
                "hotel": 100,
                "transportation": 20,
                "food": 20
                }
                },
                "day7": {
                "location": "Osaka",
                "what to do": "Visit the Universal Studios Japan, ride the roller coasters, take the studio tour, and watch a show.",
                "cost": {
                "flight": 0,
                "activity": 150,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                }
                }"""

        plan2 = """{
                "day1": {
                "location": "New York",
                "what to do": "Fly to Tokyo. Visit the Tokyo Tower, have lunch at a local ramen restaurant, and explore the Sensoji Temple.",
                "cost": {
                "flight": 800,
                "activity": 100,
                "hotel": 150,
                "transportation": 30,
                "food": 50
                }
                },
                "day2": {
                "location": "Tokyo",
                "what to do": "Visit the Imperial Palace, the Meiji Shrine, and have dinner at a sushi restaurant.",
                "cost": {
                "flight": 0,
                "activity": 150,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day3": {
                "location": "Tokyo",
                "what to do": "Visit the Tsukiji Fish Market, the Ueno Park, and have dinner at a local izakaya.",
                "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day4": {
                "location": "Kyoto",
                "what to do": "Take a bullet train to Kyoto. Visit the Fushimi Inari Shrine, the Kinkakuji Temple, and have dinner at a kaiseki restaurant.",
                "cost": {
                "flight": 200,
                "activity": 100,
                "hotel": 100,
                "transportation": 40,
                "food": 50
                }
                },
                "day5": {
                "location": "Kyoto",
                "what to do": "Visit the Nijo Castle, the Kiyomizu Temple, and have dinner at a local restaurant.",
                "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day6": {
                "location": "Osaka",
                "what to do": "Take a train to Osaka. Visit the Osaka Castle, the Shitennoji Temple, and have dinner at a local restaurant.",
                "cost": {
                "flight": 0,
                "activity": 100,
                "hotel": 100,
                "transportation": 30,
                "food": 30
                }
                },
                "day7": {
                "location": "Osaka",
                "what to do": "Visit the Universal Studios Japan, ride the roller coasters, take the studio tour, and watch a show. Have dinner at a local restaurant.",
                "cost": {
                "flight": 0,
                "activity": 200,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                }
                }"""

        plan3 = """{
                "day1": {
                "location": "New York",
                "what to do": "Fly to Tokyo. Visit the Tokyo Tower, have lunch at a local ramen restaurant, and explore the Sensoji Temple.",
                "cost": {
                "flight": 800,
                "activity": 100,
                "hotel": 150,
                "transportation": 30,
                "food": 50
                }
                },
                "day2": {
                "location": "Tokyo",
                "what to do": "Visit the Imperial Palace, the Meiji Shrine, and have dinner at a sushi restaurant.",
                "cost": {
                "flight": 0,
                "activity": 150,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day3": {
                "location": "Tokyo",
                "what to do": "Visit the Tsukiji Fish Market, the Ueno Park, and have dinner at a local izakaya.",
                "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day4": {
                "location": "Kyoto",
                "what to do": "Take a bullet train to Kyoto. Visit the Fushimi Inari Shrine, the Kinkakuji Temple, and have dinner at a kaiseki restaurant.",
                "cost": {
                "flight": 200,
                "activity": 100,
                "hotel": 100,
                "transportation": 40,
                "food": 50
                }
                },
                "day5": {
                "location": "Kyoto",
                "what to do": "Visit the Nijo Castle, the Kiyomizu Temple, and have dinner at a local restaurant.",
                "cost": {
                "flight": 0,
                "activity": 50,
                "hotel": 0,
                "transportation": 20,
                "food": 30
                }
                },
                "day6": {
                "location": "Osaka",
                "what to do": "Take a train to Osaka. Visit the Osaka Castle, the Shitennoji Temple, and have dinner at a local restaurant.",
                "cost": {
                "flight": 0,
                "activity": 100,
                "hotel": 100,
                "transportation": 30,
                "food": 30
                }
                },
                "day7": {
                "location": "Osaka",
                "what to do": "Visit the Universal Studios Japan, ride the roller coasters, take the studio tour, and watch a show. Have dinner at a local restaurant.",
                "cost": {
                "flight": 0,
                "activity": 200,
                "hotel": 0,
                "transportation": 20,
                "food": 30
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
        #     ).choices[0].text
        #     print(plans[i])
        #     print(type(plans[i]))

        plans[0] = plan1
        plans[1] = plan2
        plans[2] = plan3

        all_plans = {"plan1": json.loads(plans[0]), "plan2": json.loads(plans[1]), "plan3": json.loads(plans[2])}
        print(all_plans)
        # return render_template("plan_card.html", result=response.choices[0].text)
        d_serialzed = json.dumps(all_plans)
        print(type(d_serialzed))
        d_jsonified = jsonify(all_plans)
        return render_template("plan_card.html", budget0=budgets[0], budget1=budgets[1], budget2=budgets[2], plandata=plans)
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
    return render_template("card_detail.html", data=plan, filename=card_id)


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
        "what to do": "Fly to San Francisco. Take a cable car ride, visit the Golden Gate Bridge, and have a seafood dinner at Fisherman's Wharf.",
        "cost": {
            "flight": 300,
            "activity": 100,
            "hotel": 100,
            "transportation": 30,
            "food": 50
        }
    },
    "day2": {
        "location": "San Francisco",
        "what to do": "Take a ferry to Alcatraz Island, learn about its history, and enjoy the view. Have lunch at Chinatown and visit the Coit Tower.",
        "cost": {
            "flight": 0,
            "activity": 150,
            "hotel": 0,
            "transportation": 20,
            "food": 30
        }
    },
    "day3": {
        "location": "San Francisco",
        "what to do": "Visit the San Francisco Museum of Modern Art, have lunch at the Ferry Building Marketplace, and go on a hike in the Golden Gate Park.",
        "cost": {
            "flight": 0,
            "activity": 50,
            "hotel": 0,
            "transportation": 20,
            "food": 30
        }
    },
    "day4": {
        "location": "Los Angeles",
        "what to do": "Fly to Los Angeles. Visit the Hollywood Walk of Fame, the Griffith Observatory, and have dinner at In-N-Out Burger.",
        "cost": {
            "flight": 300,
            "activity": 100,
            "hotel": 100,
            "transportation": 30,
            "food": 20
        }
    },
    "day5": {
        "location": "Los Angeles",
        "what to do": "Spend the day at Universal Studios Hollywood, ride the roller coasters, take the studio tour, and watch a show. Have dinner at Pink's Hot Dogs.",
        "cost": {
            "flight": 0,
            "activity": 200,
            "hotel": 0,
            "transportation": 20,
            "food": 30
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
