from sqlalchemy import Column, Integer,String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, backref, relationship

Base=declarative_base()

#Models:  movie, genre,director

#Association Table
genre_director=Table(
    'genre_directors',
    Base.metadata,
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True),
    Column('director_id', Integer, ForeignKey('directors.id'), primary_key=True),
    extend_existing=True
)

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

class Genre(Base):
    __tablename__='genres'
    id=Column(Integer, primary_key=True)
    genre_name=Column(String)

    #relationships
    movies=relationship('Movie', backref=backref('genre'))
    directors=relationship('Director', secondary=genre_director, back_populates='genres')

class Director(Base):
    __tablename__='directors'
    id=Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)

    #relationship
    movies=relationship('Movie', backref=backref('director'))
    genres=relationship('Genre', secondary=genre_director, back_populates='directors')
    


