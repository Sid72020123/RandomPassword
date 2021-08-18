"""
RandomPassword ~ A simple python library to generate customizable random passwords in python!
This library is made with less than 50 lines of code!
Installation:
    pip install RandomPassword
Import:
    import RandomPassword
Info:
    This is a simple library made by Siddhesh Chavan (https://Sid72020123.github.io/)
"""
import random
import string

from RandomPassword import Exceptions

print("RandomPassword v1.0 ~ https://github.com/Sid72020123/RandomPassword")


class RandomPassword:
    def generate_random_password(self, length=5, include_upper_case_alphabets=True, include_lower_case_alphabets=True,
                                 include_special_characters=True, include_numbers=True):
        """
        The function to generate random password
        :param length: The length of the password
        :param include_upper_case_alphabets: Set to 'True' if you want uppercase alphabets in your password
        :param include_lower_case_alphabets: Set to 'True' if you want lowercase alphabets in your password
        :param include_special_characters: Set to 'True' if you want special characters in your password
        :param include_numbers: Set to 'True' if you want digits in your password
        :return: The password
        """
        if length <= 0:
            raise Exceptions.NoLengthToPassword("The Password must have a length greater than 0!")
        chars = ""
        if include_upper_case_alphabets:
            chars += string.ascii_uppercase
        if include_lower_case_alphabets:
            chars += string.ascii_lowercase
        if include_special_characters:
            chars += string.punctuation
        if include_numbers:
            chars += string.digits
        if chars == "":
            raise Exceptions.NoCharsAdded("No characters were added to make a password!")
        password = ""
        for i in range(0, length):
            password += random.choice(chars)
        return password
