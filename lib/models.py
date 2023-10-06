#!/usr/bin/env python3
from sqlalchemy import Column, Integer,String, Table, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, backref, relationship,sessionmaker

Base=declarative_base()
engine=create_engine('sqlite:///movies.db')
Session=sessionmaker(bind=engine)
session=Session()
#Models:  movie, genre,director

#Association Table
genre_director=Table(
    'genre_directors',
    Base.metadata,
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True),
    Column('director_id', Integer, ForeignKey('directors.id'), primary_key=True),
    extend_existing=True
)

#Movie Model
class Movie(Base):
    __tablename__='movies'
    id=Column(Integer, primary_key=True)
    movie_name=Column(String)
    genre=Column(String)
    overview=Column(String)
    director=Column(String)

    #relationship
    genre_id=Column('genre_id', ForeignKey('genres.id'))
    director_id=Column('director_id',ForeignKey('directors.id'))

    #String representation for Movie
    def __repr__(self):
        return f"Title: {self.movie_name}, Genre: {self.genre}, Overview: {self.overview}, Directed By: {self.director}"
    
    #Methods
    def add_movie(title,genre_id,overview,director_id):
        genre_instance=session.query(Genre).filter(Genre.id==genre_id).first()
        director_instance=session.query(Director).filter(Director.id==director_id).first()

        my_movie=Movie(
            movie_name=title,
            genre=genre_instance.genre_name,
            overview=overview,
            director=f'{director_instance.first_name} {director_instance.last_name}',
            genre_id=genre_instance.id,
            director_id=director_instance.id
        )
        session.add(my_movie)
        session.commit()
        return my_movie
    
    #Search movie by title
    def search_by_name(title):
        movie= session.query(Movie).filter(Movie.movie_name==title).first()
        if movie is not None:
            return movie
        else:
            return "Movie not found"

#Genre Model
class Genre(Base):
    __tablename__='genres'
    id=Column(Integer, primary_key=True)
    genre_name=Column(String)

    #relationships
    movies=relationship('Movie', backref=backref('genre_movie'))
    directors=relationship('Director', secondary=genre_director, back_populates='genres')

    #String representation for Genre
    def __repr__(self):
        return f"Movie_Genre: {self.genre_name}"
    
    #Methods
    #Returns all movie instances of a given genre
    def search_by_genre(genre):
        movies = session.query(Movie).join(Genre).filter(Genre.genre_name == genre).all()
        
        if not movies:
            print("No movies found for the genre:", genre)
        else:
            return movies

    
    #Deletes movie given by name
    def delete_movie(name):
        all_movies=session.query(Movie).filter(Movie.movie_name==name)
        all_movies.delete()
        session.commit()
        return all_movies.first()

class Director(Base):
    __tablename__='directors'
    
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)

    #relationship
    movies=relationship('Movie', backref=backref('director_movie'))
    genres=relationship('Genre', secondary=genre_director, back_populates='directors')

    #String representation for Director
    def __repr__(self):
        return f" First_Name: {self.first_name} Surname: {self.last_name}"
    
    #Methods
    #display all movies made by one director
    def search_by_director_name(name):
        movies=session.query(Movie).filter(Movie.director==name).all()
        if not movies:
            print("No movies found for Director:", name)
        else:
            return movies


