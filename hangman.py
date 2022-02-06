import random
from functions import find_occurrences


class HangMan:
    def __init__(self, words: list, attempt_limit: int, big_letters: bool):
        """
        :param words: list of words to guess
        :param attempt_limit: maximum number of attempts in one game
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
            output = f"You have lost the game!!!" + '\n' + f"The word was: {self.word_to_guess}"
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
            output = 'Would you like to play again? Write yes or no' + '\n'
        if self.big_letters is True:
            output = output.upper()
        return output
