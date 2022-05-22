import os
import jsonlines
from sentence_splitter import split_into_sentences as make_sentences

# FILEPATHS
# --
# filePath = "../test-data/NewYorkTimes.txt"
filePath = "../test-data/m2w.txt"
# filePath = "../test-data/Debs Speech 1918 copy.docx"
# filePath = "../test-data/Klein-Studying the History of Those Who Would Rather Forget- Oral History and the Experience of Slavery copy.pdf"

output_folder = '../jsonl-data/'

# GET THE DATA
# --
article_title = os.path.basename(filePath).split(".")[0]
raw_text_file = open(filePath,"r")
raw_text = raw_text_file.readlines()

# DATA CLEANING
# --
# Remove empty lines and strip new-lines
def strip_text(text_list):
  '''
  Takes in a list of strings. 
  Strips each string and then removes empty lines in the list.
  Returns a list of strings.
  '''
  text = [line.strip() for line in text_list if line.strip() != ""]
  return text

# Reduce lines if lines are larger than the paragraph size
def reduce_lines(text_list, max_paragraph_size = 200):
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
      reduced_line = consolidate_lines(sentences)
      reduced_text.extend(reduced_line)
  return reduced_text


# Consolidate small lines into uniform paragraphs ~200 words
def consolidate_lines(text_list, max_paragraph_size = 200):
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
def clean_text(raw_text_input):
  '''
  Takes in a list of strings. 
  Applies cleaning functions to the raw text.
  Returns a list of strings.
  '''
  clean_text_temp = strip_text(raw_text_input)
  clean_text_temp = reduce_lines(clean_text_temp)
  clean_text_temp = consolidate_lines(clean_text_temp)
  clean_text_temp = strip_text(clean_text_temp)
  return clean_text_temp

# WRITE TEXT TO JSONLINES FILE
# --
def generate_jsonl_file(data, title, path_to_output):
  '''
  Takes a list of strings as 'data', a string as 'title', and a path to a folder as 'path_to_output'. 
  Converts the list data into a JSONL object and puts that file into the output folder.
  Returns json version of list.
  '''
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
cleaned_data = clean_text(raw_text)
generate_jsonl_file(cleaned_data, article_title, output_folder)