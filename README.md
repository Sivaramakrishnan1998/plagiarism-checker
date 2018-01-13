# Plagiarism Checker

Plagiarism Checking  is the process of locating instances of plagiarism within a work or document.
It is a  Internet-based plagiarism-detection , which checks submitted documents against the 
content of other websites with the aim of identifying plagiarism. 
Results can identify similarities with existing sources, and the links from which the content is taken is displayed.
Most cases of plagiarism are found in academia, where documents are typically essays or reports. However, plagiarism can be found in virtually any field, including novels, scientific papers, art designs, and source code.
 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
python 3.6
virtualenv 
easy_install or pip
BeautifulSoup
nltk
```

### Installing

A step by step series of examples that tell you have to get a development env running

Installing the virtualenv

```
sudo apt-get update
sudo apt-get install virtualenv
```
Creating the virtualenv

```
virtualenv -p python3 environment_name or
python3 -m venv environment_name
```

Installing the requirements.txt file
```
pip install -r requirements.txt
pip freeze
```
Open the python3 interpreter to download the nltk data

```
import nltk
nltk.download('popular')
```
To run the server type the command

 ```
python manage.py runserver
 ```
 To make migrations type
 ```
 python manage.py makemigrations
 python manage.py migrate
 
 ```
 
## Built With

* [Django](https://docs.djangoproject.com/en/2.0/) - The web development framework used
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Scraping data from web
* [Nltk](http://www.nltk.org/) - Natural Language Processing





## Author

* **Syed Ali**
* **Sivaramakrishnan**
