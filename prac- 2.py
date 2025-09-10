games = [
    {"title": "The Legend of Zelda", "genre": "Adventure", "year": 1986, "platform": "NES"},
    {"title": "Minecraft", "genre": "Sandbox", "year": 2011, "platform": "PC"},
    {"title": "Overwatch", "genre": "Shooter", "year": 2016, "platform": "PC"}
]

for game in games:
    print(f"Title: {game['title']}, Genre: {game['genre']}, Year: {game['year']}, Platform: {game['platform']}")

def print_game_info(game: dict) -> None:
    print(f"Title: {game['title']}, Genre: {game['genre']}, Year: {game['year']}, Platform: {game['platform']}")

for game in games:
    print_game_info(game)