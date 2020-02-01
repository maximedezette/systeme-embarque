"""Hello Analytics Reporting API V4."""

#from googleapiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials

import RPi.GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
import time
import math

lcd_rs=26
lcd_en=19
lcd_d4=13
lcd_d5=6
lcd_d6=5
lcd_d7=11

lcd_columns=16
lcd_rows=2

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'arboreal-drake-711-439eedbba062.json'
VIEW_ID = '199779379'

#To create query https://ga-dev-tools.appspot.com/request-composer/

request = {}
request['last7']={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }
request['last30']={
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


def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body=request['last30']

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


#  analytics = initialize_analyticsreporting()
 # response = get_report(analytics)
  #print_response(response)
while 1:
  lcd = Adafruit_CharLCD(lcd_rs,lcd_en,lcd_d4,lcd_d5,lcd_d6,lcd_d7,lcd_columns,lcd_rows)
  lcd.clear()
  lcd.message('Test')
  time.sleep(5.0)

