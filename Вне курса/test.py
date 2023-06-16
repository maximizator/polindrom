def is_palindrome(s):
    for i in range(len(s) // 2): # проходим до середины строки
        if s[i] != s[-i-1]: # сравниваем символы с обоих концов строки
            return False
    return True


s = input('Введите палиндром: ')
print(is_palindrome(s))
