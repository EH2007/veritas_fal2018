s = "We promptly judged antique ivory buckles for the next prize"
def pangrams(s):
    letter = 'abcdefghijklmnopqrstuvwxyz'
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_s = ''
    for i in range(len(s)):
        if s[i] in capital:
            for b in range(len(capital)):
                if capital[b] == s[i]:
                    result_s += letter[b]
        else:
            result_s += s[i]
    for i in range(len(result_s)):
        if result_s[i] in letter:
            for b in range(len(letter)):
                if letter[b] == result_s[i]:
                    letter = letter[:b] + letter[b + 1:]
                    break
    if len(letter) == 0:
        return "pangram"
    else:
        return "not pangram"
print(pangrams(s))