
#  Pyreimu

- [Pyreimu](#pyreimu)
  - [About](#about)
  - [Installing](#installing)
  - [ExampleGame](#examplegame)
  - [Contributing](#contributing)

  

##  About

  

PyReimu is a visual novel framework to make prototyping easy.

  

##  Installing

  PyReimu is avaiable at PyPI.
```bash
pip install pyreimu
```

  

##  ExampleGame

```python
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
```

##  Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for more information.