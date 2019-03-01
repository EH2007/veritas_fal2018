s = "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
def hackerrankInString(s):
    hackerrank = "hackerrank"
    for i in range(len(s)):
        if s[i] in hackerrank:
            ss = s[i]
            for b in range(len(hackerrank)):
                if hackerrank[b] == s[i]:
                    hackerrank = hackerrank[:b] + hackerrank[b + 1:]
                    break
    if len(hackerrank) == 0:
        return "YES"
    else:
        return "NO"
print(hackerrankInString(s))