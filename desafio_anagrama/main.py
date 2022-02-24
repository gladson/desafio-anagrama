from typing import List

LIST_WORDS_A = [
    "plasma",
    "gerador",
    "miudo",
    "secar",
    "montar",
    "cavalo",
    "predio",
    "escada",
]
LIST_WORDS_B = [
    "amplas",
    "palmas",
    "regador",
    "umido",
    "ceras",
    "tornam",
    "alavanca",
    "coragem",
]


def check_anagram(word_a, word_b):
    return sorted(word_a) == sorted(word_b)


def quantity_in_anagram(param_list_words_a: List, param_list_words_b: List):
    count_anagram = 0
    for word_a in param_list_words_a:
        [
            count_anagram := count_anagram + 1
            for word_b in param_list_words_b
            if check_anagram(word_a, word_b)
        ]

    print(count_anagram)
    return count_anagram


if __name__ == "__main__":
    quantity_in_anagram(LIST_WORDS_A, LIST_WORDS_B)
