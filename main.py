b = input()
num = [int(i) for i in input().split(" ")]

odd = 0
even = 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

group = 0
while True:
    group += 1
    if group % 2 == 1:
        if even == 0 and odd <= 1:
            break
        elif even == 0:
            odd -= 2
        else:
            even -= 1
    else:
        if odd == 0:
            break
        else:
            odd -= 1

if odd == 1:
    if group - 2 <= 0:
        print(0)
    else:
        print(group - 2)
else:
    if group - 1 <= 0:
        print(1)
    else:
        print(group - 1)
