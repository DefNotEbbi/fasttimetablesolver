# FAST Timetable Solver

This program filters the provided Google Spreadsheet Timetable from FAST NUCES and creates a timetable for you based on your section

## Setup

Make sure Python 3 is installed on your system

Clone the project

    git clone https://github.com/DefNotEbbi/fasttimetablesolver.git
    cd fasttimetablesolver

Create a Python virtual environment and install dependencies

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

Replace the url at the start of the `main.py` file with the spreadsheet url, ensure that its in this format:

    https://docs.google.com/spreadsheets/d/<sheet_id>/export?format=csv&gid=<gid>

Finally, run the program

    python3 main.py

It will prompt you for your section, check your flex portal for your exact section and enter that, for e.g, `BCS-1J`

### Notes

Make sure to enter the Google Spreadsheets URL into the program, I couldn't leave the link in as I wasn't sure if I'm allowed to share it publically.

- Planned Updates:
    - Generating Timetable for multiple days at the same time
    - Making it easier to add sheet URLs to the program without the weird formatting
    - Personal timetable PDF Generator (no guarantees on when)
    - Google Calender integration (maybe, google's api is a pain to use)

## License

This project is open-source under the [MIT License](LICENSE).