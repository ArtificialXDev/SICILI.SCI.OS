import subprocess
import os
import sys
import webbrowser

# Kernel script path setup
kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')

# Welcome message and GitHub URL input
print("Welcome! This application helps you open GitHub repos straight from the command line.")
print("Just enter the URL, and we will bring you there!")

while True:
    url = input("URL: ").strip()

    # Check if the input contains exactly 'github.com'
    if url.startswith("https://github.com") or url.startswith("http://github.com"):
        # Open the URL in the web browser
        webbrowser.open(url)
    elif url == "quit":
        break 
        cry()        
     # Exit the loop once the URL is opened or user quits
    else:
        print("The URL has to be a GitHub link! Try something like https://github.com/")
        print("Maybe perhaps you also forgot a https:// or http:// ?")

# Define the function to run the kernel script
def cry():
    if os.path.isfile(kernel_script):
        try:
            # Run the kernel script as a subprocess
            subprocess.run([sys.executable, kernel_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the kernel script: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("yay! success!")

# Call the cry function to execute the kernel script if the user quits

