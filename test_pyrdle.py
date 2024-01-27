# test_pyrdle 2024-01-21 8:32 p.m.
# Tom Legrady - Tom@TomLegrady.com
# (c) 2024 Tom Legrady - All Rights Reserved
#
#
import pyrdle
from icecream import ic

ic.configureOutput(includeContext=True)


def main():
    test_fetch_word()
    test_validate_user_keypress()
    test_process_guess()
    test_eval_letters()
    test_handle_game_over()
    test_won_or_lost()
    test_out_of_guesses()
    test_game_solved()


def test_fetch_word():
    gfw = pyrdle.Game()
    gfw.fetch_word()
    word = gfw.secret_word
    assert len(word) == 6
    assert word.isalpha()
    assert word.isupper()


def test_validate_user_keypress():
    gvuk = pyrdle.Game()
    assert gvuk.user_input_text.get() == ""

    gvuk.user_input_text.set("1")
    gvuk.validate_user_keypress()
    assert gvuk.user_input_text.get() == ""

    gvuk.user_input_text.set("^")
    gvuk.validate_user_keypress()
    assert gvuk.user_input_text.get() == ""

    gvuk.user_input_text.set("A")
    gvuk.validate_user_keypress()
    assert gvuk.user_input_text.get() == "A"

    gvuk.user_input_text.set("Ab")
    gvuk.validate_user_keypress()
    assert gvuk.user_input_text.get() == "AB"


def test_process_guess():
    gpg = pyrdle.Game()
    gpg.secret_word = "SECRET"
    gpg.eval_letters("CHERRY")
    gpg.eval_letters("VICTOR")
    gpg.current_guess = 1
    assert gpg.alphabet.get() == "AB D FG  JKLMN PQ S U WX Z"

    gpg.user_input_text.set("NEWEST")
    gpg.process_guess()
    assert gpg.alphabet.get() == "AB D FG  JKLM  PQ   U  X Z"
    assert gpg.current_guess == 2
    assert gpg.eval[1].get() == "NEWEST"
    assert gpg.eval[1].tag_names(1.0) == ("centered", "lightgrey")
    assert gpg.eval[1].tag_names(1.1) == ("centered", "green")
    assert gpg.eval[1].tag_names(1.2) == ("centered", "lightgrey")
    assert gpg.eval[1].tag_names(1.3) == ("centered", "yellow")
    assert gpg.eval[1].tag_names(1.4) == ("centered", "yellow")
    assert gpg.eval[1].tag_names(1.5) == ("centered", "green")


def test_eval_letters():
    gel = pyrdle.Game()
    gel.secret_word = "SECRET"
    gel.eval_letters("CHERRY")

    assert gel.alphabet.get() == "AB D FG IJKLMNOPQ STUVWX Z"
    assert gel.eval[gel.current_guess].get() == "CHERRY"
    assert gel.eval[gel.current_guess].tag_names() == (
        "sel",
        "centered",
        "lightgrey",
        "yellow",
        "green",
    )
    assert gel.eval[gel.current_guess].tag_names(1.0) == ("centered", "yellow")
    assert gel.eval[gel.current_guess].tag_names(1.1) == ("centered", "lightgrey")
    assert gel.eval[gel.current_guess].tag_names(1.2) == ("centered", "yellow")
    assert gel.eval[gel.current_guess].tag_names(1.3) == ("centered", "green")
    assert gel.eval[gel.current_guess].tag_names(1.4) == ("centered", "yellow")
    assert gel.eval[gel.current_guess].tag_names(1.5) == ("centered", "lightgrey")
    assert gel.eval[gel.current_guess].tag_names(1.6) == ("centered",)


def test_game_solved():
    ggs = pyrdle.Game()
    ggs.secret_word = "SECRET"
    assert not ggs.game_solved("CHERRY")
    assert ggs.game_solved("SECRET")


def test_won_or_lost():
    gwol = pyrdle.Game()
    gwol.secret_word = "SECRET"
    assert gwol.score == {"losses": 0, "wins": 0}
    assert gwol.score_display.cget("text") == "Won: 0  Lost: 0"
    assert gwol.window["background"] == "#9abdf5"

    gwol.won_or_lost("CHERRY")
    assert gwol.score == {"losses": 1, "wins": 0}
    assert gwol.score_display.cget("text") == "Won: 0  Lost: 1"
    assert gwol.window["background"] == "red"

    gwol.won_or_lost("SECRET")
    assert gwol.score == {"losses": 1, "wins": 1}
    assert gwol.score_display.cget("text") == "Won: 1  Lost: 1"
    assert gwol.window["background"] == "green"


def test_handle_game_over():
    ghgo = pyrdle.Game()
    ghgo.secret_word = "VICTOR"
    ghgo.handle_game_over("VICTOR", testing=True)
    assert ghgo.window["background"] == "#9abdf5"
    assert ghgo.alphabet.get() == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert ghgo.user_input_text.get().strip() == ""
    assert ghgo.eval[0].get() == ""
    assert ghgo.eval[1].get() == ""
    assert ghgo.eval[2].get() == ""
    assert ghgo.eval[3].get() == ""
    assert ghgo.eval[4].get() == ""
    assert ghgo.eval[5].get() == ""
    assert ghgo.secret_word != "VICTOR"
    assert ghgo.current_guess == 0


def test_out_of_guesses():
    goog = pyrdle.Game()
    assert not goog.out_of_guesses()
    goog.current_guess = 5
    assert goog.out_of_guesses()


if __name__ == "__main__":
    main()
