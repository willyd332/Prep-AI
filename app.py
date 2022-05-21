import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def prompt():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            engine="text-ada-001",
            prompt=return_prompt(prompt),
            temperature=0.6,
        )
        return redirect(url_for("prompt", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

@app.route("/animal", methods=("GET", "POST"))
def animal():
    if request.method == "POST":
        prompt = request.form["animal"]
        response = openai.Completion.create(
            engine="text-ada-001",
            prompt=generate_animal_prompt(prompt),
            temperature=0.6,
        )
        return redirect(url_for("animal", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


# Helper Functions
def generate_animal_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )

def return_prompt(prompt):
  return prompt


# Run The App With Debug
app.run(debug=True)