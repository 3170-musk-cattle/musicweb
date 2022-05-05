# Music Cultural Community Management System (MCCMS)

## Overview
CSC3170 course project.


## User Guide

The code is based on python django back-end frame work and applies Vue.js for the front-end.
And the applied database is `MySQL Ver 8.0.28-0ubuntu0.20.04.3 for Linux on x86_64`

To run the code on your machine, we recommand you to create a anaconda environment by running:
```bash
conda create -n 3170MC-web -f environments.yaml
```

Or, alternatively, you can use `pip` to config your environment:
```bash
pip install -r packages.txt
```

Futhermore, make sure you have a vue environment on your machine.

### Run the back-end programmes
```bash
python manage.py runserver
```
Open `localhost:8000` in your expoler and you will see the web app

### Run the front-end (for debug)

cd into `templates` and run:

```bash
npm run dev
```

The front-end application will be live-comiled.

build the project:

```bash
npm run build
```

