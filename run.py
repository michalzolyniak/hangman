import argparse
import random
from functions import (load_data, check_args_parameter, only_polish_letters)
from hangman import HangMan


if __name__ == '__main__':
    ATTEMPTS = 5
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--big_letters",
        action='store_true'
    )
    polish_words = load_data('polish_words.txt')
    hang_man = HangMan(polish_words, ATTEMPTS, check_args_parameter("--big_letters"))

    while hang_man.word_is_guessed is False and hang_man.attempts <= hang_man.attempt_limit:
        if len(hang_man.guessed_words) > 0:
            print(hang_man.output("guessed_words"))
        if len(hang_man.used_letters) > 0:
            print(hang_man.output("used_expression"))
        print(hang_man.output("attempts"))
        hang_man.user_input = input(hang_man.output("input_guess"))
        if only_polish_letters(hang_man.user_input) is False:
            print(hang_man.output("wrong input"))
        else:
            if hang_man.user_input not in hang_man.used_letters:
                hang_man.used_letters.add(hang_man.user_input)
            hang_man.user_output = hang_man.create_user_output()
            hang_man.word_is_guessed = hang_man.check_if_word_is_guessed(hang_man.user_output)
            hang_man.attempts += 1
            if hang_man.attempts > hang_man.attempt_limit or hang_man.word_is_guessed is True:
                if hang_man.word_is_guessed is True:
                    print(hang_man.output("win"))
                    hang_man.guessed_words.add(hang_man.word_to_guess)
                else:
                    print(hang_man.output("lose"))
                hang_man.user_input = input(hang_man.output("new_game"))
                if hang_man.user_input == "yes":
                    hang_man.word_is_guessed = False
                    hang_man.attempts = 1
                    hang_man.word_to_guess = random.choice(hang_man.words)
                    hang_man.user_output = len(hang_man.word_to_guess) * "_"
                    hang_man.used_letters = set()
                else:
                    print(hang_man.output("game_over"))
