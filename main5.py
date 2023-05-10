import math
import tkinter

root = tkinter.Tk()
root.resizable(width=False, height=False)

CurrentShow = tkinter.StringVar()
CurrentShow.set('0')

left = '0'
right = '0'
result = 0

operator = ''
memory = '0'

is_operator = False
is_memory = False


def press_number(number):
    global left
    global right
    global operator
    global is_operator
    global is_memory

    if CurrentShow.get() == '0' or CurrentShow.get() == '':
        if number == '.':
            CurrentShow.set('0.')
        # print(f'CurrentShow {CurrentShow.get()}')

    if not is_operator:  # 状态量未被激活，数字在左边
        if CurrentShow.get() == '0':  # 如果是0，则直接赋值
            CurrentShow.set(number)
            left = number
        else:
            if number == '.':
                if '.' not in CurrentShow.get():
                    CurrentShow.set(CurrentShow.get() + number)
                else:
                    return  # 已经有小数点了，不能再输入小数点
            else:
                left = CurrentShow.get() + number
                CurrentShow.set(left)

    else:  # 右边
        if CurrentShow.get() == '0':
            CurrentShow.set(number)
            right = number
        else:
            if number == '.':
                if '.' not in CurrentShow.get():
                    CurrentShow.set(CurrentShow.get() + number)
                else:
                    return  # 已经有小数点了，不能再输入小数点
            else:
                right = CurrentShow.get() + number
                CurrentShow.set(right)


def set_operator(_operator):
    global is_operator
    global operator

    is_operator = True
    operator = _operator
    CurrentShow.set('0')


def equal():
    global left
    global right
    global result

    global operator

    print(f'left: {left}')
    print(f'right: {right}')
    print(f'operator: {operator}')

    if operator == '+':
        result = eval(left) + eval(right)
    elif operator == '-':
        result = eval(left) - eval(right)
    elif operator == '*':
        result = eval(left) * eval(right)
    elif operator == '/':
        result = eval(left) / eval(right)

    print(f'result: {result}\n')
    CurrentShow.set(result)
    left = str(result)


def percentage():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        eval(f'{left} /= 100')
    else:  # 右边
        eval(f'{right} /= 100')


def clear_all():
    global left
    global right
    global result

    global memory
    global operator
    global is_operator
    global is_memory

    CurrentShow.set('0')

    left = '0'
    right = '0'
    result = 0

    operator = ''
    memory = '0'

    is_operator = False
    is_memory = False


def clear():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        CurrentShow.set('0')
        left = '0'
    else:  # 右边
        CurrentShow.set('0')
        right = '0'


def delete_one():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        if len(CurrentShow.get()) == 1:
            CurrentShow.set('0')
        else:
            CurrentShow.set(CurrentShow.get()[:-1])
            left = CurrentShow.get()
    else:  # 右边
        if len(CurrentShow.get()) == 1:
            CurrentShow.set('0')
        else:
            CurrentShow.set(CurrentShow.get()[:-1])
            right = CurrentShow.get()


def negation():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        CurrentShow.set(str(-eval(CurrentShow.get())))
        left = CurrentShow.get()
    else:  # 右边
        CurrentShow.set(str(-eval(CurrentShow.get())))
        right = CurrentShow.get()


def sqrt():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        CurrentShow.set(str(math.sqrt(eval(CurrentShow.get()))))
        left = CurrentShow.get()
    else:  # 右边
        CurrentShow.set(str(math.sqrt(eval(CurrentShow.get()))))
        right = CurrentShow.get()


def reciprocal():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        CurrentShow.set(str(1 / eval(CurrentShow.get())))
        left = CurrentShow.get()
    else:  # 右边
        CurrentShow.set(str(1 / eval(CurrentShow.get())))
        right = CurrentShow.get()


def square():
    global left
    global right
    if not is_operator:  # 状态量未被激活，数字在左边
        CurrentShow.set(str(eval(CurrentShow.get()) ** 2))
        left = CurrentShow.get()
    else:  # 右边
        CurrentShow.set(str(eval(CurrentShow.get()) ** 2))
        right = CurrentShow.get()


