def solution(s):
    answer = 0
    number = ""
    
    for i in s:
        number += i
        
        if number == "zero" or number == "0":
            answer = answer * 10 + 0
            number = ""
        elif number == "one" or number == "1":
            answer = answer * 10 + 1
            number = ""
        elif number == "two" or number == "2":
            answer = answer * 10 + 2
            number = ""
        elif number == "three" or number == "3":
            answer = answer * 10 + 3
            number = ""
        elif number == "four" or number == "4":
            answer = answer * 10 + 4
            number = ""
        elif number == "five" or number == "5":
            answer = answer * 10 + 5
            number = ""
        elif number == "six" or number == "6":
            answer = answer * 10 + 6
            number = ""
        elif number == "seven" or number == "7":
            answer = answer * 10 + 7
            number = ""
        elif number == "eight" or number == "8":
            answer = answer * 10 + 8
            number = ""
        elif number == "nine" or number == "9":
            answer = answer * 10 + 9
            number = ""
    
    return answer
