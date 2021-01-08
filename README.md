# Machine Learning and Statistics - Project 2020 - Assignment
## Eoin Lees - G00387888 - January 2021


The following program i the project for the machine learning and statistics module in January 2021. 


It is run using Jupyter notebooks and docker.

It can be read directly from git hub, however for full functionallity please download and run directly from your desktop. 

## Jupyter notebooks

* Installation
    Visit https://jupyter.org/ and follow instructions to install on your macine
* To Run
    Navigate to the correct folder in the console and type the following command: Jupyter notebooks
    Use the gui provided in the web explorer and select `Project-2020.ipynb`

## Docker

### Linux
```bash
export FLASK_APP=server.py
python3 -m flask run
```

### Windows
```bash
set FLASK_APP=server.py
python -m flask run
```

```bash
docker build -t server-app .
docker run --name server-container -d -p 5000:5000 server-app
```

```Run locally at
http://127.0.0.1:5000/
```
