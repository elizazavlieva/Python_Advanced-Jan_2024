def movie_organizer(*args):
    movie_collection = {}

    for movie, genre in args:
        if genre not in movie_collection:
            movie_collection[genre] = []

        movie_collection[genre].append(movie)

    sorted_movies = dict(sorted(movie_collection.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = []

    for genre, movies in sorted_movies.items():
        result.append(f'{genre} - {len(movies)}')
        [result.append(f'* {el}') for el in sorted(movies)]

    return '\n'.join(result)


'''TESTS'''
print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
