import media
import fresh_tomatoes

# create some movies using the IMDb ID and the YouTube URL
copycat = media.Movie("tt0112722",
                    "https://www.youtube.com/watch?v=lsmXhM4yfU0")

alien = media.Movie("tt0078748",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

matrix = media.Movie("tt0133093",
                    "https://www.youtube.com/watch?v=_Ls19O-9p3s")

terminator2 = media.Movie("tt0103064",
                    "https://www.youtube.com/watch?v=aAr8llumKnY")

memento = media.Movie("tt0209144",
                    "https://www.youtube.com/watch?v=0vS0E9bBSL0")

serial_mom = media.Movie("tt0111127",
                    "https://www.youtube.com/watch?v=OAcimdt8Po0")

close_encounters = media.Movie("tt0075860",
                    "https://www.youtube.com/watch?v=iHN1RIK8Tkg")

iron_man = media.Movie("tt0371746",
                    "https://www.youtube.com/watch?v=1GnJJtpUL_M")

inception = media.Movie("tt1375666",
                    "https://www.youtube.com/watch?v=YoHD9XEInc0")

# create a collection using the movies above
movies = [alien, matrix, terminator2, memento,
          serial_mom, close_encounters, iron_man, inception, copycat]

# open the movie web page using the collection of movies
fresh_tomatoes.open_movies_page(movies)




