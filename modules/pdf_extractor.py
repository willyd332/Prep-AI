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

# FILENAMES & GET PDF
# --

filePath = "../test-data/Klein-Studying the History of Those Who Would Rather Forget- Oral History and the Experience of Slavery copy.pdf"
# filePath = "../test-data/Havlick2007_Article_LogicsOfChangeForMilitary-to-w.pdf"

output_folder = '../extracted-text/'

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


print(extract_txt_from_pdf(pdf_file))