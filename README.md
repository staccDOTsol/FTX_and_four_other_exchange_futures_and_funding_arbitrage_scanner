# Market Neutral POC

## Setup

1. Clone this repo
2. cd into this repo
3. Running python3.7, do python -m pip install -r requirements.txt

## Acquiring new data

1. python gather_1.py. Will take maybe an hour. You can adjust how far back it looks with 'yearago,' which isn't right now set to a year, which is the amount of time to look back for data.
2. python gather_2.py. This takes an egregious amount of time, but you can run the report as it saves data periodically. You can adjust how far back it looks with 'yearago,' which isn't right now set to a year, which is the amount of time to look back for data.

## Using sample data

1. To speed up verification, you can extract this zip in the root of the repo: https://drive.google.com/file/d/1i-81S9-vx6wJ9YjbTndCbGS8jvkBxxvv/view?usp=sharing

## Running reports

1. python report_1.py will run the reports on the first set of data
2. python report_2.py will run the 2nd leg of reports on granular data