# SICILI.SCI.OS
>  Note:  $ Means Important
> Due To Bots I Have Added Verification.
## An Os Full of Sci. And Sci.cmdname.sciex
> # $*Notice:*
>### I Took No Absolutely NO Code From Anyone, Each And Every Part Of This Code Is Mine, And Mine Alone
> #
#

# $How To Run:

First Open Your Terminal/Command Prompt.
Then Type:

```bash
cd path\to\the\SICILI.SCI.OS-0.0.0.1\kernel\folder
```

#
Then Run: 
```bash
python kernel.py
```

# $Documentation:
When You Are In The OS (SICILI.SCI.OS)
You Will Be Prompted To Wait Or You Can Skip Loading.
#
When You Are Prompted To Enter A Command, Enter:
```bash
sci.help
```
This Will Run The `Help` Command And You Will Be Able To Understand The Commands.


## $Commands:

> ### These  Are  The  Available  Commands:
```bash
sci.help - show this help message

sci.info.sciex.kernel - show information about this program
        
sci.echo.sciex - echo back what you type

sci.runapp.sciex   - run an application

sci.tree.danger.sciex - create a value for tree. use the -p command to print  the value.

sci.history - show  command history

sci.shutdown - shut down the system

sci.reboot - reboot the system

sci.shell - run a shell command

sci.applescript.sciex - Run AppleScript code (needs a Mac)

sci.bios.sciex - run the bios  
sci.clear.screen - clears the screen 
sci.dumb.wait.why.you.should.not.do.this.it.is.dumb-intentionally left without description   
```
> ### Also Note: That This Has Error-Reporting, And Version 0.3 Is Releasing On 31 of December.

# $Contributing:
 To Contribute To This Project (SICILI.SCI.OS), Make A Fork Of This Repository, Make Your Changes, Then Make A PULL REQUEST, With Your Changes Described, And A Link To Your Fork. Then If We Think That Your Code Has Something Better(e.g More Commands, Better Calculator), We Will Use That Code Instead.
#
# $Making Your Own Version:
> ### $If You Make Your Own Version, You Have To Credit Me (ArtificialXDev).
 First Start By Editing `kernel.py` in Kernel Folder, After Editing `kernel.py` in Kernel Folder, Edit `BIOS.py` in `BIOS` Folder, After Editing `BIOS.py` in `BIOS` Folder, Edit All The `Apps` in The `apps` Folder. Also Make Sure You Have `Python 12.6` Or `Python 11.0` Or It Won't Work

## $Custom Apps:
To Make A Custom App, Go In To The `Apps` Folder And Make A New File With A ".py" Extension, After That Make Some Code For It.
It Must Include This Code To Go Back To The Kernel:
```bash
# Needed Imports:
import subprocess
import os
import sys
kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
    
    # Check if the kernel script exists before trying to run it
    if os.path.isfile(kernel_script):
        try:
            # Run the kernel script as a subprocess
            subprocess.run([sys.executable, kernel_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the kernel script: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("yay! sucsess!")

```
Here Is A Calculator Example:

```bash
import os
import subprocess
import sys

def calculator():
    while True:
        # Print options for the user
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'quit' to end the program and run kernel script")

        # Get user input
        user_input = input(": ").lower()

        # Check if the user wants to quit
        if user_input in ["quit", "q"]:
            kernel_script = os.path.join(os.getcwd(), 'KERNEL', '(link unavailable)')
            if os.path.isfile(kernel_script):
                try:
                    subprocess.run([sys.executable, kernel_script], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing kernel script: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")
            else:
                print("Yay! Success!")
            break

        # Check if the user input is a valid operator
        elif user_input in ["+", "-", "*", "/"]:
            # Get first number
            num1 = float(input("Enter a number: "))

            # Get second number
            num2 = float(input("Enter another number: "))

            # Perform operation
            if user_input == "+":
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif user_input == "-":
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif user_input == "*":
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif user_input == "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero.")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()

```
## $Custom Commands:
To Make *CUSTOM COMMANDS* 
Go To Kernel.py In `Kernel` Folder  And Go To Commands Area And Make Your Commands.

> Also Also Also Note: Setup.py Is Under active Development, And Won't Be Updated Until, We Make It `PERFECT`

-Shahzain Khan(ArtificialXDev)