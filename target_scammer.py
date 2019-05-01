from bs4 import BeautifulSoup
import requests
import os
import random
import string

# Scrape Public Email Domains From HubSpot - Return Array
def getEmailDomains():
    email_list = []
    html_doc = requests.get('https://knowledge.hubspot.com/articles/kcs_article/forms/what-domains-are-blocked-when-using-the-forms-email-domains-to-block-feature')
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    sections = soup.find('span', { 'id': 'hs_cos_wrapper_post_body'}).find_all('p')
    sections.pop(0)
    for section in sections:
        for br in section.find_all('br'):
            br.replace_with("\n")
        email_list = email_list + section.text.split("\n")

    email_list.sort()
    return email_list

# Scrape A List Of Names For Either Boys or Girls
def getPeopleNames(sex='boy'):
    url = {}
    url['boy'] = 'https://www.babble.com/pregnancy/1000-most-popular-boy-names/'
    url['girl'] = 'https://www.babble.com/pregnancy/1000-most-popular-girl-names/'
    name_list = []
    html_doc = requests.get(url[sex])
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    sections = soup.find('ol').find_all('li')
    for section in sections:
        name_list.append(section.text.lower())

    name_list.sort()
    return name_list

# Set Target URL (Enter URL To Send, Update userfield/passwordfield target fields below)
target_url = None
no_emails = 1000

# Configure Random Generator
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# Build Names Database
names = getPeopleNames('boy') + getPeopleNames('girl')
names.sort()

# Build Domain Database
domains = getEmailDomains()

for x in range(0, no_emails):
    name_extra = ''.join(random.choice(string.digits))
    username = random.choice(names).lower() + name_extra + '@' + random.choice(domains)
    password = ''.join(random.choice(chars) for i in range(random.randint(8,12)))

    if target_url:
        requests.post(target_url, allow_redirects=False, data= {
            'userfield': username,
            'passwordfield': password
            })

    print('Sending username %s and password %s' % (username, password))

