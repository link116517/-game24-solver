import itertools
from typing import List, Optional, Tuple

def evaluate_expression(a: float, b: float, c: float, d: float) -> Optional[str]:
    """
    尝试所有可能的四则运算和括号组合，判断是否能得到24
    如果可以得到24，返回表达式字符串；否则返回None
    """
    ops = ['+', '-', '*', '/']
    
    def calculate(x: float, y: float, op: str) -> Optional[float]:
        """执行单个运算，如果除零则返回None"""
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
    
    def format_number(num: float) -> str:
        """格式化数字，如果是整数则不显示小数点"""
        if num == int(num):
            return str(int(num))
        else:
            return f"{num:.2f}"
    
    # 遍历所有运算符组合
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
                            expr = f"(({format_number(a)}{op1}{format_number(b)}){op2}{format_number(c)}){op3}{format_number(d)}"
                            return expr
                
                # 方式2: (a op (b op c)) op d
                result = calculate(b, c, op2)
                if result is not None:
                    result2 = calculate(a, result, op1)
                    if result2 is not None:
                        result3 = calculate(result2, d, op3)
                        if result3 is not None and abs(result3 - 24) < 1e-6:
                            expr = f"({format_number(a)}{op1}({format_number(b)}{op2}{format_number(c)})){op3}{format_number(d)}"
                            return expr
                
                # 方式3: a op ((b op c) op d)
                result = calculate(b, c, op2)
                if result is not None:
                    result2 = calculate(result, d, op3)
                    if result2 is not None:
                        result3 = calculate(a, result2, op1)
                        if result3 is not None and abs(result3 - 24) < 1e-6:
                            expr = f"{format_number(a)}{op1}(({format_number(b)}{op2}{format_number(c)}){op3}{format_number(d)})"
                            return expr
                
                # 方式4: a op (b op (c op d))
                result = calculate(c, d, op3)
                if result is not None:
                    result2 = calculate(b, result, op2)
                    if result2 is not None:
                        result3 = calculate(a, result2, op1)
                        if result3 is not None and abs(result3 - 24) < 1e-6:
                            expr = f"{format_number(a)}{op1}({format_number(b)}{op2}({format_number(c)}{op3}{format_number(d)}))"
                            return expr
                
                # 方式5: (a op b) op (c op d)
                result1 = calculate(a, b, op1)
                result2 = calculate(c, d, op3)
                if result1 is not None and result2 is not None:
                    result3 = calculate(result1, result2, op2)
                    if result3 is not None and abs(result3 - 24) < 1e-6:
                        expr = f"({format_number(a)}{op1}{format_number(b)}){op2}({format_number(c)}{op3}{format_number(d)})"
                        return expr
    
    return None

def can_make_24(nums: List[int]) -> Optional[str]:
    """判断4个数字是否能通过四则运算得到24，如果可以返回一个表达式"""
    # 尝试所有排列
    for perm in itertools.permutations(nums):
        result = evaluate_expression(perm[0], perm[1], perm[2], perm[3])
        if result is not None:
            return result
    return None

def main():
    print("=" * 60)
    print("24点游戏求解器")
    print("=" * 60)
    print("\n请输入4个数字（1-10），程序会尝试找出能得到24的运算方式\n")
    
    while True:
        try:
            # 获取用户输入
            user_input = input("请输入4个数字（用空格分隔，输入q退出）：").strip()
            
            if user_input.lower() == 'q':
                print("\n感谢使用，再见！")
                break
            
            # 解析输入
            parts = user_input.split()
            if len(parts) != 4:
                print("错误：请输入4个数字！\n")
                continue
            
            nums = [int(x) for x in parts]
            
            # 验证数字范围
            if any(n < 1 or n > 10 for n in nums):
                print("错误：数字必须在1-10范围内！\n")
                continue
            
            print(f"\n输入的数字：{nums}")
            print("-" * 60)
            
            # 尝试计算
            result = can_make_24(nums)
            
            if result:
                print(f"✓ 可以找到解法！")
                print(f"  表达式：{result} = 24")
                
                # 验证结果
                try:
                    check = eval(result.replace('÷', '/'))
                    print(f"  验证：{result} = {check}")
                except:
                    pass
            else:
                print(f"✗ 无法得出24")
                print(f"  这4个数字的所有组合都无法通过四则运算得到24")
            
            print()
            
        except ValueError:
            print("错误：请输入有效的整数！\n")
        except KeyboardInterrupt:
            print("\n\n感谢使用，再见！")
            break
        except Exception as e:
            print(f"发生错误：{e}\n")
    
    # 程序结束时等待用户按键
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()