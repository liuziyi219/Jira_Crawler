# Jira_Crawler
This is a crawler to crawl issues in Jira and save them into csv file.
## How to use it
To run the file: `python crawler.py Issue_ID`

The Issue_ID I used for example is CAMEL-10597
You can see the results in crawl.csv

## Supplement

Since it is my first time to write a crawler. I choose requests_html which is simple to use. There are also others tools like BeautifulSoup but which is also based on request and response. 

I did not crawl the comments part, instead I use the Jira Rest API to get the comments.Because HTML of comments section contains too many elements and it is complicated to combine them. Also,  Here is the tutorial: https://docs.atlassian.com/software/jira/docs/api/REST/7.6.1/#api/2/issue-getComments

The interface GET /rest/api/2/issue/{issueIdOrKey}/comment will return a json file of comments. I extract the needed contents from json and combine them.

## To crawl all the data
Jira has 14526 issue in total for now. 

I used BeautifulSoup to crawl the data at this time because it is more flexible and some element can only be find by class or other features.

And there are 2 adjustments:

1. check if the element is in the page. Some pages did not include "Environment","Description",etc.

2. Extract the time from 'datetime' instead of the text. Because some texts are "2 days ago","Yesterday" which are not timestamp.







