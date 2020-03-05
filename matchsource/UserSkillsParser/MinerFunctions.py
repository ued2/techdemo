# importing the requests library
import requests
import json
import csv
import sys
import os
from git.repo.base import Repo
from datetime import datetime, timedelta
import os.path
from os import path
import shutil
import pickle
import schedule 
import time 
import git
import subprocess
from subprocess import check_output
import databaseMAIN
import pandas as pd

# delete ~/matchsource

################################################################################################################################################
################################################################################################################################################
#function used to find the difference between two lists
def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 

################################################################################################################################################
################################################################################################################################################
def githubProjectDownloader(user):
    
    #username and token so that I can make more requests per hour
    username = 'joedanciu'
    token = 'ebad37771d9f132dc822a3639df28a8c6d2e5e78'

    # TODO 
    # Grab the users username from a HTML form using Django 

    #input_username = raw_input("Enter a GitHub username: ")
    input_username = user

    #create a call to the api to check if the username is real 
    URL_username = "https://api.github.com/users/" + input_username

    #start to check if the username is valid
    username_check = requests.get(URL_username)

    #print statements if the URL is valid..aka the username is correct.. 200 = request succeeded
    if username_check.status_code == 200:
        #print("")
        pass
        
    #terminate the program if the username is invalid
    else:
        #print(" ")
        #print('INVALID USERNAME')
        sys.exit()

    #the username is valid so add it to the database/function    #######################################
    #usernameCollector(input_username)

    #get the current date
    date2 = datetime.date(datetime.now())

    #subtract 90 days from the current date
    date1 = date2 - timedelta(days=90)

    #produce the url in the 90 day requirement frame
    URL2 = "https://api.github.com/search/issues?q=author:" + input_username + "+type:pr+is:merged+created:" + str(date1) + ".." + str(date2)

    #start to check if the dates entered are valid
    request = requests.get(URL2)

    #print statements if the URL is valid..aka the dates are correct
    if request.status_code == 200:
        #print(" ")
        #print(
           # "========================================STARTING PULL REQUESTS FROM " + input_username + "=========================================")
        #print(" ")
        pass

    #terminate the program if the dates are invalid
    else:
        #print(" ")
        #print('INVALID DATE/DATES')
        sys.exit()

    #connect to GitHub using the url and authentication token
    r = requests.get(url=URL2, auth=(username,token))

    #load the data so you can parse through it
    data = json.loads(r.text)

    #print(data)

    #count how many contributions the user has made
    count = int(data['total_count'])

    #count how many repos the user has contributed to
    repo_count = len(data['items'])


    #print("Total number of pull requests merged for " + input_username + " is " +
          #str(count) + " from " + str(repo_count) + " repositories." )
    #print(" ")

    #index used for parsing through JSON data
    index = 0

    #list used to store projects that have been contributed to
    user_project_list = []


    while index < repo_count:
        #get the url of the project that they have contributed to
        url3 = data['items'][index]['repository_url']

        #go to that repository url
        r = requests.get(url=url3, auth=(username, token))

        #load that repositories data
        data2 = json.loads(r.text)

        #check if its language is JAVA
        if str(data2['language']) == 'Java':

            #check if you have already added this project into the user_project_list
            if url3 in user_project_list:

                #if its already in the list, do nothing
                #print("Project " + url3 + " is already cloned.")
                pass

            else:

                #if the project is new, add it to the list
                user_project_list.append(url3)

                #check if the project is already downloaded (from previous attempts)...this is more used for testing
                if path.exists("UserSkillsParser/Projects/" + data2['name']):

                    #print("Hmm...it seems like " + data['items'][index]['repository_url'] + " is already downloaded from a previous attempt. I'm going to skip over that one.")
                    pass

                else:

                    #print("Cloning repo..." + data['items'][index]['repository_url'] + " because its a " + str(data2['language']) + " project")

                    #remove the api. from the url mined
                    updatedurl3 = url3.replace('api.','')

                    #remove the repos/ from the url mined
                    newerurl3 = updatedurl3.replace('repos/','')

                    #clone the repo locally in the projects folder
                    Repo.clone_from(newerurl3, "UserSkillsParser/Projects/" + data2['name'] + "/")
        else:

            #dont clone the repo since its not a JAVA project
            #print("Not cloning repo..." + data['items'][index]['repository_url'] + " because its a " + str(data2['language']) + " project")
            pass

        #check the next user project in the list
        index = index + 1

    #print(" ")
    #print("========================================FINISHED PULL REQUESTS FROM " + input_username +"=========================================")
    #print(" ")
    return input_username
    #print("Cloned a total of: " + str(len(user_project_list)) + " Java projects.")

