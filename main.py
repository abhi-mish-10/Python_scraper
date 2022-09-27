# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Using HTML to do web scraping
# Step 0:- Get all imports and installation done
# Step 1: Get the Html content
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

r = requests.get(url)
htmlContent = r.content
# print(hmtlContent)

# Step 2:- Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

#Step 3:- Traversing the HTML treee














