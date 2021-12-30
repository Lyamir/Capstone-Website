import os
import sys
import subprocess
import time
import datetime
import sys
import json
import signal
import shutil
import getpass
import subprocess
from git import Repo

state= True;
caseState = True;


confirmationState = True;

sites_blogsite= "/home/caikit/Documents/caikit/sites/capstone-blogsite"
roles_programmer1= "/home/caikit/Documents/caikit/roles/programmer1"
roles_programmer2= "/home/caikit/Documents/caikit/roles/programmer2"
roles_devopsengineer= "/home/caikit/Documents/caikit/roles/devopsengineer"
roles_qaengineer= "/home/caikit/Documents/caikit/roles/qaengineer"
roles_techlead= "/home/caikit/Documents/caikit/roles/techlead"
server_capstone_git= "/home/caikit/Documents/caikit/git-server/capstone-blogsite.git"

#Loops while the user has not selected a valid choice
while state:
        print('Welcome to the DevOps Toolkit to get started on which part of the Pipeline you would like to work on Enter a number:')
        print("Select 1 for Continuous Integration")
        print("Select 2 for Continuous Testing")
        print("Select 3 for Continuous Deployment and Delivery")
        print("Select 4 for Resetting the toolkit")
        print("Select 5 to exit")        
        #Asks for the user input in choosing from the three Key concepts
        option = int(input("Enter your choice: "))
        if option == 1:
            print("You have Chosen Continuous Integration")
            state = False
            while confirmationState:
                #Asks the user to pick which case they would like or if they would like to reset the case
                print("Choose a Case to work on:")
                print("Select 1 for Teacher-led case")
                print("Select 2 for Self-learned case")
                print("Select 3 for Project-based case")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_git])
                    subprocess.run(['rm','-r', sites_blogsite])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_git])                    
                    subprocess.run(['mkdir',sites_blogsite])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/programmer1'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/programmer2'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/devopsengineer'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/qaenginner'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/techlead'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/sites/capstone-blogsite'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/git-server/capstone-blogsite'])
                    subprocess.run(['sudo','chown','-R','caikit','/home/caikit/Documents/caikit/git-server/capstone-blogsite.git'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/git-server/capstone-blogsite.git'])
                    
                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                 
                    #Copies the files from src directory into the dest directory for this use it moves the file for the teacher led case for 
                    #integration into the model to simulate the case
                    #Change the path directory to fit where the Capstone-Website is
                    src = r"/home/caikit/Documents/caikit/cases/teacher-led/integration/model"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-blogsite/model"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_git)
                    subprocess.run(['git','init'], cwd=sites_blogsite)
                    subprocess.run(['git','add','.'], cwd=sites_blogsite)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_blogsite)
                    subprocess.run(['git','remote','add','origin',server_capstone_git],cwd=sites_blogsite)
                    subprocess.run(['git','push','origin','master'],cwd=sites_blogsite)

                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Self-learned case")
                    print("Please wait while we prepare the case")
                    #os.chdir(src)
                    #for file in files:
                    #r"/home/caikit/Documents/caikit/capstone-messaging"
                    #    if os.path.isfile(file):
                    #        shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #r"/home/caikit/Documents/caikit/capstone-todolist"
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False
                
                else:
                    print("Unknown option Try again")
        elif option == 2:
            print("You have Chosen Continuous Testing")
            state = False
            while confirmationState:
                print("Choose a Case to work on:")
                print("Select 1 for Teacher-led case")
                print("Select 2 for Self-learned case")
                print("Select 3 for Project-based case")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_git])
                    subprocess.run(['rm','-r', sites_blogsite])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                    
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])                                        
                    subprocess.run(['mkdir',server_capstone_git])                    
                    subprocess.run(['mkdir',sites_blogsite])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/programmer1'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/programmer2'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/devopsengineer'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/qaenginner'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/techlead'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/sites/capstone-blogsite'])
                    subprocess.run(['sudo','chown','-R','caikit','/home/caikit/Documents/caikit/git-server/capstone-blogsite.git'])
                    #sudo chown -r caikit ~/Documents/caikit/git-server/capstone-blogsite.git
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/git-server/capstone-blogsite.git'])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src = r"/home/caikit/Documents/caikit/cases/teacher-led/testing/model"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-blogsite/model"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)
                    src2 = r"/home/caikit/Documents/caikit/cases/teacher-led/testing/test"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite/test"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2)  

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_git)
                    subprocess.run(['git','init'], cwd=sites_blogsite)
                    subprocess.run(['git','add','.'], cwd=sites_blogsite)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_blogsite)
                    subprocess.run(['git','remote','add','origin',server_capstone_git],cwd=sites_blogsite)
                    subprocess.run(['git','push','origin','master'],cwd=sites_blogsite)

                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Self-learned case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #r"/home/caikit/Documents/caikit/capstone-messaging"                
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #r"/home/caikit/Documents/caikit/capstone-todolist"
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False
                else:
                    print("Unknown option Try again")             
        elif option == 3:
            print("You have Chosen Continuous Deployment and Delivery")
            state = False
            while confirmationState:
                print("Choose a Case to work on:")
                print("Select 1 for Teacher-led case")
                print("Select 2 for Self-learned case")
                print("Select 3 for Project-based case")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_git])
                    subprocess.run(['rm','-r', sites_blogsite])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                    
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])                                        
                    subprocess.run(['mkdir',server_capstone_git])                    
                    subprocess.run(['mkdir',sites_blogsite])
                    
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/programmer1'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/programmer2'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/devopsengineer'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/qaenginner'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/roles/techlead'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/sites/capstone-blogsite'])
                    subprocess.run(['sudo','chown','-R','caikit','/home/caikit/Documents/caikit/git-server/capstone-blogsite.git'])
                    subprocess.run(['sudo','chmod','777','/home/caikit/Documents/caikit/git-server/capstone-blogsite.git'])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src = r"/home/caikit/Documents/caikit/cases/teacher-led/delivery-and-deployment/model"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-blogsite/model"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)
                    src2 = r"/home/caikit/Documents/caikit/cases/teacher-led/delivery-and-deployment"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2) 
                     
                    subprocess.run(['git','init','--bare'],cwd = server_capstone_git)
                    subprocess.run(['git','init'], cwd=sites_blogsite)
                    subprocess.run(['git','add','.'], cwd=sites_blogsite)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_blogsite)
                    subprocess.run(['git','remote','add','origin',server_capstone_git],cwd=sites_blogsite)
                    subprocess.run(['git','push','origin','master'],cwd=sites_blogsite)

                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Self-learned case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #r"/home/caikit/Documents/caikit/capstone-messaging"
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #r"/home/caikit/Documents/caikit/capstone-todolist"
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False
                else:
                    print("Unknown option Try again")

        elif option == 4:
            print("Are you sure you want to reset the cases?")
            confirmation = str(input("Press Y if you want to reset N if not"))
            if (confirmation == 'y' or confirmation == "Y"):
                print("Resetting")
                confirmationState = True
                src = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite"
                dest = r"/home/caikit/Documents/caikit/capstone-blogsite"
                files = os.listdir(src)
                files2 = os.listdir(dest)
                os.chdir(src)
                shutil.rmtree(dest, ignore_errors= True)
                shutil.copytree(src, dest, dirs_exist_ok=True)
                
                caseState = False
                exit()
            elif (confirmation == 'n'or confirmation == 'N'):
                print("Going back to case selection")
                state = False
        elif option == 5:
            print("Exiting")
            exit()        
        else:
            print('Unknown Option try again')

