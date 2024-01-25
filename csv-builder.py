import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import csv

# Step 1: Send request and get HTML response
url = 'https://scorecard.lcv.org/scorecard?year=2022'
response = requests.get(url)
html = response.content

# Step 2: Parse HTML and extract bill information
soup = BeautifulSoup(html, 'html.parser')
bill_list = soup.find('div', {'id': 'scorecard-votes-page-senate-table-data'}).find_all('div', {'class' : 'tableRow dataItem'})

bill_data = []
vote_data = []
for bill in bill_list[:3]:
    vote_year = bill.find('span', {'class': 'voteYear'}).text.strip()
    vote_number = bill.find('span', {'class': 'voteNumber'}).text.strip()
    href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
    vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
    vote_issues = bill.find('span', {'class': 'voteIssues'}).text.strip()
    
    new_url = 'https://scorecard.lcv.org/' + href
    

    driver = webdriver.Chrome()
    driver.get(new_url)
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="scorecard-table-export"]')))  

    driver.find_element_by_xpath('//a[@class="scorecard-table-export"]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="scorecard-table-export"]')))
    csv_link = driver.find_element_by_xpath('//a[@class="scorecard-table-export"]').get_attribute('href')
    response = requests.get(csv_link)
    csv_file = response.content
    
    print(csv_file)
    break;
    
    # soup1 = BeautifulSoup(response1.content, 'html.parser')
    
    # vote_list = soup1.find('div', {'class': 'tableRow pagination scFooter greenpage'})
    # print(vote_list)
    # bill_data.append([vote_year, vote_number, vote_title, vote_issues])

    # Append the extracted data to the list
    




print(bill_data[0])