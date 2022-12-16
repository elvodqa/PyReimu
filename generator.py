import toml

config = toml.load("my_game.toml")
print("Configuring for game: " + config["info"]["name"])
print("By: "+config["info"]["creator"])