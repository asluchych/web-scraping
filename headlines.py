# get the latest news about Manchester United FC from a Mirror website
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime

now = datetime.now()
month_day_year = now.strftime('%m%d%Y')


# webstite to get news headlines
web = 'https://www.mirror.co.uk/all-about/manchester-united-fc'

# path to chromedriver
path = '/home/anatol/Downloads/chromedriver'

# add headless mode
options = Options()
options.headless = True
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//article[@class="story story--news"]')
titles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/div/div/h2').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    links.append(link)

my_dict = {'title': titles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

file_name = f'manutd_headlines_{month_day_year}.csv'
df_headlines.to_csv(file_name)

driver.quit()
