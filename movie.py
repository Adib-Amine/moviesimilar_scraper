import urllib3
from bs4 import BeautifulSoup
import json
import urllib.parse
from schema import Movie

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



http = urllib3.PoolManager()
url_imdb = "https://v2.sg.media-imdb.com/suggestion/{search_query[0]}/{search_query}.json"
url_similar = "https://www.movie-map.com/"

def find_similar_movies(movie_name : str):
    movie_decode =  urllib.parse.unquote(movie_name)
    movie_query = url_similar + urllib.parse.quote_plus(movie_decode)
    resp = http.request('GET', movie_query)
    data = resp.data
    reponse_html = BeautifulSoup(data, 'html.parser')
    list_movie  = [] 
    for link in reponse_html.findAll("a", {"class": "S"}):
        list_movie.append(link.text)
    return list_movie

def find_url_movie_imdb(movie_name : str):
    movie_name = movie_name.lower().replace(" ", "_")
    resp = http.request('GET', url_imdb.format(search_query = movie_name))
    data = json.loads(resp.data.decode())
    url = "https://www.imdb.com/title/"+data['d'][0]['id']
    return url

def find_detail_movie_imdb(url_movie : str):
    data = {}
    resp = http.request('GET', url_movie)
    soup = BeautifulSoup(resp.data, 'html.parser')

    titleName = soup.find("div",{'class':'titleBar'}).find("h1")
    data['title'] = titleName.contents[0].replace(u'\xa0', u'')

    imageUrl = soup.find('div' ,{'class' : 'poster'}).find('img')
    data['imageUrl'] = imageUrl["src"]

    ratingValue = soup.find("span", {"itemprop" : "ratingValue"})
    data["ratingValue"] = ratingValue.text

    ratingCount = soup.find("span", {"itemprop" : "ratingCount"})
    data["ratingCount"] = ratingCount.text

    duration = soup.find("div",{'class':'subtext'}).find("time")
    data['duration'] = duration.text.strip()

    genre = soup.find("div",{'class':'subtext'}).findAll("a")
    for i in range(len(genre)-1):
        data['genre'] = genre[i].text
    release_date = genre[len(genre)-1]
    data['release_date'] = release_date.text.strip()

    summary_text = soup.find("div",{'class':'summary_text'})
    data['summary_text'] = summary_text.text.strip()

    data["credits"] = {}
    credit_summary = soup.findAll("div",{'class':'credit_summary_item'})
    for i in credit_summary:
        items = i.findAll('a')
        name = i.find("h4")
        data['credits'][name.text] = []
        name.text
        for j in items:
            data['credits'][name.text].append(j.text.strip())





    return data

def find_detail_movie_imdb2(url_movie : str):
    data = {}
    resp = http.request('GET', url_movie)
    soup = BeautifulSoup(resp.data, 'html.parser')
    titleName = soup.find("div",{'class':'titleBar'}).find("h1")
    data['title'] = titleName.contents[0].replace(u'\xa0', u'')
    imageUrl = soup.find('div' ,{'class' : 'poster'}).find('img')
    data['imageUrl'] = imageUrl["src"]
    ratingValue = soup.find("span", {"itemprop" : "ratingValue"})
    data["ratingValue"] = ratingValue.text
    ratingCount = soup.find("span", {"itemprop" : "ratingCount"})
    data["ratingCount"] = ratingCount.text
    duration = soup.find("div",{'class':'subtext'}).find("time")
    data['duration'] = duration.text.strip()
    genre = soup.find("div",{'class':'subtext'}).findAll("a")
    data['genre'] = []
    for i in range(len(genre)-1):
        data['genre'].append(genre[i].text)
    release_date = genre[len(genre)-1]
    data['release_date'] = release_date.text.strip()
    summary_text = soup.find("div",{'class':'summary_text'})
    data['summary_text'] = summary_text.text.strip()
    
    credit_summary = soup.findAll("div",{'class':'credit_summary_item'})
    data['credits'] = {}
    for i in credit_summary:
        items = i.findAll('a')
        name = i.find("h4")
        data['credits'][name.text] = []
        for j in items:
            data['credits'][name.text].append(j.text.strip())
    model = Movie(**data)
    return model




# movie  = find_url_movie_imdb("John Wick 3")
# print('url = ', movie)
# print()
# print(find_detail_movie_imdb2("https://www.imdb.com/title/tt6146586"))
