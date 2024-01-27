"""
    test_game_tk 2024-01-26 3:26 p.m.
    Test the game_tk widgets
    Tom Legrady - Tom@TomLegrady.com
    (c) 2024 Tom Legrady - All Rights Reserved
"""
import game_tk as tltk


def test_main():
    test_window()
    test_alphabet()


def test_window():
    win = tltk.Tk()

    assert win["background"] == "#9abdf5"

    win.set_bg("red")
    assert win["background"] == "red"

    win.set_bg("green")
    assert win["background"] == "green"

    win.reset()
    assert win["background"] == "#9abdf5"


def test_alphabet():
    win = tltk.Tk()
    alpha = tltk.Alphabet(win)
    assert alpha.get() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in "TESTING":
        alpha.hide_used_letter(c)
    assert alpha.get() == "ABCD F H JKLM OPQR  UVWXYZ"

    alpha.init_text()
    assert alpha.get() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


if __name__ == "__main__":
    test_main()
