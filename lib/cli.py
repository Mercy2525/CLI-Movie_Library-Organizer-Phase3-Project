#!/usr/bin/env python3

# CLI inteface
from models import Movie,Genre,Director

def welcome():
    return print('Hello, Welcome To Your Movie Library Organizer\n')

def main_menu():
    print('Menu Options:')
    print('1. Search For Movies')
    print('2. Add a Movie')
    print('3. Delete a Movie')
    print('4. Exit\n')

def search_movies():
    print('Search Movies\n')
    print('Search By:')
    print('1. Title')
    print('2. Genre')
    print('3. Director')
   

def exit():
    print("Thank you for using Movie Library Organizer! Goodbye.")


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
                print('INVALID OPTION !\n')
                continue
        elif choice =='2':
            print('Add Movie')
            title=input('Enter the name of your movie: ')
            genre_id=input('Enter genre_id between(1-9): ')
            overview=input('Enter Movie Overview: ')
            director_id=input('Enter director_id between(1-18): ')
            Movie.add_movie(title,genre_id,overview,director_id)
            print('Movie added successfully!')
        elif choice =='3':
            print('Delete a Movie')
            to_delete= input('Enter the Movie Title to delete: ')
            Genre.delete_movie(to_delete)
            print(f"The Movie '{to_delete}' deleted successfully")
        elif choice =='4':
            exit()
            break
        else:
            print('INVALID OPTION !\n ')
            
