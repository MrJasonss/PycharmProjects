
'''
    #从键盘中输入一个值,这个值用来控制这行中*的个数
    num = int(input("请输入这个行里的*的个数:"))
    
    j = 1
    while j<=num:
        print("*", ed="")
        j+=1
 '''
i= 1

num = input("请输入您要的三角形的高度：")
num_int = int(num)
while i<=num_int:
    j=1
    while j<=5:
        print("*",end="");
        j += 1
    print("")
    i+=1


