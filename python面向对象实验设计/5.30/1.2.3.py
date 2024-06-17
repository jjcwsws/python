import tkinter as tk
from tkinter import colorchooser, simpledialog

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简单画图板")

        # 创建画布
        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # 初始化绘图属性
        self.current_tool = '直线'
        self.current_color = 'black'
        self.line_width = 1
        self.start_coords = None

        # 用于存储绘制的图形
        self.drawings = []

        # 创建工具栏
        self.create_toolbar()

        # 绑定事件
        self.canvas.bind('<ButtonPress-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_motion)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # 绘图工具按钮
        tools = ['直线', '矩形', '圆']
        for tool in tools:
            button = tk.Button(toolbar, text=tool.capitalize(), command=lambda t=tool: self.set_tool(t))
            button.pack(side=tk.LEFT, padx=2, pady=2)

        # 颜色选择按钮
        color_button = tk.Button(toolbar, text="颜色", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=2, pady=2)

        # 线宽调整按钮
        width_scale = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, label="线宽", command=self.change_line_width)
        width_scale.set(self.line_width)
        width_scale.pack(side=tk.LEFT, padx=2, pady=2)

        # 清除按钮
        clear_button = tk.Button(toolbar, text="清除", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=2, pady=2)

        # 撤销按钮
        undo_button = tk.Button(toolbar, text="撤销", command=self.undo_drawing)
        undo_button.pack(side=tk.LEFT, padx=2, pady=2)

    def set_tool(self, tool):                   #类的实例，定义一个名为set_tool的方法
        self.current_tool = tool                #用于更新类的实例所使用的工具，将参数tool赋值给self.current_tool

    def choose_color(self):                                 #类的实例，定义一个名为choose_color的方法
        self.current_color = colorchooser.askcolor()[1]     #调用colorchooser模块的askcolor函数，将选择的颜色的十六进制颜色码赋值给实例的属性 current_color。

    def change_line_width(self, value):                     #类的实例，定义一个名为change_line_width的方法。这个方法接受一个参数 value，并将这个值转换为整数类型后，赋值给实例的一个属性 line_width。
        self.line_width = int(value)                        #int(value)：将参数 value 转换为整数类型。self.line_width = ...：将转换后的整数值赋值给实例的属性 line_width。类的其他方法可以通过访问 self.line_width 来获取或使用新的线条宽度值。
                       

    def on_button_press(self, event):                       #类的实例，定义一个名为on_button_press的方法.第二个参数 event 是一个事件对象，包含了触发该方法的具体事件信息，比如鼠标点击事件的位置
        self.start_coords = (event.x, event.y)              #从事件对象 event 中提取鼠标的当前位置，x 和 y 分别代表鼠标在窗口中的水平和垂直坐标。将这两个坐标值打包成一个元组。将这个元组赋值给实例的属性 start_coords。这样，start_coords 属性就保存了鼠标按钮按下时的起始坐标。

#拖动鼠标时实现绘制

    def on_motion(self, event):				    															 #定义一个名为on_motion的方法。用于创建一个绘图应用程序或者类似的图形交互界面
        if self.start_coords:				    															 #start_coords存储鼠标按下时的初始坐标的属性。
            self.canvas.delete('preview') 		    															 #清除画布上所有标记为'preview'的预览线条或者其他图形元素。
            if self.current_tool == '直线': 		    															 #表明用户当前选择的绘图工具是直线工具。
                self.canvas.create_line(self.start_coords[0], self.start_coords[1], event.x, event.y, tags='preview', width=self.line_width, fill=self.current_color)    	 #在画布上创建一条直线，起点是 self.start_coords 中存储的坐标，终点是当前鼠标事件的坐标 (event.x, event.y)。tags='preview' 给这条线打上 'preview' 标签，这样可以通过标签来选择和管理这条线。width=self.line_width 设置线的宽度。fill=self.current_color 设置线的颜色。
            elif self.current_tool == '矩形': 		    															 #表明用户当前选择的绘图工具是矩形工具。
                self.canvas.create_rectangle(self.start_coords[0], self.start_coords[1], event.x, event.y, tags='preview', width=self.line_width, outline=self.current_color)    #在画布上创建一个矩形。同上
            elif self.current_tool == '圆': 		    															 #表明用户当前选择的绘图工具是圆工具。
                self.canvas.create_oval(self.start_coords[0], self.start_coords[1], event.x, event.y, tags='preview', width=self.line_width, outline=self.current_color)  	 #在画布上创建一个圆。同上

