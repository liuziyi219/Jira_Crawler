# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 02:12:06 2020

@author: lenovo
"""

from bs4 import BeautifulSoup
import urllib.request
import csv
import json
import sys
import os
issue=[]

'''process comments json'''
def getcomments(issue_id):
    url="https://issues.apache.org/jira/rest/api/2/issue/"+issue_id+"/comment"
    resp=urllib.request.urlopen(url)
    com_json=json.loads(resp.read())
    comments=""
    for i in range(0,com_json["total"]):
        comments+='{'+com_json["comments"][i]["updateAuthor"]["displayName"]+','+com_json["comments"][i]["created"]+","+com_json["comments"][i]["body"]+'}'
    return comments

def check(soup,ele_id):
    if(soup.find(id=ele_id)):
        return soup.find(id=ele_id).get_text()
    return " "

if __name__=='__main__':
    with open("jira_issues.csv","w",newline="",encoding="utf-8-sig") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(["Issue Key","Type","Status","Priority","Affects Version/s","Fixed Version/s","Component/s","Labels","Environment","Estimated Complexity","Resolution","Assignee","Reporter","Votes","Watchers","Created","Updated","Resolved","Description","Comments","Patch Info","Flags"])
        for i in range(1,14527):
            issuekey="CAMEL-"+str(i)
            url="https://issues.apache.org/jira/browse/"+issuekey
            req=urllib.request.Request(url)
            webpage=urllib.request.urlopen(req)
            html=webpage.read()
            soup=BeautifulSoup(html,'html.parser')
            issue.append(issuekey)
            issue.append(soup.find(id='type-val').get_text())
            issue.append(soup.find(id='status-val').get_text())
            issue.append(check(soup,'priority-val'))
            issue.append(check(soup,'versions-val'))
            issue.append(check(soup,'fixVersions-field'))
            issue.append(check(soup,'components-field'))
            if(soup.find(attrs={"class":"labels"})):
                issue.append(soup.find(attrs={"class":"labels"}).get_text())
            else:
                issue.append("")
            issue.append(check(soup,'environment-val'))
            if(soup.find(name='div',attrs={"class":"value type-select"})):
                issue.append(soup.find(name='div',attrs={"class":"value type-select"}).get_text())
            else:
                issue.append("")
            issue.append(check(soup,'resolution-val'))
            issue.append(check(soup,'assignee-val'))
            issue.append(check(soup,'reporter-val'))
            issue.append(check(soup,'vote-data'))
            issue.append(check(soup,'watcher-data'))
            issue.append(soup.find(id="created-val").find(name="time").get('datetime'))
            if(soup.find(id="updated-val")):
                issue.append(soup.find(id="updated-val").find(name="time").get('datetime'))
            else:
                issue.append("")
            if(soup.find(id="resolutiondate-val")):
                issue.append(soup.find(id="resolutiondate-val").find(name="time").get('datetime'))
            else:
                issue.append("")
            issue.append(check(soup,'description-val'))
            issue.append(getcomments(issuekey))
            writer.writerow(issue)
            issue.clear()
            print(issuekey)
    print("Down")
'''


'''