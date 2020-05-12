####buoi2
#bai1
n1=int(input("enter n1 value"))
n2=int(input("enter n2 value"))
if n1>n2:
    print("n1 is big")
else:
    print("n2 is big")
#bai2
import math;
x1=int(input("Enter x1--->"))
y1=int(input("Enter y1--->"))

x2=int(input("Enter x2--->"))
y2=int(input("Enter y2--->"))

d1=(x2-x1)*(x2-x1);
d2=(y2-y1)*(y2-y1);
res=math.sqrt(d1+d2)
print("Distance between two points:",res);
#bai3
n=int(input("Enter a number---->"))
if n%2==0:
    print("EVEN Number");
else:
    print("ODD Number");
#bai4
i=1;
for j in range(2,10):
    print("i:",i,"j:",j)
    print(i,"/",j)
    print (i/j);
#bai5
n=int (input("Enter A Number--->"));
while n>0:
     print (n);
     n = n - 1;
#bai6
j=[]
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        j.append (str(i))
print (','.join(j))
#bai7
n=int(input("Nhap vao mot so:"))
d=dict()
for i in renge (1,n+1):
    d[i]=i*i
print(d)
#bai8
a , b  =  1 , 2
tổng  =  0
in ( a , end = "" )
trong khi ( a <= 4000000 - 1 ):
    nếu  một  %  2  ==  0 :
        tổng  + =  a
    a , b  =  b , a + b
    in ( a , end = "" )
in ( " \ n tổng số thuật ngữ số nguyên tố trong chuỗi:" , tổng cộng )
#bai9
str = input ( "Nhập chuỗi:" )
dict  = {}
cho  n  trong  str :
    phím  =  dict . phím ()
    nếu  n  trong  các phím :
        ra lệnh [ n ] + =  1
    khác :
        dict [ n ] =  1
in ( dict )
#bai10
a = "xin chào tôi là lập trình viên trăn"
b = a . chia ()
in ( b )
c = "" . tham gia ( b )
in ( c )
#bai11
l = [ 1 , 'trăn' , 4 , 7 ]
k = [ 'cse' , 2 , 'guntur' , 8 ]
m = []
m . phụ lục ( l );
m . phụ lục ( k );
in ( m )
d = { 1 : 1 , 2 : k , 'kết hợp_list' : m }
in ( d )
#bai12
nhập khẩu  lại
giá trị = []
vật phẩm = [ x  cho  x  trong  đầu vào ( "Lời nói:" ). chia ( ',' )]
# #############
cho  p  trong  các mục :
    nếu  len ( p ) < 6  hoặc  len ( p ) > 12 :
        tiếp tục
    khác :
        vượt qua
    nếu  không  lại . tìm kiếm ( "[az]" , p ):
        tiếp tục
    elif  không  tái . tìm kiếm ( "[0-9]" , p ):
        tiếp tục
    elif  không  tái . tìm kiếm ( "[AZ]" , p ):
        tiếp tục
    elif  không  tái . tìm kiếm ( "[$ # @]" , p ):
        tiếp tục
    elif  lại . tìm kiếm ( "\ s" , p ):
        tiếp tục
    khác :
        vượt qua
    giá trị . phụ lục ( p )
    in ( "," . tham gia ( giá trị ))