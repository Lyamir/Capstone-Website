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

state= True;
caseState = True;

username = getpass.getuser()
confirmationState = True;

#Loops while the user has not selected a valid choice
while state:
        print('Welcome to the DevOps Toolkit to get started on which part of the Pipeline you would like to work on Enter a number:')
        print("Select 1 for Continuous Integration")
        print("Select 2 for Continuous Testing")
        print("Select 3 for Continuous Deployment and Delivery")
        print("Select 4 for Resetting the toolkit")
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
                print("Select 4 to reset the case")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    #Copies the files from src directory into the dest directory for this use it moves the file for the teacher led case for 
                    #integration into the model to simulate the case
                    #Change the path directory to fit where the Capstone-Website is
                    src = r"~/Documents/caikit/capstone-blogsite/cases/teacher-led_cases/integration"
                    dest = r"~/Documents/caikit/capstone-blogsite/model"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Self-learned case")
                    print("Please wait while we prepare the case")
                    #os.chdir(src)
                    #for file in files:
                    #~/Documents/caikit/capstone-messaging
                    #    if os.path.isfile(file):
                    #        shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #~/Documents/caikit/capstone-todolist
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
                print("Select 4 to reset the case")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    # src = r"C:\Users\Panda\Desktop\Capstone\Capstone-Website\cases\teacher-led_cases\"
                    # dest = r"C:\Users\Panda\Desktop\Capstone\Capstone-Website\model"
                    # files = os.listdir(src)
                    # files2 = os.listdir(dest)
                    # os.chdir(src)
                    # for file in files:
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Self-learned case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #~/Documents/caikit/capstone-messaging                    
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #~/Documents/caikit/capstone-todolist
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
                print("Select 4 to reset the case")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    src = r"~/Documents/caikit/capstone-blogsite/cases/teacher-led_cases/integration"
                    dest = r"~/Documents/caikit/capstone-blogsite/model"
                    # files = os.listdir(src)
                    # files2 = os.listdir(dest)
                    # os.chdir(src)
                    # for file in files:
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Self-learned case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #~/Documents/caikit/capstone-messaging
                    #     if os.path.isfile(file):
                    #         shutil.copy(file,dest)
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    # os.chdir(src)
                    # for file in files:
                    #~/Documents/caikit/capstone-todolist
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
                src = r"~/Documents/caikit/capstone-blogsite/cases/teacher-led_cases/integration"
                dest = r"~/Documents/caikit/capstone-blogsite/model"
                files = os.listdir(src)
                files2 = os.listdir(dest)
                os.chdir(src)
                shutil.rmtree(dest, ignore_errors= True)
                shutil.copytree(src, dest, dirs_exist_ok=True)
                # insert copying of hidden file to case file
                caseState = False
                exit()
            elif (confirmation == 'n'or confirmation == 'N'):
                print("Going back to case selection")
                state = False
        else:
            print('Unknown Option try again')
