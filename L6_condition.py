# 判斷式
x=input("請輸入數字: ") # 取得字串形式
x=int(x) # 將字串型態轉換成數字型態
if x>200:
    print("大於200")
elif x>100:
    print("大於100，小於等於200")
else:
    print("小於等於100") 
# 此結構只會跑1,2,3的其中一塊，跑完後會直接跳出

# 四則運算
n1=int(input("請輸入數字一: "))
n2=int(input("請輸入數字二: "))
op=input("請輸入運算: +, -, *, /: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")