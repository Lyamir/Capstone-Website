from asyncio.subprocess import PIPE
from doctest import OutputChecker
import os
import sys
import subprocess
import time
import datetime
import sys
import json
import signal
import shutil
import subprocess

state= True;
caseState = True;


confirmationState = True;

root_folder = "/home/caikit/Documents/caikit/"
cases_folder = "/home/caikit/Documents/caikit/cases/"
cases_teacher_led="/home/caikit/Documents/caikit/cases/teacher-led/"
cases_student_led="/home/caikit/Documents/caikit/cases/student-led/"
cases_project_based="/home/caikit/Documents/caikit/cases/project-based/"
teacher_integ="/home/caikit/Documents/caikit/cases/teacher-led/integration/"
teacher_test="/home/caikit/Documents/caikit/cases/teacher-led/testing/"
teacher_dd="/home/caikit/Documents/caikit/cases/teacher-led/delivery-and-deployment/"
student_integ="/home/caikit/Documents/caikit/cases/student-led/integration/"
student_test="/home/caikit/Documents/caikit/cases/student-led/testing"
student_dd="/home/caikit/Documents/caikit/cases/student-led/delivery-and-deployment/"
proj_integ="/home/caikit/Documents/caikit/cases/project-based/integration/"
proj_test="/home/caikit/Documents/caikit/cases/project-based/testing/"
proj_dd="/home/caikit/Documents/caikit/cases/project-based/delivery-and-deployment/"
root_roles="/home/caikit/Documents/caikit/roles/"
roles_programmer1= "/home/caikit/Documents/caikit/roles/programmer1"
roles_programmer2= "/home/caikit/Documents/caikit/roles/programmer2"
roles_devopsengineer= "/home/caikit/Documents/caikit/roles/devopsengineer"
roles_qaengineer= "/home/caikit/Documents/caikit/roles/qaengineer"
roles_techlead= "/home/caikit/Documents/caikit/roles/techlead"
sites_root="/home/caikit/Documents/caikit/sites/"
sites_blogsite= "/home/caikit/Documents/caikit/sites/capstone-blogsite"
sites_messaging="/home/caikit/Documents/caikit/sites/capstone-messaging"
sites_todolist="/home/caikit/Documents/caikit/sites/capstone-todolist"
UA_blogsite="/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite"
UA_messaging="/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging"
UA_todolist="/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist"
git_server="/home/caikit/Documents/caikit/git-server"
server_capstone_blog_git= "/home/caikit/Documents/caikit/git-server/capstone-blogsite.git"
server_capstone_message_git= "/home/caikit/Documents/caikit/git-server/capstone-messaging.git"
server_capstone_todo_git= "/home/caikit/Documents/caikit/git-server/capstone-todolist.git"

