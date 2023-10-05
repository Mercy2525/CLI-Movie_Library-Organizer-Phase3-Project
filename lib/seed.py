#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Genre,Director,Movie
from faker import Faker
import random

if __name__ == "__main__":
    engine = create_engine('sqlite:///movies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    fake=Faker()

    session.query(Genre).delete()
    session.query(Director).delete()
    session.query(Movie).delete()

    movie_genre=['Action','Adventure','Mystery','Comedy','Drama','Fantasy','Thriller','Crime','Science-Fiction']
    
    available_movie_names=['The Shawshank Redemption','Interstellar', 'Forrest Gump','Saving Private Ryan','Goodfellas', 
        'Back to the Future', 'Alien', 'The Graduate','The Usual Suspects', 'Back to the Future', 'The Breakfast Club',
        'The Exorcist','A Beautiful Mind','The Sixth Sense','The Grand Budapest Hotel','Spirited Away','The Shining',
        'The Graduate', 'No Country for Old Men','12 Angry Men','Apocalypse Now','The Usual Suspects','Gone with the Wind',
        'The Wizard of Oz', 'Casablanca','The Sound of Music','A Streetcar Named Desire'
    ]

    #generate directors data
    directors=[]
    for i in range(9):
        director= Director(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        session.add(director)
        session.commit() #commit each
        directors.append(director)

    #generate genres
    genres=[]
    for genre_name in movie_genre:
        genre=Genre(
            genre_name=genre_name                
        )

        session.add(genre)
        session.commit()
        genres.append(genre)

    #generate movies
    movies=[]

    director_genre_relationship=set()
    for director in directors:
        for i in range(1,3):
            director=random.choice(directors)
            genre=random.choice(genres)

            if available_movie_names:
                movie_name = random.choice(available_movie_names)
                available_movie_names.remove(movie_name)  # Remove the used movie name
            else:
                break  # No more available movie names

            movie=Movie(
                movie_name=movie_name,
                genre=genre.genre_name,
                overview=fake.sentence(),
                director=f'{director.first_name} {director.last_name}',
                genre_id=genre.id,
                director_id=director.id
            )
            movies.append(movie)

        


    session.bulk_save_objects(movies)
    session.commit()
    session.close()

