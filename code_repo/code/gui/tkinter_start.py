# 在写软著的时候，需要使用到GUI工具，推荐 tkinter 和 pyQt

# 这是 tkinter 的入门教程
# 参考学习 https://docs.python.org/3/library/tkinter.html

from tkinter import *

# 创建窗口
root = Tk()
# 标题
root.title("窗口标题")

# tkinter一共有21个核心组件： toplevel, label, button, canvas, checkbutton, entry, frame, labelframe, listbox, menu,
# menubutton,  message, optionmenu,  panewindow, radiobutton
# scale, scrollbar, spinbox, text, bitmap, image

# 标签组件
label = Label(root, text="你好")
label.grid(row=0, column=1)

# 按钮组件


# 展示窗口
root.mainloop()
