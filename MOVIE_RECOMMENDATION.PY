# Movie Recommendation System

movies = {
    "Action": ["John Wick", "Mad Max", "Avengers", "The Dark Knight"],
    "Comedy": ["3 Idiots", "The Hangover", "Home Alone", "Superbad"],
    "SciFi": ["Interstellar", "Inception", "Avatar", "The Matrix"],
    "Romance": ["Titanic", "The Notebook", "La La Land", "Pride & Prejudice"],
    "Horror": ["The Conjuring", "Get Out", "A Quiet Place", "It"]
}
print("🎬 Movie Recommendation System")
print("-------------------------------")

print("Available Genres:")
for genre in movies:
    print("-", genre)

user_genre = input("\nEnter your favorite genre: ")

if user_genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[user_genre]:
        print(movie)
else:
    print("Sorry, genre not found!")