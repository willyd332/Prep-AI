import os
import openai
from dotenv import load_dotenv
from paragraph_extractor import reduce_lines, consolidate_lines, strip_text, merge_lines


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



class RecursiveSummarization:
  '''
  Summarize an entire article by summarizing each paragraph and then summarizing the summaries until it is short enough.
  '''
  def __init__(self):
      print("Recursive Summarization Initialized!")

  def make_prompt(self, paragraph):
    '''
    Takes in a paragraph of text to summarize.
    Generates the string that will be sent to Open AI.
    Returns that string.
    '''
    prompt =''''''

  def regenerate_paragraphs(self, overall_text, max_paragraph_size = 200):
    '''
    Takes in a large block of text.
    Reprocesses it into paragraph sized chunks to re-run analysis.
    Return list of new paragraphs
    '''

  def make_string(self, data):
    '''
    Takes in a list of paragraphs.
    Combines them into a string.
    Returns that string.
    '''
  
  def count_words(self, text):
    '''
    Takes in a string.
    Counts the number of words.
    Returns the word count.
    '''

  def summarize(self, data, max_summary_size = 500):
    '''
    Takes in a list of paragraphs.
    Summarizes them recursively until the total word count is less than max summary size.
    Returns summary in a string
    '''
  


'''
Notes

 3 Basic Prompt Creating Guidelines
  1. Show and Tell, give instructions and examples
  2. Provide quality data
  3. Check your settings (Temperature & top_p). Is there only one right answer?
'''