# CLI-Movie_Library-Organizer-Phase3-Project

# Movie Library Organizer

Simplify your movie collection management with the Movie Library Organizer, a Python application. 

This application allows you to catalog your movies, search for them easily, and perform basic CRUD (Create, Read, Update, Delete) operations.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Command Line Interface (CLI)](#command-line-interface-cli)
  - [Searching Movies](#searching-movies)
  - [Adding a Movie](#adding-a-movie)
  - [Deleting a Movie](#deleting-a-movie)
- [Contributing](#contributing)
- [License](#license)

## Features
- Search for movies by title, genre, or director.
- Add new movies to your collection.
- Delete movies from your collection.
- Intuitive command-line interface (CLI).

## Getting Started

### Prerequisites
- Python 3
- SQLAlchemy library
- SQLite database

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mercy2525/CLI-Movie_Library-Organizer-Phase3-Project.git


1. Navigate to the project directory:
    cd movie-library-organizer
2. Install the required dependencies:
    pip install and pipenv shell to work in the environment
3. Create the SQLite database (movies.db):
    use alembic as a tool

## Usage
### Command Line Interface (CLI)
The Movie Library Organizer is primarily used via the command-line interface (CLI). To start the application, run:
python model.py or ./main.py(making use of the shebang line)

![main menu](images/welcome.jpg)

### Searching Movies
You can search for movies by title, genre, or director:

- To search by title:
Select Search Option (1/2/3): 1
Enter the title of the movie you want to search: [Movie Title]
- To search by genre:
Select Search Option (1/2/3): 2
Enter the genre of the movie you want to search: [Genre Name]
- To search by director:
Select Search Option (1/2/3): 3
Enter the name of the director you want to search: [Director Name]

![search movie](images/search.jpg)

### Adding a Movie
To add a new movie, follow these steps:

Choose option 2 from the main menu.
Enter the movie details as prompted, including title, genre ID, overview, and director ID.

![add movie](images/add_movie.jpg)

### Deleting a Movie
To delete a movie from your collection:

Choose option 3 from the main menu.
Enter the title of the movie you want to delete.

![delete movie](images/delete.jpg)
## Contributing
We welcome contributions to improve the Movie Library Organizer. To contribute:

Fork the repository.
Create a branch for your feature or bug fix.
Make your changes.
Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.


## Author

[MERCY MURIITHI](https://github.com/Mercy2525)



