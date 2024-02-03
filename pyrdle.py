"""
    pyrdle 2024-01-16 12:39 p.m.
    Tom Legrady - Tom@TomLegrady.com
    (c) 2024 Tom Legrady - All Rights Reserved
"""
import re
import sys
import tkinter
from tkinter import messagebox
import requests
from icecream import ic

import game_tk
from config import Config as cfg

ic.disable()


class Game:
    """Controller for the python wordle game"""

    # pylint: disable=too-many-instance-attributes
    __slots__ = (
        "config",
        "window",
        "alphabet",
        "user_input_text",
        "secret_word",
        "user_input",
        "evalbox",
        "score_display",
        "quit",
        "current_guess",
        "score",
    )

    def __init__(self):
        """Constructor"""
        self.fetch_word()
        self.current_guess = 0
        self.score = {
            cfg.SCORE_DISPLAY_KEY_WINS(): 0,
            cfg.SCORE_DISPLAY_KEY_LOSSES(): 0,
        }
        self.window = game_tk.Tk()
        self.alphabet = game_tk.Alphabet(self.window)
        self.user_input_text = tkinter.StringVar()
        self.user_input_text.trace_add(
            cfg.USER_INPUT_TEXT_VALIDATE_CONDITION(), self.validate_user_keypress
        )
        self.user_input = game_tk.UserInput(
            self.user_input_text, self.process_guess, self.window
        )
        self.create_n_guess_evaluations()
        self.score_display = game_tk.ScoreDisplay(self.window)
        self.quit = game_tk.Quit(self.window)

    def fetch_word(self) -> None:
        """Send a request to random word website for a single English,
        six-letter word. Convert the string to upper case. The word comes
        in quotes inside square brackets; filter the out the alphabetic
        letters, and then join the list of letters together into a string.
        """
        try:
            word = requests.get(
                cfg.RANDOM_WORD_URL(), timeout=cfg.REQUEST_TIMEOUT()
            ).text
            word = word.upper()
            self.secret_word = cfg.EMPTY_STRING().join(filter(str.isalpha, word))
        except requests.exceptions.RequestException as error:
            messagebox.showerror(
                "Error",
                cfg.REQUEST_ERROR_MESSAGE()
                + cfg.CHAR_NL()
                + type(error)
                + cfg.CHAR_NL()
                + error,
                icon=messagebox.ERROR,
            )
            sys.exit(1)

    def create_n_guess_evaluations(self) -> None:
        """Create a number of evaluation display boxes, one for each
        guess the player is allowed. The boxes will display their guesses
        with a letter on a green background if it is in the correct position;
        on a yellow background if the word is in the secret word but in
        the wrong position; and on a light grey background if it is not
        in the word at all.
        """
        self.evalbox = [None] * cfg.MAX_GUESSES()
        for i in range(cfg.MAX_GUESSES()):
            self.evalbox[i] = game_tk.Eval(self.window)

    def validate_user_keypress(self, *_):
        """Examine the player's latest keypress, that is, the last character
        in the StringVar. Alphabetic characters are converted to upper
        case; non-alpha characters are replaced with an empty string.
        """
        word = self.user_input_text.get()
        if len(word):
            if word.isalpha():
                ic(word)
                word = word.upper()
            else:
                ic(word)
                word = re.sub("[^A-Z]", "", word)
                ic(word, "--------------------")
            self.user_input_text.set(word)

    def process_guess(self, *_: object) -> None:
        """When the player presses the return key at the end of typing
        their guess, display an evaluation of the guess. If the player
        is out of guess, meaning they have lost, or if they have guessed
        the word, meaning they have won, then handle the game being over.
        If the game is not yet over, increment the number of guesses used up.
        In any case, empty the input box.
        """
        word = self.user_input_text.get()
        if len(word) == 0:
            return

        self.eval_letters(word)

        if self.out_of_guesses() or self.game_solved(self.user_input_text.get()):
            self.handle_game_over(self.user_input_text.get())
        else:
            self.current_guess += 1
        self.user_input_text.set(cfg.EMPTY_STRING())

    def eval_letters(self, word):
        """Determine letter and position matches in guess, display green
        and yellow indications of letters used / used in right position. If
        current letter has same status as previous letter, lump all similar
        letters into a single batch.
        """
        prev_colour = cfg.BG_NONE()
        colour_start_index = 0
        eval_text = self.evalbox[self.current_guess]
        eval_text.insert(cfg.TAG_START_INDEX(), word)

        for idx, char in enumerate(word):
            self.alphabet.hide_used_letter(char)
            if char in self.secret_word:
                if self.secret_word[idx] == word[idx]:
                    new_colour = cfg.BG_POSITION()
                else:
                    new_colour = cfg.BG_LETTER()
            else:
                new_colour = cfg.BG_NONE()

            eval_text.add_text_tag(prev_colour, colour_start_index, idx)
            prev_colour = new_colour
            colour_start_index = idx

        length = len(word)  # handle last batch going to end of word.
        if colour_start_index < length:
            eval_text.add_text_tag(prev_colour, colour_start_index, length + 1)

    def handle_game_over(self, word, testing=False) -> None:
        """When the game is over, display the new score and change the
        game-board colour reflecting whether the player has won or lost.
        Display a popup box displaying the secret word. Reset the various
        game-board widgets to prepare for a new game, display the score,
        fetch a new secret word and reset the number of guesses used up.
        """
        self.gui_update_win_loss(word)

        if not testing:
            messagebox.showinfo(
                cfg.GAME_OVER_POPUP_TYPE(),
                f"{ cfg.FINAL_MESSAGE()} '{self.secret_word}'.",
            )

        for widget in cfg.WIDGETS():
            getattr(self, widget).reset()
        self.user_input_text.set(cfg.EMPTY_STRING())
        for i in cfg.WIDGETS_EVAL():
            self.evalbox[i].reset()
        self.fetch_word()
        self.current_guess = 0

    def gui_update_win_loss(self, word) -> None:
        """If the player has guessed the secret word, they have won, otherwise
        they have lost. Update the stored score, generate a message for the
        scoreboard and set an appropriate background colour,

        """
        if word == self.secret_word:
            self.score[cfg.SCORE_DISPLAY_KEY_WINS()] += 1
            colour = cfg.BG_WON()
        else:
            self.score[cfg.SCORE_DISPLAY_KEY_LOSSES()] += 1
            colour = cfg.BG_LOST()

        self.window.set_bg(colour)
        score_text = cfg.SCORE_DISPLAY_TEXT_FORMAT().format(
            self.score[cfg.SCORE_DISPLAY_KEY_WINS()],
            self.score[cfg.SCORE_DISPLAY_KEY_LOSSES()],
        )
        self.score_display.update(score_text)

    def out_of_guesses(self) -> bool:
        """Available guesses are 0, 1, 2 ... < MAX_GUESSES."""
        return cfg.MAX_GUESSES() <= 1 + self.current_guess

    def game_solved(self, word: str) -> bool:
        """If the players guess matches the secret word, the game is solved."""
        return word == self.secret_word

    def mainloop(self):
        """Run the Tk main loop"""
        self.window.mainloop()


if __name__ == "__main__":
    # pylint broad-exception-caught
    Game().mainloop()

# ======================================================================
# End of File
#
