import requests
from fake_useragent import UserAgent
from BeautifulSoup import  BeautifulSoup
import regex as re
import pandas
from itertools import izip
import csv

import datetime

currentDT = datetime.datetime.today()
print (str(currentDT))
filename='ROckfellar-' + str(currentDT) + str('.csv')
print filename
ua=UserAgent()
#page=requests.get("https://www.google.com/search?q=%22Rockefeller+Institute%22&rlz=1C1NHXL_enIN687IN700&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjvseLx_p3iAhVCnuAKHZFfDNMQ_AUIDigB&biw=1396&bih=642")
#soup=BeautifulSoup(page.content)
s="Rockfellar Institute"
number=3
pages=0
#page = requests.get("https://searx.ch/search?" + s + "&pageno=" + str(number))
#page = requests.get("http://www.google.com/search?q=" + s + "&tbm=nws" + "&start=" + str(pages)+ "&num=" + str(number))

#page = requests.get("http://www.google.com/search?q=" + s + "&tbm=nws", params=dict(   page=5))
#i=2

pages=[]
for i in range(0,30):
    url1="http://www.google.com/search?q=" + s + "&tbm=nws" +  "&start=" + str(i)
    pages.append(url1)
print "pages"
print pages
i=0
links = []
titles = []
dates = []
for page1 in  pages:
    page = requests.get(page1)
    print "iiiiiiiiiiiiii"
    print i
    i=i+1
    print(page.status_code)  # Print the status code
    print(page.text)
    print(page1)
    soup=BeautifulSoup(page.content)


    results=soup.findAll('div',attrs={'class':'g'})
    print i
    print results
    for r in results:

      try:
        print "try"
        link = r.find('a', href=True)
        print link
        print "try1"

        title = r.find('h3', attrs={'class': 'r'})
        print title.text
        print "try2"

        time = r.find('div', attrs={'class': 'slp'})
        print time.text
        date=time.text.split("-")
        time11=date[1]
        print time11
        print "try3"

        if link != '':
            print "inside if"
            links.append(link['href'])
        else :
            links.append("not available")
        if title != '' :
            print links
            titles.append(title.text)
        else:
            titles.append("Title Unavaible")
            print titles
        if time11 != '':
            dates.append(time11)
        else:
            dates.append("not avaiable")
            #descriptions.append(description)
        # Next loop if one element is not present
      except:
        continue

print "links"
print links
print "title"
print titles
print dates

print i
to_remove = []
cleanlinks = []
for i, l in enumerate(links):
    clean = re.search('\/url\?q\=(.*)\&sa',l)
    # Anything that doesn't fit the above pattern will be removed
    print clean
    if clean is None:
        to_remove.append(i)
        continue
    cleanlinks.append(clean.group(1))
    print cleanlinks
# Remove the corresponding titles & descriptions
for x in to_remove:
    print "inside x"
    del titles[x]
    print titles

print cleanlinks
print titles






#l = [[1, 2], [2, 3], [4, 5]]
#out = open('4.csv', 'w')
##   for column in row:
  #      out.write('%d;' % column)
   # out.write('\n')
#out.close()

myData = [titles,cleanlinks,dates]
mydata=[[1,2,3],[4,5,6],[7,8,9]]
#csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_NONE,skipinitialspace=True,escapechar='\n')



with open('8.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Links', 'Dates'])
    writer.writerows(izip(titles, cleanlinks,dates))

#with open('2.csv','a+') as fileee:
 #   writer = csv.writer(fileee)
  #  writer.writerow(['Title','Links','Dates'])
    #for i in titles :
     #   writer.writerow([titles[i],cleanlinks[i],dates[i]])
   # writer.writerows(myData)

    #for row in myData:
     #    writer.writerow(zip())
#fileee.close()


#df = pandas.DataFrame(myData)
#df.to_csv('test.csv', index=False, header=False)
#columns = ["Titles","Links","Dates"] #a csv with 3 columns
#print columns
#index1 = [i[0] for i in myData] #first element of every list in yourlist
#print index1
#not_index_list = [i[0:] for i in myData]
#print not_index_list
#pd = pandas.DataFrame(not_index_list, columns = columns, index = index1)

#pd.to_csv("mylist.csv")
print filename



