import itertools
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.resources import resource_add_path
import os

# 设置配置
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '700')

# 注册中文字体（使用系统字体）
try:
    # Windows系统字体
    if os.name == 'nt':
        chinese_font = 'C:/Windows/Fonts/msyh.ttc'  # 微软雅黑
        if not os.path.exists(chinese_font):
            chinese_font = 'C:/Windows/Fonts/simsun.ttc'  # 宋体
    # macOS系统字体
    elif os.name == 'posix':
        chinese_font = '/System/Library/Fonts/PingFang.ttc'
    else:
        chinese_font = None
    
    if chinese_font and os.path.exists(chinese_font):
        LabelBase.register(name='chinese', fn_regular=chinese_font)
        print(f"✅ 成功加载中文字体: {chinese_font}")
    else:
        print("⚠️ 未找到中文字体，使用默认字体")
except Exception as e:
    print(f"⚠️ 字体加载失败: {e}")


class EvaluateExpression:
    """24点求解核心逻辑"""
    
    @staticmethod
    def evaluate_expression(a, b, c, d):
        """尝试所有可能的四则运算和括号组合"""
        ops = ['+', '-', '*', '/']
        
        def calculate(x, y, op):
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x * y
            elif op == '/':
                if y == 0:
                    return None
                return x / y
            return None
        
        def format_number(num):
            if num == int(num):
                return str(int(num))
            else:
                return f"{num:.2f}"
        
        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    # 方式1: ((a op b) op c) op d
                    result = calculate(a, b, op1)
                    if result is not None:
                        result2 = calculate(result, c, op2)
                        if result2 is not None:
                            result3 = calculate(result2, d, op3)
                            if result3 is not None and abs(result3 - 24) < 1e-6:
                                expr = f"(({format_number(a)} {op1} {format_number(b)}) {op2} {format_number(c)}) {op3} {format_number(d)}"
                                return expr
                    
                    # 方式2: (a op (b op c)) op d
                    result = calculate(b, c, op2)
                    if result is not None:
                        result2 = calculate(a, result, op1)
                        if result2 is not None:
                            result3 = calculate(result2, d, op3)
                            if result3 is not None and abs(result3 - 24) < 1e-6:
                                expr = f"({format_number(a)} {op1} ({format_number(b)} {op2} {format_number(c)})) {op3} {format_number(d)}"
                                return expr
                    
                    # 方式3: a op ((b op c) op d)
                    result = calculate(b, c, op2)
                    if result is not None:
                        result2 = calculate(result, d, op3)
                        if result2 is not None:
                            result3 = calculate(a, result2, op1)
                            if result3 is not None and abs(result3 - 24) < 1e-6:
                                expr = f"{format_number(a)} {op1} (({format_number(b)} {op2} {format_number(c)}) {op3} {format_number(d)})"
                                return expr
                    
                    # 方式4: a op (b op (c op d))
                    result = calculate(c, d, op3)
                    if result is not None:
                        result2 = calculate(b, result, op2)
                        if result2 is not None:
                            result3 = calculate(a, result2, op1)
                            if result3 is not None and abs(result3 - 24) < 1e-6:
                                expr = f"{format_number(a)} {op1} ({format_number(b)} {op2} ({format_number(c)} {op3} {format_number(d)}))"
                                return expr
                    
                    # 方式5: (a op b) op (c op d)
                    result1 = calculate(a, b, op1)
                    result2 = calculate(c, d, op3)
                    if result1 is not None and result2 is not None:
                        result3 = calculate(result1, result2, op2)
                        if result3 is not None and abs(result3 - 24) < 1e-6:
                            expr = f"({format_number(a)} {op1} {format_number(b)}) {op2} ({format_number(c)} {op3} {format_number(d)})"
                            return expr
        
        return None
    
    @staticmethod
    def can_make_24(nums):
        """判断4个数字是否能通过四则运算得到24"""
        for perm in itertools.permutations(nums):
            result = EvaluateExpression.evaluate_expression(perm[0], perm[1], perm[2], perm[3])
            if result is not None:
                return result
        return None


