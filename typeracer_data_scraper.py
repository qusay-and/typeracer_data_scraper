import requests
import argparse
from bs4 import BeautifulSoup

# create an argument parser object
parser = argparse.ArgumentParser(description="This is a simple python script scrapes typeracer data and stores it in a text file.")

# Set the flags that can be used with the script
parser.add_argument('-u', '--username', required=True, help='Typeracer username', type=str)
parser.add_argument('-o', '--output', default='output.txt', help='Output file name', type=str)
parser.add_argument('-r', '--races', default=0, help='number of races to scrape [default all races]', type=int)

# Parse the arguments
args = parser.parse_args()

# update races data
requests.get(f'https://typeracerdata.com/import?username={args.username}')
print("Finished Requesting Data update")

# Get the number of races
def get_races():
    url = f'https://typeracerdata.com/profile?username={args.username}'

    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')

    td = soup.find_all('table')[0].find_all('td')[0].text

    return td.replace(',', '')

# store the nubmer of races to request races data
number = int(get_races())
if args.races > 0 and args.races <= number:
    number = args.races
print(f'{number} races to scrape, Hold on')

# request the site with the number of races
url = f'https://typeracerdata.com/profile?username={args.username}&last={number}'

# Store the request text
html = requests.get(url).text

# Initialize the BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# holds all the <td> tags in the races data table
td = soup.find_all('table')[2].find_all('td')

# open the output.txt file for storing the data
output_file_name = args.output
out_file = open(output_file_name, 'w')

print("Fitched Data time to write it to a file")

# carve the data from the table and store it in output.txt
for i in range(0, len(td), 7):
    # race number
    out_file.write(td[i].text[0:-1])
    out_file.write(' ')

    # date and time
    out_file.write(td[i+1].text)
    out_file.write(' ')

    # wpm
    out_file.write(td[i+2].text)
    out_file.write(' ')

    # accuracy 
    out_file.write(td[i+5].text.replace('%', ''))
    out_file.write(' ')

    # points
    out_file.write(td[i+6].text)
    out_file.write('\n')

# close output_file
out_file.close()

print(f"Your all set up, go check {args.output}")