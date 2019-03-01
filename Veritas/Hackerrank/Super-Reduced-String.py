s = "baab"
# def superReducedString(s):
#     pair = ['aa', 'bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
#     for i in range(len(s)):
#         if s[i:i + 2] in pair:
#             s = s[:i] + s[i + 2:]
#     if len(s) > 0:
#         return s
#     else:
#         return "Empty String"
def superReducedString(s):
    pair = ['aa', 'bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    ss = ''
    counter = 0
    while counter < len(s):
        sss = s[counter:counter + 2]
        if s[counter:counter + 2] in pair:
            ss = s[:counter] + s[counter + 2:]
            s = s[:counter] + s[counter + 2:]
        counter += 1
    if len(ss) > 0:
        return ss
    else:
        return "Empty String"
print(superReducedString(s))

#아빠랑 같이
