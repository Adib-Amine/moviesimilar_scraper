from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import movie 
from typing import List
import schema

app = FastAPI(debug=True)

#middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get('/similar_movies/{movie_name}')
async def get_similar_movies(movie_name : str):
    return movie.find_similar_movies(movie_name=movie_name)

@app.get('/movie_details/{movie_name}', response_model=schema.Movie)
async def get_similar_movies(movie_name : str):
    return movie.find_detail_movie_imdb2(movie.find_url_movie_imdb(movie_name=movie_name))

@app.get('/similar_movies/details/{movie_name}', response_model=List[schema.Movie])
async def get_similar_movies(movie_name : str):
    list_movie = movie.find_similar_movies(movie_name=movie_name)
    data = []
    for mv in list_movie:
        data.append(movie.find_detail_movie_imdb2(movie.find_url_movie_imdb(movie_name=mv)))
    return data


if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port='8000')