# README

This file describes the process to install a virtual environment on CMM cluster to run osiris models

## Python version

models have built on python 3.4.3, so you need to activate that version in CMM cluster, to do that you need to execute the next sentence:
```
module load python/3.4.3
```

## Create virtual env

```
# move to osiris folder
cd ~/osiris
# create virtualenv
# obs: you can not change the virtual environment name
virtualenv env
# activate environment
source env/bin/activate
# update pip library
pip3 install --upgrade pip3
# install dependencies
pip3 install -r requirements.txt
```
