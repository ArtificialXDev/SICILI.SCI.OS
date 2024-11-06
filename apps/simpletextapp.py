import subprocess
import os
import sys

def main():
    print("Simple Text")
    print("(What did you expect from an app called simpletext?)")
    

    
    kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
    
    
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

if __name__ == "__main__":
    main()