def ms():
    global memory
    global is_memory
    memory = CurrentShow.get()
    is_memory = True
    print(memory)


def mr():
    global memory
    global left
    global right
    if is_memory:
        CurrentShow.set(memory)
    if not is_operator:
        left = CurrentShow.get()
    else:
        right = CurrentShow.get()


def mc():
    global memory
    global is_memory
    memory = '0'
    is_memory = False


def mplus():
    global memory
    global is_memory
    if is_memory:
        memory = str(eval(memory) + eval(CurrentShow.get()))
    else:
        memory = CurrentShow.get()
        is_memory = True
    print(memory)


def mminus():
    global memory
    global is_memory
    if is_memory:
        memory = str(eval(memory) - eval(CurrentShow.get()))
    else:
        memory = CurrentShow.get()
        is_memory = True
    print(memory)


def demo():
    root.minsize(320, 420)
    root.title('Calculator')

    # 布局
    # --文本框
    label = tkinter.Label(root, textvariable=CurrentShow, bg='black', anchor='e', bd=5, fg='white', font=('楷体', 20))
    label.place(x=20, y=50, width=280, height=50)

    # --第一行
    # ----Memory clear
    button1_1 = tkinter.Button(text='MC', bg='darkgray', bd=2, command=lambda: mc(), font=("KaiTi", 16, 'bold'))
    button1_1.place(x=20, y=110, width=50, height=35)
    # ----Memory read
    button1_2 = tkinter.Button(text='MR', bg='darkgray', bd=2, command=lambda: mr(), font=("KaiTi", 16, 'bold'))
    button1_2.place(x=77.5, y=110, width=50, height=35)
    # ----Memory save
    button1_3 = tkinter.Button(text='MS', bg='darkgray', bd=2, command=lambda: ms(), font=("KaiTi", 16, 'bold'))
    button1_3.place(x=135, y=110, width=50, height=35)
    # ----Memory +
    button1_4 = tkinter.Button(text='M+', bg='darkgray', bd=2, command=lambda: mplus(),
                               font=("KaiTi", 16, 'bold'))
    button1_4.place(x=192.5, y=110, width=50, height=35)
    # ----Memory -
    button1_5 = tkinter.Button(text='M-', bg='darkgray', bd=2, command=lambda: mminus(),
                               font=("KaiTi", 16, 'bold'))
    button1_5.place(x=250, y=110, width=50, height=35)

    # --第二行
    # ----删除单个数字
    button2_1 = tkinter.Button(text='del', bg='darkgray', bd=2, command=lambda: delete_one(),
                               font=("Courier New", 16, 'bold'))
    button2_1.place(x=20, y=155, width=50, height=35)
    # ----清除当前显示框内所有数字
    button2_2 = tkinter.Button(text='CE', bg='darkgray', bd=2, command=lambda: clear(),
                               font=("Courier New", 16, 'bold'))
    button2_2.place(x=77.5, y=155, width=50, height=35)
    # ----清零(相当于重启)
    button2_3 = tkinter.Button(text='C', bg='darkgray', bd=2, command=lambda: clear_all(),
                               font=("Courier New", 16, 'bold'))
    button2_3.place(x=135, y=155, width=50, height=35)
    # ----取反
    button2_4 = tkinter.Button(text='+/-', bg='darkgray', bd=2, command=lambda: negation(),
                               font=("Courier New", 16, 'bold'))
    button2_4.place(x=192.5, y=155, width=50, height=35)
    # ----开根号
    button2_5 = tkinter.Button(text='sqrt', bg='darkgray', bd=2, command=lambda: sqrt(),
                               font=("Courier New", 16, 'bold'))
    button2_5.place(x=250, y=155, width=50, height=35)

    # --第三行
    # ----7
    button3_1 = tkinter.Button(text='7', bg='pink', bd=2, command=lambda: press_number('7'),
                               font=("Courier New", 16, 'bold'))
    button3_1.place(x=20, y=200, width=50, height=35)
    # ----8
    button3_2 = tkinter.Button(text='8', bg='pink', bd=2, command=lambda: press_number('8'),
                               font=("Courier New", 16, 'bold'))
    button3_2.place(x=77.5, y=200, width=50, height=35)
    # ----9
    button3_3 = tkinter.Button(text='9', bg='pink', bd=2, command=lambda: press_number('9'),
                               font=("Courier New", 16, 'bold'))
    button3_3.place(x=135, y=200, width=50, height=35)
    # ----除
    button3_4 = tkinter.Button(text='/', bg='khaki', bd=2, command=lambda: set_operator('/'),
                               font=("Courier New", 16, 'bold'))
    button3_4.place(x=192.5, y=200, width=50, height=35)
    # ----平方
    button3_5 = tkinter.Button(text='x²', bg='khaki', bd=2, command=lambda: square(), font=("Courier New", 16, 'bold'))
    button3_5.place(x=250, y=200, width=50, height=35)

    # --第四行
    # ----4
    button4_1 = tkinter.Button(text='4', bg='pink', bd=2, command=lambda: press_number('4'),
                               font=("Courier New", 16, 'bold'))
    button4_1.place(x=20, y=245, width=50, height=35)
    # ----5
    button4_2 = tkinter.Button(text='5', bg='pink', bd=2, command=lambda: press_number('5'),
                               font=("Courier New", 16, 'bold'))
    button4_2.place(x=77.5, y=245, width=50, height=35)
    # ----6
    button4_3 = tkinter.Button(text='6', bg='pink', bd=2, command=lambda: press_number('6'),
                               font=("Courier New", 16, 'bold'))
    button4_3.place(x=135, y=245, width=50, height=35)
    # ----乘
    button4_4 = tkinter.Button(text='*', bg='khaki', bd=2, command=lambda: set_operator('*'),
                               font=("Courier New", 16, 'bold'))
    button4_4.place(x=192.5, y=245, width=50, height=35)
    # ----取倒数
    button4_5 = tkinter.Button(text='1/x', bg='khaki', bd=2, command=lambda: reciprocal(),
                               font=("Courier New", 16, 'bold'))
    button4_5.place(x=250, y=245, width=50, height=35)

    # --第五行
    # ----3
    button5_1 = tkinter.Button(text='3', bg='pink', bd=2, command=lambda: press_number('3'),
                               font=("Courier New", 16, 'bold'))
    button5_1.place(x=20, y=290, width=50, height=35)
    # ----2
    button5_2 = tkinter.Button(text='2', bg='pink', bd=2, command=lambda: press_number('2'),
                               font=("Courier New", 16, 'bold'))
    button5_2.place(x=77.5, y=290, width=50, height=35)
    # ----1
    button5_3 = tkinter.Button(text='1', bg='pink', bd=2, command=lambda: press_number('1'),
                               font=("Courier New", 16, 'bold'))
    button5_3.place(x=135, y=290, width=50, height=35)
    # ----减
    button5_4 = tkinter.Button(text='-', bg='khaki', bd=2, command=lambda: set_operator('-'),
                               font=("Courier New", 16, 'bold'))
    button5_4.place(x=192.5, y=290, width=50, height=35)
    # ----等于
    button5_5 = tkinter.Button(text='=', bg='khaki', bd=2, command=lambda: equal(), font=("Courier New", 16, 'bold'))
    button5_5.place(x=250, y=290, width=50, height=80)

    # --第六行
    # ----0
    button6_1 = tkinter.Button(text='0', bg='pink', bd=2, command=lambda: press_number('0'),
                               font=("Courier New", 16, 'bold'))
    button6_1.place(x=20, y=335, width=107.5, height=35)
    # ----小数点
    button6_2 = tkinter.Button(text='.', bg='pink', bd=2, command=lambda: press_number('.'),
                               font=("Courier New", 16, 'bold'))
    button6_2.place(x=135, y=335, width=50, height=35)
    # ----加
    button6_3 = tkinter.Button(text='+', bg='khaki', bd=2, command=lambda: set_operator('+'),
                               font=("Courier New", 16, 'bold'))
    button6_3.place(x=192.5, y=335, width=50, height=35)

    root.mainloop()


if __name__ == '__main__':
    demo()
