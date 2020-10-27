from fastapi import FastAPI
import uvicorn
import urllib3


http = urllib3.PoolManager()
url = "https://www.movie-map.com/"
movie_input  = input(" write movie name : ")
movie_query = movie_input.replace(' ',"+") 
resp = http.request('GET', url+movie_query)
data = print(resp.data.decode('utf-8'))


# app = FastAPI(debug=True)


# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port='8000')