def isRightString(s):
    stack = []
    for char in s:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack:
                return False
            last = stack.pop()
            if (char == ')' and last != '(') or (char == ']' and last != '['):
                return False
    return not stack
n = open("input.txt").readline()
f = open('input.txt').readlines()[1:]
words = []
for i in range(len(f)):
    if (isRightString(f[i][0:])):
        words.append('YES')
    else:
        words.append('NO')
r = open('output.txt', 'w')
for i in range(len(words)):
    r.write(str(words[i]) + '\n')
r.close()