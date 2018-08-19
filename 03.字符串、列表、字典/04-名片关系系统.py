#1. 打印功能提示
print("="*50)
print("   名片管理系统 V0.01")
print(" 1. 添加一个新的名片")
print(" 2. 删除一个名片")
print(" 3. 修改一个名片")
print(" 4. 查询一个名片")
print(" 5. 显示所有的名片")
print(" 0. 退出系统")
print("="*50)


#用来储存名片

card_infors = []

while True:

    #2.获取用户输入
    num = int(input("请输入操作序列号："))
    #3.根据用户数据，执行相对应的功能

    if   num==1:
        new_name = input("请输入新的名字:")
        new_qq = input("请输入新的QQ:")
        new_weixin = input("请输入新的微信:")
        new_addr = input("请输入新的住址:")

        #定义一个新的字典,用来存储一个新的名片
        new_infor = {}
        new_infor['name'] = new_name
        new_infor['qq'] = new_qq
        new_infor['weixin'] = new_weixin
        new_infor['addr'] = new_addr
        card_infors.append(new_infor)

    elif num==2:
        pass
    elif num==3:
        pass
    elif num==4:
        find_name = input("请输入您要查询的姓名")
        find_flag = 0
        for temp in card_infors:
            if find_name==temp['name']:
                print("姓名\tQQ\t微信\t住址")
                print("%s\t%s\t%s\t%s" % (temp['name'], temp['qq'], temp['weixin'], temp['addr']))
                find_flag = 1  # 表示找到了
                break
    elif num==5:
        #显示所有的数据  直接for遍历即可
        print("姓名\tQQ\t微信\t住址")
        for temp in card_infors:
            print("%s\t%s\t%s\t%s\t"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
    elif num==0:
        break
    else:
        print("您的输入有误,请重新输入")
    print("")