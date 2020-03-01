''' 简单计算器制作 '''
def change(mark):  #提取"+","-","*","/"的通用功能
    global Sum
    m=d.index(mark)
    if mark=="*":
        Sum = k[m] * k[m+1]
    elif mark=="/":
        Sum = k[m] / k[m+1]
    elif mark=="+":
        Sum = k[m] + k[m+1]
    elif mark=="-":
        Sum = k[m] - k[m+1]
    k[m]=Sum
    del k[m+1]
    d.remove(d[m])

def JS(Num):
    #k存储数字字符,d存储符号字符
    global k
    k=[]
    global d
    d=[]
    cba=Num
    for item in Num:
        #用","替换源字符串中所有符号,再按","分割得到新的数字列表Num
        if item=="+" or item=="-" or item=="*" or item=="/":
            d.append(item)
            Num=Num.replace(item,",")
    Num=Num.split(",")
    if Num[0]=="":
        Num[0]=0
    #判断是不是数字,如果不是数字则添加到列表d,否则添加进列表k
    # for item in Num:
    #     if item.isnumeric()or isnumber(item):
    #         item=float(item)
    #         k.append(item)
    #     else:
    #         # print("输入的方式不正确！！正确格式例如:(a+b)*c")
    #         pass
    for i in Num:
            if i=="":
                pass
            else:
                i=float(i)
                k.append(i)
    count = 0
    for i in range(len(cba)):
        if cba[i] == "+" or cba[i] == "-" or cba[i] == "*" or cba[i] == "/":
            count += 1
            if cba[i+1] == "-":
                k[count] = -k[count]
                del d[count]
                count-=1
    for i in range(len(d)):
        if "*" in d and "/" in d:
            m=d.index("*")
            n=d.index("/")
            if m<n:
                change("*")
            else:
                change("/")
        elif "*" in d :
            change("*")
        elif "/" in d :
            change("/")
    for i in range(len(d)):
        if "+" in d and "-" in d:
            m=d.index("+")
            n=d.index("-")
            if m<n:
                change("+")
            else:
                change("-")
        if "+" in d:
            change("+")
        elif "-" in d:
            change("-")
def chazhao():
    global Nba
    global Num
    m=Nba.rfind("(")  #从右向左查找第一个左括号即最里层括号中的左括号
    n=Nba[m:]  #从这个左括号起把以后的字符赋给N
    c=n.find(")")#在N中从左向右查找第一个右括号即最里层括号中的右括号
    Num=n[1:c]  #找到括号把里面的字符赋值给Num
    JS(Num)   #调用基本的操作函数,并算出结果
    j=str(Sum)
    Nba=Nba.replace(Nba[m:m+c+1],j)   #将计算出的结果添加进最初的字符串中
    #JS(Nba)
while True:
    Nba=input("请输入计算公式：")
    while True:
        if "(" in Nba or ")" in Nba:
            chazhao()  #有括号时一直循环执行chazhao(),把括号全部替换
        else:
            JS(Nba)    #字符串中没有括号时直接调用基本运算
            print(Sum)
            break
