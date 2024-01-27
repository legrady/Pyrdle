# pylint: disable=invalid-name
"""
    GameTk 2024-01-18 4:39 p.m.
    Tom Legrady - Tom@TomLegrady.com
    (c) 2024 Tom Legrady - All Rights Reserved
"""
import sys
import tkinter as tk
from config import Config as cfg

# ic.disable()


class Tk(tk.Tk):
    """The top level window widget"""

    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.title(cfg.GAME_TITLE())
        self.geometry(cfg.GEOMETRY())
        self.reset()

    def set_bg(self, colour: str) -> None:
        """Set the window background colour"""
        self.configure(background=colour)

    def reset(self) -> None:
        """Set the background colour to the PLAY condition."""
        self.set_bg(cfg.BG_PLAY())


class Alphabet(tk.Text):  # pylint: disable=too-many-ancestors
    """Display the letters of the alphabet which the player  has not yet tried."""

    def __init__(self, window) -> None:
        super().__init__(
            window,
            font=cfg.FONT_SIZE(),
            height=cfg.ALPHA_HEIGHT(),
            width=cfg.ALPHA_WIDTH(),
            borderwidth=cfg.ALPHA_BORDER_WIDTH(),
            relief=cfg.ALPHA_RELIEF(),
            pady=cfg.PAD_Y(),
        )
        self.pack(side=cfg.ALPHA_PACK_SIDE(), pady=cfg.PAD_Y())
        self.init_text()

    def init_text(self) -> None:
        """Delete any existing characters in the display, and insert
        the letters of the alphabet.
        """
        self.delete(cfg.TAG_START_INDEX(), cfg.TAG_END_INDEX())
        self.insert(
            cfg.ALPHA_INSERT_AT(),
            cfg.ALPHABET(),
            cfg.TEXT_ALIGN(),
        )

    def hide_used_letter(self, c: str) -> None:
        """Replace the specified letter of the alphabet with a space character."""
        i = ord(c) - ord(cfg.CHAR_UC_A())
        pos = "1." + str(i)
        self.delete(pos)
        self.insert(pos, cfg.CHAR_SPACE())

    def get(self):
        return super().get(cfg.TAG_START_INDEX(), cfg.TAG_END_INDEX()).strip()

    def reset(self) -> None:
        """Restore the full alphabet  display."""
        self.init_text()


class UserInput(tk.Entry):  # pylint: disable=too-many-ancestors
    """Where the player types their guess"""

    def __init__(self, textvar, process_guess, window) -> None:
        super().__init__(
            window,
            width=cfg.USERINPUT_WIDTH(),
            borderwidth=cfg.USERINPUT_BORDER_WIDTH(),
            font=cfg.FONT_SIZE(),
            textvariable=textvar,
            justify=cfg.USERINPUT_JUSTIFY(),
        )
        self.pack(side=cfg.USERINPUT_PACK_SIDE(), pady=cfg.PAD_Y())
        self.bind(cfg.USERINPUT_EVENT(), process_guess)


class Eval(tk.Text):  # pylint: disable=too-many-ancestors
    """For each player guess, display which letters are in the
    right position; are in the word but in another position; or are
    not in the word at all.
    """

    def __init__(self, window) -> None:
        super().__init__(window)
        self.config(
            font=cfg.FONT_SIZE(),
            width=cfg.EVAL_WIDTH(),
            height=cfg.EVAL_HEIGHT(),
            state=cfg.EVAL_STATE_DISABLED(),
            background=cfg.EVAL_BG(),
        )
        self.tag_config(cfg.TAG_CENTER(), justify=cfg.TEXT_ALIGN())
        self.tag_config(cfg.BG_NONE(), background=cfg.BG_NONE())
        self.tag_config(cfg.BG_LETTER(), background=cfg.BG_LETTER())
        self.tag_config(cfg.BG_POSITION(), background=cfg.BG_POSITION())
        self.pack(side=cfg.EVAL_PACK_SIDE(), pady=cfg.PAD_Y() / 2)

    def insert(self, index: str, chars: str, *_) -> None:
        """Insert  some text into an empty eval box. Call insert() on
        super() to avoid infinite loop.
        """
        self.config(state=cfg.EVAL_STATE_ENABLED())
        super().insert(index, chars)
        self.tag_add(cfg.TAG_CENTER(), cfg.TAG_START_INDEX(), cfg.TAG_END_INDEX())
        self.config(state=cfg.EVAL_STATE_DISABLED())

    def add_text_tag(self, colour: str, start: int, stop: int) -> None:
        """Apply a colour tag to one of more letters."""
        self.config(state=cfg.EVAL_STATE_ENABLED())
        start = cfg.EVAL_INDEX_START() + str(start)
        stop = cfg.EVAL_INDEX_START() + str(stop)
        self.tag_add(colour, start, stop)
        self.config(state=cfg.EVAL_STATE_DISABLED())

    def get(self):  # pylint: disable=arguments-differ
        return super().get(1.0, "end").strip()

    def reset(self) -> None:
        """delete the text contents of the eval box."""
        self.config(state=cfg.EVAL_STATE_ENABLED())
        self.delete(cfg.TAG_START_INDEX(), cfg.TAG_END_INDEX())
        self.config(state=cfg.EVAL_STATE_DISABLED())


class ScoreDisplay(tk.Label):
    """Display the games won and lost."""

    def __init__(self, window) -> None:
        super().__init__(
            window,
            anchor=cfg.TEXT_ALIGN(),
            bg=cfg.EVAL_BG(),
            width=cfg.SCORE_DISPLAY_WIDTH(),
            pady=cfg.PAD_Y(),
            text=cfg.SCORE_DISPLAY_INITIAL_TEXT(),
            font=cfg.FONT_SIZE(),
            relief=cfg.SCORE_DISPLAY_RELIEF(),
        )
        self.pack(side=cfg.SCORE_DISPLAY_PACK_SIDE(), pady=cfg.PAD_Y())

    def update(self, display_text) -> None:  # pylint: disable=arguments-differ
        """Change the text displayed in the score."""
        self.config(text=display_text)


class Quit(tk.Button):
    """The Quit Button"""

    def __init__(self, window) -> None:
        super().__init__(
            window,
            text=cfg.QUIT_TEXT(),
            width=cfg.QUIT_WIDTH(),
            font=cfg.FONT_SIZE(),
            padx=cfg.PAD_X(),
            pady=cfg.PAD_Y(),
            command=self.close,
        )
        self.pack(side=cfg.QUIT_PACK_SIDE(), pady=cfg.PAD_Y())

    def close(self):
        """Game over! ... close the window .. shut the door!"""
        sys.exit(0)


# ======================================================================
# End of File
#
