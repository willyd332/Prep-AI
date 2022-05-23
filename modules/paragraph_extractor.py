import os
import re
from html import unescape
from urllib.parse import unquote
import jsonlines
from sentence_splitter import split_into_sentences as make_sentences

class ParagraphExtraction:
  '''
  Takes in raw text.
  This class deals with extracting and cleaning raw text into clean, uniform paragraphs
  '''

  def __init__(self, urlToText):
    '''
    Init the extraction by creating an object for that text file
    '''
    print("Recursive Summarization Initialized!")
    # Create Title
    self.article_title = self.clean_filename(os.path.basename(urlToText).split(".")[0])
    # Generate and clean text
    raw_text_file = open(urlToText,"r")
    raw_text_list = raw_text_file.readlines()
    self.raw_text_list = raw_text_list
    self.cleaned_text_list = self.clean_text(raw_text_list)
  
  # DATA CLEANING
  # --
  # Remove empty lines and strip new-lines
  def strip_text(self, text_list):
    '''
    Takes in a list of strings. 
    Strips each string and then removes empty lines in the list.
    Returns a list of strings.
    '''
    text = [line.strip() for line in text_list if line.strip() != ""]
    return text


  def merge_lines(self, text_list):
    '''
    Takes in a list of strings. 
    Ensures that all of the lines end on a period so there aren't uneven cutoffs in the text.
    Returns a list of strings.
    '''
    merged_text = []
    # Create a temp string to store created strings
    temp_string = ""
    for line in text_list:
      this_line = line
      # if it doesn't end in punctuation add to temp string
      if this_line[-1] not in [".", "!", "?"]:
        # If the line splits off mid-word
        if this_line[-1] == "-":
          this_line = this_line[:-1]
          temp_string = temp_string + this_line
        else:
          temp_string = temp_string + this_line + " "
      # When you find a punctuation mark append the temp string to the merged text
      else:
        if temp_string == "":
          merged_text.append(this_line)
        else:
          temp_string = temp_string + this_line
          merged_text.append(temp_string)
          temp_string = ""
    # Add any remaining lines (in case it doesn't end on punctuation)
    if temp_string != "":
      merged_text.append(temp_string)
    # Return
    return merged_text


  # Reduce lines if lines are larger than the paragraph size
  def reduce_lines(self, text_list, max_paragraph_size = 200):
    '''
    Takes in a list of strings.
    Reduces the strings that are too long into new smaller strings.
    Returns a list of strings.
    '''
    reduced_text = []
    # If line is too big split into sentences and remake line
    for line in text_list:
      if len(line.split()) <= max_paragraph_size:
        reduced_text.append(line)
      else:
        sentences = make_sentences(line)
        reduced_line = self.consolidate_lines(sentences)
        reduced_text.extend(reduced_line)
    return reduced_text


  # Consolidate small lines into uniform paragraphs ~200 words
  def consolidate_lines(self, text_list, max_paragraph_size = 200):
    '''
    Takes in a list of strings. 
    Consolidates them into paragraphs or new strings of a generally uniform size.
    Returns a list of strings.
    '''
    consolidated_text = []
    temp_string = ""
    # Add text to the new array
    for i in range(len(text_list)):
      this_string = text_list[i]
      if temp_string == "":
        temp_string = temp_string + this_string
      elif len(temp_string.split()) + len(this_string.split()) <= max_paragraph_size:
        temp_string = temp_string + " " + this_string
      else:
        consolidated_text.append(temp_string)
        temp_string = " " + this_string
    if temp_string != "":
      consolidated_text.append(temp_string)
    return consolidated_text

  # CLEAN THE TEXT
  # --
  def clean_text(self, raw_text_input):
    '''
    Takes in a list of strings. 
    Applies cleaning functions to the raw text.
    Returns a list of strings.
    '''
    clean_text_temp = self.strip_text(raw_text_input)
    clean_text_temp = self.merge_lines(clean_text_temp)
    clean_text_temp = self.reduce_lines(clean_text_temp)
    clean_text_temp = self.consolidate_lines(clean_text_temp)
    clean_text_temp = self.strip_text(clean_text_temp)
    return clean_text_temp

  def clean_filename(self, string):
    """
    Sanitize a string to be used as a filename.
    """
    string = unescape(string)
    string = unquote(string)
    string = re.sub(r'<(?P<tag>.+?)>(?P<in>.+?)<(/(?P=tag))>', "\g<in>", string)
    string = string.replace(':', '_').replace('/', '_').replace('\x00', '_')
    string = re.sub('[\n\\\*><?\"|\t]', '', string)
    string = string.strip()
    string = string.replace(' ', '_').replace('-', '_').replace('__', '_')
    return string

  # WRITE TEXT TO JSONLINES FILE
  # --
  def generate_jsonl_file(self, path_to_output):
    '''
    Takes in 'path_to_output' url to output folder. 
    Converts the class's list data into a JSONL object and puts that file into the output folder.
    Returns json version of list.
    '''
    # Set Defaults
    data = self.cleaned_text_list
    title = self.article_title
    # Create JSONs
    json_items = []
    for i in range(len(data)):
      obj = {'text': data[i], 'metadata': title + "_" + str(i)}
      json_items.append(obj)
    # Create a JSONL file for the cleaned text
    with jsonlines.open(path_to_output + title + ".jsonl", mode="w") as writer:
      writer.write_all(json_items)
      writer.close()
    return json_items
  
  def generate_jsonl_file_with_external_data(self, path_to_output, data, title):
    '''
    Takes a list of strings as 'data', a string as 'title', and a path to a folder as 'path_to_output'. 
    Converts the list data into a JSONL object and puts that file into the output folder.
    Returns json version of list.
    '''
    # Create JSON
    json_items = []
    for i in range(len(data)):
      obj = {'text': data[i], 'metadata': title + "_" + str(i)}
      json_items.append(obj)
    # Create a JSONL file for the cleaned text
    with jsonlines.open(path_to_output + title + ".jsonl", mode="w") as writer:
      writer.write_all(json_items)
      writer.close()
    return json_items


# RUN & TEST
# --

# file_paths
# --
# file_path = "../test-data/NewYorkTimes.txt"
# file_path = "../test-data/m2w.txt"
file_path = "../extracted-text/Klein_Studying_the_History_of_Those_Who_Would_Rather_Forget_Oral_History_and_the_Experience_of_Slavery_copy.txt"
output_folder = '../jsonl-data/'

klein = ParagraphExtraction(file_path)
print(klein.cleaned_text_list)
klein.generate_jsonl_file(output_folder)