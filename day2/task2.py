# 1. 定义Car类
class Car:
    def __init__(self, brand, speed=0):
        """
        初始化汽车对象
        :param brand: 品牌
        :param speed: 初始速度，默认为0
        """
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        """
        加速方法，增加速度m次，每次增加10
        :param m: 加速次数
        """
        for _ in range(m):
            self.speed += 10
        return self

    def brake(self, n):
        """
        刹车方法，减少速度n次，每次减少10（不低于0）
        :param n: 刹车次数
        """
        for _ in range(n):
            # 确保速度不低于0
            self.speed = max(0, self.speed - 10)
        return self

    def __str__(self):
        """
        返回当前状态的字符串表示
        """
        return f"{self.brand} 当前速度: {self.speed} km/h"


# 2. 创建Car类的实例并调用方法
# 创建Car实例
my_car = Car("Toyota", 30)
print("初始状态:", my_car)

# 加速3次
my_car.accelerate(3)
print("加速3次后:", my_car)  # 30 + 30 = 60

# 刹车2次
my_car.brake(2)
print("刹车2次后:", my_car)  # 60 - 20 = 40

# 尝试刹车到负值
my_car.brake(5)
print("刹车5次后:", my_car)  # 40 - 50 = 0（不会低于0）


# 3. 定义ElectricCar子类
class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        """
        初始化电动车对象
        :param brand: 品牌
        :param speed: 初始速度，默认为0
        :param battery: 初始电量，默认为50（0-100）
        """
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self, amount=20):
        """
        充电方法，电量增加指定值（不超过100）
        :param amount: 充电量，默认为20
        """
        self.battery = min(100, self.battery + amount)
        return self

    def __str__(self):
        """
        返回当前状态的字符串表示（包含电量信息）
        """
        return f"{super().__str__()}，当前电量: {self.battery}%"


# 创建ElectricCar类的实例并调用方法
print("\n测试电动车类:")
my_tesla = ElectricCar("Tesla", 40, 30)
print("初始状态:", my_tesla)

# 充电一次
my_tesla.charge()
print("充电一次后:", my_tesla)  # 电量30+20=50

# 充电三次（超过100）
my_tesla.charge(150)
print("充电150后:", my_tesla)  # 电量50+150=200 → 限制为100

# 加速和刹车操作（继承自Car类）
my_tesla.accelerate(2).brake(1)
print("加速2次刹车1次后:", my_tesla)  # 速度40+20-10=50