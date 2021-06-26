import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
publish_date = []
skills = []
links = []
salary = []

# Use requests to fetch the url
result = requests.get("https://fr.indeed.com/Emplois-python")
#Save page Content/markup
src = result.content
#print(src)

#Creat soup object to parse content
soup = BeautifulSoup(src, "lxml")
#print(soup)

job_titles = soup.find_all("div", ({"class": "heading4 color-text-primary singleLineTitle tapItem-gutter"}))
company_names = soup.find_all("span", {"class": "companyName"})
location_names = soup.find_all("div", {"class": "companyLocation"})
skills_job = soup.find_all("div", {"class": "job-snippet"})
#link = soup.find_all("a", {"data-jk": True, "aria-labelledby": True, "data-hide-spinner": True})
#salaries = soup.find_all("span", {"class": "salary-snippet"})
date = soup.find_all("span", {"class": "date"})
#print(link)

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    skills.append(skills_job[i].text)
    publish_date.append(date[i].text)
    #links.append(link[i].find("a").attrs["href"])
#print(links)

#print("job :", job_title,"\n" ,"company :", company_name,"\n", "location:", location_name,"\n", "skills:" , skills,"\n", "publish_date:", publish_date )
#7th step creat csv file and fill it with values
file_list = [job_title, company_name, location_name, publish_date, skills]
exported = zip_longest(*file_list)
with open('/Users/BENAISSA & HOUDA/PycharmProjects/ecrt/jobs1.csv', 'w') as myfile :
    wr = csv.writer(myfile)
    wr.writerow(["job title", "company name", "location", "publish date", "skills"])
    wr.writerows(exported)
