from django.test import TestCase
from .models import UserSkill, ApiSpecific, Project

#query data
skills = UserSkill.objects.all()
api = ApiSpecific.objects.all().distinct('general')
project_name = (str(Project.objects.all()).replace(
    "<QuerySet [<Project: ", '').strip('>]').replace('>', '')).replace(' ', '')

user_skills = []
project_skills = []
count = 0

#takes out unwanted characters 
for skill in skills:
    # removes extra
    user_skills.append((str(skill).replace("<QuerySet [<ApiSpecific: ", '').replace(
        '<ApiSpecific: ', '').strip('>]').replace('>', '')).replace(' ', ''))
    # ver (user#) splits into a list [email,skills]
    # exec("user"+str(count)+" = user_skills[count].split('-')")
    count = count+1

#takes out unwanted characters 
for project in api:
    project_skills.append((str(project).replace("<QuerySet [<ApiSpecific: ", '').replace(
        '<ApiSpecific: ', '').strip('>]').replace('>', '')).replace(' ', ''))


def printing():
    if user_skills[-1].split('-')[2] in project_skills:
        print('----------------------------------------------------------------------')
        print('The Project Skills are: ' + str(project_skills) + '\n')
        print(str(user_skills[-1].split('-')[0]) +
              '\'s user skills are: ' + str(user_skills[-1].split('-')[2]))
        print('----------------------------------------------------------------------')
        print('Matched to Project: ' + project_name)
        print('----------------------------------------------------------------------')


# multiple entries/skills
def match():
    hold = []
    comma = ','
    stop = 0
    if comma in user_skills[-1].split('-')[2]:
        print('The Project Skills are: ' + str(project_skills) + '\n')
        print(str(user_skills[-1].split('-')[0]) +
              '\'s user skills are: ' + str(user_skills[-1].split('-')[2]))
        while (user_skills[-1].split('-')[2]).count(',') >= stop:
            if user_skills[-1].split('-')[2].split(',')[stop] in project_skills:

                print(user_skills[-1].split('-')[2].split(',')
                      [stop]+' matched to Project: ' + project_name)
            else:
                print(user_skills[-1].split('-')[2].split(',')
                      [stop]+' matched to Project: NONE')
            stop = stop+1
    else:
        printing()

