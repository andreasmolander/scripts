""" Print git repository versions

This script will print the latest commit hash for each subdirectory in the current directory.
It does not check whether the subdirectory is a git repository or not.

It can be used for documenting the versions of the repositories in a project, e.g. before
a `git pull` so one can revert back in case of breakage.
"""

import os
import subprocess

def print_latest_commit(repo_dir):
    try:
        # Change to the repository directory
        os.chdir(repo_dir)
        
        # Run the git log command to get the latest commit
        result = subprocess.run(['git', 'log', '-1'], capture_output=True, text=True)

        # Fetch only the commit hash
        result.stdout = result.stdout.split('\n')[0]
        
        # Check if the command was successful
        if result.returncode == 0:
            print(f"Latest commit for {repo_dir}:\n{result.stdout}\n")
        else:
            print(f"Failed to fetch latest commit for {repo_dir}:\n{result.stderr}")
    except Exception as e:
        print(f"An error occurred for {repo_dir}: {e}")

def print_latest_commits(repo_dirs):
    # Iterate over each repository directory and fetch the print commit
    for repo_dir in repo_dirs:
        print_latest_commit(repo_dir)

if __name__ == '__main__':
    # current directory
    current_dir = os.getcwd()

    # Check all subdirs
    repo_dirs = [d for d in os.listdir(current_dir) if os.path.isdir(d)]

    # Set full paths
    repo_dirs = [os.path.join(current_dir, repo_dir) for repo_dir in repo_dirs]

    print_latest_commits(repo_dirs)