class Game24App(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title_label = Label(
            text='24 Point Game Solver',
            font_size='24sp',
            bold=True,
            size_hint=(1, 0.1),
            color=(0.2, 0.3, 0.8, 1)
        )
        main_layout.add_widget(title_label)
        
        # 说明文字
        instruction_label = Label(
            text='Enter 4 numbers (1-10)',
            font_size='16sp',
            size_hint=(1, 0.08),
            color=(0.3, 0.3, 0.3, 1)
        )
        main_layout.add_widget(instruction_label)
        
        # 输入框布局
        input_layout = GridLayout(cols=4, spacing=10, size_hint=(1, 0.15))
        
        self.input1 = TextInput(hint_text='Num 1', input_filter='int', multiline=False, font_size='18sp')
        self.input2 = TextInput(hint_text='Num 2', input_filter='int', multiline=False, font_size='18sp')
        self.input3 = TextInput(hint_text='Num 3', input_filter='int', multiline=False, font_size='18sp')
        self.input4 = TextInput(hint_text='Num 4', input_filter='int', multiline=False, font_size='18sp')
        
        input_layout.add_widget(self.input1)
        input_layout.add_widget(self.input2)
        input_layout.add_widget(self.input3)
        input_layout.add_widget(self.input4)
        
        main_layout.add_widget(input_layout)
        
        # 按钮布局
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, 0.12))
        
        solve_button = Button(
            text='Solve',
            font_size='18sp',
            bold=True,
            background_color=(0.2, 0.6, 1.0, 1),
            background_normal='',
            color=(1, 1, 1, 1)
        )
        solve_button.bind(on_press=self.solve)
        
        clear_button = Button(
            text='Clear',
            font_size='18sp',
            background_color=(0.6, 0.6, 0.6, 1),
            background_normal='',
            color=(1, 1, 1, 1)
        )
        clear_button.bind(on_press=self.clear_inputs)
        
        button_layout.add_widget(solve_button)
        button_layout.add_widget(clear_button)
        
        main_layout.add_widget(button_layout)
        
        # 结果显示区域
        result_label = Label(
            text='Result:',
            font_size='16sp',
            size_hint=(1, 0.05),
            halign='left',
            valign='middle',
            color=(0.2, 0.2, 0.2, 1)
        )
        main_layout.add_widget(result_label)
        
        # 滚动视图用于显示结果
        scroll_view = ScrollView(size_hint=(1, 0.4))
        self.result_text = Label(
            text='Waiting for input...',
            font_size='16sp',
            size_hint_y=None,
            height='300dp',
            text_size=(Window.width - 40, None),
            halign='left',
            valign='top',
            color=(0.2, 0.2, 0.2, 1),
            padding=(10, 10)
        )
        self.result_text.bind(texture_size=self.result_text.setter('size'))
        scroll_view.add_widget(self.result_text)
        
        main_layout.add_widget(scroll_view)
        
        return main_layout
    
    def solve(self, instance):
        """求解24点"""
        try:
            # 获取输入
            nums = []
            inputs = [self.input1, self.input2, self.input3, self.input4]
            
            for inp in inputs:
                if inp.text.strip() == '':
                    self.result_text.text = 'Error: Please fill all 4 numbers!'
                    self.result_text.color = (0.8, 0.2, 0.2, 1)
                    return
                num = int(inp.text.strip())
                if num < 1 or num > 10:
                    self.result_text.text = 'Error: Numbers must be 1-10!'
                    self.result_text.color = (0.8, 0.2, 0.2, 1)
                    return
                nums.append(num)
            
            # 显示输入的数字
            input_str = f"Numbers: {nums}\n\n"
            
            # 求解
            result = EvaluateExpression.can_make_24(nums)
            
            if result:
                self.result_text.text = f"{input_str}Success! Found a solution:\n\n{result} = 24"
                self.result_text.color = (0.1, 0.6, 0.1, 1)
            else:
                self.result_text.text = f"{input_str}Cannot make 24\n\nNo combination of these numbers can make 24"
                self.result_text.color = (0.8, 0.2, 0.2, 1)
                
        except ValueError:
            self.result_text.text = 'Error: Please enter valid integers!'
            self.result_text.color = (0.8, 0.2, 0.2, 1)
    
    def clear_inputs(self, instance):
        """清空输入框"""
        self.input1.text = ''
        self.input2.text = ''
        self.input3.text = ''
        self.input4.text = ''
        self.result_text.text = 'Waiting for input...'
        self.result_text.color = (0.2, 0.2, 0.2, 1)


if __name__ == '__main__':
    Game24App().run()