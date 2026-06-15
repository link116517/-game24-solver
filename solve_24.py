import itertools
from typing import List, Tuple, Optional

def generate_numbers() -> List[int]:
    """生成4组1-10的数字，共40个数字"""
    numbers = []
    for _ in range(4):
        numbers.extend(range(1, 11))
    return numbers

def get_all_permutations(nums: List[int]) -> List[List[int]]:
    """获取4个数字的所有排列"""
    return list(itertools.permutations(nums))

def evaluate_expression(a: float, b: float, c: float, d: float) -> bool:
    """
    尝试所有可能的四则运算和括号组合，判断是否能得到24
    5种基本的括号组合方式：
    1. ((a op b) op c) op d
    2. (a op (b op c)) op d
    3. a op ((b op c) op d)
    4. a op (b op (c op d))
    5. (a op b) op (c op d)
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
    
    # 遍历所有运算符组合
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                # 方式1: ((a op b) op c) op d
                result = calculate(a, b, op1)
                if result is not None:
                    result = calculate(result, c, op2)
                    if result is not None:
                        result = calculate(result, d, op3)
                        if result is not None and abs(result - 24) < 1e-6:
                            return True
                
                # 方式2: (a op (b op c)) op d
                result = calculate(b, c, op2)
                if result is not None:
                    result = calculate(a, result, op1)
                    if result is not None:
                        result = calculate(result, d, op3)
                        if result is not None and abs(result - 24) < 1e-6:
                            return True
                
                # 方式3: a op ((b op c) op d)
                result = calculate(b, c, op2)
                if result is not None:
                    result = calculate(result, d, op3)
                    if result is not None:
                        result = calculate(a, result, op1)
                        if result is not None and abs(result - 24) < 1e-6:
                            return True
                
                # 方式4: a op (b op (c op d))
                result = calculate(c, d, op3)
                if result is not None:
                    result = calculate(b, result, op2)
                    if result is not None:
                        result = calculate(a, result, op1)
                        if result is not None and abs(result - 24) < 1e-6:
                            return True
                
                # 方式5: (a op b) op (c op d)
                result1 = calculate(a, b, op1)
                result2 = calculate(c, d, op3)
                if result1 is not None and result2 is not None:
                    result = calculate(result1, result2, op2)
                    if result is not None and abs(result - 24) < 1e-6:
                        return True
    
    return False

def can_make_24(nums: List[int]) -> bool:
    """判断4个数字是否能通过四则运算得到24"""
    # 尝试所有排列
    for perm in get_all_permutations(nums):
        if evaluate_expression(perm[0], perm[1], perm[2], perm[3]):
            return True
    return False

def find_impossible_combinations() -> List[Tuple[int, int, int, int]]:
    """找出所有无法得到24的4个数字组合"""
    # 生成40个数字
    all_numbers = generate_numbers()
    
    # 去重后获取所有唯一的4个数字组合
    unique_numbers = sorted(set(all_numbers))
    combinations = list(itertools.combinations_with_replacement(unique_numbers, 4))
    
    impossible = []
    total = len(combinations)
    
    print(f"总共有 {total} 个唯一的4数字组合需要检查...")
    
    for i, combo in enumerate(combinations):
        if (i + 1) % 100 == 0:
            print(f"已检查 {i + 1}/{total} 个组合...")
        
        nums = list(combo)
        if not can_make_24(nums):
            impossible.append(combo)
    
    return impossible

def main():
    print("=" * 60)
    print("24点游戏 - 无解组合查找程序")
    print("=" * 60)
    print("\n生成4组1-10的数字（共40个数字）")
    print("正在查找无法通过四则运算得到24的数字组合...\n")
    
    impossible_combinations = find_impossible_combinations()
    
    print("\n" + "=" * 60)
    print(f"查找完成！")
    print(f"共有 {len(impossible_combinations)} 个无解的数字组合")
    print("=" * 60)
    
    if impossible_combinations:
        print("\n无解的数字组合列表：")
        for i, combo in enumerate(impossible_combinations, 1):
            print(f"{i:3d}. {combo}")
    else:
        print("\n所有数字组合都可以得到24！")

if __name__ == "__main__":
    main()
