import os
import subprocess
import sys
import time 
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
  
    sys.stdout.write('\x1b[2K')





def wait():
           for i in range(5):
                             print("Moving To The Kernel.")
                             time.sleep(1)
                             delete_last_line()
                             print("Moving To The Kernel..")
                             time.sleep(1)
                             delete_last_line()
                             print("Moving To The Kernel...")
                             time.sleep(1)
                             delete_last_line()    

kernelState = None

print("SICILI.SCI.OS v0.3 bugfix + Package manager[?]")
print("This device is running SICILI.SCI.OS")
print("/kernel/bios")
print(" ^ BIOS is running here")
setting = input("Would you Like To Change Any Settings?(y/n)")
if setting == 'y':
    print('This Function Is Not Yet Avaiable ')
    wait()
elif setting == "n":
   wait()
# Path to the kernel script in the KERNEL folder
kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
            
            # Check if the kernel script exists beforeg  trying to run itI
if os.path.isfile(kernel_script):
                try:
                    # Run the kernel script as a subprocess
                    subprocess.run([sys.executable, kernel_script], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing the kernel script: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
else:
                print("sucsess!!!!!")
                pass
                print()




