# pylint disable=invalid-name
"""
    Constants 2024-01-16 12:39 p.m.
    part of the pyrdle game
    Tom Legrady - Tom@TomLegrady.com
    (c) 2024 Tom Legrady - All Rights Reserved
"""
import tkinter as tk
from config import Config as cfg


def main():  # pylint disable=missing-function-docstring
    test_constants()


def test_constants():  # pylint disable=too-many-statements
    assert cfg.ALPHABET() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert cfg.ALPHA_BORDER_WIDTH() == 5
    assert cfg.ALPHA_HEIGHT() == 1
    assert cfg.ALPHA_INSERT_AT() == tk.END
    assert cfg.ALPHA_PACK_SIDE() == tk.TOP
    assert cfg.ALPHA_RELIEF() == tk.FLAT
    assert cfg.ALPHA_WIDTH() == 26
    assert cfg.BG_LETTER() == "yellow"
    assert cfg.BG_LOST() == "red"
    assert cfg.BG_NONE() == "lightgrey"
    assert cfg.BG_PLAY() == "#9abdf5"
    assert cfg.BG_POSITION() == "green"
    assert cfg.BG_WON() == "green"
    assert cfg.CHAR_HASH() == "#"
    assert cfg.CHAR_SPACE() == " "
    assert cfg.CHAR_UC_A() == "A"
    assert cfg.DELETE_THESE() == [
        "alphabet",
        "entry",
        "score_display",
    ]
    assert cfg.EMPTY_STRING() == ""
    assert cfg.EVAL_BG() == "lightblue"
    assert cfg.EVAL_HEIGHT() == 1
    assert cfg.EVAL_INDEX_START() == "1."
    assert cfg.EVAL_PACK_SIDE() == tk.TOP
    assert cfg.EVAL_STATE_DISABLED() == tk.DISABLED
    assert cfg.EVAL_STATE_ENABLED() == "normal"
    assert cfg.EVAL_WIDTH() == 8
    assert cfg.FINAL_MESSAGE() == "The word was"
    assert cfg.FONT_SIZE() == ("Helvetica Bold", 16)
    assert cfg.GEOMETRY() == "375x500+200+200"
    assert cfg.GEO_HEIGHT() == 500
    assert cfg.GEO_WIDTH() == 375
    assert cfg.MAX_GUESSES() == 6
    url = "https://random-word-api.herokuapp.com/word?number=1&length=6&lang=en"
    assert cfg.RANDOM_WORD_URL() == url
    assert cfg.QUIT_PACK_SIDE() == tk.BOTTOM
    assert cfg.QUIT_TEXT() == "Quit"
    assert cfg.QUIT_WIDTH() == 14
    assert cfg.REQUEST_ERROR_MESSAGE() == "Error accessing random word"
    assert cfg.SCORE_DISPLAY_INITIAL_TEXT() == "Won: 0  Lost: 0"
    assert cfg.SCORE_DISPLAY_KEY_LOSSES() == "losses"
    assert cfg.SCORE_DISPLAY_KEY_WINS() == "wins"
    assert cfg.SCORE_DISPLAY_PACK_SIDE() == tk.BOTTOM
    assert cfg.SCORE_DISPLAY_RELIEF() == tk.RIDGE
    assert cfg.SCORE_DISPLAY_TEXT_FORMAT() == "Won: {}  Lost: {}"
    assert cfg.SCORE_DISPLAY_WIDTH() == 16
    assert cfg.TAG_CENTER() == "centered"
    assert cfg.TAG_END_INDEX() == "end"
    assert cfg.TAG_START_INDEX() == "1.0"
    assert cfg.TEXT_ALIGN() == "center"
    assert cfg.TEXT_LAST_CHAR_INDEX() == -1
    assert cfg.USERINPUT_BORDER_WIDTH() == 5
    assert cfg.USERINPUT_EVENT() == "<Return>"
    assert cfg.USERINPUT_JUSTIFY() == tk.CENTER
    assert cfg.USERINPUT_PACK_SIDE() == tk.TOP
    assert cfg.USERINPUT_STATE_DISABLED() == tk.DISABLED
    assert cfg.USERINPUT_WIDTH() == 8
    assert cfg.USER_INPUT_TEXT_VALIDATE_CONDITION() == "write"
    assert cfg.WIDGETS() == ("window", "alphabet")
    assert cfg.WIDGETS_EVAL() == (0, 1, 2, 3, 4, 5)


if __name__ == "__main__":
    main()
