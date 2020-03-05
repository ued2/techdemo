import MinerFunctions
import requests 
import json
#import psycopg2
#import sys
# used to access scripts in other directories
# path needs to be changed to work on local 

#ProfileMiner.runEverything(username)
#import sys
# used to access scripts in other directories
# path needs to be changed to work on local 

#path = '/Users/udk/Desktop/OSSMatching/TestDatabaseScripts'
#sys.path.insert(0, path)
#import config
#from query import githubusername


url = 'http://64.227.61.240:8000/github/'
r = requests.get(url)
data = json.loads(r.github)

print(data)

#github username from db gets last one entered
#username = githubusername()
#print(username)
#test username davidxia
#username = input("Enter a GitHub username: ")
#print(username)

#MinerFunctions.runEverything(username)