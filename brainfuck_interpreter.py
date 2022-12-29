code = input(': ')
mem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ptr = 0
loop = 0
i = 0
def interpret(n):
    global ptr
    global loop
    global mem
    if code[n]== '[':
        loop +=1
    elif code[n]== '+':
        mem[ptr] += 1
    elif code[n]== '>':
        ptr += 1
    elif code[n]== '<':
        ptr -= 1
    elif code[n]== '-':
        mem[ptr] -= 1
    elif code[n]== '.':
        print(chr(mem[ptr]),end='')
    elif code[n]== ',':
        mem[ptr] = int(input(':'))
print("Output: \n")
while i < len(code):
    if loop != 0:
        while mem[ptr] !=0:
            l=i
            while True:
                if code[l] == ']':
                    break;
                interpret(l)
                l+=1
        i = l
        loop-=1
    else:
        interpret(i)
        i += 1
