import requests
from names import get_first_name
from selenium import webdriver

# API TESTING

# 1
aviel_git = requests.get('https://api.github.com/users/avielb/repos')
num_repos = len(aviel_git.json())
assert(num_repos > 5)

# 2
for i in range(3):
    assert 0 <= requests.get(f'https://api.agify.io/?name='+get_first_name()).json()['age'] <= 120

# 3
unis = requests.get('http://universities.hipolabs.com/search?country=Israel').json()
assert len(unis) > 30

# UI TESTING

# 4
driver = webdriver.Chrome()
driver.get('https://www.ycombinator.com/')
try:
    t = driver.title
except BaseException as e:
    print("issue retrieving title from url, ", e.args)
assert t == "Y Combinator"

# 5
driver2 = webdriver.Chrome()
driver2.get('https://hub.docker.com')
try:
    tt = driver2.title
    print(tt)
except BaseException as e:
    print("issue retrieving title from url, ", e.args)
assert tt == "Docker Hub Container Image Library | App Containerization"