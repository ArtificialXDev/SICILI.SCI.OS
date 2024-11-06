import webbrowser
from github import Github
from github import Auth
import subprocess
import os
import sys

# Prompt the user for their GitHub access token (REQURED)
access_token = input("Please enter your GitHub access token: ")

# Authenticate using the provided token
auth = Auth.Token(access_token)
github = Github(auth=auth)

while True:
    # Prompt the user for the action they want to perform
    print("\nwould you like to:")
    print("1. Open a repository URL")
    print("2. Search for GitHub repository contributors")
    print("q- quit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Option 1: Open the repository URL
        repo_name = input("Enter the repository (owner/repo) to open the URL: ")
        try:
            repo = github.get_repo(repo_name)
            repo_url = repo.html_url
            print(f"Opening {repo_name} at {repo_url}")
            webbrowser.open(repo_url)
        except Exception as e:
            print(f"Error: {e}\n")
    
    elif choice == "2":
        # Option 2: Search for GitHub repository contributors
        repo_name = input("Enter the repository (owner/repo): ")
        
        try:
            repo = github.get_repo(repo_name)
            
            contributors = []
            page = 1
            per_page = 50  # You can adjust this number (max 100 per page)
            
            print(f"\nContributors for {repo_name}:\n")
            
            while True:
                # Fetch contributors for the current page
                current_page_contributors = repo.get_contributors().get_page(page - 1)
                
                if not current_page_contributors:
                    break  # No more contributors to fetch
                
                contributors.extend(current_page_contributors)
                page += 1  # Move to the next page
            
            # Print the contributors and their contribution counts
            for idx, contributor in enumerate(contributors, start=1):
                print(f"{idx}. {contributor.login} - {contributor.contributions} contributions")
                
                # Fetch and display user profile data
                user = github.get_user(contributor.login)
                print(f"    Name: {user.name or 'N/A'}")
                print(f"    Bio: {user.bio or 'N/A'}")
                print(f"    Location: {user.location or 'N/A'}")
                print(f"    Public Repos: {user.public_repos}")
                print(f"    Followers: {user.followers}")
                print(f"    URL: {user.html_url}")
                
                # Ask user if they want to open the profile URL in the browser
                open_profile = input(f"Do you want to open {contributor.login}'s profile in the browser? (yes/no): ").lower().strip()
                if open_profile == 'yes':
                    webbrowser.open(user.html_url)
            
            print(f"\nTotal contributors fetched: {len(contributors)}\n")
        
        except Exception as e:
            print(f"Error: {e}\n")
    
    elif choice == "q-":
        # Path to the kernel script in the KERNEL folder
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
    
else:
    print("Invalid choice. Please enter 1 or 2.\n")
