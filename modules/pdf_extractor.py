import os
import re
from html import unescape
from urllib.parse import unquote
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from os.path import *
import paragraph_extractor as paragraphs

# FILENAMES & GET PDF
# --

filePath = "../test-data/Klein-Studying the History of Those Who Would Rather Forget- Oral History and the Experience of Slavery copy.pdf"

text_output_folder = '../extracted-text/'
json_output_folder = '../jsonl-data/'

# GET THE DATA
# --
pdf_title = os.path.basename(filePath).split(".")[0]
pdf_file = open(filePath, 'rb')

# EXTRACT FROM PDF
# -- 
def extract_txt_from_pdf(pdf):
  '''
  '''
  parser = PDFParser(pdf)
  document_content = PDFDocument(parser)
  if not document_content.is_extractable:
      raise PDFTextExtractionNotAllowed
  else:
      rsrcmgr = PDFResourceManager()
      laparams = LAParams()
      device = PDFPageAggregator(rsrcmgr, laparams=laparams)
      interpreter = PDFPageInterpreter(rsrcmgr, device)
      results = ''
      for page in PDFPage.create_pages(document_content):
          interpreter.process_page(page)
          layout = device.get_result()
          for x in layout:
              if (isinstance(x, LTTextBoxHorizontal)):
                  result = x.get_text() + '\n'
                  if result.strip() != '':
                      results = results + result
  return results

def clean_filename(string):
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

def save_raw_text_to_file(text, filename, output_folder):
  """
  Write a string into a new text file.
  """
  text_file = open(output_folder + filename + ".txt", "w")
  text_file.write(text)
  text_file.close()

# RUN & TEST
# --
cleaned_filename = clean_filename(pdf_title)
raw_text = extract_txt_from_pdf(pdf_file)
save_raw_text_to_file(raw_text, cleaned_filename, text_output_folder)

# WHAT TO DO ABOUT THE FACT THAT THE EXTRACTED TEXT IS SOMETIMES DIRTY???
'''
It's quite simple really, I will just force the user to clean it up. It will take them 10 seconds.
All they really need is a rough clean, ask them to delete the obvious metadata and that't the end.

I will give them two options:

  1. Paste the text you would like to analyze directly.
  2. Upload a PDF and then manually clean the data.

The code doesn't have to do everything!!
'''