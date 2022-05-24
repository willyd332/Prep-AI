from itertools import count
import os
import openai
from dotenv import load_dotenv
from modules.paragraph_extractor import ParagraphExtraction

# Load env variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Summariazation Class
class Summarization:
  '''
  Summarize an entire article by summarizing each paragraph and then summarizing the summaries until it is short enough.
  '''
  def __init__(self, text_list, max_summary_size = 500):
    '''
    Takes in a cleaned_text_list (see paragraph_extractor.py)
    Returns a summary
    '''
    print("Recursive Summarization Initialized!")
    self.text_list = text_list
    self.length_of_text = self.count_words(self.make_string(self.text_list))
    self.max_summary_size = max_summary_size
    self.bullet_points = self.create_bullet_points(text_list)
    self.summary_list = self.create_summary_list()
    self.summary = self.make_string(self.summary_list)

  def make_prompt(self, paragraph, question):
    '''
    Takes in a paragraph of text to summarize.
    Generates the string that will be sent to Open AI.
    Returns that string.
    '''
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
      temperature=0.1,
      max_tokens=100
    )
    return response.choices[0].text

  def create_bullet_points(self, data):
    bullet_point_prompt = "Rewrite this paragraph in a one sentence summary"
    bullet_points = []
    for paragraph in data:
      prompt = self.make_prompt(paragraph, bullet_point_prompt)
      this_summary = self.query_openai(prompt)
      bullet_points.append(this_summary)
    return bullet_points


  def create_summary_list(self):
    '''
    Takes in a list of paragraphs.
    Summarizes them recursively until the total word count is less than max summary size.
    Returns summary in a string
    '''
    # Summarize article directly, or summarize bullet points
    clean_bullet_points = ParagraphExtraction.strip_text(self.bullet_points)
    clean_bullet_points = ParagraphExtraction.reduce_lines(clean_bullet_points)
    clean_bullet_points = ParagraphExtraction.consolidate_lines(clean_bullet_points)
    clean_bullet_points = ParagraphExtraction.strip_text(clean_bullet_points)
    text_to_summarize = clean_bullet_points
    # Make sure summary isn't too long
    summary_size = self.max_summary_size 
    if self.length_of_text < 1500:
      summary_size = max(round(self.length_of_text/3), 200)
    num_paragraphs = len(text_to_summarize)
    max_paragraph_size = summary_size/num_paragraphs
    # Create summary
    summary_prompt = f"Rewrite this paragraph into a new paragraph not longer than {str(max_paragraph_size)} words"
    summary_list = []
    for paragraph in text_to_summarize:
      prompt = self.make_prompt(paragraph, summary_prompt)
      this_summary = self.query_openai(prompt)
      print("--")
      print(this_summary)
      print("--")
      summary_list.append(this_summary)
    # Clean the summaries
    clean_summary_list = ParagraphExtraction.strip_text(summary_list)
    clean_summary_list = ParagraphExtraction.consolidate_lines(summary_list)
    for i in range(len(clean_summary_list)):
      new_summary = clean_summary_list[i].rsplit(".", 1)[0] + "."
      clean_summary_list[i] = new_summary
    return clean_summary_list