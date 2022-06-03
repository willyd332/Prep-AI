import os
from os.path import *
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from modules.paragraph_extractor import ParagraphExtraction

class PdfExtraction:

  def __init__(self, urlToPDF):
    '''
    Init the extraction by creating an object for that PDF file
    '''
    print("PdfExtraction Initialized!")
    # Create Title
    self.article_title = ParagraphExtraction.clean_filename(os.path.basename(urlToPDF).split(".")[0])
    # Generate and clean text
    pdf_file = open(urlToPDF, 'rb')
    self.raw_text = self.extract_txt_from_pdf(pdf_file)

  # EXTRACT FROM PDF
  # -- 
  def extract_txt_from_pdf(self, pdf):
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

  def save_raw_text_to_file(self, output_folder):
    """
    Write a extracted text into a new text file.
    """
    text_file = open(output_folder + self.article_title + ".txt", "w")
    text_file.write(self.raw_text)
    text_file.close()

  @staticmethod
  def save_external_text_to_file(raw_text, title, output_folder):
    """
    Write any string into a new text file.
    """
    text_file = open(output_folder + title + ".txt", "w")
    text_file.write(raw_text)
    text_file.close()