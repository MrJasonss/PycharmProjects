#缺省参数   在定义函数的时候定义好参数值  如果参数不传值  就用默认参数   有参数  使用参数


#  缺省参数要定义到后面

def test(a,d,b=22,c=33):
    print(a)
    print(b)
    print(c)
    print(d)

test(d=11,a=22,c=44)
