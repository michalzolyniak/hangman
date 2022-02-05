import random
import argparse
from functions import (load_data, find_occurrences,
                       check_args_parametr, only_polish_letters)


class HangMan:
    def __init__(self, words: list(), attempt_limit: int, big_letters: bool):
        """
        :param words: list of words to guess
        :param attempt_limit: maximum number of attemps in one game
        :param big_letters: True displaying capital letters
        """
        self.words = words
        self.word_to_guess = random.choice(self.words)
        self.user_output = len(self.word_to_guess) * "_"
        self.user_input = ''
        self.used_letters = set()
        self.word_is_guessed = False
        self.attempts = 1
        self.attempt_limit = attempt_limit
        self.play_again = False
        self.guessed_words = set()
        self.big_letters = big_letters

    def create_user_output(self) -> str:
        """
        :return: create user output
        """
        output = self.user_output
        if len(self.user_input) == 1:
            occurrences = find_occurrences(self.word_to_guess, self.user_input, "letter")
            if len(occurrences) > 0:
                for occur in occurrences:
                    temp = list(output)
                    temp[occur] = self.user_input
                    output = "".join(temp)
        else:
            occurrences = find_occurrences(self.word_to_guess, self.user_input, "expression")
            if len(occurrences) > 0:
                for occur in occurrences:
                    new_value = self.user_input
                    output = "".join((output[:occur[0]], new_value, output[occur[1]:]))
        return output

    def check_if_word_is_guessed(self, word_to_check: str) -> bool:
        """
        :param word_to_check: word to compare with word to guess
        :return: True when word is guessed
        """
        if word_to_check == self.word_to_guess:
            return True
        else:
            return False

    def output(self, op_type: str) -> str:
        """
        :param op_type: operation type
        :return: string for user
        """
        output = ""
        if op_type == "win":
            output = f"Congratulation you have guessed " + '\n' + f"the word: {self.word_to_guess} !!!"
        elif op_type == "lose":
            output = f"You have lost the game!!!" + '\n' +f"The word was: {self.word_to_guess}"
        elif op_type == "game_over":
            output = "See you next time!!!"
        elif op_type == "wrong input":
            output = "Please use only letters from polish alphabet"
        elif op_type == "guessed_words":
            output = f"In this game, you have guessed the following words: {self.guessed_words}"
        elif op_type == "used_expression":
            output = f"Used expression or letters: {self.used_letters}"
        elif op_type == "attempts":
            output = f"Attempt: {self.attempts} of {self.attempt_limit}"
        elif op_type == "input_guess":
            output = 'Guess word:' + self.user_output + '\n'
        elif op_type == "new_game":
            output = 'Would you like to play again? Write yes or no'+ '\n'
        if self.big_letters is True: output = output.upper()
        return output


if __name__ == '__main__':
    ATTEMPS = 5
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--big_letters",
        action='store_true'
    )
    polish_words = load_data('polish_words.txt')
    hang_man = HangMan(polish_words, ATTEMPS, check_args_parametr("--big_letters"))

    while hang_man.word_is_guessed is False and hang_man.attempts <= hang_man.attempt_limit:
        if len(hang_man.guessed_words) > 0:
            #list guessed word
            print(hang_man.output("guessed_words"))
        if len(hang_man.used_letters) > 0:
            #list used expressions and letter
            print(hang_man.output("used_expression"))
        print(hang_man.output("attempts"))
        hang_man.user_input = input(hang_man.output("input_guess"))
        if only_polish_letters(hang_man.user_input) is False:
            #user input contains sign outside polish alphabet
            print(hang_man.output("wrong input"))
        else:
            if hang_man.user_input not in hang_man.used_letters:
                hang_man.used_letters.add(hang_man.user_input)
            hang_man.user_output = hang_man.create_user_output()
            hang_man.word_is_guessed = hang_man.check_if_word_is_guessed(hang_man.user_output)
            hang_man.attempts += 1
            if hang_man.attempts > hang_man.attempt_limit or hang_man.word_is_guessed is True:
                if hang_man.word_is_guessed is True:
                    #word was guessed
                    print(hang_man.output("win"))
                    hang_man.guessed_words.add(hang_man.word_to_guess)
                else:
                    #word wasn't guessed after all attempts
                    print(hang_man.output("lose"))
                hang_man.user_input = input(hang_man.output("new_game"))
                if hang_man.user_input == "yes":
                    #new game
                    hang_man.word_is_guessed = False
                    hang_man.attempts = 1
                    hang_man.word_to_guess = random.choice(hang_man.words)
                    hang_man.user_output = len(hang_man.word_to_guess) * "_"
                    hang_man.used_letters = set()
                else:
                    #end of game
                    print(hang_man.output("game_over"))

