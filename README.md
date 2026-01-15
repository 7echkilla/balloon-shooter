# 🎈 Balloon Shooter Game
A simple 2D Balloon Shooter game built Pygame, following OOP principles. The player controls a gun to shoot moving balloons across different levels.

## 🎮 Game Overview
- Control a gun using the keyboard
- Shoot bullets to pop balloons
- Choose between different levels
- Balloons vary in movement, size, and count depending on the level

## 🕹️ Controls
| Key   |     Action    |
|:-----:|:--------------|
| W     | Move gun up   |
| S     | Move gun down |
| SPACE | Move gun down |

## 🧠 Game Design (OOP)
The project is structured using object-oriented principles:
- **Encapsulation**: Each game entity (balloon, bullet, gun, level) is its own class
- **Inheritance**: Levels inherit from a common base Level class
- **Modularity**: Each component is separated into its own file for clarity and scalability

## 📁 Project Structure
balloon-shooter/\
├── [assets](./assets/)/ # Game assets (images and sound effects)\
│   ├── [balloon.png](./assets/balloon.png) # Balloon sprite\
│   ├── [cannon.png](./assets/cannon.png) # Gun sprite\
│   ├── [impact.mp3](./assets/impact.mp3) # Bullet impact sound effect\
│   ├── [pop.mp3](./assets/pop.mp3) # Balloon pop sound effect\
│   └── [silencer.mp3](./assets/silencer.mp3) # Shot sound effect\
├── [src](./src/)/ # Core game source code\
│   ├── [balloon.py](./src/balloon.py) # Balloon entity and behavior\
│   ├── [bullet.py](./src/bullet.py) # Bullet/projectile logic\
│   ├── [game.py](./src/game.py) # Main game loop and state management\
│   ├── [gun.py](./src/gun.py) # Player mechanics\
│   ├── [level_1.py](./src/level_1.py) # Level 1 configuration and logic\
│   ├── [level_2.py](./src/level_2.py) # Level 2 configuration and logic\
│   └── [level.py](./src/level.py) # Base level class and shared functionality\
├── [.gitignore](.gitignore) # Files and folders ignored by Git\
├── [config.env](./config.env) # Environment and game configuration variables\
├── [LICENSE](./LICENSE) # Project license information\
├── [main.py](./main.py) # Game entry point\
├── [README.md](./README.md) # Project documentation\
└── [requirements.txt](./requirements.txt) # Python dependencies

### File Descriptions
- [main.py](./main.py): Entry point of the game. Initialises and starts the game.
- [game.py](./src/game.py): Handles the main game loop and prompts the user to select a level.
- [level.py](./src/level.py): Base class for all game levels. Defines common behavior and structure.
- [level_1.py](./src/level_1.py) implements Level 1:
  - Single balloon
  - Random movement and size
- [level_2.py](./src/level_2.py) Implements Level 2:
  - Multiple balloons
  - Randomized movement and sizes for each balloon
- [gun.py](./src/gun.py): Manages gun movement and rendering.
- [bullet.py](./src/bullet.py): Handles bullet creation, movement, and collision logic.
- [balloon.py](./src/balloon.py): Defines balloon properties such as size, movement, and behavior.

## ▶️ How to Run
1. Clone the repository: `git clone https://github.com/7echkilla/balloon-shooter.git`
2. Navigate to the project directory: `cd balloon-shooter`
3. Load dependencies: `pip install -r requirements.txt`
3. Run the game: `python main.py`