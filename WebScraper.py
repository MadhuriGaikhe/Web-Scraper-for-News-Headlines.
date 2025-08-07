import requests 
from bs4 import BeautifulSoup

#Make the HTTP Request to the News website
response = requests.get("https://www.indiatvnews.com/maharashtra")

#Parse the HTML Document
soup = BeautifulSoup(response.content , 'html.parser')

#Extract the News Headlines
headlines = soup.find_all("h3")

#Display the News Headlines
for headline in headlines:
    
    #Convert the HTML tag into String Format
    headline_text = headline.text

    #Write to the file
    with open("WebScraper.txt","a",encoding="utf-8") as file:
        file.write(headline_text)
        file.write("\n")
        