'''
Imports: 

@BeautifulSoup: used for webscraping HTML obtained from the political score-card website 
@requests: used to get the html for BeautifulSoup to scrape
@csv: used to write rows into a bills.csv 


@see https://scorecard.lcv.org/scorecard?year=2022: the website that we scraped for information regarding
    proposed bill name, proposed bill summary and the related environmental concern. 

@authors: Joshua Wu (jww2145) and Brian Echvarria (be2298)
'''
from bs4 import BeautifulSoup
import requests
import csv

# Step 1: request the HTML content from the given website
url = 'https://scorecard.lcv.org/scorecard?year=2022'
response = requests.get(url)
html = response.content

# Step 2: Parse HTML and extract the list of bills that the Senate has voted on
soup = BeautifulSoup(html, 'html.parser')
bill_list = soup.find('div', {'id': 'scorecard-votes-page-senate-table-data'}).find_all('div', {'class' : 'tableRow dataItem'})


# Step 3: Loop through the bill_list to extract information about each individual bill
for bill in bill_list:
    
    try:
        # basic bill information
        vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
        vote_issues_span = bill.find('span', class_='voteIssues')
        vote_issues = vote_issues_span.contents
        
        
        # href needed in order to extract the summary of the bill
        href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
        new_url = 'https://scorecard.lcv.org/' + href
        bill_response = requests.get(new_url)
        bill_html = bill_response.content
        
        #a new BeautifulSoup instance to scrape the sub-webpage
        bill_soup = BeautifulSoup(bill_response.content, 'html.parser')
        bill_summary_div = bill_soup.find('div',{'class':'field-item even'})
        bill_summary = bill_summary_div.find('p')

        
        # open CSV file in append mode 
        with open('bills.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write header row if file is empty
            if csvfile.tell() == 0:
                writer.writerow(["Bill", "Summary", "Issues"])

            # Write row for each bill
            row = [vote_title, bill_summary.text, vote_issues[0]]
            writer.writerow(row)
                
    except Exception as e:
        print(e) 
    