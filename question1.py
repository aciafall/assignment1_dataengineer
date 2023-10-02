import requests as r
from bs4 import BeautifulSoup
import re
import os

# get the html page of the xinhuawang
url=r"https://english.news.cn"
res=r.get(url)
html=res.text
bf=BeautifulSoup(html,'lxml')

# get the hyper-reference from the html page
# use the Regex to identify the correct link and append the link to the list
hrefs=[]
for item in bf.find_all("a"):
    href=item.get('href')
    http_pattern = re.compile(r'^https?://')
    if http_pattern.match(href):
        hrefs.append(href)

# print(hrefs)
title=0

# get the article of the link
for href_crwal in hrefs:
    # if title >=30:
    #
    response=r.get(href_crwal,verify=False)
    title+=1 # to name the article
    if response.status_code==200:
        html_crwal=response.text
        bf_crwal = BeautifulSoup(html_crwal, 'lxml')
        text = bf_crwal.get_text()
        folder_path = "./text"
        # create the folder
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # set the file name and the path
        file_name = str(title)+".txt"
        file_path = os.path.join(folder_path, file_name)

        # save the text to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

print("all news has been converted")

# for test one link
# res_test=r.get("https://english.cctv.com")
# html_test=res_test.text
# bf_test=BeautifulSoup(html_test,'lxml')
# text=bf_test.get_text()
# print(text)