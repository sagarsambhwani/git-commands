# Step 1: Create a New File in VS Code
# Open VS Code.
# Create a new folder and open it in VS Code.
# Inside the folder, create a new file named example.txt.
# Open a terminal in VS Code by clicking Terminal > New Terminal.


# Step 2: Initialize a Git Repository
# git init

# Step 3: Check Git Status
# git status

# Step 4: Stage the File
# git add example.txt
# git status

# Step 5: Commit the Staged Changes
# git commit -m "Initial commit"


# Step 6: Create a New Branch
# git branch new-feature
# git branch        #### Showing all the branches 


# Step 7: Switch to the New Branch
# git checkout new-feature


#### Step 8: Make Changes to example.txt
# Open example.txt and add some text like "Hello Git!".
# Save the file.

### Step 9: Stage and Commit the Changes
# git add example.txt
# git commit -m "Updated example.txt"


#### Step 10: Switch Back to the Master Branch
# git checkout master

#### Step 11: Merge the new-feature Branch into master
# git merge new-feature

#### Step 12: Create a Remote Repository and Push
# Create a new repository on GitHub (or another platform).
### Add the remote repository
# git remote add origin https://github.com/username/repository.git
### Push the changes
# git push -u origin master


### Step 13: View the Commit History
# git log


### Step 14: Create and Apply a Git Stash
#### Make a change in example.txt (e.g., add another line "New change").
#### Instead of committing it, stash it:
# git stash


### To apply the stashed changes back:
# git stash apply


##### Step 15: Clean Untracked Files
###  If you have any untracked files (not added to Git), you can remove them:
# git clean -f



# 16. Git Merge Conflict (Example)
# Scenario: You have two branches (master and feature) that modify the same file, leading to a merge conflict.
# step-1 : Create a new branch: git checkout -b feature
# step-2 : Modify example.txt in the feature branch:
# Feature branch change.
# step-3  : Stage and commit the change
# git add example.txt
# git commit -m "Updated example.txt in feature branch"
# step-4 : Switch back to the master branch. 
# git checkout master
# step-5 : Modify example.txt in the master branch
# Master branch change.
# step-6 : Stage and commit the change
# git add example.txt
# git commit -m "Updated example.txt in master branch"
# step-7 : Merge the feature branch into master:
# git merge feature

# Expected_output ===> 
# Auto-merging example.txt
# CONFLICT (content): Merge conflict in example.txt
# Automatic merge failed; fix conflicts and then commit the result.
# Reason: The changes in both branches are conflicting because the same lines were modified.


# step-8 : Fix the conflict
# # Open example.txt
# <<<<<<< HEAD
# Master branch change.
# =======
# Feature branch change.
# >>>>>>> feature

#### Edit the file to resolve the conflict .
# Master branch change.
# Feature branch change.


# step-9 : Stage and complete the merge
# git add example.txt
# git commit -m "Resolved merge conflict between master and feature"




# (17). Git Reset (Example)
# Scenario: You made an incorrect commit and want to undo it.

# step-1 : Create and commit a new file:
# echo "Incorrect commit" > wrong.txt
# git add wrong.txt
# git commit -m "Added wrong.txt (incorrect commit)"


# step-2 : Use git reset to undo the last commit: Soft reset (keeps changes in the working directory but unstages them):
# git reset --soft HEAD~1       ####This will undo the commit but leave wrong.txt in the staging area.

#step-3 : Hard reset (discards the commit and the changes):
# git reset --hard HEAD~1   #### This will discard both the commit and the changes.

# step-4 : Expected Output (after hard reset):
# HEAD is now at <previous commit hash> <previous commit message>     #####The changes in wrong.txt will be lost, and the file will be removed if not tracked earlier.


# (18). Git Revert (Example) : Scenario: You want to undo a specific commit without affecting other changes.

# step-1 : Create and commit a file:
# echo "Content for revert" > revert.txt
# git add revert.txt
# git commit -m "Added revert.txt"


# step-2 : View the commit log:
# git log 

# step-3 : Find the hash of the commit you want to revert, for example:
# commit a1b2c3d4...

# step-4 : Revert the commit:
# git revert a1b2c3d4 


### Expected Output:
# [master abc123d] Revert "Added revert.txt"
#  1 file changed, 1 deletion(-)
#  delete mode 100644 revert.txt


# (19). Git Tagging (Example)
# Scenario: You want to create a tag to mark a specific version of your project.

# step-1 : Create and commit a file
# echo "Version 1.0" > version.txt
# git add version.txt
# git commit -m "Added version 1.0 file"


# step-2 : Create a tag 
# git tag v1.0

# step-3 :Verify the tag
# git tag 

# step-4 : Push the tag to the remote repository
# git push origin v1.0

# Expected_output : 
# Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/user/repo.git
#  * [new tag]         v1.0 -> v1.0



# (20). gitignore 

# Using .gitignore to Exclude Unnecessary Files from Version Control
# Imagine you’re working on a Python project, and your project generates temporary or unnecessary files that you don’t want to include in the Git repository (e.g., .pyc files, virtual environment directories, log files, etc.).
# You can use a .gitignore file to prevent these files and directories from being tracked by Git.

# step-1 : Create a New Project Folder
# mkdir my-python-project
# cd my-python-project


# step-2 : Initialize Git Repository
# git init 

# step-3 : Create Necessary Files and Directories
# echo "print('Hello, world!')" > main.py
# mkdir logs
# mkdir venv
# touch logs/app.log
# echo "Temporary data" > temp.txt


# step-4 : Create a .gitignore File:Create a .gitignore file to specify which files and directories Git should ignore
# touch .gitignore

# step-5 : Add Rules to .gitignore :Open the .gitignore file in your code editor and add the following rules:
# # Ignore virtual environments
# venv/

# # Ignore log files
# logs/

# # Ignore all .log files
# *.log

# # Ignore temp files
# temp.txt

# # Ignore Python cache files
# __pycache__/
# *.pyc


# step-6 : Check the Status of Your Files
# git status 

# Expected_output : 
# On branch master

# No commits yet

# Untracked files:
#   (use "git add <file>..." to include in what will be committed)

#     .gitignore
#     main.py

# nothing added to commit but untracked files present (use "git add" to track)


# step-7 : commit the changes 
# git add .
# git commit -m "Initial commit with .gitignore"
