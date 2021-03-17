"""
PYPDF2 DOESN'T LIKE THE FORMATTING -- DOES NOT WORK
codegrepper.com/code-examples/python/how+to+loop+through+pages+of+pdf+using+python
slate: https://github.com/mstamy2/PyPDF2/issues/437
"""

import PyPDF2 as pdf2
import re
import slate3k as slate

def get_info(route):
    list = []
    with open(route, "rb") as f:
        pdf = pdf2.PdfFileReader(f)  # pdf object
        num_pages = pdf.getNumPages()

        id_circuit = "Circuit"  # use this string to find circuit info (in the same line as "Circuit"
        id_district_court = "District Court"  # use to find the district court info (in the same line)
        id_judge = "Total All Cases for District Judge"  # use to find judge name and case#
        print(num_pages)
        for i in range(num_pages):
            page = pdf.getPage(i)  # page object
            print("page", i)
            if i == 1:
                text = slate.PDF(page)  # slate works for entire pdf not single pg
                print(text)

        # print(info)
    # author = info.author
    # creator = info.creator
    # producer = info.producer
    # subject = info.subject
    # title = info.title


if __name__ == '__main__':
    # path = "w9.pdf"
    path = 'full_courtcases1.pdf'
    # https link doesn't work for some reason, need to access downloaded version and put in this folder
    # https: // www.uscourts.gov / sites / default / files / data_tables / CJRA_8_03312020.pdf
    get_info(path)
