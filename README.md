# TicTacToe
A web based TicTacToe with login and mutiplayer and singleplayer mode. And also has matchmaking. This is made in Django.

## **Setup**
### Install Python
It should be **easy** to download and install python, but if you\'re still unsure then you can try these guides:  
* [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download)  
* [Complete Python Installation](https://realpython.com/installing-python/)

### Install pipenv Or Install dependencies manually
You either need to install pipenv or Install the dependencies manually

### Getting the project files
1. Clone the repository with git  
			`git clone https://github.com/ColorCookie-dev/TicTacToe.git`
2. Download the zip file from github  
	Click "clone or download" on the github page of the project, and click "Download ZIP".

### Opening the Terminal
* For Windows [Opening the terminal](https://www.lifewire.com/how-to-open-command-prompt-2618089)
and [Traverse to the project folder, in Command Prompt](https://www.windows-commandline.com/command-prompt-change-directory/)
* For Mac OS and Unix like systems, the process is nearly same, and commands are same for traversing are completely same.

### Getting the dependencies
#### Install pipenv
1. With pip
	* [Installing pip](https://pip.pypa.io/en/stable/installing/)     
	* [Installing pipenv with pip](https://pipenv.kennethreitz.org/en/latest/install/#pragmatic-installation-of-pipenv)
	* For archlinux install the package: python-pip  
			`pacman -S python-pip`
	* In the Command Prompt (assuming, the current working directory is the project directory) run the command below  
			`python -m pipenv install`

2. Without pip
	* [Installing pipenv without pip](https://pypi.org/project/pipenv/)
	* For archlinux install the package: python-pipenv  
			`pacman -S python-pipenv`

#### Without Pipenv
Install django and django-mathfilters with pip.  
			`python -m pip install django django-mathfilters`

### Run the server
Run the command below, in the project's directory  
			`python -m pipenv run python manage.py runserver`

### Go to browser of choice, and open the link `localhost:8000/game/3`
Your server should now be running, if you got any errors or problem, just make an github issue.

