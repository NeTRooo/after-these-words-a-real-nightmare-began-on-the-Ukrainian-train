#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def insert_letter_before_last_i(sentence, letter_to_insert):
    last_i_index = sentence.rfind('и')

    modified_sentence = sentence[:last_i_index] + letter_to_insert + sentence[last_i_index:]

    return modified_sentence

if __name__ == '__main__':
    original_sentence = input("Введите предложение: ")
    letter_to_insert = "X"
    result_sentence = insert_letter_before_last_i(original_sentence, letter_to_insert)

    print(result_sentence)
