def solution(my_string):
    vowel = "aeiou"
    for i in vowel:
        my_string = my_string.replace(i, '')
    return my_string