from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from telegramBotManager import TelegramBotManager

import socket
import os
import requests 
import constants

from datetime import datetime 
from sqlite3 import Error

# Telegram group ID
TELEGRAM_GROUP_ID = os.environ.get('TelegramAperoTechGroupId')
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'arboreal-drake-711-439eedbba062.json'


def initialize_analytics_reporting():
   """Initializes an Analytics Reporting API V4 service object.

    Returns:
    An authorized Analytics Reporting API V4 service object.
   """
   credentials = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE_LOCATION, SCOPES)

   # Build the service object.
   analytics = build('analyticsreporting', 'v4', credentials=credentials)

   return analytics


def get_report(request, analytics,id):
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
    column_header = report.get('columnHeader', {})
    dimension_headers = column_header.get('dimensions', [])
    metric_headers = column_header.get('metricHeader', {}).get('metricHeaderEntries', [])
    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      date_range_values = row.get('metrics', [])
      for header, dimension in zip(dimension_headers, dimensions):
        print (header + ': ' + dimension)
      for i, values in enumerate(date_range_values):
        print ('Date range: ' + str(i))
        for metric_header, value in zip(metric_headers, values.get('values')):
          print (metric_header.get('name') + ': ' + value)


def get_request():
  #To create query https://ga-dev-tools.appspot.com/request-composer/
  request = {}
  request[1]={
          'reportRequests': [
          {
            'viewId': constants.VIEW_ID,
            'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
            'metrics': [{'expression': 'ga:sessions'}],
            'dimensions': [{'name': 'ga:country'}]
          }]
        }
  request[2]={
    "reportRequests": [
      {
        "viewId": constants.VIEW_ID,
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
  return request


def get_ip_address():
    return [
             (s.connect(('8.8.8.8', 53)),
              s.getsockname()[0],
              s.close()) for s in
                  [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
           ][0][1]


class InfoFactory:

  number_of_info = 4


  def get_number_of_info(self):
    return self.number_of_info


  def generate_info(self, id_info):
    analytics = initialize_analytics_reporting()
    request = get_request()
    
    info = []

    if id_info == 1:
      try:
        response = get_report(request,analytics, id_info)
        number_of_user_last_week = response.get("reports")[0].get("data").get("rows")[0].get("metrics")[0].get("values")[0]
        info.insert(0,"SEMAINE DERNIERE")
        info.insert(1,str(number_of_user_last_week) + " utilisateurs")
      except:
        print ("Erreur lors de la recuperation des visiteurs de la semaine dernière")

    elif id_info == 2:
     try:
      response = get_report(request,analytics, id_info)
      number_of_user_last_week = response.get("reports")[0].get("data").get("rows")[0].get("metrics")[0].get("values")[0]
      info.insert(0,"MOIS DERNIER")
      info.insert(1,str(number_of_user_last_week) + " utilisateurs")
     except:
       print ("Erreur lors de la recuperation des visiteurs du mois dernier")

    elif id_info == 3:
     ip = get_ip_address()
     info.insert(0,datetime.now().strftime('%b %d  %H:%M:%S\n'))
     info.insert(1,'IP {}'.format(ip))
     
    
    elif id_info == 4:
      hostname = "apero-tech.fr"
      http_status_of_host = requests.get("https://"+hostname).status_code      
      if http_status_of_host == 200:
        info.insert(0, hostname)
        info.insert(1, "Est up :)")
      else:
      # Call method for send message
        try:
          tbm = TelegramBotManager()
          tbm.send_message_to_group(constants.TELEGRAM_GROUP_ID, "@Vinvin27 Le site est down!!")
          info.insert(0, hostname)
          info.insert(1, "Est down !! :(")
        except:
          print ("Erreur lors de l'envoi de message par le Bot Telegram")

    else:
     info.insert(0, "ERREUR")
    return info