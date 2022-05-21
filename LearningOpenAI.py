import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
# ------------------------------------------------------------
# Learning the completions endpoint
# ------------------------------------------------------------
# Testing it out
def ask_about_historical_figure(figure):
  prompt = "Tell me about " + figure + "."

def return_prompt(prompt):
  return prompt

def do_completion_request(inp, make_prompt, max_tokens=128):
    response = openai.Completion.create(
        engine="text-ada-001",
        prompt=make_prompt(inp),
        max_tokens=max_tokens,
    )
    return response['choices'][0]['text']

# test1 = do_completion_request("Suggest one name for a black horse.", return_prompt)
# print(test1)

'''
Notes:

Open AI has different models with differnt levels of quality and price
- Ada fucking sucks but it is cheap (use this for development!)
- Davinci is the best but expensive

Requests you make aren't free. Be careful!

Writing prompts is extremely important, for example:

  You can write this:
    "Suggest three names for a horse that is a superhero."

  Or you can write this:
    "Suggest three names for an animal that is a superhero.

    Animal: Cat
    Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
    Animal: Dog
    Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
    Animal: Horse
    Names:"

Stop treating like it's not an NLP tool. If you were asking a human, what would you ask?

'''

# ------------------------------------------------------------
# Playing with Temperature

'''
Notes:

If "temperature" is set to 0, which it is by default, the model will return the same thing each time.
The higher the temperature, the more 'risks' the model will take in its response, resulting in more diverse completions

'''

# ------------------------------------------------------------
# Building an application

'''
Notes:

They provide a quickstart guide... I downloaded the one for Flask. Fuck it. Time to learn.
'''

# ------------------------------------------------------------




# ------------------------------------------------------------