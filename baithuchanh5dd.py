#bai2
nhập  datetime  dưới dạng  dt
định dạng =  '% Y-% m-% dT% H:% M:% S'
t1 =  dt . datetime . strptime ( '2008-10-12T14: 45: 52' , định dạng )
in ( 'Ngày' + str ( t1 . ngày ))
in ( 'Ngày' + str ( t1 . ngày ))
in ( 'Tháng' + str ( t1 . tháng ))
in ( 'Phút' + str ( t1 . phút ))
in ( 'Thứ hai' +  str ( t1 . giây ))

# Xác định ngày và giờ
t2 = dt . datetime . bây giờ ()
khác biệt = t2 - t1
in ( 'bao nhiêu ngày khác biệt?' +  str ( diff . ngày ))
#bai3
import numpy as np
x=np.arange(12,38)
print(x)
#bai4
a = [ 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 ]
a = a [:: - 1 ]
in ( a )
#bai5
lst  = []
num  =  int ( đầu vào ( 'Co bao nhieu gia tri:' ))
cho  n  trong  phạm vi ( num ):
    gia_tri  =  đầu vào ( ' Nháp gia tri:' )
    lst . chắp thêm ( gia_tri )
    in ( lst )
in ( "Phan tu lon nhat:" , max ( lst ), "\ Phan tu nho nhat:" , min ( lst ))
#bai6
#bai7
nhập  numpy  như  np
data_type  = [( 'name' , 'S15' ), ( 'class' , 'int' ), ( 'height' , float )]
student_details = [( 'Jame' , 5 , 48.5 ), ( 'Nail' , 6 , 52.5 ), ( 'Paul' , 5 , 42.10 ), ( 'Hố' , 5 , 40.1 )]
# tạo một mảng có cấu trúc
sinh viên = np . mảng ( students_details , dtype = data_type )
in ( 'mảng gốc:' )
in ( sinh viên )
in ( "Sắp xếp theo chiều cao" )
in ( np . sort ( sinh viên , thứ tự = 'chiều cao' ))
#bai8
def  Sequential_Search ( mảng , n , x ):
    cho  tôi  trong  phạm vi ( n ):
        if ( mảng [ i ] ==  x ):
            trả lại  tôi
    trở lại  - 1

mảng = []
n  = int ( đầu vào ( 'Mục bao nhieu:' ))
cho  k  trong  phạm vi ( n ):
    mục = đầu vào ( 'mục Nhap:' )
    mảng . phụ lục ( mục )
x  = input ( 'Nhap vao mục có thể hẹn giờ:' )
n =  len ( mảng )
result  =  Sequential_Search ( mảng , n , x )
nếu ( kết quả  ==  - 1 ):
    in ( "Phan tu khong co trong mang" )
khác :
    in ( "Phan tu co trong mang" , 'va co vi tri:' , kết quả )