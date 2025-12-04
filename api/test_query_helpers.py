from database import SessionLocal
from query_helpers import*

db = SessionLocal()

#movies = get_movies(db, limit = 5)
#for film in movies:
#    print(f"ID : {film.movieId},Titre : {film.title}, Genres :{film.genres}")

#rating = get_rating(db, movie_id=1, user_id=1)
#print(f"User ID : {rating.userId}, Movie ID :{rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")

#ratings = get_ratings(db, min_rating=3.5, limit=10)

#for film in ratings:
#    print(f"ID : {film.movieId}, Note : {film.rating}")

#n_movies = get_movie_count(db)
#print(f"Nombre de films : {n_movies}")

n_rating =get_rating_count(db)
print(f"Nombre d'évaluation : {n_rating}")

db.close()
