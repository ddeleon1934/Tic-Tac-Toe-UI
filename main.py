import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox

# Initialize the game state
squares = [' '] * 9
players = ['X', 'O']
current_player = players[0]

# Winning conditions
win_lines = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# Check if a player has won
def check_win(player):
    for a, b, c in win_lines:
        if squares[a] == squares[b] == squares[c] == player:
            return True
    return False

class TicTacToeGame(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Tic-Tac-Toe Game")
        self.setGeometry(100, 100, 400, 400)

        # Set up the layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Create buttons for the game grid
        self.buttons = []
        for i in range(9):
            button = QPushButton(' ')
            button.setFixedSize(100, 100)
            button.setStyleSheet("font-size: 24px")
            button.clicked.connect(lambda checked, i=i: self.handle_click(i))
            self.layout.addWidget(button, i // 3, i % 3)
            self.buttons.append(button)

    def handle_click(self, index):
        global current_player

        # If the square is already taken, do nothing
        if squares[index] != ' ':
            QMessageBox.warning(self, "Invalid Move", "This square is already taken.")
            return

        # Update the game state
        squares[index] = current_player
        self.buttons[index].setText(current_player)

        # Check for win
        if check_win(current_player):
            QMessageBox.information(self, "Game Over", f"{current_player} is the winner.")
            self.reset_game()
            return

        # Check for draw
        if ' ' not in squares:
            QMessageBox.information(self, "Game Over", "It's a draw.")
            self.reset_game()
            return

        # Switch player
        current_player = players[1] if current_player == players[0] else players[0]

    def reset_game(self):
        global squares, current_player
        squares = [' '] * 9
        current_player = players[0]
        for button in self.buttons:
            button.setText(' ')

# Create the application
app = QApplication(sys.argv)
game_window = TicTacToeGame()
game_window.show()

# Run the application
sys.exit(app.exec_())
