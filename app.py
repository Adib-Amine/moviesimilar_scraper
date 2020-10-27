from fastapi import FastAPI
import uvicorn
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
url = "https://www.movie-map.com/"
movie_input  = input(" write movie name : ")
movie_query = movie_input.replace(' ',"+") 
resp = http.request('GET', url+movie_query)
data = resp.data
reponse_html = BeautifulSoup(data, 'html.parser')
for link in reponse_html.findAll("a", {"class": "S"}):
    print(link.text)

# app = FastAPI(debug=True)


# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port='8000')