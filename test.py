from modules.paragraph_extractor import *
from modules.pdf_extractor import *
from modules.summarization import *
from modules.question_answering import *

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
pennTxt = "./extracted-text/American_J_Political_Sci_2008_Penn_A_Model_of_Farsighted_Voting.txt"
brownTxt = "./extracted-text/brown.txt"

# PDF Inputs
kleinPdf_URL = "../test-data/KleinTest.pdf"
candido_URL = "../test-data/Will Dinneen — All This To Capture One Man — Final Paper copy.pdf"
penn_URL = "../test-data/American J Political Sci - 2008 - Penn - A Model of Farsighted Voting.pdf"
brown_URL = "../test-data/brown.pdf"

# JSONL Inputs
kein_jsonl_URL = "./jsonl-data/Klein_Studying_the_History_of_Those_Who_Would_Rather_Forget_Oral_History_and_the_Experience_of_Slavery_copy.jsonl"

# # RUN PDF TEST
# penn = PdfExtraction(penn_URL)
# brown = PdfExtraction(brown_URL)
# # print(candido.raw_text)
# penn.save_raw_text_to_file(text_output_folder)
# brown.save_raw_text_to_file(text_output_folder)

# # RUN PARAGRAPH TEST
# penn = ParagraphExtraction(pennTxt)
# brown = ParagraphExtraction(brownTxt)
# # print(shanghai.cleaned_text_list[0])
# # nyt.save_data_to_jsonl_file(jsonl_output_folder)

# # # RUN SUMMARY TEST
# penn_summary = Summarization(penn.cleaned_text_list)
# brown_summary = Summarization(brown.cleaned_text_list)
# for bullet in penn_summary.bullet_points:
#   print("-")
#   print(bullet)
# print("")
# print("-------------------------Summary-------------------------")
# print(penn_summary.summary)

# RUN QUESTIONS TEST
#klein_oracle = Answers(kein_jsonl_URL)
answer = Answers.submit_query("Why is are oral techniques important for studying the history of slavery?", "file-Nb2sytJ1WLWpVfaKwhSU94fa")
print(answer)