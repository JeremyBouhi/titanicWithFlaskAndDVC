# Titanic
First you need to download data from Kaggle : https://www.kaggle.com/c/titanic
or you can also just create your own data folder which contains your data files
### Installation
    pip install dvc
### Initialisation    
    dvc init
    dvc remote add localStorage /tmp/titanic-storage (you can add -d option for setting a default remote)
### Share Data
     dvc add data
     dvc push
     git add data.dvc
You can check now that actual data file has been copied to the remote we created in the configuration chapter

    ls -R /tmp/titanic-storage
You can then check all works by first deleting your data folder to retrieve them from the remote

    rm -rf data
    dvc pull
### Reproducibility
    dvc repro pipeline/Dvcfile
### Keep track of your experiment
    git add .
    git commit -m '...'
    git tag -a '...' -m ''
    dvc push 
### Visualize your experiments
    dvc metrics show -T
### Launch Flask App
    python __main__.py
### Keep in .dvc/cache only what you need on your current branch
    dvc gc
### Retrieve the right outputs considering your branch    
    dvc checkout