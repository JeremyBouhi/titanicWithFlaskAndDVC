# Testing the data sharing

First you need to download data from Kaggle : https://www.kaggle.com/c/titanic
or you can also just create your own data folder which contains your data files

### Installation
    pip install dvc
### Initialisation    
    dvc init
    dvc remote add -d localStorage /tmp/titanic-storage
### Share Data
     dvc add data
     dvc push
     git add data.dvc

You can check now that actual data file has been copied to the remote we created in the configuration chapter

    ls -R /tmp/titanic-storage
    
You can then check all works by first deleting your data folder to retrieve them from the remote

    rm -rf data
    dvc pull
