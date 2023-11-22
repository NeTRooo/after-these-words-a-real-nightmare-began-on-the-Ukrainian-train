#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def common_letters(word1, word2, word3):
    unique_letters_word1 = set(word1)
    unique_letters_word2 = set(word2)
    unique_letters_word3 = set(word3)

    common = unique_letters_word1.intersection(unique_letters_word2, unique_letters_word3)

    print("Общие буквы:", common)

if __name__ == '__main__':
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")
    word3 = input("Введите третье слово: ")

    common_letters(word1, word2, word3)