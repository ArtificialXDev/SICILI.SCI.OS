import subprocess
import os
import sys
import platform
import scratchattach as sa
import time
import getpass
import random

print("Hey, Due To Actual Bots, I Have To Implement Verification, I Swear To God Your Passwords Are Not Stored!!, I'm Very Sorry Though!")
print("I'll Be Using Scratch For Verification.")

try:
    username = input("Enter your Scratch username: ")
    if username == "ar":
        pass
    
    
    password = getpass.getpass("Enter your Scratch password(P.S Don't ): ")
    session = sa.login(username, password)
    
    verification_project_id = 1094331367
    verification_code = str(random.randint(10, 99999999999999999999999999999999999999999999999999999999999999))

    print("Please comment this code at: https://scratch.mit.edu/projects/1094331367/")
    print("Verification Code:", verification_code)

    # Access the project object
    project = session.connect_project(verification_project_id)

    # Verification loop with a 4-minute timeout
    start_time = time.time()
    timeout = 240  # seconds

    while True:
        comments = project.comments()  # Fetch comments from the project
        
        # Check if any comment contains the verification code
        if any(verification_code in comment.get("content", "") for comment in comments):  # Use get() to avoid KeyError
            print("Verification Successful! (No Robots Yay!)")
            
            break
        elif time.time() - start_time > timeout:
            print("Verification timed out. Please try again or there was no code in the comments.")
            break
        time.sleep(5)

except Exception as e:
    print(f"An unexpected error occurred: {e}")








def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line()
delete_last_line() 
delete_last_line()
q = random.randint(1,100)


treevalue = 1

panicErrorCode = None

def panic(errorCode):
    print(f"SICILI.SCI.OS has crashed. Error code: {errorCode}")
                
                                                                                                                                                   
print("Verification Successful!!")                                                                                                                                                
print("Welcome to SICILI.SCI.OS! Thank you to all those contributors who worked on this!")
print("Hope you find this OS useful!")
print("SICILI.SCI.OS v0.00001 arcitechure written in Python 3.12.6") 

def wait():
           for i in range(5):
                             print(".")
                             time.sleep(1)
                             delete_last_line()
                             print("..")
                             time.sleep(1)
                             delete_last_line()
                             print("...")
                             time.sleep(1)
                             delete_last_line()      


god = input("Skip Loading? Nothing Happens if You Skip As It Only Loads Apps, Which Will Also Work If You Skip. Type `Bios` or `b` to run bios.(y/n)").strip()




# Assuming the apps directory is one level up from the KERNEL directory

apps_dir = os.path.join(os.path.dirname(os.getcwd()), 'apps')
BIOS_location = os.path.join(os.path.dirname(os.getcwd()), "BIOS")

if god == "y":
     pass
     delete_last_line()
elif god == "n":
    delete_last_line()
    print("Wait a Few Moments, Getting Things Tight! (Yeah Hold Tight)") 
    wait()
elif god == "bios" or 'b':
 script_path = os.path.join(BIOS_location, 'BIOS.py')
 if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
else:
            panicErrorCode = "MISSING_BIOS"



command_history = []
delete_last_line()
print("Tip: Run sci.help for help")

while True:
    command = input("command: ").strip().lower()
    command_history.append(command)
    
    if command == "sci.help":
        print("Available commands:")
        print("sci.help - show this help message")
        print("sci.info.sciex.kernel - show information about this program")
        print("sci.echo.sciex - echo back what you type")
        print("sci.runapp.sciex   - run an application")
        print("sci.tree.danger.sciex - create a value for tree. use the -p command to print the value.")
        print("sci.history - show all command history")
        print("sci.shutdown - shut down the system")
        print("sci.reboot - reboot the system")
        print("sci.shell - run a shell command")
        print("sci.applescript.sciex - Run AppleScript code (needs a Mac)")
        print("sci.bios.sciex - run the bios")
        print("sci.clear.screen- clears the screen")   
        print("sci.dumb.wait.why.you.should.not.do.this.it.is.dumb-intentionally left without description")
    
    elif command == "":
         
         print("Please Enter A Command, An Empty Space/Whitespace is Not A Command, If You Don't Know The Commands Yet, Run sci.help ")

    elif command == "sci.dumb.wait.why.you.should.not.do.this.it.is.dumb":
        wait()
    
    
    elif command == "sci.info.sciex.kernel":
        print("Developed by Shahzain Khan. All rights reserved.")
        print("This kernel may be reproduced in any way under the MIT License.")
        print("You can archive (make sure the archive is public).")
    
    elif command == "sci.echo.sciex":
        echotxt = input("Echo what: ").strip()
        print(echotxt)

    elif command == "sci.tree.danger.sciex":
        treevalue = input("tree:")
        print("the value of tree is set to" + " " + treevalue)
    elif command == "sci.tree.danger.sciex -p":
        print(treevalue)
        
    elif command == "sci.runapp.sciex":
        script_path = os.path.join(apps_dir, input("Enter the app name (w/o a .py):") + ".py")
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("App not found in the 'apps' directory.")
         
              
    
    elif command == "sci.history":
        print("Command History:")
        for index, cmd in enumerate(command_history, start=1):
            print(f"{index}: {cmd}")

    elif command == "sci.shutdown":
        os_option = input("Are you sure? Type 'yes' to confirm: ")
        if os_option == "yes":
            if platform.system() == "Darwin":
                os.system("shutdown -h now")
            elif platform.system() == "Linux":
                os.system("shutdown -h now")
            elif platform.system() == "Windows":
                os.system("shutdown /s")
        else:
            print("Shutdown cancelled.")
            continue
            
    elif command == "sci.reboot.":
        os_option = input("Are you sure? Type 'y' to confirm(This Won't Turn Off This System, But TURN OFF YOUR SYSTEM!!): ")
        if os_option == "y":
            if platform.system() == "Darwin":
                os.system("shutdown -r now")
            elif platform.system() == "Linux":
                os.system("shutdown -r now")
            elif platform.system() == "Windows":
                os.system("shutdown /r")
        else:
            print("Reboot cancelled.")
            continue

    elif command == "sci.shell":
        os.system(input("Enter a shell command: "))
    
    elif command == "sci.applescript.sciex":
        if platform.system() == "Darwin":
            os.system("oascript" + input("Enter your AppleScript file or command: "))
        else:
            print("You need a Mac for this!")

    elif command == "sci.bios.sciex":
        script_path = os.path.join(BIOS_location, 'BIOS.py')
        if os.path.isfile(script_path):
            try:
                subprocess.run([sys.executable, script_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing the script: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            panicErrorCode = "MISSING_BIOS"
            break
    
    elif command == "sci.adw.peak":
         print("New adw dev os coming soooon!")
    
    elif command == "sci.clear.screen": 
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      delete_last_line()
      print("Tip: Run sci.help to learn commands")
       
      
    
    else:
        print(command + " is not a valid command. Type 'sci.help' for a list of commands.")

panic(panicErrorCode)
panicErrorCode = "erorr"