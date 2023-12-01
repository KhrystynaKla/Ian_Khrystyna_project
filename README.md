# Flashcards App for Learning Ukrainian Words

This is a simple flashcards app designed to help users learn Ukrainian words. The app is built using the Pygame library and incorporates features like studying words, reviewing dropped words, and taking quizzes.

## How to Use

User Name Entry:
When you launch the app, you will be prompted to enter your name. Use the keyboard to type your name and press Enter.

## Main Menu:

After entering your name, you will see the main menu with the following options:
Press 1 to study words.

Only if you have played before: Press 2 to see dropped words.
Press 3 to take a quiz.

## Study Words (Option 1):

If it's your first time, the app will create a new user profile for you.
You will be presented with a list of words to study. Press any key to reveal the answers.
After studying, you will be prompted to check the words you've learned or go back to the main menu.

## See Dropped Words (Option 2):

View words that need review.
Press any key to continue and return to the main menu.

## Take a Quiz (Option 3):

You can take a quiz to test your knowledge of Ukrainian words.
Press 1 to check words you've learned or 2 to go back to the main menu.
Exiting the App:
You can exit the app by closing the window.

## Spaced Repetition for Smart Learning

As you play, the game remembers how well you rate your recall of each word and intelligently decides which words will appear in your review session based on your history. You can drop words that you feel you no longer wish to study, and when you view drop words you can add them back into the pool of words to review.

To do this, we store each word reviewed with a datetime stamp and a time interval for the next review; you will not see the word in a review session before the time interval elapses. If you easily recall the next word, the time interval increases; otherwise it decreases depending on how difficult you found the word.

## Notes for Developers

The app uses Pygame for the graphical user interface.
User profiles are created, and progress is tracked for personalized learning.
Words are shuffled and presented in a quiz format to enhance memorization.
Feel free to explore and customize the code for additional features or improvements. Happy learning!

We also used a random word generator to come up with most of the English words to plug into our AI.

https://www.randomlists.com/random-words

The game is played in the pygame environment.

To make your own cards, simply add to the list in word_list.py in the same format.