"""
    Config 2024-01-18 4:40 p.m.
    Part of the pyrdle wordle program.
    Tom Legrady - Tom@TomLegrady.com
    (c) 2024 Tom Legrady - All Rights Reserved
"""

from enum import Enum
import tkinter as tk


class Config(Enum):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ALPHA_BORDER_WIDTH = 5
    ALPHA_HEIGHT = 1
    ALPHA_INSERT_AT = tk.END
    ALPHA_PACK_SIDE = tk.TOP
    ALPHA_RELIEF = tk.FLAT
    ALPHA_WIDTH = 26

    BG_LETTER = "yellow"
    BG_LOST = "red"
    BG_NONE = "lightgrey"
    BG_PLAY = "#9abdf5"
    BG_POSITION = "green"
    BG_WON = "green"

    CHAR_HASH = "#"
    CHAR_SPACE = " "
    CHAR_UC_A = "A"
    CHAR_NL = "\n"

    DELETE_THESE = [
        "alphabet",
        "entry",
        "score_display",
    ]

    EMPTY_STRING = ""

    EVAL_BG = "lightblue"
    EVAL_HEIGHT = 1
    EVAL_INDEX_START = "1."
    EVAL_PACK_SIDE = tk.TOP
    EVAL_STATE_DISABLED = tk.DISABLED
    EVAL_STATE_ENABLED = "normal"
    EVAL_WIDTH = 8

    FINAL_MESSAGE = "The word was"
    FONT_SIZE = ("Helvetica Bold", 16)

    GAME_OVER_POPUP_TYPE = "INFO"
    GAME_TITLE = "Pyrdle"
    GEOMETRY = "375x500+200+200"
    GEO_HEIGHT = 500
    GEO_WIDTH = 375

    MAX_GUESSES = 6

    PAD_X = 10
    PAD_Y = 10

    RANDOM_WORD_URL = (
        "https://random-word-api.herokuapp.com/word?number=1&length=6&lang=en"
    )

    QUIT_PACK_SIDE = tk.BOTTOM
    QUIT_TEXT = "Quit"
    QUIT_WIDTH = 14

    REQUEST_ERROR_MESSAGE = "Error accessing random word"
    REQUEST_TIMEOUT = 2

    SCORE_DISPLAY_INITIAL_TEXT = "Won: 0  Lost: 0"
    SCORE_DISPLAY_KEY_LOSSES = "losses"
    SCORE_DISPLAY_KEY_WINS = "wins"
    SCORE_DISPLAY_PACK_SIDE = tk.BOTTOM
    SCORE_DISPLAY_RELIEF = tk.RIDGE
    SCORE_DISPLAY_TEXT_FORMAT = "Won: {}  Lost: {}"
    SCORE_DISPLAY_WIDTH = 16

    TAG_CENTER = "centered"
    TAG_END_INDEX = "end"
    TAG_START_INDEX = "1.0"
    TEXT_ALIGN = "center"
    TEXT_LAST_CHAR_INDEX = -1

    USERINPUT_BORDER_WIDTH = 5
    USERINPUT_EVENT = "<Return>"
    USERINPUT_JUSTIFY = tk.CENTER
    USERINPUT_PACK_SIDE = tk.TOP
    USERINPUT_STATE_DISABLED = tk.DISABLED
    USERINPUT_WIDTH = 8

    USER_INPUT_TEXT_VALIDATE_CONDITION = "write"

    WIDGETS = ("window", "alphabet")
    WIDGETS_EVAL = (0, 1, 2, 3, 4, 5)

    def __call__(tag):
        return tag.value
