import re
numbers = ['06$%^&*(72456845', '0672178965', '0982255468','067245888','06756845',
           '067856845','0982456845','09832456845','0972456845','0992456845','099092456845','0902456845'
           ]

def program(numbers):
    l = []
    k = 0
    n = input('input something')
    for i in numbers:
        if i.startswith(n) and re.match(r'((8|\+3)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}',i):
            l.append(i)
            k += 1
            if k == 10:
                break
    return l


print(program(numbers))