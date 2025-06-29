#练习1
# 创建1-100的整数列表
numbers = [i for i in range(1, 101)]

# 使用列表推导式筛选偶数
even_numbers = [num for num in numbers if num % 2 == 0]

print("1-100的所有偶数：")
print(even_numbers)

#练习2
def remove_duplicates(lst):
    """删除重复元素并保持原始顺序"""
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# 测试数据
test_list = [3, 1, 2, 2, 4, 3, 5, 4, 1, 6]
result = remove_duplicates(test_list)

print("\n原始列表:", test_list)
print("去重后保持顺序:", result)

#练习3
keys = ["a", "b", "c"]
values = [1, 2, 3]

# 使用zip函数合并列表为字典
merged_dict = dict(zip(keys, values))

print("\n合并后的字典:")
print(merged_dict)

#练习4
# 定义学生信息元组
student_info = ("张三", 18, 92.5)

# 解包元组
name, age, score = student_info

# 格式化输出
print("\n学生信息:")
print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"成绩: {score}")