#* FOLDER DIRECTORY
#* /home/caikit/Documents/caikit/                                           caikit root folder (insert script here)
#* /home/caikit/Documents/caikit/cases/                                     cases
#* /home/caikit/Documents/caikit/cases/teacher-led/                         all teacher-led cases
#* /home/caikit/Documents/caikit/cases/student-led/                         all student-led cases
#* /home/caikit/Documents/caikit/cases/project-based/                       all project-based cases
#* /home/caikit/Documents/caikit/cases/*/integration/                       continuous integration case (CASEx-1)
#* /home/caikit/Documents/caikit/cases/*/testing/                           continuous testing case (CASEx-2)
#* /home/caikit/Documents/caikit/cases/*/delivery-and-deployment/           continuous delivery and deployment case (CASEx-3)
#* /home/caikit/Documents/caikit/roles/                                     roles 
#* /home/caikit/Documents/caikit/roles/programmer1                          Programmer 1's folder
#* /home/caikit/Documents/caikit/roles/programmer2                          Programmer 2's folder
#* /home/caikit/Documents/caikit/roles/techlead                             Tech Lead's folder 
#* /home/caikit/Documents/caikit/roles/qaengineer                           QA Engineer's folder
#* /home/caikit/Documents/caikit/roles/devopsengineer                       DevOps Engineer's folder
#* /home/caikit/Documents/caikit/sites/                                     all git sites
#* /home/caikit/Documents/caikit/sites/capstone-blogsite                    capstone-blogsite folder
#* /home/caikit/Documents/caikit/sites/capstone-messaging                   capstone-messaging folder
#* /home/caikit/Documents/caikit/sites/capstone-todolist                    capstone-todolist folder
#* /home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite          unaltered capstone-blogsite folder (NO GIT)
#* /home/caikit/Documents/caikit/sites/unaltered-capstone-messaging         unaltered capstone-messaging folder (NO GIT)
#* /home/caikit/Documents/caikit/sites/unaltered-capstone-todolist          unaltered capstone-todolist folder (NO GIT)
#* /home/caikit/Documents/caikit/git-server                                 git server
#* /home/caikit/Documents/caikit/git-server/capstone-blogsite.git           working git repo

#! case initialization (assuming we already have the finished pipeline)
# rm -r /home/caikit/Documents/caikit/roles/programmer1/*
# rm -r /home/caikit/Documents/caikit/roles/programmer2/*
# rm -r /home/caikit/Documents/caikit/roles/devopsengineer/*
# rm -r /home/caikit/Documents/caikit/roles/qaengineer/*
# rm -r /home/caikit/Documents/caikit/roles/techlead/*
# rm -r /home/caikit/Documents/caikit/git-server/capstone-blogsite.git
# mkdir /home/caikit/Documents/caikit/git-server/capstone-blogsite.git
# cd /home/caikit/Documents/caikit/git-server/capstone-blogsite.git
# git init --bare
# rm -r /home/caikit/Documents/caikit/sites/capstone-blogsite
# cp -r /home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/* /home/caikit/Documents/caikit/sites/capstone-blogsite
# cp -r /home/caikit/Documents/caikit/cases/teacher-led/integration/* /home/caikit/Documents/caikit/sites/capstone-blogsite
# git init
# git remote add origin /home/caikit/Documents/caikit/git-server/capstone-blogsite.git
# git add .
# git commit -m "Initial Commit"
# git push origin master



