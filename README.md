# Top-Starred-Repos
* This script allows you to see the most starred repositories on GitHub for any technology. GitHub's API is used to get the required data in the form of json using the ```requests``` HTTP library. The formatted data is then scraped off to be used in plotly to create visually interpretable information about projects with most stars. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Screenshots](#screenshots)

## General info

* Run the python script.
```$ python3 repos_visual.py ```
* Enter the name of the technology or language you would like to see the projects of.
* Press Enter.
* The result loads in your default browser.
* The names of the repositories are clickable and thus link to their GitHub source page.

![Most Starred Vim](https://github.com/bistimulus/Shoot-Aliens/blob/main/Screenshots/Vim.png?raw=true)

## Technologies
Project is created with:
* Python3 (v==3.8.10)
* Requests (v==2.28.1)
* Plotly (v==5.10.0)
	
## Setup
* Install the dependencies  ```requests``` and ```plotly```

```
$ pip install requests
$ pip install plotly
```

* To run this project, clone it locally using git or simply download the source code ```repos_visual.py```:

```
$ git clone https://github.com/bistimulus/Top-Starred-Repos.git
$ cd Top-Starred-Repos
$ python3 repos_visual.py

```

## Screenshots
![Screenshot 1](https://github.com/bistimulus/Shoot-Aliens/blob/main/Screenshots/Python.png?raw=true)

![Screenshot 2](https://github.com/bistimulus/Shoot-Aliens/blob/main/Screenshots/CPP.png?raw=true)

