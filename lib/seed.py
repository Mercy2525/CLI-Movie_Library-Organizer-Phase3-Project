#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Genre,Director,Movie
from faker import Faker
import random

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    fake=Faker()

    session.query(Genre).delete()
    session.query(Director).delete()
    session.query(Movie).delete()

    movie_genre=['The Hungry Hearth',
            'SpiceHub Kitchen',
            'Epicurean Eats',
            'Fork & Knife Grille',
            'Sizzle & Savor',
            'The Cozy Table',
            'Umami Junction',
            'Hearthstone Cafe',
            'Basil & Sage Bistro',
            'The Dining Den',
            'Gastronomic Garden',
            'Firefly Grillhouse'
            ]
    
    movie_names=[

    ]

    