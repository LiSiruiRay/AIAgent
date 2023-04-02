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
    first_sentence = "Give in the form of json file: \{'day': \{which day}, 'location': \{location from you}, 'what to do': \{what to do}, 'cost': \{cost details}}. Give me a travel plane based on the theme"
    templates = f"""{first_sentence}
    
    Input: {input1}
    Output: {output1}
    Input: {input2}
    Output: {output2}
    Input: {formate_prompt}
    Output: """
    
    return templates

prompt = generate_prompt("New York", "Japan", 7, 5000, "excited")
print(prompt)