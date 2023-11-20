#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_occurrences(sentence, target_char):
    for index, char in enumerate(sentence):
        if char == target_char:
            print(f'Символ "{char}" найден в позиции {index + 1}')

if __name__ == '__main__':
    input_sentence = input('Введите предложение: ')
    target_character = input('Введите символ для поиска: ')

    print_occurrences(input_sentence, target_character)
