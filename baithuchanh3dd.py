#bai1
def sum(a,b):
    print("sum="+str(a+b))
#bai2
def sum(a,b):
    return a+b
c=sum(4,5);
print("tong cua 4va 5="+str(c))

#bai3
a="hello"
def say_hello():
    a="Hello"
    print(a)
print(a)
#BAI4
a="hello guy"
def say(a):
    a="vinh university"
    print(a)
say(a)
print(a)
#bai5
a="hello guy!"
def say():
    global a
    a="vinh university"
    print(a)
say()
print(a)
#bai6
def get_sum(*num):
    tmp=0
    #duyet cac tham so
    for i in num:
        tmp+=i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)
#bai7
def checkValue(n):
    if n%2==0:
        print("đây là một số chẵn")
    else:
        print("đây là một số lẻ")
checkValue(7)
#bai8

#bai9
"" "Chương trình tạo một máy tính đơn giản có thể cộng, trừ, nhân và chia bằng các hàm" ""
# Hàm này thêm hai số
def  aff ( x , y ):
    trả lại  x + y
# Hàm này trừ hai số
def  trừ ( x , y ):
    trả lại  x - y
# Hàm này nhân hai số
def  bội ( x , y ):
    returnx * y
# This fjection chia hai số
 chia def ( x , y ):
    trả lại  x / y
in ( "Chọn thao tác." )
in ( "1.Thêm" )
in ( "2.Subtract" )
in ( "3.Multiply" )
in ( "4.Divide" )

#Take đầu vào từ người dùng
sự lựa chọn  =  đầu vào ( "Nhập sự lựa chọn (1/2/3/4):" )
num1  =  int ( đầu vào ( "Nhập số đầu tiên:" ))
num2  =  int ( đầu vào ( "Nhập số thứ hai:" ))

nếu  lựa chọn == '1' :
    in ( mum1 , "+" , num2 , "=" , thêm ( num1 , num2 ))
 lựa chọn elif == '2' :
    in ( num1 , "-" , num2 , "=" , trừ ( num1 , num2 ))
 lựa chọn elif == '3' :
    in ( num1 , "*" , num2 , "=" , nhân ( num1 , num2 ))
 lựa chọn elif == '4' :
    in ( num1 , "/" , num2 , "=" , chia ( num1 , num2 ))
khác :
    in ( "Đầu vào không hợp lệ" )
#bai10
nhập môn toán
def Tinh(R):
    nếu R < 0:
        in ("Ban kinh khong nho hon 0")
        in ("Ban nhap khong hop le")
    khác:
        CV = 2 * R * toán.số Pi
        DT = R * R * toán.số Pi
        in ("Chu vi la:", CV)
        in ("Điện thoại:", DT)

in ("------- Tinh Chu Vi, Điện Tử Hinh Tron ---------")
r = float(đầu vào("Nhap ban kinh hinh tron:"))
Tinh(r)
#bai11
def  bai1 ( t , n , k ):
 cho  tôi  trong  phạm vi ( k ):
    n = n + n * t / 100
    in ( "Tống so tien nhan duoc la:" , n )
if  __name__ == "__main__" :
 t = float ( đầu vào ( "Nhap lai suat:" ))
 n = float ( đầu vào ( "Nhap so tien gui ban dau:" ))
 k = int ( đầu vào ( "Nhap so thang gui:" ))
 bai1 ( t , n , k )