#Loops while the user has not selected a valid choice
while state:
        print('Welcome to the DevOps Toolkit to get started on which part of the Pipeline you would like to work on Enter a number:')
        print("Select 1 for Continuous Integration")
        print("Select 2 for Continuous Testing")
        print("Select 3 for Continuous Deployment and Delivery")
        print("Select 4 for Initialize/Reset the Toolkit")
        print("Select 5 to exit")        
        #Asks for the user input in choosing from the three Key concepts
        option = int(input("Enter your choice: "))
        if option == 1:
            state = False
            confirmationState = True
            print("You have Chosen Continuous Integration")
            while confirmationState:
                #Asks the user to pick which case they would like or if they would like to reset the case
                print("Choose a Case to work on:")
                print("Select 1 for Teacher-led case")
                print("Select 2 for Student-led case")
                print("Select 3 for Project-based case")
                print("Select 4 to go back")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")

                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_blog_git])
                    subprocess.run(['rm','-r', sites_blogsite])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_blog_git])                    
                    subprocess.run(['mkdir',sites_blogsite])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_blogsite])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_blog_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_blog_git])
                    
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

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_blog_git)
                    subprocess.run(['git','init'], cwd=sites_blogsite)
                    subprocess.run(['git','add','.'], cwd=sites_blogsite)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_blogsite)
                    subprocess.run(['git','remote','add','origin',server_capstone_blog_git],cwd=sites_blogsite)
                    subprocess.run(['git','push','origin','master'],cwd=sites_blogsite)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_blog_git])
                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Student-led case")
                    print("Please wait while we prepare the case")
                    
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_message_git])
                    subprocess.run(['rm','-r', sites_messaging])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_message_git])                    
                    subprocess.run(['mkdir',sites_messaging])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_messaging])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_message_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_message_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                   
                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                    
                    src = r"/home/caikit/Documents/caikit/cases/student-led/integration/model"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-messaging/model"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)
                            
                    subprocess.run(['git','init','--bare'],cwd = server_capstone_message_git)
                    subprocess.run(['git','init'], cwd=sites_messaging)
                    subprocess.run(['git','add','.'], cwd=sites_messaging)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_messaging)
                    subprocess.run(['git','remote','add','origin',server_capstone_message_git],cwd=sites_messaging)
                    subprocess.run(['git','push','origin','master'],cwd=sites_messaging)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_message_git])
                   
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_todo_git])
                    subprocess.run(['rm','-r', sites_todolist])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_todo_git])                    
                    subprocess.run(['mkdir',sites_todolist])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_todolist])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_todo_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_todo_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                   
                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src = r"/home/caikit/Documents/caikit/cases/project-based/integration"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)

                    src2 = r"/home/caikit/Documents/caikit/cases/project-based/integration/"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2)

                    src3 = r"/home/caikit/Documents/caikit/cases/project-based/integration/model"
                    dest3 = r"/home/caikit/Documents/caikit/sites/capstone-todolist/model"
                    files5 = os.listdir(src3)
                    files6 = os.listdir(dest3)
                    os.chdir(src3)
                    for file in files5:
                        if os.path.isfile(file):
                            shutil.copy(file,dest3)

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_todo_git)
                    subprocess.run(['git','init'], cwd=sites_todolist)
                    subprocess.run(['git','add','.'], cwd=sites_todolist)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_todolist)
                    subprocess.run(['git','remote','add','origin',server_capstone_todo_git],cwd=sites_todolist)
                    subprocess.run(['git','push','origin','master'],cwd=sites_todolist)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_todo_git])
                    caseState = False
                    confirmationState = False
                
                elif caseoption == 4:
                    confirmationState = False
                    state = True
                else:
                    print("Unknown option Try again")
        elif option == 2:
            print("You have Chosen Continuous Testing")
            state = False
            confirmationState = True
            while confirmationState:
                print("Choose a Case to work on:")
                print("Select 1 for Teacher-led case")
                print("Select 2 for Student-led case")
                print("Select 3 for Project-based case")
                print("Select 4 to go back")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_blog_git])
                    subprocess.run(['rm','-r', sites_blogsite])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_blog_git])                    
                    subprocess.run(['mkdir',sites_blogsite])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_blogsite])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_blog_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_blog_git])

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

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_blog_git)
                    subprocess.run(['git','init'], cwd=sites_blogsite)
                    subprocess.run(['git','add','.'], cwd=sites_blogsite)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_blogsite)
                    subprocess.run(['git','remote','add','origin',server_capstone_blog_git],cwd=sites_blogsite)
                    subprocess.run(['git','push','origin','master'],cwd=sites_blogsite)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_blog_git])                    

                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Student-led case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_message_git])
                    subprocess.run(['rm','-r', sites_messaging])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_message_git])                    
                    subprocess.run(['mkdir',sites_messaging])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_messaging])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_message_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_message_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                   
                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src = r"/home/caikit/Documents/caikit/cases/student-led/testing/test"
                    dest =r"/home/caikit/Documents/caikit/sites/capstone-messaging/test"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)

                    src2 = r"/home/caikit/Documents/caikit/cases/student-led/testing/model"
                    dest2 =r"/home/caikit/Documents/caikit/sites/capstone-messaging/model"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2)

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_message_git)
                    subprocess.run(['git','init'], cwd=sites_messaging)
                    subprocess.run(['git','add','.'], cwd=sites_messaging)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_messaging)
                    subprocess.run(['git','remote','add','origin',server_capstone_message_git],cwd=sites_messaging)
                    subprocess.run(['git','push','origin','master'],cwd=sites_messaging)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_message_git])
                    


                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_todo_git])
                    subprocess.run(['rm','-r', sites_todolist])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_todo_git])                    
                    subprocess.run(['mkdir',sites_todolist])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_todolist])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_todo_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_todo_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                   
                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src = r"/home/caikit/Documents/caikit/cases/project-based/testing"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)

                    src2 = r"/home/caikit/Documents/caikit/cases/project-based/testing/"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2)

                    src4 = r"/home/caikit/Documents/caikit/cases/project-based/testing/test"
                    dest4 = r"/home/caikit/Documents/caikit/sites/capstone-todolist/test"
                    files7 = os.listdir(src4)
                    files8 = os.listdir(dest4)
                    os.chdir(src4)
                    for file in files7:
                        if os.path.isfile(file):
                            shutil.copy(file,dest4)
                    

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_todo_git)
                    subprocess.run(['git','init'], cwd=sites_todolist)
                    subprocess.run(['git','add','.'], cwd=sites_todolist)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_todolist)
                    subprocess.run(['git','remote','add','origin',server_capstone_todo_git],cwd=sites_todolist)
                    subprocess.run(['git','push','origin','master'],cwd=sites_todolist)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_todo_git])
                    caseState = False
                    confirmationState = False
                
                elif caseoption == 4:
                    confirmationState = False
                    state = True

                else:
                    print("Unknown option Try again")             
        elif option == 3:
            print("You have Chosen Continuous Deployment and Delivery")
            state = False
            confirmationState = True
            while confirmationState:
                print("Choose a Case to work on:")
                print("Select 1 for Teacher-led case")
                print("Select 2 for Student-led case")
                print("Select 3 for Project-based case")
                print("Select 4 to go back")
                caseoption = int(input("Enter your choice: "))
                if caseoption == 1:
                    print("You have chosen the Teacher-led case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_blog_git])
                    subprocess.run(['rm','-r', sites_blogsite])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_blog_git])                    
                    subprocess.run(['mkdir',sites_blogsite])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_blogsite])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_blog_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_blog_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src2 = r"/home/caikit/Documents/caikit/cases/teacher-led/delivery-and-deployment"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-blogsite"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2) 
                     
                    subprocess.run(['git','init','--bare'],cwd = server_capstone_blog_git)
                    subprocess.run(['git','init'], cwd=sites_blogsite)
                    subprocess.run(['git','add','.'], cwd=sites_blogsite)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_blogsite)
                    subprocess.run(['git','remote','add','origin',server_capstone_blog_git],cwd=sites_blogsite)
                    subprocess.run(['git','push','origin','master'],cwd=sites_blogsite)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_blog_git])
                    
                    caseState = False
                    confirmationState = False
                elif caseoption == 2:
                    print("You have chosen the Student-led case")
                    print("Please wait while we prepare the case")

                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_message_git])
                    subprocess.run(['rm','-r', sites_messaging])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_message_git])                    
                    subprocess.run(['mkdir',sites_messaging])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_messaging])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_message_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_message_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                   
                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src2 = r"/home/caikit/Documents/caikit/cases/student-led/delivery-and-deployment"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-messaging"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2)

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_message_git)
                    subprocess.run(['git','init'], cwd=sites_messaging)
                    subprocess.run(['git','add','.'], cwd=sites_messaging)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_messaging)
                    subprocess.run(['git','remote','add','origin',server_capstone_message_git],cwd=sites_messaging)
                    subprocess.run(['git','push','origin','master'],cwd=sites_messaging)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_message_git])
                    
                    caseState = False
                    confirmationState = False                        
                elif caseoption == 3:
                    print("You have chosen the Project-based case")
                    print("Please wait while we prepare the case")
                    subprocess.run(['rm','-r', roles_programmer1])
                    subprocess.run(['rm','-r', roles_programmer2])
                    subprocess.run(['rm','-r', roles_devopsengineer])
                    subprocess.run(['rm','-r', roles_qaengineer])
                    subprocess.run(['rm','-r', roles_techlead])
                    subprocess.run(['rm','-r', server_capstone_todo_git])
                    subprocess.run(['rm','-r', sites_todolist])
                    subprocess.run(['mkdir',roles_programmer1])
                    subprocess.run(['mkdir',roles_programmer2])                   
                    subprocess.run(['mkdir',roles_devopsengineer])
                    subprocess.run(['mkdir',roles_qaengineer])
                    subprocess.run(['mkdir',roles_techlead])       
                    subprocess.run(['mkdir',server_capstone_todo_git])                    
                    subprocess.run(['mkdir',sites_todolist])
                    subprocess.run(['sudo','chmod','777',roles_programmer1])
                    subprocess.run(['sudo','chmod','777',roles_programmer2])
                    subprocess.run(['sudo','chmod','777',roles_devopsengineer])
                    subprocess.run(['sudo','chmod','777',roles_qaengineer])
                    subprocess.run(['sudo','chmod','777',roles_techlead])
                    subprocess.run(['sudo','chmod','777',sites_todolist])
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_todo_git])
                    subprocess.run(['sudo','chmod','777',server_capstone_todo_git])

                    src5 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist"
                    dest5 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    shutil.copytree(src5,dest5,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)
                   
                    src6 = r"/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/"
                    dest6 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    shutil.copytree(src6,dest6,symlinks=False,ignore=None,ignore_dangling_symlinks=False,dirs_exist_ok=True)

                    src = r"/home/caikit/Documents/caikit/cases/project-based/delivery-and-deployment"
                    dest = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    files = os.listdir(src)
                    files2 = os.listdir(dest)
                    os.chdir(src)
                    for file in files:
                        if os.path.isfile(file):
                            shutil.copy(file,dest)

                    src2 = r"/home/caikit/Documents/caikit/cases/project-based/delivery-and-deployment/"
                    dest2 = r"/home/caikit/Documents/caikit/sites/capstone-todolist"
                    files3 = os.listdir(src2)
                    files4 = os.listdir(dest2)
                    os.chdir(src2)
                    for file in files3:
                        if os.path.isfile(file):
                            shutil.copy(file,dest2)

                    src3 = r"/home/caikit/Documents/caikit/cases/project-based/delivery-and-deployment/model"
                    dest3 = r"/home/caikit/Documents/caikit/sites/capstone-todolist/model"
                    files5 = os.listdir(src3)
                    files6 = os.listdir(dest3)
                    os.chdir(src3)
                    for file in files5:
                        if os.path.isfile(file):
                            shutil.copy(file,dest3)

                    src4 = r"/home/caikit/Documents/caikit/cases/project-based/delivery-and-deployment/test"
                    dest4 = r"/home/caikit/Documents/caikit/sites/capstone-todolist/test"
                    files7 = os.listdir(src4)
                    files8 = os.listdir(dest4)
                    os.chdir(src4)
                    for file in files7:
                        if os.path.isfile(file):
                            shutil.copy(file,dest4)

                    subprocess.run(['git','init','--bare'],cwd = server_capstone_todo_git)
                    subprocess.run(['git','init'], cwd=sites_todolist)
                    subprocess.run(['git','add','.'], cwd=sites_todolist)
                    subprocess.run(['git','commit','-m','Initial commit'], cwd=sites_todolist)
                    subprocess.run(['git','remote','add','origin',server_capstone_todo_git],cwd=sites_todolist)
                    subprocess.run(['git','push','origin','master'],cwd=sites_todolist)
                    subprocess.run(['sudo','chown','-R','caikit',server_capstone_todo_git])
                    caseState = False
                    confirmationState = False

                
                elif caseoption == 4:
                    confirmationState = False
                    state = True                
                
                else:
                    print("Unknown option Try again")

        elif option == 4:
            print("Are you sure you want to reset the cases?")
            confirmation = str(input("Press Y if you want to reset: "))
            if (confirmation == 'y' or confirmation == "Y"):
                print("Resetting")
                confirmationState = True
                subprocess.run(['sudo','rm','-d','-r',root_folder])
                subprocess.run(['sudo','mkdir',root_folder])
                subprocess.run(['sudo','mkdir',cases_folder])
                subprocess.run(['sudo','mkdir',cases_teacher_led])
                subprocess.run(['sudo','mkdir',cases_student_led])
                subprocess.run(['sudo','mkdir',cases_project_based])
                subprocess.run(['sudo','mkdir',teacher_integ])
                subprocess.run(['sudo','mkdir',teacher_test])
                subprocess.run(['sudo','mkdir',teacher_dd])
                subprocess.run(['sudo','mkdir',student_integ])
                subprocess.run(['sudo','mkdir',student_test])
                subprocess.run(['sudo','mkdir',student_dd])
                subprocess.run(['sudo','mkdir',proj_integ])
                subprocess.run(['sudo','mkdir',proj_test])
                subprocess.run(['sudo','mkdir',proj_dd])
                subprocess.run(['sudo','mkdir',root_roles])
                subprocess.run(['sudo','mkdir',roles_programmer1])
                subprocess.run(['sudo','mkdir',roles_programmer2])
                subprocess.run(['sudo','mkdir',roles_techlead])
                subprocess.run(['sudo','mkdir',roles_qaengineer])
                subprocess.run(['sudo','mkdir',roles_devopsengineer])
                subprocess.run(['sudo','mkdir',sites_root])
                subprocess.run(['sudo','mkdir',sites_blogsite])
                subprocess.run(['sudo','mkdir',sites_messaging])
                subprocess.run(['sudo','mkdir',sites_todolist])
                subprocess.run(['sudo','mkdir',UA_blogsite])
                subprocess.run(['sudo','mkdir',UA_messaging])
                subprocess.run(['sudo','mkdir',UA_todolist])
                subprocess.run(['sudo','mkdir',git_server])
                subprocess.run(['sudo','mkdir',server_capstone_blog_git])
                subprocess.run(['sudo','mkdir',server_capstone_message_git])
                subprocess.run(['sudo','mkdir',server_capstone_todo_git])
                subprocess.run(['sudo','chmod','777',root_folder])
                subprocess.run(['sudo','chown','-R','caikit',root_folder])
               
                #Initializing blogsite
                subprocess.Popen(['git','clone','https://github.com/Lyamir/capstone-blogsite.git','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/']).wait()
                subprocess.Popen(['npm','install','-f'],cwd='/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite').wait()
                
                #Initializing messaging
                subprocess.Popen(['git','clone','https://github.com/Lyamir/capstone-messaging.git','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/']).wait()
                subprocess.Popen(['npm','install','-f'],cwd='/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging').wait()

                #Initializing todolist
                subprocess.Popen(['git','clone','https://github.com/Lyamir/capstone-todolist.git','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/']).wait()
                subprocess.Popen(['npm','install','-f'],cwd='/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist').wait()

                #Changing permissions for blogsite
                subprocess.run(['sudo','chmod','-R','777','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/'])
                subprocess.run(['sudo','chown','-R','caikit','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/'])
                
                #Changing permissions for messaging
                subprocess.run(['sudo','chmod','-R','777','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/'])
                subprocess.run(['sudo','chown','-R','caikit','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/'])  

                #Changing permissions for todolist
                subprocess.run(['sudo','chmod','-R','777','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/'])
                subprocess.run(['sudo','chown','-R','caikit','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/'])

                #Copying teacher-led cases
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/cases/teacher-led/delivery-and-deployment','/home/caikit/Documents/caikit/cases/teacher-led/'])
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/cases/teacher-led/integration','/home/caikit/Documents/caikit/cases/teacher-led/'])
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/cases/teacher-led/testing','/home/caikit/Documents/caikit/cases/teacher-led/'])
                
                #Copying student-led cases
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/cases/student-led/integration','/home/caikit/Documents/caikit/cases/student-led/'])
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/cases/student-led/delivery-and-deployment','/home/caikit/Documents/caikit/cases/student-led/'])
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/cases/student-led/testing','/home/caikit/Documents/caikit/cases/student-led/'])

                #Copying project-based cases
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/cases/project-based/integration','/home/caikit/Documents/caikit/cases/project-based/'])
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/cases/project-based/delivery-and-deployment','/home/caikit/Documents/caikit/cases/project-based/'])
                subprocess.run(['sudo','cp','-r','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/cases/project-based/testing','/home/caikit/Documents/caikit/cases/project-based/'])

                subprocess.run(['sudo','rm','-dr','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/.git'])
                subprocess.run(['sudo','rm','-dr','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/.gitattributes'])
                subprocess.run(['sudo','rm','-dr','/home/caikit/Documents/caikit/sites/unaltered-capstone-blogsite/.gitignore'])
                subprocess.run(['sudo','rm','-dr','/home/caikit/Documents/caikit/sites/unaltered-capstone-messaging/.git'])
                subprocess.run(['sudo','rm','-dr','/home/caikit/Documents/caikit/sites/unaltered-capstone-todolist/.git'])
                subprocess.run(['sudo','chmod','-R','777',cases_teacher_led])
                subprocess.run(['sudo','chmod','-R','777',cases_student_led])
                subprocess.run(['sudo','chmod','-R','777',cases_project_based])
                subprocess.run(['sudo','chown','-R','caikit',cases_teacher_led])
                subprocess.run(['sudo','chown','-R','caikit',cases_student_led])
                subprocess.run(['sudo','chown','-R','caikit',cases_project_based])
                caseState = False
                exit()
            elif (confirmation != 'y'or confirmation != 'Y'):
                print("Going back to case selection")
                state = True
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



