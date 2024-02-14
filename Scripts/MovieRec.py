from pip._vendor import requests
import json

def get_movies_from_tastedive(name):
    parameter = {"q": name, "type": "movies", "limit": "5"}
    resp = requests.get("https://tastedive.com/api/similar", params=parameter)
    td_resp = json.loads(resp.text)
    return td_resp


def extract_movie_titles(name):
    movies = []
    name = name["Similar"]
    for inner2 in name["Results"]:
        if inner2["Type"] == "movie":
            movies.append(inner2["Name"])
    return movies

def get_related_titles(titles):
    lot = [] # lof stands for list of titles
    for i in titles:
        extracted = extract_movie_titles(get_movies_from_tastedive(i))
        for title in extracted:
            if title not in lot:
                lot.append(title)
    return lot
def get_movie_data(title):
    parameter = {"t": title ,"r": "json"}
    resp = requests.get("http://www.omdbapi.com/", params=parameter)
    data_resp = json.loads(resp.text)
    return data_resp

def get_movie_rating(d):
    for rate in d["Ratings"]:
        if rate["Source"] == "Rotten Tomatoes":
            num = int(rate["Value"][:len(rate["Value"])-1])
            return num
    return 0

def get_sorted_recommendations(alist):
    movies = []
    rt = get_related_titles(alist)
    rt_rate = []
    for i in rt:
        rt_rate.append(get_movie_rating(get_movie_data(i)))
    combined = dict(zip(rt, rt_rate))
    temp = sorted(combined.items(), key=lambda x:x[1], reverse=True)
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i][1] == temp[j][1] and temp[i][0][0] > temp[j][0][0]:
                tmp = temp[i]
                temp[i] = temp[j]
                temp[j] = tmp       
    for i in temp:
        movies.append(i[0])
    return movies
