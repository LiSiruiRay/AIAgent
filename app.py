# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/hello')
# def hello():
#     return "<h1>hello world</h1>"
#
# if __name__ == '__main__':
#     app.run()

# from flask import Flask, render_template, request, jsonify, make_response, json
from flask import Flask, redirect, render_template, request, jsonify, json
from flask_cors import CORS
import requests
import os
import sys
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
print("Python executable:", sys.executable)
CORS(app)

jsontext = """{
    "plan": [{
            "day": 1,
            "location": "Beijing",
            "what to do": "Visit the Great Wall of China and Forbidden City",
            "cost": "$300"
        },
        {
            "day": 2,
            "location": "Beijing",
            "what to do": "Explore the Temple of Heaven and Tiananmen Square",
            "cost": "$200"
        },
        {
            "day": 3,
            "location": "Xi'an",
            "what to do": "See the Terracotta Army",
            "cost": "$250"
        },
        {
            "day": 4,
            "location": "Xi'an",
            "what to do": "Visit the Giant Wild Goose Pagoda and Muslim Quarter",
            "cost": "$150"
        },
        {
            "day": 5,
            "location": "Shanghai",
            "what to do": "Enjoy a relaxing boat tour on the Huangpu River and visit the Yuyuan Garden",
            "cost": "$300"
        },
        {
            "day": 6,
            "location": "Shanghai",
            "what to do": "Explore the modern cityscape of Pudong and Nanjing Road",
            "cost": "$200"
        },
        {
            "day": 7,
            "location": "Shanghai",
            "what to do": "Take a day trip to the peaceful water town of Zhujiajiao",
            "cost": "$250"
        }
    ],
    "total cost": "$1650",
    "remaining budget": "$3350",
    "notes": "This itinerary offers a relaxing mix of cultural and natural attractions, with plenty of time to unwind and enjoy the surroundings. All costs include transportation, accommodation, and activities."
}"""

data = {
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
}

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

@app.route("/", methods=["GET", "POST"])
def index():
    # return render_template("index.html")
    print(request.method)
    if request.method == "POST":
        print("POST")
        placeFrom = request.form["placeFrom"]
        placeTo = request.form["placeTo"]
        date = request.form["date"]
        budget = request.form["budget"]
        # promptRegular = generate_prompt(placeFrom, placeTo, date, price)
        # promptCheap = generate_prompt(placeFrom, placeTo, date, price)
        # promptLuxury = generate_prompt(placeFrom, placeTo, date, price)
        # print(promptRegular)
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(placeFrom, placeTo, date, price),
        #     temperature=0.6,
        # )
        # return redirect(url_for("index", result=response.choices[0].text))

        # return redirect(url_for("result", result=jsontext))
        # return jsontext
        # response = make_response(json.dump(data))
        # response.mimetype = 'application/json'
        # return response
        dict1 = json.loads(plan1)
        dict2 = json.loads(plan2)
        dict3 = json.loads(plan3)
        # merged_dict = {key: value for (key, value) in (dict1.items() + dict2.items() + dict3.items())}

        # print(merged_dict)
        data2 = json.loads(jsontext)
        all_plan = {"plan1": dict1, "plan2": dict2, "plan3": dict3}
        print(type(dict1))
        # all_plan_text =
        return jsonify(all_plan)

    # result = request.args.get("result")
    return render_template("index.html")

@app.route("/generate_itinerary", methods=["POST"])
def generate_itinerary():
    place = request.form.get("place")

    # Get itinerary from GPT API
    itinerary = get_itinerary_from_gpt_api(place)

    return jsonify(itinerary=itinerary)


def get_itinerary_from_gpt_api(place):
    # Replace with your GPT API key and endpoint
    API_KEY = "your_gpt_api_key"
    ENDPOINT = "your_gpt_api_endpoint"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "input_text": place
    }

    response = requests.post(ENDPOINT, headers=headers, json=data)
    itinerary = response.json().get("output_text", "")

    return itinerary


def generate_prompt(placeFrom, placeTo, date, price, theme):
    return




if __name__ == "__main__":
    app.run(debug=True)