import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv
job_name=[]
company_name=[]
location_=[]
typeof_job=[]
applaying_link=[]
job_details=[]
web_page=0
while web_page<=4:     
     website=(f'https://wuzzuf.net/search/jobs/?a=navbg%7Cspbg&q=web%20scraping&start={web_page}')
     url=requests.get(website)
     soup=BeautifulSoup(url.text,'html.parser')
     #website data extraction
     jobname=soup.find_all('h2',class_='css-m604qf')
     Companyname=soup.find_all('a',class_='css-17s97q8')
     location=soup.find_all('span',class_='css-5wys0k')
     typeofjob=soup.find_all('span',class_='css-1ve4b75 eoyjyou0')
     #for loop to get data from home page
     for i in range(len(jobname)):
          job_name.append(jobname[i].text)
          applaying_link.append(jobname[i].find('a').attrs['href'])
          company_name.append(Companyname[i].text)
          location_.append(location[i].text)
          typeof_job.append(typeofjob[i].text)
     web_page=web_page+1
     print(web_page,'Processed pages')
# Save the data to a CSV file
     data = zip_longest(job_name, company_name, location_, typeof_job, applaying_link)
     with open('C:\\Users\\gmeyg\\Downloads\\classes\\data_analisys.csv', 'w') as job_scrabing_file_envo:
               writer = csv.writer(job_scrabing_file_envo)
               writer.writerow(["Job Name", "Company Name", "Location", "Type of Job", "Applying Link"])
               writer.writerows(data)
print('DONE')