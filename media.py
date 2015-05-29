import json
import urllib

class Movie:
    # construct a new movie object using the imdb id and its trailer URL
    def __init__(self, movie_imdb_id, movie_trailer_url):
        
        # store imdb id in a private member
        self.__imdb_id = movie_imdb_id

        # store the trailer url
        self.trailer_youtube_url = movie_trailer_url

        # use the omdb api to return the imdb json data about the movie
        conn = urllib.urlopen("http://www.omdbapi.com/?i=" + self.__imdb_id + "&plot=short&r=json")
        movie_data = conn.read()
        conn.close()

        # store the imdb json data        
        self.movie_json = json.loads(movie_data)

    # return the movie title from json data
    @property
    def title(self):
        return self.movie_json["Title"]

    # return the movie poster URL from json data
    @property
    def poster_image_url(self):
        return self.movie_json["Poster"]

    #return the movie plot
    @property
    def plot(self):
        return self.movie_json["Plot"]
    
    #return the movie year
    @property
    def year(self):
        return self.movie_json["Year"]
        
