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
        return f"Title: {self.movie_name} Genre: {self.genre} Overview: {self.overview} Director: {self.director}"
        pass

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
    


