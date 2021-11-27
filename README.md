
# pdf crawler for CJRA Tables 
## uses Python Programming Language; pandas and pdfminer libraries
## exports info to excel sheet (judge name, case amount, district court, circuit)

# run createExcel.py to use the code
## assumptions:
## --pdf is no more than 999,999 pages long
## --# of cases is the last int in the important list (see "organizeData.py")
## --file name has the number table (i.e., table 7 has "7" in its filename)


--
### pdfs to crawl 
CJRA Table 7: Reports Of Civil Cases Pending Over Three Years (For Period Ending March 31, 2020)
https://www.uscourts.gov/sites/default/files/data_tables/CJRA_7_03312020.pdf

CJRA Table 8: Report Of Motions Pending Over Six Months (For Period Ending March 31, 2020)
https://www.uscourts.gov/sites/default/files/data_tables/CJRA_8_03312020.pdf

CJRA Table 9: Report Of Bench Trials Submitted Over Six Months (For Period Ending March 31, 2020)
https://www.uscourts.gov/sites/default/files/data_tables/CJRA_9_03312020.pdf

note: pdfminer (library used) doesn't like it when you link to url, so just download and drag into folder
--


*some code taken from
stack overflow:
    https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python
    https://stackoverflow.com/questions/2369440/how-to-delete-all-blank-lines-in-the-file-with-the-help-of-python
*
other useful links
https://overiq.com/python-101/file-handling-in-python/
https://stackoverflow.com/questions/43438303/how-to-read-print-the-io-textiowrapper-data
http://projectpython.net/chapter08/ 
*
