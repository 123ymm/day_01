# 这是一个示例 Python 脚本。
from xml.etree.ElementTree import tostring


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    name = "Tom"
    age = 24
    height = 167

    #数字型 转为 字符串类型
    print("名字：" + name)
    #print("年龄：" + tostring(age))
    #print("身高：" + tostring(height))
    print("年龄：" + str(age))
    print("身高：" + str(height))

    # f-string 以及对齐
    #前面加 f（或 F），字符串里用 {变量/表达式} 直接插值。
    #字符串前写 f；
    #花括号里放变量或表达式；
    #需要格式就在冒号后写规则（.2f、<10 等）
    print(f"年龄：{age}")
    print(f"身高：{height}")
    print(f"宽度 10 右对齐：{name:>10}")  #占10个格，向右对齐
    print(f"宽度 10 左对齐：{name:<10}")
    print(f"宽度 10 居中对齐：{name:^10}")

    #多行f-string
    info = f"""
       姓名：{name}
       年龄：{age}
       身高：{height}
       """
    print(info)

    pi = 3.1415926
    print(f"保留 2 位小数：{pi:.2f}")  # 3.14

    #分别查看name、age、height的类型
    print(type(name))
    print(type(age))
    print(type(height))
    print(type(info))

    weight = 66.45
    #格式化输出
    print('姓名：%s,年龄：%d,体重：%.1f公斤'%(name,age,weight))
    print(f'姓名：{name}，年龄：{age}，体重：{weight:.1f}')

    #接受用户输入：input()函数
    user_name = input('请输入用户名：')
    user_pwd = input('请输入密码：')
    print(f'宁输入的用户名是：{user_name}，密码是：{user_pwd}')

    num1 = int(input('请输入第一个数：'))
    num2 = int(input('请输入第二个数：'))
    result = num1 + num2
    print(result)

    apple_price = 6.6
    orange_price = 5
    apple_weight = float(input("请请输入你想要购买的苹果斤数："))
    orange_weight = float(input("请输入你想要购买的橘子斤数："))
    result = apple_price * apple_weight + orange_price * orange_weight
    print(f'这次购买水果的总价是：{result:.2f}')
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
