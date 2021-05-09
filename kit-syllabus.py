
from bs4 import BeautifulSoup
import requests as r
import pandas as pd
import re

courseName =[]
classID= []
cred_list=[]
year_list=[]
sem_list=[]

pages_to_find = 4
pages =[]
for i in range(1,pages_to_find+1):
    urls = f'https://www.syllabus.kit.ac.jp/?c=search_list&sk=99&dc=01&ac=05&sc=040&page={i}'   #機械工学課程の科目のみ
    pages.append(urls)

# print(pages)

for url in pages:
    try:
        response = r.get(url).text
        soup = BeautifulSoup(response,'lxml')
        print(r.get(url))
    except:
        print("Page cannot be found. Try again.")


    # COURSE TITLE
    for x in soup.find_all('tr'):
        if x.a != None:
            title = x.find('form').a.text
            course_title = re.split(r'([a-zA-Z]+)', title)[0]
            courseName.append(course_title)

    ## TIMETABLE NUMBER
    for x in soup.find_all('tr'):
        if x.a != None:
            class_id = x.find('td').text
            classID.append(class_id)

    ## CREDITS
    for y in soup.find('table',class_='gen_tbl2 data_list_tbl').find_all('tr'):
        if y != None:
            credits = y.find_all('td')
            for x in credits[4:5]:
                data = {}
                # print(x.text)
                data['Credit'] = x.text
                cred_list.append(int(x.text)) #change string to integer for credits.

    ## Year
    for y in soup.find('table',class_='gen_tbl2 data_list_tbl').find_all('tr'):
        if y != None:
            year = y.find_all('td')
            for x in year[6:7]:
                # print(x.text[0])
                data['Year'] = x.text[0]
                year_list.append(x.text[0])

    ## SEMESTER
    for y in soup.find('table',class_='gen_tbl2 data_list_tbl').find_all('tr'):
        if y != None:
            sm = y.find_all('td')
            for x in sm[7:8]:
                y = x.text
                sem =  re.split(r'([a-zA-Z]+)', y)[0]
                data['Semester'] = sem
                sem_list.append(sem)

## Change multiple lists into a dictionary
data = {'Timetable number' : classID,
    'Course name': courseName,
        'Credits' : cred_list,
        'Year' : year_list,
        'Semester' : sem_list
    }

## Create dataframe from the dictionary
df = pd.DataFrame(data=data)
df.index+=1

## Save as csv file
df.to_csv('syllabus-output.csv',index=True,header=True) 