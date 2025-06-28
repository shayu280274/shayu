#练习1
def is_prime(n):
    """判断一个数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 输出1-100之间的素数
primes = [n for n in range(1, 101) if is_prime(n)]
print("1到100之间的素数：")
print(primes)

#练习2
def fibonacci(n):
    """生成斐波那契数列的前n项"""
    fib = [0, 1]  # 初始化前两项
    if n <= 2:
        return fib[:n]

    # 计算后续项
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


# 计算并输出前20项
fib_sequence = fibonacci(20)
print("\n斐波那契数列前20项：")
print(fib_sequence)

#练习3
total = 0
num = 1

while num <= 10000:
    # 检查条件：能被3整除或能被5整除，且不能被15整除
    if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
        total += num
    num += 1

print(f"\n1-10000之间满足条件的数之和：{total}")