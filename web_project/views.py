from django.shortcuts import render
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import regex as re
import pandas
import csv

import datetime

def button(request):
    return render(request,'home.html')

def output(request):      
    currentDT = datetime.datetime.today()
    print(str(currentDT))
    filename='ROckfellar-' + str(currentDT) + str('.csv')
    print(filename)
    ua=UserAgent()
    s="Rockfellar Institute"
    number=3
    pages=0

    pages=[]
    for i in range(0,30):
        url1="http://www.google.com/search?q=" + s + "&tbm=nws" +  "&start=" + str(i)
        pages.append(url1)
    print("pages")
    print(pages)
    i=0
    links = []
    titles = []
    dates = []
    for page1 in  pages:
        page = requests.get(page1)
        print(page.status_code)  # Print the status code
        print(page.text)
        print(page1)
        soup=BeautifulSoup(page.content)
        results=soup.findAll('div',attrs={'class':'g'})
        print(i)
        print(results)
        for r in results:
            try:
                print("tryyy")
                link = r.find('a', href=True)
                print(link)

                title = r.find('h3', attrs={'class': 'r'})
                print(title.text)

                time = r.find('div', attrs={'class': 'slp'})
                print(time.text)
                date=time.text.split("-")
                time11=date[1]
                print(time11)

                if link != '':
                    links.append(link['href'])
                else :
                    links.append("not available")
                if title != '' :
                    titles.append(title.text)
                else:
                    titles.append("Title Unavaible")
                if time11 != '':
                    dates.append(time11)
                else:
                    dates.append("not avaiable")
            #descriptions.append(description)
        # Next loop if one element is not present
            except:
                continue

    to_remove = []
    cleanlinks = []
    for i, l in enumerate(links):
        clean = re.search('\/url\?q\=(.*)\&sa',l)
    # Anything that doesn't fit the above pattern will be removed
        print(clean)
        if clean is None:
            to_remove.append(i)
            continue
        cleanlinks.append(clean.group(1))
        print(cleanlinks)
    for x in to_remove:
        del titles[x]
        print(titles)

    print(cleanlinks)
    print(titles)

    with open('8.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Links', 'Dates'])
        writer.writerows(zip(titles, cleanlinks,dates))
    print(filename)        
    return render(request,'home.html',{'data':url1,'Links':cleanlinks})