# 定义变量
x = 10
y = "10"
z = True

# 判断并输出数据类型
print(f"变量 x 的数据类型是：{type(x).__name__}")   # int
print(f"变量 y 的数据类型是：{type(y).__name__}")   # str
print(f"变量 z 的数据类型是：{type(z).__name__}")   # bool

# 接收用户输入的半径（转换为浮点数）
radius = float(input("请输入圆的半径："))

# 定义π的值
pi = 3.14

# 计算圆面积
area = pi * (radius ** 2)

# 输出结果（保留两位小数）
print(f"半径为 {radius} 的圆的面积是：{area:.2f}")

# 原始字符串
num_str = "3.14"

# 转换为浮点数
float_num = float(num_str)

# 转换为整数（会丢失小数部分）
int_num = int(float_num)

# 输出结果
print(f"原始字符串：'{num_str}' → 类型：{type(num_str).__name__}")
print(f"转换为浮点数：{float_num} → 类型：{type(float_num).__name__}")
print(f"再转换为整数：{int_num} → 类型：{type(int_num).__name__}")