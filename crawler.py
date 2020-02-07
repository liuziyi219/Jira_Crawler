from requests_html import HTMLSession

import csv
import json
import urllib.request
import sys

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
        
def get_data(getsession,id):
    result=getsession.html.find(id)
    issue.append(result[0].text)
    
def main(args):
    issue_id=args[0]
    url="https://issues.apache.org/jira/browse/"+issue_id
    session=HTMLSession()
    r=session.get(url)
    '''copy selector for find elements'''
    get_data(r,"#type-val") 
    get_data(r,"#priority-val")
    get_data(r,"#versions-field > span")
    get_data(r,"#components-field > a")
    get_data(r,"#labels-13028113-value")
    get_data(r,"#customfield_12310041-field > span")
    get_data(r,"#customfield_12310060-val")
    get_data(r,"#status-val > span")
    get_data(r,"#resolution-val")
    get_data(r,"#fixVersions-field > a:nth-child(1)")
    get_data(r,"#issue_summary_assignee_davsclaus")
    get_data(r,"#issue_summary_reporter_bobpaulin")
    get_data(r,"#vote-data")
    get_data(r,"#watcher-data")
    get_data(r,"#created-val > time")
    get_data(r,"#updated-val > time")
    get_data(r,"#resolutiondate-val > time") 
    get_data(r,"#description-val")
    issue.append(getcomments(issue_id))
    with open("crawl.csv","w",newline="") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(["Type","Priority","Affects Version/s","Component/s","Labels","Patch Info","Estimated Complexity","Status","Resolution","Fix Version/s","Assignee","Reporter","Votes","Watchers","Created","Updated","Resolved","Description","Comments"])
        writer.writerow(issue)
        print("Down")
if __name__=='__main__':
    main(sys.argv[1:])

