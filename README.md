# Prep-AI
An NPL Tool with Open.AI to help students who have no time to read their assignments
## [Link To Frontend React.js App](https://github.com/willyd332/Prep.AI-Frontend)

--------------------------------------------------

## Running
Clone this repo `https://github.com/willyd332/Prep-AI.git`

Then download `pip install -r requirements.txt`

Set `.env` variables

Run server with `flask run`

--------------------------------------------------


## MVP #1
- Student inputs a PDF
- Student receives helpful summary

## MVP #2
- Student can input a PDF
- Student receives a full "Prep Sheet"
  - Important Quotes
  - Summary of Information
  - Main/Counter Argument (a Dialectic?)
- Student can download a sexy PDF of Prep Sheet

## MVP 3
- Student can create an account
- Student pays $1
- Repeat MVP #2

## TODO List
- Turn paragraph_extractor into a class
- Turn pdf_extractor into a pdf class







# TODO PLAN

The most important thing is how you ingest the data.

Open AI does a great job if the data is clean...

Try out a few other options

1. Nice interface that makes used paste clean text into boxes
2. Check to see if academic journals can be downloaded in other formats
3. Get more creative with your paragraph extraction
  - Think of how Resultid uses clustering model
  - How can you organize the data?
  - Start with simple solutions, like user has to do it!