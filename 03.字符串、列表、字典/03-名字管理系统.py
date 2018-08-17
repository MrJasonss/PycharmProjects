# 1.打印动能提示
print("="*50)
print("         名字管理系统V8.0            ")
print("1:添加一个新的名字")
print("2:删除一个名字")
print("3:修改一个名字")
print("4:查询一个名字")
print("0:退出系统")

print("="*50)
names = []  # 定义一个空的列表  存储添加的名字
# 2.获取用户选择
while True:
    num = int(input("请输入功能序号："))
    # 3.根据用户选择，执行相应的功能
    if num==1:
        new_name = input("请输入一个名字:")
        names.append(new_name)
        print(names)
    elif num==2:
        remove_name = input("请输入要删除的名字:")
        names.remove(remove_name)
    elif num==3:
        while True:
            update_name =input("请输入你要修改的名字：")
            if update_name in names:
                print("系统已为您找到了该名字！！")
                replace_name = input("请输入您想修改的名字：")
                names.remove(update_name)
                names.append(replace_name)
                print("修改后信息显示为:%s"%names)
                break
            else:
                print("不好意思，您要修改的信息不存在！！！")
    elif num==4:
        find_name = input("请输入要查询的名字:")
        if find_name in names:
            print("找到了。。。。")
        else:
            print("没找到你查询的人名。。。。")
    elif num==0:
        break
    else:
        print("您的输入有误！！请重新输入")