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

Finally, run the program

    python3 main.py

If you're running the program for the first time, it will prompt you to enter the URL of the timetable's Google Sheet:

    Please enter the Google Sheet URL (one-time setup only): <enter URL here>

After that, just run the program again and enter your full section code when prompted. For e.g: `BCS-1J` (no spaces between the dash)

### Notes

Ensure that you enter the correct Google Sheet URL, I couldn't hardcode the link in as I wasn't sure if I'm allowed to share it publically.

Ensure that you have an internet connection when running the program as it pulls the timetable each time you run the program. This is done to ensure that you get the most recent and updated timetable each time.

- Future Updates:
    - Personal timetable PDF Generator (no guarantees on when)
    - Google Calender integration (maybe, google's api is a pain to use)

## License

This project is open-source under the [MIT License](LICENSE).