#在画布上创建相应的图形元素，并将该元素的ID或句柄添加到一个列表中，然后重置起始坐标以准备下一次绘制。

    def on_button_release(self, event):																		 #定义一个名为on_button_release的方法。用于创建一个绘图应用程序或者类似的图形交互界面
        if self.start_coords:																			 
            if self.current_tool == '直线':																	 #在Python中，特别是使用图形库如Tkinter时，直线的ID（Identifier）是一个唯一的整数值，用于标识画布（Canvas）上创建的直线对象。当你使用 create_line 方法在画布上创建一条直线时，该方法会返回这个直线的ID。这个ID是由图形库自动生成的，用于在后续的操作中引用和管理该直线对象。
                line = self.canvas.create_line(self.start_coords[0], self.start_coords[1], event.x, event.y, width=self.line_width, fill=self.current_color)			 #在画布上创建一条直线，起点是 self.start_coords 中存储的坐标，终点是当前鼠标事件的坐标 (event.x, event.y)。width=self.line_width 设置线的宽度。fill=self.current_color 设置线的颜色。line 是一个变量，用于存储新创建直线的ID.
            elif self.current_tool == '矩形':
                line = self.canvas.create_rectangle(self.start_coords[0], self.start_coords[1], event.x, event.y, width=self.line_width, outline=self.current_color)
            elif self.current_tool == '圆':
                line = self.canvas.create_oval(self.start_coords[0], self.start_coords[1], event.x, event.y, width=self.line_width, outline=self.current_color)
            self.drawings.append(line)																		 #新创建的图形元素的IDsW添加到 self.drawings 列表中。这个列表可能用于保存用户绘制的所有图形元素，以便后续可以对其进行管理或操作。
            self.start_coords = None																		 #将 self.start_coords 重置为 None，准备下一次绘制操作.

#清空画布

    def clear_canvas(self):		
        self.drawings = []				#将self.drawings 属性设置为一个空列表。通过将其设为空列表，可以清空所有已保存的图形元素，从而在逻辑上清除用户的绘图历史。
        self.canvas.delete('all')			#用 self.canvas 的 delete 方法，并传入参数 'all'，使画布上所有的图形元素都被删除。

#撤销操作

    def undo_drawing(self):
        if self.drawings:				#检查 self.drawings 列表是否非空。如果列表非空，说明至少有一个图形元素可以被撤销。
            last_drawing = self.drawings.pop()		#从 self.drawings 列表中弹出（即移除并返回）最后一个元素，这个操作实现了撤销功能，因为它从列表中移除了最近的绘图记录。last_drawing 是一个变量，用于存储弹出的图形元素ID。
            self.canvas.delete(last_drawing)		#调用 self.canvas 的 delete 方法，并传入 last_drawing 作为参数，这将在画布上删除对应的图形元素。这样，用户最近绘制的图形就被从画布上移除了，达到了撤销的效果。

#启动一个基于Tkinter的图形用户界面应用程序，其中 DrawingApp 类负责管理画布和绘图相关的功能

if __name__ == "__main__":				#当你直接运行一个Python脚本时，if __name__ == "__main__" 条件判断为真，因此会执行括号内的代码。
    root = tk.Tk()					#首先创建了一个Tkinter的根窗口 root
    app = DrawingApp(root)				#然后创建了一个 DrawingApp 类的实例 app，并将 root 传递给 app。
    root.mainloop()					#最后，调用 root.mainloop() 启动事件循环，这是Tkinter GUI应用程序的核心部分，负责处理事件和更新GUI。
