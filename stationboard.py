import datetime
import getopt
import json
import requests
import sys
from tabulate import tabulate

def do_request(ID):
  url = "http://transport.opendata.ch/v1/stationboard?id="+ID+"&limit=10"
  r = requests.get(url)
  return r.json()

def print_station_infos(data):
  for stationboard in data['stationboard']:
    table = [["Nummer",stationboard['number']],["Ziel",stationboard['to']],
    ["Zeit",(datetime.datetime.fromtimestamp(int(stationboard['stop']['departureTimestamp'])).strftime('%H:%M'))]]
    
    print tabulate(table)

def main(argv):
   ID = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ID="])
   except getopt.GetoptError:
      print 'Usage: stationboard.py [options]'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'Usage: stationboard.py -i <ID>'
         sys.exit()
      elif opt in ("-i", "--ID"):
         ID = arg
   data = do_request(ID);
   print_station_infos(data);

if __name__ == "__main__":
   main(sys.argv[1:])