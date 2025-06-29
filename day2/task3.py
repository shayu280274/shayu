#1
def extract_username(email):
    """
    从邮箱地址中提取用户名部分
    :param email: 邮箱地址字符串
    :return: 用户名部分
    """
    # 找到@符号的位置
    at_index = email.find('@')

    # 提取@符号前的用户名
    if at_index != -1:
        return email[:at_index]
    else:
        return "无效邮箱地址"


# 测试示例
email = "user_name@example.com"
username = extract_username(email)
print(f"邮箱 '{email}' 的用户名是: {username}")

#2
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# (1) 使用切片反转列表
reversed_nums = nums[::-1]
print("反转后的列表:", reversed_nums)  # 输出: [9, 8, 7, 6, 5, 4, 3, 2, 1]

# (2) 提取索引为0、2、4的元素
# 方法1: 使用列表推导式
selected_elements = [reversed_nums[i] for i in [0, 2, 4]]
print("索引0、2、4的元素:", selected_elements)  # 输出: [9, 7, 5]

#3
s = "a1b2c3d4e5"

# 方法1: 使用列表推导式
digits_only = ''.join([char for char in s if char.isdigit()])
print("提取的数字字符串:", digits_only)  # 输出: 12345



