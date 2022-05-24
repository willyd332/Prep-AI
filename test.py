from modules.paragraph_extractor import *
from modules.pdf_extractor import *
from modules.summarization import *

# Output Folders
jsonl_output_folder = './jsonl-data/'
text_output_folder = './extracted-text/'

# Text Inputs
nyt_URL = "../test-data/NewYorkTimes.txt"
nyt2_URL = "../test-data/nytPass2.txt"
shanghai_URL = "../test-data/shanghai.txt"
shanghai2_URL = "../test-data/shanghai2.txt"
ivan_URL = "../test-data/ivan-800-words.txt"
m2w_URL = "../test-data/m2w.txt"
klein_URL = "./extracted-text/Klein_Studying_the_History_of_Those_Who_Would_Rather_Forget_Oral_History_and_the_Experience_of_Slavery_copy.txt"

# PDF Inputs
kleinPdf_URL = "../test-data/KleinTest.pdf"
candido_URL = "../test-data/Will Dinneen — All This To Capture One Man — Final Paper copy.pdf"


# # RUN PDF TEST
# candido = PdfExtraction(candido_URL)
# print(candido.raw_text)
# # candido.save_raw_text_to_file(text_output_folder)

# RUN PARAGRAPH TEST
ivan = ParagraphExtraction(ivan_URL)
# print(shanghai.cleaned_text_list[0])
# nyt.save_data_to_jsonl_file(jsonl_output_folder)

# # RUN SUMMARY TEST
ivan_summary = Summarization(ivan.cleaned_text_list)
for bullet in ivan_summary.bullet_points:
  print("-")
  print(bullet)
print("")
print("-------------------------Summary-------------------------")
print(ivan_summary.summary)

