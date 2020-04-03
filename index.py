import requests
from bs4 import BeautifulSoup

def get_HTML_text(url):
    response = requests.get(url)
    response_page=response.text
    
    if response_status == 200:
        return response_page
    elif response_status == 403:
        raise Exception("Try after few minute")
    else:
        raise Exception("something went wrong")


response_page_soup = BeautifulSoup(response_page,"html.parser")
container = response_page_soup.find("table",{"class":"chart full-width"})
movies = container.find("tbody").findAll("tr")

try:

    f = open("movieees.cvs","w")
    f.write("name,image \n")

    for movie in movies:
    title = movie.find("td",{"class","titleColumn"}).a.text
    image = movie.find("td",{"class","posterColumn"}).a.img["src"]
    f.write(title+",\"" +image+"\"\n")

except Exception as e:
    print("oops",e )

else:
    f.close()






print(container)