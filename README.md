##Number Guessing Game
This is a simple Number Guessing Game built using Flask, where users try to guess a randomly generated number between 1 and 100. The game keeps track of the number of attempts and provides feedback on whether the guess is too low, too high, or correct.

**Features**
Random Number Generation: The game generates a random number between 1 and 100 at the start.
Attempts Counter: Tracks the number of guesses made by the player.
Feedback: Displays whether the guess is too low, too high, or correct.
Session Management: The game uses Flask sessions to keep track of the player's current game state (the number to guess, number of attempts, and feedback).
Restart Option: Players can restart the game at any time.

**How to Run the Project**
1. Clone the Repository:
    git clone https://github.com/ChauhanKomal9455/NumberGuessingGame.git
    cd NumberGuessingGame

2.Installtion
    pip install Flask

3.Start the Flask app:
    python GuessGame.py

4.The game will run on http://127.0.0.1:5000/ by default. Open this URL in your browser.

**Game Instructions**
1.Enter a number between 1 and 100 in the input field.
2.The game will give feedback if your guess is too low or high.
3.Once you guess correctly, the game will display the number of attempts it took you to guess the correct number.
4.You can restart the game at any time by clicking the "Restart Game" button.

**License**
This project is open-source and available under the MIT License.

Developed By
Komal | https://www.linkedin.com/in/komal-chauhan-3a2538289/ | https://github.com/ChauhanKomal9455

