from bs4 import BeautifulSoup
import requests
import pandas as pd


Titles_List=[]
Category_List=[]
Amount_List=[]
Date_List=[]
City_List=[]
State_List=[]

for i in range(0,1000,10):
    s="#gsc.tab=0"
    webadd="http://www.ipaidabribe.com/reports/paid?page="
    finalweb=webadd+str(i)+s
    result=requests.get(finalweb)
    soup=BeautifulSoup(result.text,"html.parser")
    para_list=soup.find_all("section", {"class": "ref-module-paid-bribe"})
    for j in para_list:
        Title=j.find("h3", {"class": "heading-3"})
        a=Title.text
        a = a.strip('\n\r\n\r\n                    \n')
        Titles_List.append(a)
        print("DONE")


        Category= j.find("li",{"class":"transaction"})
        b=Category.text
        b=b.strip('\n\n')
        Category_List.append(b)

        Amount=j.find("li",{"class":"paid-amount"})
        c=Amount.text
        c=c.partition("Paid INR")[2]
        c=c.strip('\n\r\n                        \n')
        Amount_List.append(c)


        Date=j.find("span", {"class":"date"})
        Date_List.append(Date.text)

        Location=j.find("a", {"class":"location"})
        l=Location.text
        l=l.replace('\r\n                      ', '')
        s=l.partition(",")[2]
        s=s.strip('\r\n              \r\n')
        c=l.partition(",")[0]
        State_List.append(s)
        City_List.append(c)


Bribe_dict={"TITLE":Titles_List,
            "CATEGORY":Category_List,
            "CITY":City_List,
            "STATE":State_List,
            "DATE":Date_List,
            "AMOUNT":Amount_List
            }
print(Bribe_dict)

Data=pd.DataFrame(Bribe_dict)
Data.to_csv("NEW_BRIBE100")
print("SUCCESS")





