from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import PyPDF2 as pdf2

# input pdf file from route parameter
# outputs txt file (raw_courtcases.txt")


# converts pdf to raw string
def convert_pdf_to_str(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    return text


# converts string to txt file (raw with white spaces)
def str_to_txt(string, txt):
    with open(txt, "w") as txt:
        txt.write(string)

    return txt


def main(filename):
    print("Reading file...")

    outp_txt_file = "raw_courtcases.txt"
    route = filename

    # opens pdf in route with pdf miner
    with open(route, "rb") as f:
        pdf = pdf2.PdfFileReader(f)  # pdf object
        num_pages = pdf.getNumPages()
        print("PAGE COUNT: ", num_pages)

    # converts pdf to str
    extracted_string = convert_pdf_to_str(route)

    # converts str to raw txt file
    raw_txt_file = str_to_txt(extracted_string, outp_txt_file)
    print('PDF converted to txt (see "raw_courtcases.txt")')

    return raw_txt_file, num_pages, filename


if __name__ == '__main__':
    main()
