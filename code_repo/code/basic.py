"""
这是理的Python入门基础教程，对应 ./readme/basic.md
"""

"""
# continue和break用法：
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        # 非双数时跳过输出
        continue
    print(i)
    # 输出双数2、4、6、8、10

i = 1
while 1:  
# 循环条件为1必定成立
    print(i)
    # 输出1~10
    i += 1
    if i > 10:
        # 当i大于10时跳出循环
        break
"""

"""
# while...else...循环，在循环条件为false时执行else语句。
count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")
"""

"""
# for循环语句基本结构
for letter in "Python":
    print("当前字母:" + letter)

# 通过序列索引迭代执行循环
fruits = ["banana", "apple", "mango"]
for index in range(len(fruits)):
    # len() 返回列表的长度，即元素的个数; range() 返回一个序列的数
    print("当前水果:" + fruits[index])

# while循环嵌套输出2~100之间的素数
i = 2
while i < 100:
    j = 2
    while j <= i/j:
        if not i%j:
            break
        j += 1
    if j > i/j:
        print(i, "是素数")
    i += 1

"""

"""

# 字符串的创建:创建字符串很easy，只要为变量分配一个值即可。
var1 = 'Hello World!'
var2 = "Python Runoob"

# python访问字符串中的值
print(var1[0])
print(var2[1:5])

# 字符串连接：对字符串进行截取并与其他字符串进行连接
print("输出：" + var1[:5] + "Runoob!")

# Unicode字符串和非Unicode字符串
if __name__ == '__main__':
    #定义一般字符串
    str="代码帮"
    #字符串前面加u,定义标准unicode字符串
    unicodestr=u"代码帮"
    #将一般字符串转化为标准unicode字符串
    unicodestrs = unicode(str, "utf-8")
    print(str)
    print(unicodestr)
    print(unicodestrs)

    print(type(str))
    print(type(unicodestr))
    print(type(unicodestrs))

# 使用replace()函数修改字符串
# 在整个过程中，实际上是创建了新的字符串对象，并指向了变量a，而不是修改以前的字符串来实现。
a = "abhdlshidada"
a.replace("a", "da")
print(a)
a = a.replace("a", "da")
print(a)

# slice切片操作
a = "sxtsxtsxtsxt"
a = a[0::3]
print(a)

# split()函数 分割字符串
a = "to be or not to be"
b = a.split()
print(b)
c = a.split("to")
print(c)

# join()函数 连接字符串
d = "*".join(a)
print(a)
print(d)

"""
"""
# join效率分析
import time
time01 = time.time()
a = ""
for i in range(10000000):
    a += "sxt"
time02 = time.time()
print("运算时间是：" + str(time02 - time01))

time03 = time.time()
a = []
for i in range(10000000):
    a.append("sxt")
a = "".join(a)
time04 = time.time()
print("运算时间是：" + str(time04 - time03))


# 字符串内存驻留机制
a = "abc_212"
b = "abc_212"
e = a is b
print(e)
c = "dd!"
d = "dd!"
e = c is d
print(e)

# 可变字符串
import io
s = "hello, sxt"
sio = io.StringIO(s)
print(sio)
asio = sio.getvalue()
print(asio)
bsio = sio.seek(4)
print(bsio)
"""

