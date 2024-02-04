'''
This script was made to scrape information about votes from senators 
Because the website we scraped had an "Export CSV" button, we had to 
open a Chrome driver that could click on each download button for us. 

We have included the output in './votes.csv', but in the case that you would
want to run the script yourself, beaware that it takes around 30-45 minutes to
build. 

@authors Joshua Wu (jww2145) 
'''


'''
Imports:

@BeautifulSoup: used to scrape the html elements that needs to be clicked
@selenium: used to create a Chrome webdriver that will download csv files 
@pandas, @unquote and @io: used to process downloaded csv from selenium 
@time: force the webdriver to wait 1 second before moving on to the next page (for consistency reasons)
'''
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


#the final dataframe result that will be converted to a csv file
big_df = pd.DataFrame(columns=['Senator','Party','State', 'Vote','Vote_Title','Vote_Issues', 'Vote_Summary'])

#Step 1: request the html content to get a full list of bills that need to be scraped 
url = 'https://scorecard.lcv.org/scorecard?year=2022'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
bill_list = soup.find('div', {'id': 'scorecard-votes-page-senate-table-data'}).find_all('div', {'class' : 'tableRow dataItem'})


#Step 2: build the webdriver to click on the 'Export CSV' button on each bill page 
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,  # To disable downloads (otherwise, it will download ~600 bills on your desktop)
    "download.directory_upgrade": True,     
    "safebrowsing.enabled": True,           # To enable Safe Browsing
    "download_restrictions": 3              
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)  # Implicit wait


#Step 3: loop through the bill list to extract necessary data
for bill in bill_list:
    
    try:
        
        #collecting the title of the bill as well as the list of issues 
        vote_title = bill.find('span', {'class': 'voteTitle'}).text.strip()
        vote_issues = bill.find('span', {'class': 'voteIssues'}).text.strip()


        #need to request content from the subpage to collect information about the bill
        href = bill.find('span', {'class': 'voteTitle'}).find('a')['href']
        new_url = 'https://scorecard.lcv.org/' + href
        bill_response = requests.get(new_url)
        bill_html = bill_response.content
        
        #a new BeautifulSoup instance to scrape the sub-webpage
        bill_soup = BeautifulSoup(bill_response.content, 'html.parser')
        bill_summary_div = bill_soup.find('div',{'class':'field-item even'})
        bill_summary = bill_summary_div.find('p').text
        
        #replicate the data 100 times - once for each senator 
        bill_data= [{'Vote_Title':vote_title,'Vote_Issues':vote_issues, 'Bill_Summary': bill_summary}]
        bill_data = bill_data*100
        to_Add = pd.DataFrame(bill_data)



        #opening up a chrome driver to click on the 'Export CSV button' to collect data on senator votes
        driver.get(new_url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="scorecard-table-export"]')))  
        driver.find_element("xpath",'//a[@class="scorecard-table-export"]').click()
        csv_link = driver.find_element("xpath",'//a[@class="scorecard-table-export"]').get_attribute('href')
        
        #processing the downloaded csv file
        encoded_csv = csv_link.split(',', 1)[1]
        # Decode the URL-encoded CSV data
        decoded_csv = unquote(encoded_csv)
        # Convert the decoded CSV data to a file-like object
        csv_file_like = io.StringIO(decoded_csv)
        
        # Read into a pandas DataFrame
        df = pd.read_csv(csv_file_like)
        
        #injecting information from previously scraped data
        df['Vote_Title'] = to_Add['Vote_Title']
        df['Vote_Issues'] = to_Add['Vote_Issues']
        df['Vote_Summary'] = to_Add['Bill_Summary']

        #combine with the big dataframe
        big_df = pd.concat([big_df,df],ignore_index=True)
        
        
        time.sleep(1)
        
    except Exception as e:
        
        print(f"Error occurred: {e}")
        

driver.quit()

big_df.to_csv('votes.csv', index=False)
