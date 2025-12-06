import json

favorite_movie = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": ["Sci-Fi", "Action"],
    "rating": 8.8,
    "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]
}

file_name = "favourite.json"
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(favorite_movie, f, indent=4)

print(f"Data saved to {file_name}")
