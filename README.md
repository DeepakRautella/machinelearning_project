# machinelearning_project
Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation

# Creating conda enviroment
........
conda create -p venv python==3.7 -y
........
to activate enviroment
........
conda activate venv/   (cmd user)

or 
conda activate venv (for others)
........

# Create requirement.txt file       

create new file requirements.txt
pip install -r requirements.txt
........

# create new  app.py file

# to ignore file from being push to git
add file name to .gitignore  for being ignore from beig pushed

# to update git reprositries

git add .   or git add file1,file2,.....
git status
git commit 
git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = @gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = demo-pipeline-ml
......