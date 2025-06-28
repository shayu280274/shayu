#练习1
def is_palindrome(number):
    """
    判断一个数是否为回文数
    参数:
        number: 要判断的数字 (整数)
    返回:
        bool: 如果是回文数返回True，否则返回False
    """
    # 将数字转换为字符串以便比较
    num_str = str(number)

    # 比较字符串与其反转是否相同
    return num_str == num_str[::-1]


# 测试示例
print(is_palindrome(121))  # 输出: True
print(is_palindrome(123))  # 输出: False
print(is_palindrome(1221))  # 输出: True
print(is_palindrome(12321))  # 输出: True
print(is_palindrome(-121))  # 输出: False (负数不是回文数)
print(is_palindrome(10))  # 输出: False

#练习2
def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# 测试示例
print(average(1, 2, 3))       # 输出 2.0
print(average(10, 20, 30, 40)) # 输出 25.0

#练习3
def longest_string(*strings):
    if not strings:
        return None
    return max(strings, key=len)

# 测试示例
print(longest_string("apple", "banana", "cherry"))  # 输出 "banana"
print(longest_string("cat", "dog", "bird"))         # 输出 "bird"

#练习4

# main.py
from geometry import rectangle_area, rectangle_perimeter

# 计算矩形面积
length = 5
width = 3
print(f"矩形面积 ({length}x{width}): {rectangle_area(length, width)}")

# 计算矩形周长
print(f"矩形周长 ({length}x{width}): {rectangle_perimeter(length, width)}")