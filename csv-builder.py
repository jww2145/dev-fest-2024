import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import io
import pandas as pd
from urllib.parse import unquote


big_df = pd.DataFrame(columns=['Senator','Party','State', 'Vote','vote_title','vote_issues'])
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

for bill in bill_list:
    
    try:
        
        href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
        vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
        vote_issues = bill.find('span', {'class': 'voteIssues'}).text.strip()
        bill_summary_div = bill.find('div',{'class':'field-item even'})
        bill_summary = bill_summary_div.find('p')


        
        bill_data= [{'vote_title':vote_title,'vote_issues':vote_issues, 'bill_summary': bill_summary}]
        bill_data = bill_data*100
        to_Add = pd.DataFrame(bill_data)
    
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
        df['vote_title'] = to_Add['vote_title']
        df['vote_issues'] = to_Add['vote_issues']

        big_df = pd.concat([big_df,df],ignore_index=True)
        # Display the DataFrame
        
        time.sleep(2)
        
    except Exception as e:
        
        print(f"Error occurred: {e}")

driver.quit()

big_df.to_csv('output.csv', index=False)