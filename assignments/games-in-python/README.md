# 🎮 Games in Python

## 🎯 Objective

Build a classic word-guessing game where players guess letters to reveal a hidden word before running out of attempts. This assignment practices string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Create a fully functional Hangman game that randomly selects a word for the player to guess. The player should be able to guess letters one at a time, see their progress, and receive feedback on whether they've won or lost.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list of words
- Accept letter guesses from the player via user input
- Display the current progress using underscores for unrevealed letters (e.g., `_ _ _ _`)
- Track and display the number of incorrect guesses remaining
- Reveal all instances of a guessed letter when it appears in the word
- End the game when the word is guessed or attempts are exhausted
- Display a win message when the player guesses the word correctly
- Display a lose message with the correct word when attempts run out
