import os
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from modules.paragraph_extractor import *
from modules.pdf_extractor import *
from modules.summarization import *
from modules.question_answering import *
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/summarize", methods=(["GET","POST"]))
@cross_origin()
def summarize():
    if request.method=='POST':
        posted_data = request.get_json()
        print("THIS IS THE POSTED DATA")
        print(posted_data)
        rawText = posted_data["textData"]
        # Create a temporary file
        temp_file = open("temp_file.txt", "w")
        temp_file.write(rawText)
        temp_file.close()
        # RUN PARAGRAPH TEST
        cleanedText = ParagraphExtraction("./temp_file.txt")
        # # RUN SUMMARY TEST
        summary = Summarization(cleanedText.cleaned_text_list)
        print("Summary Created!")
        print(summary.summary)
        return jsonify(summary.summary)

# Run The App With Debug
app.run(debug=True)