# Author: Ebrahim Muneer
# Filters FAST NUCES Google Spreadsheets timetable and returns your sections' timetable
#
# TODO: Test this program for other semesters
# TODO: Allow for printing multiple days
# TODO: Add error checking for section input

url = "" # Add the sheets url here between the two "

import pandas as pd
import re

def fetchToDict(url):
    df = pd.read_csv(url)
    schedule = {}
    
    rowsToDrop = [0, 1, 2, 49, 64]
    
    df = df.drop(rowsToDrop, axis=0)
    df = df.reset_index(drop=True)
    
    day = df.columns[0]

    df.columns = ["class", 1, 2, 3, 4, 5, 6, 7, 8, 9]

    schedule = df.to_dict()
    schedule.update({"day" : day})

    return schedule

def classStringToDict(cell: str) -> dict:
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
    if not url:
        print("ERROR: Please edit this main.py file and add the Google Sheets link in the format specified in the README")
        exit(0)

    df = fetchToDict(url)
    section = str(input("Enter your section (e.g BCS-1J): "))
    personalData = tableSolver(df, section)
    tableOutput(personalData)