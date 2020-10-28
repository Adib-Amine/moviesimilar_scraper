from fastapi import FastAPI
import uvicorn
import urllib3
from bs4 import BeautifulSoup
import urllib.parse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
url = "https://www.movie-map.com/"


def find_similar_movies(movie_name : str):
    # movie_query = url + movie_name.replace(' ',"+")
    movie_decode =  urllib.parse.unquote(movie_name)
    movie_query = url + movie_decode.replace(" ","+") 
    resp = http.request('GET', movie_query)
    data = resp.data
    reponse_html = BeautifulSoup(data, 'html.parser')
    list_movie  = [] 
    for link in reponse_html.findAll("a", {"class": "S"}):
        list_movie.append(link.text)
    return list_movie
    

app = FastAPI(debug=True)

@app.get('/{movie_name}')
async def get_similar_movies(movie_name : str):
    return find_similar_movies(movie_name=movie_name)

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port='8000')