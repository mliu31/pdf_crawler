exfrom readPdf import main as read_pdf

# input raw txt file
# output clean txt file (see "cleaned_output.txt"),
# && list of dictionaries (contains information we want to export to excel)


# identifiers when reading txt lines
ID_CIRCUIT = "Circuit"  # use this string to find circuit info (in the same line as "Circuit"
ID_DISTRICT_COURT = "District Court"  # use to find the district court info (in the same line)
# ---ones below are different based on the file imported
PAGE_DIVIDER = "of "
ID_JUDGE = "Total Cases"


# extract info from raw pdf "raw_courtcases.txt" (sees if matches the above identifiers)
# puts in a new txt file "cleaned_courtcases.txt"
def extract_impt_info(txt, output):
    print("Extracting info from raw_courtcases.txt...")
    new_file_lines = []

    with open(txt.name, 'r') as inp:  # won't let me do both rw (read and write)
        for line in inp:
            if ID_CIRCUIT in line:  # page number
                new_file_lines.append(line)
            elif ID_DISTRICT_COURT in line:
                new_file_lines.append(line)
            elif ID_JUDGE in line:
                new_file_lines.append(line)
            elif PAGE_DIVIDER in line:
                new_file_lines.append(line + "\n")  # add divider sby page num
            try:  # adds all ints; last int is what we want (court case amt)
                int(line)
                new_file_lines.append(line)
            except ValueError:
                pass

    with open(output, "w") as cleaned_txt:
        cleaned_txt.writelines(new_file_lines)

    return cleaned_txt


# read "cleaned_courtcases.txt" and adds everything into a master list (each elem is a page)
def create_master_list(txt):
    print("Creating a master list; each pdf page is an element in master list...")
    master = []
    with open(txt, 'r') as inp:
        inner_list = []
        for line in inp:
            if line.isspace():  # new line is separator between the pages, create a new list element for each new page
                master.append(inner_list)
                inner_list = []
            else:
                inner_list.append(line.strip())
    return master


# loops through master list
# creates and returns new list of important info (checks if has ID_JUDGE)
def create_clean_master_list(mlist):
    print("Cleaning the master list...")
    impt_list = []
    for r in range(len(mlist)):
        has_impt_info = False
        for e in range(len(mlist[r])):
            if ID_JUDGE in mlist[r][e]:
                has_impt_info = True
                break
        if has_impt_info:
            impt_list.append(mlist[r])
            # del master_list[r]  # messes up looping

    return impt_list


# from important list, creates dictionary for each page
# stores dictionaries in a list (to convert to excel)
def create_list_of_dictionaries(mlist):
    print("Creating a list of dictionaries to export to excelsheet...")
    list_of_diction = []

    for innlist in mlist:
        d = {"circuit": "", "district_court": "", "judge": "", "case_amt": ""}

        for elem in innlist:
            if ID_JUDGE in elem:
                d["judge"] = elem.split(": ")[1]
            elif ID_DISTRICT_COURT in elem:
                d["district_court"] = elem
            elif ID_CIRCUIT in elem and "Judge" not in elem:
                d["circuit"] = elem
            # add all ints (last int will be case amt)
            try: # assume the # of cases is the last element in the list (worked for the ones i've tested)
                int(elem)
                d["case_amt"] = elem
            except ValueError:
                pass

        list_of_diction.append(d)

    return list_of_diction


def main(filename):
    global ID_JUDGE, PAGE_DIVIDER

    raw_file, page_count, filename = read_pdf(filename)
    cleaned_output = "cleaned_courtcases.txt"

    # adds commas to match the pages in the pdf (e.g., 2677--> 2,677); assumes pdf is no more than 999,999 pages long
    if len(str(page_count)) > 3:
        temp = ""
        for i in range(len(str(page_count)) - 1, -1, -1):
            if i == len(str(page_count)) - 4:
                temp = ',' + temp
            temp = str(page_count)[i] + temp
        page_count = temp

    # table 7 uses "Total All Cases" instead of "Total Cases" like in table 8, 9
    if "7" in filename:
        ID_JUDGE = "Total All Cases"

    # update page divider with page count
    PAGE_DIVIDER = "of " + str(page_count)

    # raw txt ("raw_courtcases.txt") to clean txt ("cleaned_courtcases.txt")-- removes unnecessary info
    extract_impt_info(raw_file, cleaned_output)

    # for each page (separated by \n in txt file), checks if has the information we need
    # if so, will add that page's info to master list
    master_list = create_master_list(cleaned_output)

    # loop through each element in the master list to see if it important
    clean_master_list = create_clean_master_list(master_list)

    # creates a dictionary for each important page (from clean_master_list)
    # stores and returns all dictionaries in a list
    dictionary_for_excel = create_list_of_dictionaries(clean_master_list)

    return dictionary_for_excel


if __name__ == '__main__':
    main()
