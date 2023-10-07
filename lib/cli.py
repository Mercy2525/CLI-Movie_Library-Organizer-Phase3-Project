#!/usr/bin/env python3
import models
from rich import print
from rich.console import Console
# CLI inteface
from models import Movie,Genre,Director
thumbs_up_emoji = "\U0001F44D"
party_popper_emoji = "\U0001F389"
sad_emoji = "\U0001F622"
cry_emoji = "\U0001F62D"

def welcome():
    return print('[magenta] Hello, Welcome To Your Movie Library Organizer\n [magenta]')

def main_menu():
    print('\n [blue] Menu Options:[blue]')
    print('1. Search For Movies')
    print('2. Add a Movie')
    print('3. Delete a Movie')
    print('4. [red]Exit\n [red]')

def search_movies():
    print('[blue]Search Movies\n[blue]')
    print('Search By:')
    print('1. Title')
    print('2. Genre')
    print('3. Director')
   

def exit():
    print(f"[magenta]Thank you for using Movie Library Organizer! Goodbye {party_popper_emoji}.[magenta]")


if __name__=='__main__':
    welcome()
    
    while True:
        main_menu()
        choice=input('Select an option (1/2/3/4): ')
        if choice =='1':
            search_movies()
            search=input('Select Search Option (1/2/3/4): ')
            if search=='1':
                name=input('Enter the name of movie you want to search: ')
                print(Movie.search_by_name(name))
            elif search == '2':
                genre= input('Enter the genre of movie you want to search: ')
                movies=(Genre.search_by_genre(genre))
                for movie in movies:
                    print(movie)
            elif search=='3':
                director_name=input('Enter the name of Director to search movies: ')
                movies=(Director.search_by_director_name(director_name))
                for movie in movies:
                    print(movie)
            else:
                print('[yellow]Invalid! Pick a valid option \n[yellow]')
        elif choice =='2':
            print('\n [blue] Add Movie [blue]')
            title=input('Enter the name of your movie: ')
            genre_id=input('Enter genre_id between(1-9): ')
            overview=input('Enter Movie Overview: ')
            director_id=input('Enter director_id between(1-18): ')
            Movie.add_movie(title,genre_id,overview,director_id)
            print(f'[green]Movie added successfully!{thumbs_up_emoji}[green]')
        elif choice =='3':
            print('\n [blue]Delete a Movie[blue]')
            to_delete= input('Enter the Movie Title to delete: ')
            Genre.delete_movie(to_delete)
            print(f"[green]The Movie '{to_delete}' deleted successfully{sad_emoji} {cry_emoji}[green]")
        elif choice =='4':
            exit()
            break
        else:
            print('[yellow]Invalid! Pick a valid Option \n [yellow]')
            
