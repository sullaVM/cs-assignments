import os, sys
import requests
import csv

response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSRVvDrJCGpOSpgS6uYDxfIm_Ooq3Ll5P_PhaTjhxENcFcXo2PvythkYj46McVUsp-IMS1tFJgVngde/pub?gid=0&single=true&output=csv')
assert response.status_code == 200, 'Wrong status code'
data = response.content
listItem = data.split('\n')
for i in listItem:
    listContent = i.split(',')
    for j in listContent:
        print j