# Author: Ebrahim Muneer
# Filters FAST NUCES Google Spreadsheets timetable and returns your sections' timetable
#
# TODO: Test this program for other semesters

import pandas as pd
import re
import os

def importSheetURL():
    if os.path.exists("data.ini"):
        sheetID = None
        with open("data.ini") as f:
            sheetID = f.read().strip().split('=')[1]

        return f"https://docs.google.com/spreadsheets/u/1/d/{sheetID}/export?format=xlsx"
    else:
        iniSetup()

def iniSetup():
    url = str(input("Please enter the Google Sheet URL (one-time setup only): "))
    match = re.search(r"/d/([a-zA-Z0-9-_]+)", url)
    sheetID = None
    if match:
        sheetID = match.group(1)
    else:
        print("Invalid URL, please paste the correct Google Sheets URL\n")
        exit()

    iniToWrite = f"sheet-id={sheetID}"
    with open("data.ini", "x") as f:
        f.write(iniToWrite)
        f.close()
    
    print("Successfully created file 'data.ini'\nPlease run the program again!")
    exit()


def xlsxToDict(xlsx, sheetNum):
    df = pd.read_excel(xlsx, sheetNum)
    schedule = {}
    
    rowsToDrop = [0, 1, 2, 49, 64]
    
    df = df.drop(rowsToDrop, axis=0)
    df = df.reset_index(drop=True)
    
    day = df.columns[0]

    df.columns = ["class", 1, 2, 3, 4, 5, 6, 7, 8, 9]

    schedule = df.to_dict()
    schedule.update({"day" : day})

    return schedule

def classStringToDict(cell):
    cell = cell.replace("\n", " ").strip()
    
    pattern = re.compile(
        r"^(?P<subject>.+?)"
        r"(?:\s+(?P<lab>[Ll]ab))?"
        r"\s+(?P<section>[A-Z]+-\s*\d+\w)"
        r"\s+(?P<teacher>.+)$"
    )
    
    match = pattern.match(cell)
    if not match:
        return {
            "subject": None,
            "isLab": False,
            "section": None,
            "teacherName": None
        }
    
    subject = match.group("subject").strip()
    is_lab = bool(match.group("lab"))
    
    raw_section = match.group("section")
    section = re.sub(r"\s*-\s*", "-", raw_section.strip())
    
    teacher = match.group("teacher").strip()
    
    return {
        "subject": subject,
        "isLab": is_lab,
        "section": section,
        "teacherName": teacher
    }

def tableSolver(dict, section):
    personalTable = {}
    personalTable.update({"day" : dict["day"]})

    for i in range(1, 10):
        for j in range(65):
            if type(dict[i][j]) == str:
                data = classStringToDict(dict[i][j])
                if str(data["section"]).upper() == str(section).upper():
                    data.update({"classroom" : dict["class"][j]})
                    personalTable.update({i : data})
                    if data["isLab"] == True:
                        personalTable.update({i+1 : data})
                        personalTable.update({i+2 : data})

    return personalTable


def tableOutput(dict):
    slotmap = {
        1 : "08:00 to 08:50",
        2 : "08:55 to 09:45",
        3 : "09:50 to 10:40",
        4 : "10:45 to 11:35",
        5 : "11:40 to 12:30",
        6 : "12:35 to 13:25",
        7 : "13:30 to 14:20",
        8 : "14:25 to 15:15",
        9 : "15:20 to 16:05"
    }

    # submap = {
    #     "PF" : "Programming Fundamentals",
    #     "IST" : "Islamic Studies/Ethics",
    #     "FE" : "Functional English",
    #     "ICP" : "Internet Communications and Protocols"
    # }

    day = dict['day']
    print(f"\n{'='*40} {day} {'='*40}")
    header = f"{'Time Slot':<20}{'Classroom':<35}{'Subject':<25}{'Teacher'}"
    print(header)
    for slot, details in dict.items():
        if isinstance(slot, int):
            slot = slotmap[slot]
            subjectName = details["subject"]
            if details["isLab"]:
                subjectName = f"{details["subject"]} Lab"
            print(f"{slot:<20}{details['classroom']:<35}{subjectName:<25}{details['teacherName']}")


if __name__ == "__main__":
    url = importSheetURL()
    try:
        xlsx = pd.ExcelFile(url)
    except:
        print("Something went wrong, please check your internet connection")
        print("If this issue persists, try deleting the 'data.ini' file and doing the first time setup again")
        exit()

    try:
        section = str(input("Enter your section (e.g BCS-1J): "))
    except:
        print("Invalid ID, try again")

    for i in range(5):
        df = xlsxToDict(xlsx=xlsx, sheetNum=i)
        personalTable = tableSolver(df, section)
        tableOutput(personalTable)