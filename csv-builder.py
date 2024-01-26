import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os
import csv
import base64
import io
import pandas as pd
from urllib.parse import unquote

# Step 1: Send request and get HTML response
url = 'https://scorecard.lcv.org/scorecard?year=2022'
response = requests.get(url)
html = response.content



# Set up Chrome options
chrome_options = webdriver.ChromeOptions()

# Disable automatic downloads
prefs = {
    "download.prompt_for_download": False,  # To disable download prompt
    "download.directory_upgrade": True,     # To enable directory monitoring
    "safebrowsing.enabled": True,           # To enable Safe Browsing
    "download_restrictions": 3              # To restrict all downloads
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver with the updated options parameter
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Implicit wait


# Step 2: Parse HTML and extract bill information
soup = BeautifulSoup(html, 'html.parser')
bill_list = soup.find('div', {'id': 'scorecard-votes-page-senate-table-data'}).find_all('div', {'class' : 'tableRow dataItem'})

bill_data = []
vote_data = []


for bill in bill_list:
    
    try:
    
        vote_year = bill.find('span', {'class': 'voteYear'}).text.strip()
        vote_number = bill.find('span', {'class': 'voteNumber'}).text.strip()
        href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
        vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
        vote_issues = bill.find('span', {'class': 'voteIssues'}).text.strip()
    
    
    
    
        new_url = 'https://scorecard.lcv.org/' + href

        driver.get(new_url)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="scorecard-table-export"]')))  

        driver.find_element("xpath",'//a[@class="scorecard-table-export"]').click()

        csv_link = driver.find_element("xpath",'//a[@class="scorecard-table-export"]').get_attribute('href')
        
        encoded_csv = csv_link.split(',', 1)[1]

        # Decode the URL-encoded CSV data
        decoded_csv = unquote(encoded_csv)

        # Convert the decoded CSV data to a file-like object
        csv_file_like = io.StringIO(decoded_csv)

        # Read into a pandas DataFrame
        df = pd.read_csv(csv_file_like)

        # Display the DataFrame
        print(df.head())
        
        time.sleep(2)
    except Exception as e:
        print(f"Error occurred: {e}")

driver.quit()