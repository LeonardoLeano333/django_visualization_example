# How to Read:
## configure the environment:
```
virtualenv --python=python3.7 venv
```
- linux:
```
source venv/bin/activate
```
- windows(git bash)
```
source venv/Scripts/activate
```
Install dependencies:
```
pip install requirements.txt
```
## jupyter notebook report
```
python -m jupyter notebook
```
Look for "jupter_treatment > data_presentation.ipynb", in the jupter platform.

## running web application for the dash boards
- running: 
```
python web_visualization_only/manage.py runserver
```
- look at browser: 
http://localhost:8000