################################################################################################################################################
################################################################################################################################################
#function to delete the users projects in the projects folder
def deleteDownloadedProjects():

    #create a list of all the folders/files in the Projects directory
    projectList = os.listdir("UserSkillsParser/Projects/")

    #check the length of that list to use in the loop 
    projectFolderLength = len(projectList)

    #set an index
    index = 0 

    #create a while loop to get rid of all the projects
    while index < projectFolderLength:

        #check if the current project at index[whatever] is equal to the .jar file
        if projectList[index] == "1.jar":

            #if they are equal, do nothing, and increment the index
            #the reason we do nothing is because we need this jar file, we dont want to delete it
            index += 1

        #check if the current project at index[whatever] is equal to the .jar file
        if projectList[index] == "dontDelete.txt":

            #if they are equal, do nothing, and increment the index
            #the reason we do nothing is because we need this jar file, we dont want to delete it
            index += 1

        #otherwise
        else:
            isFile = os.path.isfile("UserSkillsParser/Projects/" + projectList[index])

            if isFile == True:
                os.remove("UserSkillsParser/Projects/" + projectList[index])

            else:
            #otherwise remove the entire tree Projects/"whatever the folder name is here"
                shutil.rmtree("UserSkillsParser/Projects/" + projectList[index])

            #increment the index
            index += 1

def runEverything(username):

    #get the current list of projects in the projects folder /// will be changed to check if projects are in database
    #user_project_list = os.listdir("UserSkillsParser/Projects/")

    #call the user profile mining function here to start the program
    githubProjectDownloader(username)

    #call the jar file that runs fabios parser downloaded projects (that the above function downloaded)
    os.system('java -jar ~/matchsource/OSSMatching/UserSkillsParser/1.jar ~/matchsource/OSSMatching/UserSkillsParser/Projects/ java Y Y devnew postgres admin jabref50 import Y jabref')
    #subprocess.call(['java', '-jar', 'UserSkillsParser/Projects/1.jar', '/Users/josephdanciu/Desktop', 'java', 'Y', 'Y', 'devnew', 'postgres', 'admin', 'jabref50', 'import', 'Y', 'jabref'])

    #return the username if function sucessfully passed
    out = githubProjectDownloader(username)

    # get all the data from the CSV into an array of arrays
    data_2d = []
    with open('UserSkillsParser/Projects/JabRefCounts.csv', newline='\n') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader) # this will skip that header
        for row in reader:
            data_2d.append(row) #this just means take each string and make it an int before appending.

    #print(data_2d)

    #have only the class and number of times it showed up appear
    for j in data_2d: 
        del j[0] 
        del j[0] 

    print(data_2d)

    #CHANGE MADE FROM WEDNESDAY 3/4/2020
    ###
    my_df = pd.DataFrame(data_2d)
    ###
    my_df.to_csv('REALCSV.csv', index=False, header=False)
    ###
    ###
    
    print("WE MADE IT PAST THE PARSER")

    file_path = 'UserSkillsParser/Projects/JabRefCounts.csv'
    #create new tabele for each user
    table_name = 'skillss'
    databaseMAIN.pg_load_table(file_path,table_name)


    #    ADD USERNAME (OUT) AND SKILLS (DATA_2D) TO DATABASE ################################################

    #finally delete everything in the folder so the folder is clean
    #deleteDownloadedProjects()
