import os
import openai
from dotenv import load_dotenv
from modules.paragraph_extractor import ParagraphExtraction

# Load env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



class RecursiveSummarization:
  '''
  Summarize an entire article by summarizing each paragraph and then summarizing the summaries until it is short enough.
  '''
  def __init__(self, text_list, max_paragraph_size = 200, max_summary_size = 500):
    '''
    Takes in a cleaned_text_list (see paragraph_extractor.py)
    Returns a summary
    '''
    print("Recursive Summarization Initialized!")
    self.text_list = text_list
    self.max_paragraph_size = max_paragraph_size
    self.max_summary_size = max_summary_size
    self.summary = self.run_summarization(self.text_list)

  def make_prompt(self, paragraph):
    '''
    Takes in a paragraph of text to summarize.
    Generates the string that will be sent to Open AI.
    Returns that string.
    '''
    question = "Rewrite this paragraph in a one sentence summary:"
    prompt = f'''
      {question}:

      {paragraph}
    '''
    return prompt

  def regenerate_paragraphs(self, text_block):
    '''
    Takes in a large block of text.
    Reprocesses it into paragraph sized chunks to re-run analysis.
    Return list of new paragraphs
    '''
    new_text_list = ParagraphExtraction(text_block).cleaned_text_list
    return new_text_list


  def make_string(self, data):
    '''
    Takes in a list of paragraphs.
    Combines them into a string.
    Returns that string.
    '''
    new_string = """{}""".format("\n".join(data))
    return new_string
  
  def count_words(self, text):
    '''
    Takes in a string.
    Counts the number of words.
    Returns the word count.
    '''
    word_list = text.split()
    number_of_words = len(word_list)
    return number_of_words
  
  def query_openai(self, prompt):
    '''
    Takes in a string prompt for Open AI.
    Queries openai.
    Returns output.
    '''
    response = openai.Completion.create(
      engine="text-ada-001",
      prompt=prompt,
      temperature=0.6,
      max_tokens=100
    )
    return response.choices[0].text


  def run_summarization(self, data):
    '''
    Takes in a list of paragraphs.
    Summarizes them recursively until the total word count is less than max summary size.
    Returns summary in a string
    '''
    summaries_list = []
    for paragraph in data:
      prompt = self.make_prompt(paragraph)
      this_summary = self.query_openai(prompt)
      print("--")
      print(this_summary)
      print("--")
      summaries_list.append(this_summary)
    summary_string = self.make_string(summaries_list)
    return summary_string

  

'''
Notes

 3 Basic Prompt Creating Guidelines
  1. Show and Tell, give instructions and examples
  2. Provide quality data
  3. Check your settings (Temperature & top_p). Is there only one right answer?
'''