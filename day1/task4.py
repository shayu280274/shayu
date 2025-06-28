#练习1
s1 = "Python is a powerful programming language"

# (1) 提取单词 "language"
words = s1.split()  # 以空格分隔所有单词
last_word = words[-1]  # 获取最后一个单词
print(f"(1) 最后一个单词: '{last_word}'")

# (2) 连接字符串并重复输出3次
s2 = " Let's learn together"
combined = s1 + s2  # 连接两个字符串
print("\n(2) 重复输出3次:")
print(combined * 3)  # 重复输出3次

# (3) 输出所有以p或P开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("\n(3) 以p或P开头的单词:")
print(p_words)

#练习2
s3 = " Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
stripped = s3.strip()
print(f"(1) 去除前后空格: '{stripped}'")

# (2) 将所有字符转换为大写
upper_str = stripped.upper()
print(f"\n(2) 转换为大写: '{upper_str}'")

# (3) 查找子串"test"的起始下标
test_index = stripped.find("test")
print(f"\n(3) 'test'的起始下标: {test_index}")

# (4) 将"test"替换为"practice"
replaced_str = stripped.replace("test", "practice")
print(f"\n(4) 替换后: '{replaced_str}'")

# (5) 分割并连接
split_list = replaced_str.split()
joined_str = "-".join(split_list)
print(f"\n(5) 分割并连接: '{joined_str}'")