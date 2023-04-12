# typeracer_data_scraper
 this is my python script to get typeracer user's data

## setup
to install the requirements use the following commands
```bash
pip install -r requirements.txt
```

## usage
just need to provide typeracer account username
```bash
python typeracer_data_scraper.py -u USERNAME
```

## Help
for more help use the following ocmmand
```bash
python typeracer_data_scraper.py -h

usage: typeracer_data_scraper.py [-h] -u USERNAME [-o OUTPUT] [-r RACES]

Simple python script to scrape typeracer data.

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Typeracer username
  -o OUTPUT, --output OUTPUT
                        Output file name
  -r RACES, --races RACES
                        number of races to scrape [default all races]
```