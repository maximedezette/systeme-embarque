from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import socket
import os
from datetime import datetime


SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'arboreal-drake-711-439eedbba062.json'
VIEW_ID = '199779379'


def initialize_analyticsreporting():
   """Initializes an Analytics Reporting API V4 service object.

    Returns:
    An authorized Analytics Reporting API V4 service object.
   """
   credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

   # Build the service object.
   analytics = build('analyticsreporting', 'v4', credentials=credentials)

   return analytics
  
def get_report(analytics,id):
    """Queries the Analytics Reporting API V4.

    Args:
      analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
      The Analytics Reporting API V4 response.
    """
    return analytics.reports().batchGet(
        body=request[id]
    ).execute()

def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response.
  Args:
    response: An Analytics Reporting API V4 response.
  """
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])
      for header, dimension in zip(dimensionHeaders, dimensions):
        print (header + ': ' + dimension)
      for i, values in enumerate(dateRangeValues):
        print ('Date range: ' + str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print (metricHeader.get('name') + ': ' + value)

#To create query https://ga-dev-tools.appspot.com/request-composer/
request = {}
request[1]={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }
request[2]={
  "reportRequests": [
    {
      "viewId": "199779379",
      "dateRanges": [
        {
          "startDate": "30daysAgo",
          "endDate": "yesterday"
        }
      ],
      "metrics": [
        {
          "expression": "ga:users",
          "alias": ""
        }
      ]
    }
  ]
}
def get_ip_address():
    return [
             (s.connect(('8.8.8.8', 53)),
              s.getsockname()[0],
              s.close()) for s in
                  [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
           ][0][1]

class InfoFactory:

  numberOfInfo = 4

  def getNumberOfInfo(self):
    return self.numberOfInfo

  def generateInfo(self,idInfo):
    analytics = initialize_analyticsreporting()

    info = []

    if idInfo == 1:
     response = get_report(analytics,idInfo)
     numberOfUserLastWeek = response.get("reports")[0].get("data").get("rows")[0].get("metrics")[0].get("values")[0]
     info.insert(0,"SEMAINE DERNIERE")
     info.insert(1,str(numberOfUserLastWeek) + " utilisateurs")

    elif idInfo == 2:
     response = get_report(analytics,idInfo)
     numberOfUserLastWeek = response.get("reports")[0].get("data").get("rows")[0].get("metrics")[0].get("values")[0]
     info.insert(0,"MOIS DERNIER")
     info.insert(1,str(numberOfUserLastWeek) + " utilisateurs")

    elif idInfo ==3:
     ip = get_ip_address()
     info.insert(0,datetime.now().strftime('%b %d  %H:%M:%S\n'))
     info.insert(1,'IP {}'.format(ip))
    
    elif idInfo ==4:
      hostname = "apero-tech.fr"
      response = os.system("ping -c 1 " + hostname)
      if response == 0:
         info.insert(0, hostname)
         info.insert(1, "  UP :)  ")
      else:
         info.insert(0,"Le site est down!!!")

    else:
     info.insert(0,"ERREUR")
    return info