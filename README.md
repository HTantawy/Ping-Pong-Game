# Ping Pong Game by Hussein

This is a simple **Ping Pong Game** developed using the Python `turtle` graphics module. The game features two players, each controlling a racket to hit a ball back and forth across the screen. The game keeps track of the score for each player and displays it on the screen.

## Features

- **Two-player mode**: Control two rackets and play against each other.
- **Ball Movement**: The ball bounces off the screen borders and rackets.
- **Score Tracking**: The game tracks and displays the score for both players.
- **Keyboard Controls**:
  - **Player 1**: Use the **H** key to move up and the **U** key to move down.
  - **Player 2**: Use the **W** key to move up and the **S** key to move down.

## Requirements

- Python 3.x
- `turtle` module (comes pre-installed with Python)

## How to Play

1. Run the game script in your Python environment.
2. The game window will open with a black background and two rackets (one for each player) in the center.
3. Player 1 uses the **H** and **U** keys to move their racket up and down.
4. Player 2 uses the **W** and **S** keys to move their racket up and down.
5. The goal is to prevent the ball from passing your racket while trying to get the ball past your opponent's racket.
6. The score will update whenever a player misses the ball, and the game continues until you close the window.

## Code Explanation

- The game initializes the screen with a width of 800px and a height of 600px. The background color is set to black.
- Two rackets (magenta and blue) are placed on opposite sides of the screen and can be moved up and down using keyboard controls.
- A white ball is created and moves around the screen, bouncing off the borders and rackets.
- The score is displayed at the top, and it updates when either player misses the ball.
- The main game loop runs continuously, updating the screen and moving the ball.

## Controls

- **Player 1**:
  - Move up: Press **H**
  - Move down: Press **U**

- **Player 2**:
  - Move up: Press **W**
  - Move down: Press **S**

## Demo Screenshot

Here is a screenshot of the game in action:

![Ping Pong Game Demo](ping_pong_demo.png)

## How to Run the Game

1. Clone the repository or download the script.
2. Open a terminal and navigate to the folder where the script is located.
3. Run the following command:
   ```bash
   python ping_pong_game.py
