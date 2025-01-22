# Tic-Tac-Toe Game (PyQt5)
![image](https://github.com/user-attachments/assets/fe100827-f52c-447c-ae8d-10c1879d1e5b)


## Overview
This project implements a simple **Tic-Tac-Toe game** using the **PyQt5** library for the graphical user interface (GUI). 
The game allows two players to play on a 3x3 grid, with the goal of aligning three symbols (either `X` or `O`) horizontally, vertically, or diagonally. The game handles player turns, checks for wins, and resets when the game ends.

## Features
- Interactive GUI created using PyQt5.
- Two-player gameplay.
- Automatic win detection for horizontal, vertical, and diagonal lines.
- Handles invalid moves (e.g., selecting an already occupied square).
- Draw detection when all squares are filled with no winner.
- Reset functionality after a win or draw.

## Prerequisites
- Python 3.x
- PyQt5 installed. You can install it using pip:
  ```bash
  pip install PyQt5
  ```

## How to Run
1. Save the code to a file, for example, `tic_tac_toe.py`.
2. Run the script:
   ```bash
   python tic_tac_toe.py
   ```
3. The game window will appear, displaying a 3x3 grid.

## Gameplay Instructions
1. The game starts with Player `X`.
2. Click on any empty square to make a move.
3. The game alternates turns between players `X` and `O`.
4. The game checks for:
   - A win: A player aligns three of their symbols in a row, column, or diagonal.
   - A draw: All squares are filled with no winner.
5. After the game ends (win or draw), the board resets automatically.

## Code Structure
### 1. **Game Logic**
- `squares`: A list of 9 elements representing the current game state (initially empty).
- `players`: A list containing the two players (`X` and `O`).
- `check_win(player)`: Checks if the given player has a winning line.

### 2. **TicTacToeGame Class**
This class manages the GUI and game interaction. Key methods include:
- `__init__`: Sets up the window, layout, and game grid.
- `handle_click(index)`: Handles player moves, checks for win/draw, and switches turns.
- `reset_game()`: Resets the board and game state after a win or draw.

### 3. **PyQt5 GUI**
- `QPushButton`: Represents each square on the grid.
- `QGridLayout`: Arranges the buttons into a 3x3 grid.
- `QMessageBox`: Displays game results and invalid move warnings.

### 4. **Application Execution**
- `QApplication`: Initializes the PyQt5 application.
- `sys.exit(app.exec_())`: Starts the event loop and runs the application.

## Example Output
### Initial Screen:
```
  X | O |  
 -----------
    | X | O
 -----------
    |   | X
```
### Win Message:
A popup message appears:
```
X is the winner.
```
### Draw Message:
A popup message appears:
```
It's a draw.
```

## Future Enhancements
- Add player name input fields.
- Include a scoreboard to track wins.
- Implement an AI opponent for single-player mode.
- Add themes or customizable grid sizes.
