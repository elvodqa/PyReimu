import pyreimu


game = pyreimu.Pyreimu("Example Game")

game.speaker("Alice")
game.talk("Hello, world!")
game.talk("This is a test.")
game.talk("I hope you enjoy it!")
game.talk("Goodbye!")

game.speaker("Bob")
game.talk("Hello, world!")
game.talk("I'm an another character.")
game.talk("I hope you enjoy it!")
game.talk("Goodbye!")

game.run()
