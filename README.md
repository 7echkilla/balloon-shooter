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

<!-- .
├── main.py
├── README.md
└── src
    ├── game.py
    ├── level.py
    ├── level_1.py
    ├── level_2.py
    ├── gun.py
    ├── bullet.py
    └── balloon.py -->

### File Descriptions
- main.py: Entry point of the game. Initializes and starts the game.
- game.py: Handles the main game loop and prompts the user to select a level.
- level.py: Base class for all game levels. Defines common behavior and structure.
- level_1.py: Implements Level 1
  - Single balloon
  - Random movement and size
- level_2.py: Implements Level 2
  - Multiple balloons
  - Randomized movement and sizes for each balloon
- gun.py: Manages gun movement and rendering.
- bullet.py: Handles bullet creation, movement, and collision logic.
- balloon.py: Defines balloon properties such as size, movement, and behavior.

## ▶️ How to Run
1. Clone the repository:
2. Navigate to the project directory: `cd balloon-shooter`
3. Load dependencies: `pip install -r requirements.txt`
3. Run the game: `python main.py`