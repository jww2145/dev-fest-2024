from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import re


url = 'https://scorecard.lcv.org/scorecard?year=2022'
response = requests.get(url)
html = response.content

bill_summary_csv = pd.DataFrame(columns=["Bill", "Summary", "Issues"])

# Step 2: Parse HTML and extract bill information
soup = BeautifulSoup(html, 'html.parser')
bill_list = soup.find('div', {'id': 'scorecard-votes-page-senate-table-data'}).find_all('div', {'class' : 'tableRow dataItem'})



for bill in bill_list:
    
    try:
        
        href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
        vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
        vote_issues_span = bill.find('span', class_='voteIssues')

        # Get text and strip whitespace
        
        vote_issues = vote_issues_span.contents
        
        new_url = 'https://scorecard.lcv.org/' + href
        
        bill_response = requests.get(new_url)
        bill_html = bill_response.content
        
        bill_soup = BeautifulSoup(bill_response.content, 'html.parser')
        
        bill_summary_div = bill_soup.find('div',{'class':'field-item even'})
        
        bill_summary = bill_summary_div.find('p')

        
            # Open CSV file in append mode 
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
    