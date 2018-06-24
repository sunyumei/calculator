'''
Software Group Project
Authors :: Jay Patel(14CE090), Vishwesh Parekh (14CE074)
Title :: Calculator in Python
Date Accomplished On :: 10/10/2015
'''
from tkinter import *
import math
import re


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False  
        self.op = ""
        self.eq = False  

    

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "raise":
            self.total = self.total ** int(self.current)
        if self.op == "rootof":
            self.total = self.total ** (1/int(self.current))
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = math.log(self.total)
        if self.op == "log":
            self.total= math.log(self.total, 10)
        if self.op == "sine":
            self.total=math.sin(self.total)
        if self.op == "cosine":
            self.total = math.cos(self.total)
        if self.op == "tangent":
            self.total = math.tan(self.total)
        if self.op == "exp":
            self.total = math.exp(self.total)
        if self.op == "inv":
            self.total = 1/self.total
        if self.op == "abs":
            self.total = math.fabs(self.total)

        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

    def inp(self):
        self.eq = False
        self.current = calculate(text_box.get())
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = Frame(root)
calc.grid()

root.title("Calculator")
# s = StringVar()
text_box = Entry(calc, justify=RIGHT,width=30,font="Times 16 bold")
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")
# expression = s.get()
#text_box.focus()

def md(l, x):
    a = l.index(x)
    if x == '*' and l[a + 1] != '-':
        k = float(l[a - 1]) * float(l[a + 1])
    elif x == '/' and l[a + 1] != '-':
        k = float(l[a - 1]) / float(l[a + 1])
    elif x == '*' and l[a + 1] == '-':
        k = -(float(l[a - 1]) * float(l[a + 2]))
    elif x == '/' and l[a + 1] == '-':
        k = -(float(l[a - 1]) / float(l[a + 2]))
    del l[a - 1], l[a - 1], l[a - 1]
    l.insert(a - 1, str(k))
    return l


def fun(s):
    l = re.findall('([\d\.]+|/|-|\+|\*)', s)
    sum = 0
    while 1:
        if '*' in l and '/' not in l:
            md(l, '*')
        elif '*' not in l and '/' in l:
            md(l, '/')
        elif '*' in l and '/' in l:
            a = l.index('*')
            b = l.index('/')
            if a < b:
                md(l, '*')
            else:
                md(l, '/')
        else:
            if l[0] == '-':
                l[0] = l[0] + l[1]
                del l[1]
            sum += float(l[0])
            for i in range(1, len(l), 2):
                if l[i] == '+' and l[i + 1] != '-':
                    sum += float(l[i + 1])
                elif l[i] == '+' and l[i + 1] == '-':
                    sum -= float(l[i + 2])
                elif l[i] == '-' and l[i + 1] == '-':
                    sum += float(l[i + 2])
                elif l[i] == '-' and l[i + 1] != '-':
                    sum -= float(l[i + 1])
            break
    return sum


def calculate(expression):
    ex = []
    ans = 0
    if '(' not in expression:
        ans = fun(expression)
        return ans
    for i in range(len(expression)):
        if expression[i] == '(':
            ex.append(i)  # ex=[6,7]
        elif expression[i] == ')':  # 14
            temp = 0
            sub = expression[ex[len(ex) - 1] + 1:i]
            temp = fun(sub)
            expression = expression[0:ex[len(ex) - 1]] + str(temp) + expression[i + 1:len(expression) + 1]
            ex.pop()
            return calculate(expression)

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
        bttn[i]["bg"]= "orange"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="orange")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="#7B68EE 	MediumSlateBlue")
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mult = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="#7B68EE 	MediumSlateBlue")
mult["command"] = lambda: sum1.operation("times")
mult.grid(row = 2, column = 3,  padx=1, pady = 1)

minus = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="#7B68EE 	MediumSlateBlue")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)

add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="#7B68EE 	MediumSlateBlue")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 3,  padx=1, pady = 1)

power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="#7B68EE 	MediumSlateBlue")
power["command"] = lambda: sum1.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "Yellow")
rootof["command"] = lambda: sum1.operation("rootof")
rootof.grid(row=2, column=5, padx=1, pady=1)

fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!",bg="Yellow")
fact["command"] = lambda: sum1.operation("fact")
fact.grid(row=3,column=4, padx=1, pady=1)

loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln",bg="Yellow")
loge["command"] = lambda: sum1.operation("ln")
loge.grid(row=3, column=5, padx=1, pady=1)

log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="Green")
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=4, column=4, padx=1 , pady=1)

sine = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "pink")
sine["command"]=lambda: sum1.operation("sine")
sine.grid(row=5,column=0,padx=1,pady=1)

cosine = Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "pink")
cosine["command"]=lambda: sum1.operation("cosine")
cosine.grid(row=5,column=1,padx=1,pady=1)

tangent = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "pink")
tangent["command"]=lambda: sum1.operation("tangent")
tangent.grid(row=5,column=2,padx=1,pady=1)

exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="Green")
exponent["command"]=lambda: sum1.operation("exp")
exponent.grid(row=5,column=3,padx=1,pady=1)

inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="Blue")
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=5,column=4,padx=1,pady=1)

point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="#708090 	SlateGray")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 4, column = 1, padx=1, pady = 1)

inp= Button(calc,height =2,width=4,padx=10, pady = 10, text = "inp",bg="#708090 	SlateGray")
inp["command"] = sum1.inp
inp.grid(row = 4, column = 2,  padx=1, pady = 1)


clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="#708090 	SlateGray")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 4,  padx=1, pady = 1)

all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="#708090 	SlateGray")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

equals = Button(calc,height =2,width=4,padx=10, pady = 10, text = "=",bg="#7B68EE 	MediumSlateBlue")
equals["command"] = sum1.calc_total
equals.grid(row = 4, column = 5,padx=1, pady = 1)

abse = Button(calc,height =2,width=4,padx=10, pady = 10, text = "abs",bg="#7B68EE 	MediumSlateBlue")
abse["command"] = lambda: sum1.operation("abse")
abse.grid(row = 5, column = 5,padx=1, pady = 1)

root.mainloop()
