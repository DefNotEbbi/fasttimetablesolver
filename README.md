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

Replace the url at the start of the `main.py` file and then just run the program

    python3 main.py

### Notes and warnings

Currently this program only searches each cell using the latter half of your section code, in testing it was fine for my section but I later realised that this doesn't work for everyone (will fix soon)

Make sure to enter the Google Spreadsheets URL into the program, I couldn't leave the link in as I wasn't sure if I'm allowed to share it publically. Besides they'll probably give us a new one for another day anyways

Ensure that it's in the following format:

    https://docs.google.com/spreadsheets/d/<sheet_id>/export?format=csv&gid=<gid>

## License

This project is open-source under the [MIT License](LICENSE).