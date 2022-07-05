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

git commit -m "message"     (created a version)
To send version/changes to github 

git push origin main      #origin main --- to push it to original main
To check remote url

# to check previous version
git log

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = @gmail.com

HEROKU_API_KEY = <>

HEROKU_APP_NAME = demo-pipeline-ml

......
Build Docker Image

docker build -t <image name>:<tag name> .

# to check docker images
docker images
____________
#to run docker image
___________
#pip .... if not want to use---- write code in setup.py
_____________
python setup.py install
______________
-e . going to install folder where  __init__.py were created  you must have setup.py 
-e . or file_package use any one

_______________________________________
housing
1)logger 2)exception 3)config         4)entity               5)pipeline                    6) component
 login                      anything that has attribute   data injection                     data injection
  to get loger                                       bringing data to the system           datavalidation    
                                                       datavalidation                       data transformation
                                                [schema validation,nullcheck,duplicate,       model training
                                                outlers,domain value,data range,data drift]    model evaluation
                                                      EDA(jupyter notebook)                     push model      
                                                Data Transformation--pickle obj for fe
                                                 Model training(model selection,model comp..
                                                hyperparameter tunning)--pickle obj for model
                                                Model evaluation(test dataset,model comp.(base model 
                                                       and minimum expectation))
                                                (saving object into a file is called serialization)
                                                Push model (saving model into directory)
                                                --collection of all component in a form flow 
5)pipeline:task to arrange each component into sequence
4)entity :defied multiple structure,for config of pipeline and output,output called artifact...every stage of pipeline we define one artifact
(artifact) anything generated during pipeline for example graph,pickle.......
artifact defined for each component of pipeline .. output we get from each component
data injection artifact: output gets from data injection component...it need some data to generate artifact
data validation artifact : training test set..artifact will utilize by data transformation
data transformation artifact
model training artifact
model evaluation artifact
model pushing artifact
 
datainjectionconfig:its gona specify what data requried for data injection stage, how artifacts will get data to create artifact....
datatransformationconfig   it store where our  pickle files/object should be saved
datavalidationconfig
modeltrainingconfig
modelevaluationconfig
modelpushconfig

3)config: all configration information we write into file... like schema info,yml file,database,.... config is going to read the file and structure from entity and provide config to pipeline when required...
(cofig is going to read the information from file )
import all entity configs

------------------------------------------------------------------------------------
entity:
ipynbkernel  
pip install ipykernel


to read entity --config_entity.py
configuration.py to read data from config_entity.py

util folder
file which is not a part of main pipeline
any helper function we store it inside util.py
to read config.yaml ---direction--

#