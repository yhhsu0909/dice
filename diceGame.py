import random
import tkinter as tk


class DiceGame():
    def __init__(self):
        self.root = tk.Tk()
        self.dices = self.gen_dices(6)
        self.label = tk.Label(self.root, text=self.dices)
        self.button_0 = tk.Button(self.root, text='洗牌', command=self.shuffle)
        self.button_1 = tk.Button(self.root, text='大的拿掉', command=self.remove_big)
        self.button_2 = tk.Button(self.root, text='小的拿掉', command=self.remove_small)
        self.button_3 = tk.Button(self.root, text='紅的拿掉', command=self.remove_red)
        self.button_4 = tk.Button(self.root, text='黑的拿掉', command=self.remove_black)
        self.button_5 = tk.Button(self.root, text='單的拿掉', command=self.remove_odd)
        self.button_6 = tk.Button(self.root, text='雙的拿掉', command=self.remove_even)
        self.label.pack()
        self.button_0.pack(side=tk.LEFT)
        self.button_1.pack(side=tk.LEFT)
        self.button_2.pack(side=tk.LEFT)
        self.button_3.pack(side=tk.LEFT)
        self.button_4.pack(side=tk.LEFT)
        self.button_5.pack(side=tk.LEFT)
        self.button_6.pack(side=tk.LEFT)
        self.root.mainloop()

    def gen_dices(self, num):
        dices = []
        for i in range(num):
            r = random.randint(1, 6)  # 產生隨機數字
            dices.append(r)  # 產生完的隨機數字加進清單
        print('目前的骰子是:', dices)
        return dices

    def print_usage(self):
        print('功能清單: ')
        print('q: 結束')
        print('s: 洗牌')
        print('1: 大的拿掉')
        print('2: 小的拿掉')
        print('3: 黑的拿掉')
        print('4: 紅的拿掉')
        print('5: 單的拿掉')
        print('6: 雙的拿掉')

    def shuffle(self):
        num = len(self.dices)  # 目前有的骰子數
        self.dices = []  # 清空
        for i in range(num):
            r = random.randint(1, 6)  # 產生隨機數字
            self.dices.append(r)  # 產生完的隨機數字加進清單
        self.label.configure(text=self.dices)

    def remove_big(self):
        new_list = []
        for i in self.dices:
            if i <= 3:
                new_list.append(i)
        self.dices = new_list
        print('目前的骰子是:', self.dices)
        self.label.configure(text=self.dices)

    def remove_small(self):
        new_list = []
        for i in self.dices:
            if i >= 4:
                new_list.append(i)
        self.dices = new_list
        print('目前的骰子是:', self.dices)
        self.label.configure(text=self.dices)

    def remove_black(self):
        new_list = []
        for i in self.dices:
            if i in [1, 4]:
                new_list.append(i)
        self.dices = new_list
        print('目前的骰子是:', self.dices)
        self.label.configure(text=self.dices)

    def remove_red(self):
        new_list = []
        for i in self.dices:
            if i in [2, 3, 5, 6]:
                new_list.append(i)
        self.dices = new_list
        print('目前的骰子是:', self.dices)
        self.label.configure(text=self.dices)

    def remove_odd(self):
        new_list = []
        for i in self.dices:
            if (i % 2) == 0:
                new_list.append(i)
        self.dices = new_list
        print('目前的骰子是:', self.dices)
        self.label.configure(text=self.dices)

    def remove_even(self):
        new_list = []
        for i in self.dices:
            if (i % 2) == 1:
                new_list.append(i)
        self.dices = new_list
        print('目前的骰子是:', self.dices)
        self.label.configure(text=self.dices)

DiceGame()