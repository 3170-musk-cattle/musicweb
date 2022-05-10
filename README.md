# Music Cultural Community Management System (MCCMS)

## Overview
CSC3170 course project.

### TODOs (Oxygen-ver)

- [ ] django back-end environment
- back-end apis
  - [ ] show all artists
  - [ ] show all songs 
  - [ ] show all albums
  - [ ] show all users
  - [ ] add artist
  - [ ] add albums
  - [ ] add songs
  - [ ] add user
  - [ ] show/edit singer
    - [ ] plugin: show number of fans
    - [ ] plugin: show fans sex rate
    - [ ] plugin: show distribution of age range of fans
    - [ ] plugin: show locational distribution of fans
  - [ ] show/edit album
    - [ ] adding new songs
  - [ ] show/edit song
    - [ ] plugin: show emotion
  - [ ] show/edit user
    - [ ] Show playlists
  - [ ] show/edit playlist/ranklist
  - [ ] recommend api
- [ ] vue front-end environment
- front-end
  - [ ] basic admin layout
  - [ ] charts, graphs slots
  - [ ] search-by-name request (general-(songs, albums, artists, users), specific) 
  - [ ] multiline request
- [ ] DataBase
- SQL queries
  - [ ] add/delete queries
  - [ ] modify queries
  - [ ] State quiries
  - [ ] robust search queries

## User Guide

The code is based on python django back-end frame work and applies Vue.js for the front-end.
And the applied database is `MySQL Ver 8.0.28-0ubuntu0.20.04.3 for Linux on x86_64`

To run the code on your machine, we recommand you to create a anaconda environment by running:
```bash
conda create -n MCCMC-web -f environments.yaml
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

