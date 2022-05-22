import os

filePath = "../test-data/NewYorkTime.txt"
# filePath = "../test-data/m2w.txt"
# filePath = "../test-data/Debs Speech 1918 copy.docx"
# filePath = "../test-data/Klein-Studying the History of Those Who Would Rather Forget- Oral History and the Experience of Slavery copy.pdf"

# GET THE DATA
# --
article_title = os.path.basename(filePath)
raw_text_file = open(filePath,"r")
raw_text = raw_text_file.readlines()

# DATA CLEANING
# --
# Remove empty lines and strip new-lines
def strip_text(text_list):
  text = [line.strip() for line in text_list if line.strip() != ""]
  return text

# Consolidate small lines into uniform paragraphs ~200 words
def consolidate_lines(text_list, max_paragraph_size = 200):
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

# PRINT
# --
cleanText = consolidate_lines(strip_text(raw_text))
print(article_title)
for line in cleanText: 
  print("--")
  print(line)
