# Python核心编程笔记汇总

本文档汇总了阶段1-Python核心编程的所有学习笔记，包含Python基础入门、流程控制、数据序列、函数、文件操作、面向对象、异常处理、模块和包等核心内容。

---

## 目录

1. [Python基础入门](#python基础入门)
   - [Python简介](#python简介)
   - [Python解释器](#python解释器)
   - [PyCharm开发环境](#pycharm开发环境)
   - [注释](#注释)
   - [变量](#变量)
   - [输出](#输出)
   - [输入](#输入)
   - [数据类型转换](#数据类型转换)
   - [运算符](#运算符)

2. [流程控制](#流程控制)
   - [条件语句](#条件语句)
   - [循环语句](#循环语句)

3. [数据序列](#数据序列)
   - [字符串](#字符串)
   - [列表](#列表)
   - [元组](#元组)
   - [字典](#字典)
   - [集合](#集合)
   - [公共操作](#公共操作)
   - [推导式](#推导式)

4. [函数](#函数)
5. [文件操作](#文件操作)
6. [面向对象](#面向对象)
7. [异常处理](#异常处理)
8. [模块和包](#模块和包)

---

## Python基础入门

### Python简介

Python是时下最流行、最火爆的编程语言之一，具体原因如下：

1. **简单、易学，适应人群广泛**
2. **免费、开源**
3. **应用领域广泛**

**Python优点：**
- 学习成本低
- 开源
- 适应人群广泛
- 应用领域广泛

**Python版本：**
- Python 2.X
- Python 3.X（推荐使用3.7版本）

**知名框架：**
- Google开源机器学习框架：TensorFlow
- 开源社区主推学习框架：Scikit-learn
- 百度开源深度学习框架：Paddle

### Python解释器

**解释器的作用：** 运行文件

**Python解释器种类：**
- **CPython**：C语言开发的解释器[官方]，应用广泛的解释器
- **IPython**：基于CPython的一种交互式解释器
- **其他解释器**：
  - PyPy：基于Python语言开发的解释器
  - Jython：运行在Java平台的解释器
  - IronPython：运行在微软.Net平台上的Python解释器

**安装步骤：**
1. 下载地址：https://www.python.org/downloads/release/python-372/
2. 双击可执行文件 — 勾选[pip] -- [Next] -- [勾选添加环境变量] -- [Install]

### PyCharm开发环境

**PyCharm的作用：**
PyCharm是一种Python IDE（集成开发环境），带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具。

**内部集成功能：**
- Project管理
- 智能提示
- 语法高亮
- 代码跳转
- 调试代码
- 解释代码(解释器)
- 框架和库

**基本使用：**
1. **新建项目：** 打开PyCharm -- [Create New Project] -- 选择项目根目录和解释器版本 -- [Create]
2. **新建文件：** 项目根目录右键 -- [New] -- [Python File] -- 输入文件名 -- [OK]
3. **运行文件：** 文件打开状态 -- 空白位置右键 -- Run

**基本设置：**
- 修改主题：[Appearance & Behavior] -- [Appearance]
- 修改代码文字格式：[Editor] -- [Font]
- 修改解释器：[Project: 项目名称] -- [Project Interpreter]

### 注释

**注释的作用：** 用人类熟悉的语言对代码进行解释说明，方便后期维护。

**注释分类：**

1. **单行注释：**
```python
# 注释内容
print('hello world')  # 输出hello world
```

2. **多行注释：**
```python
"""
第一行注释
第二行注释
第三行注释
"""

'''
注释1
注释2
注释3
'''
```

**快捷键：** Ctrl + /

**注意：** 解释器不执行任何的注释内容。

### 变量

**变量的作用：** 存储数据的内存地址的名字，方便后期查找和使用。

**定义变量语法：**
```python
变量名 = 值
```

**标识符命名规则：**
- 由数字、字母、下划线组成
- 不能数字开头
- 不能使用内置关键字
- 严格区分大小写

**命名习惯：**
- 见名知义
- 大驼峰：MyName
- 小驼峰：myName
- 下划线：my_name

**数据类型：**
- 整型：int
- 浮点型：float
- 字符串：str
- 布尔型：bool
- 列表：list
- 元组：tuple
- 集合：set
- 字典：dict

**检测数据类型：** `type()`

### 输出

**格式化输出：**

1. **格式化符号：**

| 格式符号 | 转换 |
|:------:|:----:|
| %s | 字符串 |
| %d | 有符号的十进制整数 |
| %f | 浮点数 |

```python
age = 18
name = 'TOM'
weight = 75.5

print('我的名字是%s' % name)
print('我的学号是%4d' % student_id)
print('我的体重是%.2f公斤' % weight)
print('我的名字是%s，今年%d岁了' % (name, age))
```

2. **f-字符串：**
```python
print(f'我的名字是{name}, 明年{age + 1}岁了')
```

**转义字符：**
- `\n`：换行
- `\t`：制表符（4个空格）

**结束符：**
```python
print('内容', end="")  # 默认end="\n"
```

### 输入

**输入语法：**
```python
input("提示信息")
```

**输入特点：**
- 当程序执行到input，等待用户输入，输入完成之后才继续向下执行
- input接收用户输入后，一般存储到变量，方便使用
- input会把接收到的任意用户输入的数据都当做字符串处理

```python
password = input('请输入您的密码：')
print(f'您输入的密码是{password}')
print(type(password))  # <class 'str'>
```

### 数据类型转换

**转换函数：**

| 函数 | 说明 |
|:----:|:----:|
| int(x) | 将x转换为一个整数 |
| float(x) | 将x转换为一个浮点数 |
| str(x) | 将对象x转换为字符串 |
| eval(str) | 用来计算在字符串中的有效Python表达式 |
| tuple(s) | 将序列s转换为一个元组 |
| list(s) | 将序列s转换为一个列表 |

**示例：**
```python
num = input('请输入您的幸运数字：')  # 输入"1"
print(type(num))  # <class 'str'>
print(type(int(num)))  # <class 'int'>
```

### 运算符

**1. 算数运算符：**

| 运算符 | 描述 | 实例 |
|:----:|:----:|:----:|
| + | 加 | 1 + 1 = 2 |
| - | 减 | 1 - 1 = 0 |
| * | 乘 | 2 * 2 = 4 |
| / | 除 | 10 / 2 = 5 |
| // | 整除 | 9 // 4 = 2 |
| % | 取余 | 9 % 4 = 1 |
| ** | 指数 | 2 ** 4 = 16 |
| () | 小括号 | (1 + 2) * 3 = 9 |

**运算优先级：** `()` > `**` > `*` `/` `//` `%` > `+` `-`

**2. 赋值运算符：**

```python
# 单个变量赋值
num = 1

# 多个变量赋值
num1, float1, str1 = 10, 0.5, 'hello world'

# 多变量赋相同值
a = b = 10
```

**3. 复合赋值运算符：**

| 运算符 | 描述 | 实例 |
|:----:|:----:|:----:|
| += | 加法赋值运算符 | c += a 等价于 c = c + a |
| -= | 减法赋值运算符 | c -= a 等价于 c = c - a |
| *= | 乘法赋值运算符 | c *= a 等价于 c = c * a |
| /= | 除法赋值运算符 | c /= a 等价于 c = c / a |

**4. 比较运算符：**

| 运算符 | 描述 |
|:----:|:----:|
| == | 判断相等 |
| != | 不等于 |
| > | 大于 |
| < | 小于 |
| >= | 大于等于 |
| <= | 小于等于 |

**5. 逻辑运算符：**

| 运算符 | 描述 |
|:----:|:----:|
| and | 布尔"与" |
| or | 布尔"或" |
| not | 布尔"非" |

```python
a = 1
b = 2
c = 3
print((a < b) and (b < c))  # True
print((a > b) or (b < c))   # True
print(not (a > b))          # True
```

---

## 流程控制

### 条件语句

**条件语句作用：** 条件成立执行某些代码，条件不成立则不执行这些代码。

**1. if语法：**
```python
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
```

**示例：**
```python
age = int(input('请输入您的年龄：'))
if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上网')
```

**2. if...else...语法：**
```python
if 条件:
    条件成立执行的代码
else:
    条件不成立执行的代码
```

**示例：**
```python
age = int(input('请输入您的年龄：'))
if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上网')
else:
    print(f'您的年龄是{age},未成年，请自行回家写作业')
```

**3. 多重判断：**
```python
if 条件1:
    条件1成立执行的代码
elif 条件2:
    条件2成立执行的代码
else:
    以上条件都不成立执行的代码
```

**示例：**
```python
age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您的年龄是{age},童工一枚')
elif 18 <= age <= 60:
    print(f'您的年龄是{age},合法工龄')
else:
    print(f'您的年龄是{age},可以退休')
```

**4. if嵌套：**
```python
if 条件1:
    条件1成立执行的代码
    if 条件2:
        条件2成立执行的代码
```

**5. 三目运算符：**
```python
值1 if 条件 else 值2

# 示例
a = 1
b = 2
c = a if a > b else b
```

### 循环语句

**循环的作用：** 让代码更高效的重复执行。

**1. while循环：**
```python
while 条件:
    条件成立重复执行的代码1
    条件成立重复执行的代码2
```

**示例：**
```python
# 输出5次"媳妇儿，我错了"
i = 0
while i < 5:
    print('媳妇儿，我错了')
    i += 1
```

**应用案例：**

*计算1-100累加和：*
```python
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)  # 5050
```

*计算1-100偶数累加和：*
```python
i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print(result)  # 2550
```

**2. break和continue：**

- **break：** 终止整个循环
- **continue：** 退出当前一次循环，继续执行下一次循环

```python
# break示例
i = 1
while i <= 5:
    if i == 4:
        print('吃饱了不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1

# continue示例
i = 1
while i <= 5:
    if i == 3:
        print(f'大虫子，第{i}个不吃了')
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1
```

**3. while循环嵌套：**
```python
while 条件1:
    条件1成立执行的代码
    while 条件2:
        条件2成立执行的代码
```

**应用案例：**

*打印星号(正方形)：*
```python
j = 0
while j <= 4:
    i = 0
    while i <= 4:
        print('*', end='')
        i += 1
    print()
    j += 1
```

*打印星号(三角形)：*
```python
j = 0
while j <= 4:
    i = 0
    while i <= j:
        print('*', end='')
        i += 1
    print()
    j += 1
```

*九九乘法表：*
```python
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={j*i}', end='\t')
        i += 1
    print()
    j += 1
```

**4. for循环：**
```python
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2
```

**示例：**
```python
str1 = 'itheima'
for i in str1:
    print(i)
```

**5. else语句：**

循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码。

```python
# while...else
i = 1
while i <= 5:
    print('媳妇儿，我错了')
    i += 1
else:
    print('媳妇原谅我了，真开心')

# for...else
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('循环正常结束之后执行的代码')
```

**注意：** 如果是break终止循环，else下方缩进的代码将不执行。

---

## 数据序列

### 字符串

**字符串特征：**

1. **一对引号字符串：**
```python
name1 = 'Tom'
name2 = "Rose"
```

2. **三引号字符串：**
```python
name3 = ''' Tom '''
name4 = """ Rose """
a = ''' i am Tom, 
        nice to meet you! '''
```

**下标（索引）：**

下标又叫索引，就是编号。通过下标快速找到对应的数据。

```python
name = "abcdef"
print(name[1])  # b
print(name[0])  # a
print(name[2])  # c
```

**注意：** 下标从0开始。

**切片：**

切片是指对操作的对象截取其中一部分的操作。

**语法：**
```python
序列[开始位置下标:结束位置下标:步长]
```

**示例：**
```python
name = "abcdefg"
print(name[2:5:1])  # cde
print(name[2:5])    # cde
print(name[:5])     # abcde
print(name[1:])     # bcdefg
print(name[:])      # abcdefg
print(name[::2])    # aceg
print(name[:-1])    # abcdef
print(name[-4:-1])  # def
print(name[::-1])   # gfedcba
```

**常用操作方法：**

**1. 查找方法：**

- `find()`：查找子串位置，找不到返回-1
- `index()`：查找子串位置，找不到报异常
- `count()`：统计子串出现次数

```python
mystr = "hello world and itcast and itheima and Python"
print(mystr.find('and'))        # 12
print(mystr.index('and'))       # 12
print(mystr.count('and'))       # 3
```

**2. 修改方法：**

- `replace()`：替换
- `split()`：分割
- `join()`：合并
- `capitalize()`：首字母大写
- `title()`：每个单词首字母大写
- `lower()`：转小写
- `upper()`：转大写
- `strip()`：删除两侧空白字符

```python
mystr = "hello world and itcast"
print(mystr.replace('and', 'he'))           # hello world he itcast
print(mystr.split('and'))                   # ['hello world ', ' itcast']
print('_'.join(['chuan', 'zhi', 'bo']))     # chuan_zhi_bo
print(mystr.capitalize())                   # Hello world and itcast
print(mystr.title())                        # Hello World And Itcast
print(mystr.upper())                        # HELLO WORLD AND ITCAST
```

**3. 判断方法：**

- `startswith()`：检查是否以指定子串开头
- `endswith()`：检查是否以指定子串结尾
- `isalpha()`：检查是否只包含字母
- `isdigit()`：检查是否只包含数字
- `isalnum()`：检查是否只包含字母和数字
- `isspace()`：检查是否只包含空白

```python
mystr = "hello world"
print(mystr.startswith('hello'))  # True
print(mystr.endswith('world'))    # True
print('abc'.isalpha())            # True
print('123'.isdigit())            # True
```

---

*注：由于内容较多，本汇总文档包含了Python核心编程的主要知识点。完整的列表、元组、字典、集合、函数、文件操作、面向对象、异常处理、模块和包等内容请参考对应的详细课件。*

---

**学习建议：**

1. **循序渐进：** 按照章节顺序学习，每个知识点都要动手实践
2. **多做练习：** 通过大量的代码练习来巩固知识点
3. **理解原理：** 不仅要知道怎么用，还要理解为什么这样用
4. **项目实战：** 学完基础知识后，通过实际项目来应用所学内容
5. **持续学习：** Python生态丰富，要保持学习的热情和好奇心

**常用资源：**

- Python官方文档：https://docs.python.org/
- Python教程：https://www.runoob.com/python3/
- 在线编程练习：https://www.codecademy.com/
- 开源项目：https://github.com/

---

*本汇总文档基于阶段1-Python核心编程课件整理，涵盖了Python编程的核心知识点，适合初学者系统学习和复习使用。*