#%%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

#%%

# Tester la récupération de quelques films
movies = db.query(Movie).limit(10).all()
for movie in movies:
    print(f"ID: {movie.movieId},Titre: {movie.title}, Genres :{movie.genres}")
else:
    print("No movie found")
# %%

##Récupérer les films genre action ###

action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(10).all()

for movie in action_movies:
    print(f"ID: {movie.movieId},Titre: {movie.title}, Genres :{movie.genres}")
else:
    print("No movie found")
# %%

# Tester la récupération de quelques évaluations

ratings = db.query(Rating).limit(10).all()

for rating in ratings:
    print(f"ID: {rating.userId}, mvId:{rating.movieId}, Rate:{rating.rating}, tp:{rating.timestamp}")
else:
    print ("None")
# %%

## les films dont la note est supérieure à 4

rated_movie = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >4)
    .limit(10)
    .all()
)
print(rated_movie)
for title, rating in rated_movie:
    print(title, rating)
# %%
#Récupération des tags associés aux films

tags = db.query(Tag).limit(10).all()

for tag in tags:
    print(f"ID :{tag.userId}, mvId:{tag.movieId}, tag:{tag.tag}, tp: {tag.timestamp}")
else:
    print("None")
# %%

#Tester les link

links = db.query(Link).limit(10).all()

for link in links:
    print(f"ID :{link.movieId}, IM:{link.imdbId}, TM:{link.tmdbId}")
else:
    print("None")
# %%

## Fermer la seesion

db.close()
# %%
