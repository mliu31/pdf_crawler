from organizeData import main as d_to_ex
import pandas as pd

def main():
    file = input("This program is a pdf crawler for CJRA Tables. It exports info to an excel sheet "
                 "(judge name, case amount, district court, circuit). \nMake sure you've downloaded the pdf you want "
                 "to crawl and that it's in the same folder as this program. "
                 "\nWhat's the filename? (include .pdf)\n>>>")

    excelsheet = input("What do you want the excel sheet to be called? (include .xlsx)\n>>>")

    courtcases = d_to_ex(file)

    df = pd.DataFrame.from_dict(courtcases)
    # print(df)

    df.to_excel(excelsheet)
    print("Complete. See " + excelsheet + " in the folder.")


if __name__ == '__main__':
    main()
