import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageGrab
import numpy as np
import torch
import string

from load_dataset import transformer, device
from mymodel import MyModel


def getImage():
    left = int(root.winfo_rootx()) + 25
    top = int(root.winfo_rooty()) + 35
    img = ImageGrab.grab((left, top, left + 750, top + 600))  # 抓取屏幕
    img = np.array(img)
    img = transformer(img).to(device)
    img = img.unsqueeze(0)
    return img


class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.init_window()
        # 前景色
        self.foreColor = '#000000'
        self.backColor = '#FFFFFF'
        # 控制是否允许画图的变量，1：允许，0：不允许
        self.canDraw = tk.IntVar(value=0)
        # 控制画图类型的变量
        self.what = tk.IntVar(value=1)
        # 记录鼠标位置的变量
        self.X = tk.IntVar(value=0)
        self.Y = tk.IntVar(value=0)
        # 记录最后绘制图形的id
        self.lastDraw = 0
        # 加载模型
        self.model = MyModel(62).to(device)
        state_dict = torch.load("../models/model.pkl")
        self.model.load_state_dict(state_dict)
        self.model.eval()
        # 编号对应字符
        self.label_string = string.digits + string.ascii_uppercase + string.ascii_lowercase

    def init_window(self):
        self.wirte_area = ttk.LabelFrame(self.master, text="写字区")
        self.wirte_area.place(x=20, y=20, width=800, height=650)  # 设置写字区
        # 创建画布
        image = tk.PhotoImage()
        self.canvas = tk.Canvas(self.wirte_area, bg='white', width=800, height=400)
        self.canvas.create_image(800, 400, image=image)
        self.canvas.bind('<B1-Motion>', self.onLeftButtonMove)
        self.canvas.bind('<Button-1>', self.onLeftButtonDown)
        self.canvas.bind('<ButtonRelease-1>', self.onLeftButtonUp)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.base = Image.new("RGB", (200, 200), (255, 255, 255))
        self.d = ImageDraw.Draw(self.base)

        action_frame = ttk.Frame(root)
        action_frame.place(x=920, y=430, width=270, height=850)
        button_clear = tk.Button(action_frame, text="清空", command=self.clear, height=5, width=100)
        button_clear.pack(pady=15)
        button_recognition = tk.Button(action_frame, text="识别", command=self.predict, height=5, width=100)
        button_recognition.pack(pady=15)

        # 识别结果显示
        self.frame2 = ttk.LabelFrame(self.master, text="识别结果")
        self.frame2.place(x=850, y=20, width=400, height=350)
        image2 = tk.PhotoImage()
        self.canvas2 = tk.Canvas(self.frame2, bg='white', width=200, height=200)
        self.canvas2.create_image(120, 120, image=image2)
        self.canvas2.pack(fill=tk.BOTH, expand=tk.YES)

    def onLeftButtonMove(self, event):
        if self.canDraw.get() != 0 and self.what.get() == 1:
            self.canvas.create_oval(self.X.get(), self.Y.get(), event.x, event.y, width=30, fill=self.foreColor)
            self.d.line([self.X.get(), self.Y.get(), event.x, event.y], width=8, fill='black')
            self.X.set(event.x)
            self.Y.set(event.y)

    def onLeftButtonDown(self, event):
        self.canDraw.set(1)  # 启用绘制
        self.X.set(event.x)
        self.Y.set(event.y)
        if self.what.get() == 4:
            self.canvas.create_text(event.x, event.y)

    def onLeftButtonUp(self, event):
        self.canDraw.set(0)  # 禁用绘制
        self.lastDraw = 0

    def clear(self):
        # 删除所有canvas对象
        for item in self.canvas.find_all():
            self.canvas.delete(item)
        for item in self.canvas2.find_all():
            self.canvas2.delete(item)

    def predict(self):
        # 清空识别结果
        for item in self.canvas2.find_all():
            self.canvas2.delete(item)
        x = getImage()
        y_pred = self.model(x)
        _, num = torch.max(y_pred.data, 1)  # 最大值
        result = self.label_string[num[0]]
        titleFont = ("微软雅黑", 50, "bold")
        self.canvas2.create_text(180, 160, text=result,
                                 font=titleFont, anchor=tk.W, justify=tk.CENTER)


if __name__ == '__main__':
    root = tk.Tk()
    window_width = 1280
    window_height = 720
    root.resizable(False, False)
    root.title("手写字符识别")
    root['width'] = window_width
    root['height'] = window_height
    window = Window(root)
    root.mainloop()
