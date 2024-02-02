#right now, the issue is that when i'm looping through senators, it will keep deleting per bill
#so kamala harris was senator in 2020, for every bill she votes on, my program will minus a senator
#effectively, double counting
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import io
from urllib.parse import unquote



big_df = pd.DataFrame(columns=['Senator','Party','State', 'Vote','Vote_Title','Vote_Issues', 'Vote_Summary'])
url = 'https://scorecard.lcv.org/scorecard?year=2022'
response = requests.get(url)
html = response.content
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,  # To disable download prompt
    "download.directory_upgrade": True,     # To enable directory monitoring
    "safebrowsing.enabled": True,           # To enable Safe Browsing
    "download_restrictions": 3              # To restrict all downloads
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Implicit wait

soup = BeautifulSoup(html, 'html.parser')
bill_list = soup.find('div', {'id': 'scorecard-votes-page-senate-table-data'}).find_all('div', {'class' : 'tableRow dataItem'})

for bill in bill_list:
    
    try:
        
        href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
        vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
        vote_issues = bill.find('span', {'class': 'voteIssues'}).text.strip()

        new_url = 'https://scorecard.lcv.org/' + href
        bill_response = requests.get(new_url)
        bill_html = bill_response.content
        
        #a new BeautifulSoup instance to scrape the sub-webpage
        bill_soup = BeautifulSoup(bill_response.content, 'html.parser')
        bill_summary_div = bill_soup.find('div',{'class':'field-item even'})
        bill_summary = bill_summary_div.find('p').text
        
        bill_data= [{'Vote_Title':vote_title,'Vote_Issues':vote_issues, 'Bill_Summary': bill_summary}]
        bill_data = bill_data*100
        to_Add = pd.DataFrame(bill_data)

        
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
        df['Vote_Title'] = to_Add['Vote_Title']
        df['Vote_Issues'] = to_Add['Vote_Issues']
        df['Vote_Summary'] = to_Add['Bill_Summary']

        big_df = pd.concat([big_df,df],ignore_index=True)
        
        time.sleep(1)
        
    except Exception as e:
        
        print(f"Error occurred: {e}")
        

driver.quit()

big_df.to_csv('votes.csv', index=False)
