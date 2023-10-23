import random

def compare_nums(max_len, hidden_num, user_guess):
    bulls = 0
    cows = 0
    for i in range(max_len):
        if user_guess[i] == hidden_num[i]:
            bulls += 1
        elif user_guess[i] in hidden_num:
            cows += 1
    return bulls, cows


def generate_secret_number(length):
    random_num = random.randint(10**(length-1), (10**length)-1)
    return str(random_num)





