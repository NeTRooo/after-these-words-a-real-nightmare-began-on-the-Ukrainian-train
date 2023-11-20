#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check_and_correct(sequence):
    words = sequence.split()

    for i in range(len(words)):
        word = words[i]

        if "чя" in word:
            corrected_word = word.replace("чя", "ча")
            words[i] = corrected_word
        elif "щя" in word:
            corrected_word = word.replace("щя", "ща")
            words[i] = corrected_word

    corrected_sequence = ' '.join(words)
    return corrected_sequence

if __name__ == '__main__':
    sequence = input("Введите последовательность: ")
    corrected_sequence = check_and_correct(sequence)

    print("Исходная последовательность:", sequence)
    print("Исправленная последовательность:", corrected_sequence)