"""

# 创建列表
list1 = ["physic", "math", 178, 928]
list2 = [1, 2, 3, 4, 5]

# 访问列表中的值
print(list1[0])
print(list2[1:3])

# 更新列表
list1.append("gooogle")
print(list1)

# 删除列表元素
del list1[1:3]
print(list1)

# 迭代
for index in list1:
    print(index)

# 判断列表长度
list_len = len(list1)
print(list_len)

# 判断元素是否在列表中
print("gooogle" in list1)

# 列表截取
list2 = list1[2:]
print(list2)

# 推导式创建列表
a = [x*2 for x in range(100) if x%9 == 0]
print(a, type(a))

# 列表中添加新元素的五种方法
a = [10, 20]
a.append(30)
print(a)
c = a + [40]
print(c)
a.extend([20, 40])
print(a)
a.insert(4, 100)
print(a)
d = a*2
print(d)

# 列表中元素删除的方法
a = [10, 20, 30, 40]
del a[0]
print(a)
b = a.pop()
print(a, b)
a.pop(1)
print(a)

# 二维列表
a = [
    ["yi", 10, 20],
    [129, 31],
    ["asdguh", 98, 2]
]
print(a)

a = [
    ["yi", 10, 20],
    [129, 31],
    ["asdguh", 98, 2]
]
print(a[0:2][1])

# 创建元组
a = (10, 20)
b = (2,)
c = (2)
print(a, b, c)
d = tuple()
e = tuple("abc")
f = tuple(range(3))
g = tuple([2, 3, 4])
print(d, e, f, g)

# 排序
print(sorted(a))

# 生成器
s1 = (x*2 for x in range(5))
print(tuple(s1))
s2 = (x*3 for x in range(4))
print(list(s2))

"""

"""
# 创建字典的方法
a = {"name":"gaoqi", "age": 18, "job": "programmer"}
b = dict(name = "gaoqi", age = 18, job = "programmer")
print(a, b)
k = ["name", "age", "job"]
v = ["gaoqi", 18, "programmer"]
d =  dict(zip(k, v))
print(d, zip(k, v))
f = dict.fromkeys(["name", "age", "job"])
print(f)

a = {"name":"gaoqi", "age": 18, "job": "programmer"}
print(a.items())

"""
"""
# 序列解包
x,y,z = (10, 20, 30)
print(x, y, z)
(a, b, c) = (8, 9, 10)
print(a, b, c)
[a, b, c] = [10, 20, 49]
print(a, b, c)

a = {"name":"gaoqi", "age": 18, "job": "programmer"}
x, y, z = a
print(x, y, z)
"""
"""
# lambda 函数
f = lambda a, b, c: a + b + c
print(f(1, 2, 3))

# eval 函数
s = "print('abcddes')"
eval(s)
"""
"""
# 类的创建
class Student:
    # 类名一般首字母大写，多个单词采用驼峰原则
    school = "sda_zjut"

    def __init__(self, name, score):
        # 实例属性
        self.name = name
        self.score = score

    def say_score(self):
        # 实例方法
        print(str(self.name) + "的分数是" + str(self.score))

s1 = Student("qh",17)
s1.say_score()
print(s1.school,s1.score, s1.name)

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# 垃圾回收机制
a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数

# 父类和子类
class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  
    # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')


c = Child()  
# 实例化子类
c.childMethod()  
# 调用子类的方法
c.parentMethod()  
# 调用父类方法
c.setAttr(200)  
# 再次调用父类的方法 - 设置属性值
c.getAttr()  
# 再次调用父类的方法 - 获取属性值


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


# 类方法
class Student:
    # 定义类属性
    company = "SXT"

    @classmethod
    def printCompany(cls):
        print(cls.company)

Student.printCompany()

# 静态方法
class Students:
    company = "dhks"

    @staticmethod
    # 静态方法
    def add(a, b):
        return a + b

cls = Students
print(cls.add(2, 8))

# 可调用方法
class SalaryAccount:

    def __call__(self, salary):
        print("计算工资")
        year_salary = salary * 12
        day_salary = salary // 22.5

        return dict(year_salary = year_salary, day_salary = day_salary)

s = SalaryAccount()
print(s(3000))

# @property
class Employee:

    @property
    def salary(self):
        return 100

emp1 = Employee()
# print(emp1.salary())
print(emp1.salary)

# get set 和修饰器
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 5000:
                self.__salary = salary
        else:
            print("录入错误。")

emp1 = Employee("d", 3989)
print(emp1.salary)
emp1.salary = 2000
print(emp1.salary)

#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, salary):
#         if 1000 < salary < 5000:
#             self.__salary = salary
#         else:
#             print("录入错误。")
#
# emp1 = Employee("da", 39900)
# print(emp1.get_salary())
# emp1.set_salary(2000)
# print(emp1.get_salary())
"""
