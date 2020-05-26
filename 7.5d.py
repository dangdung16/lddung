nhập khẩu  hệ thống
nhập khẩu  os
def  file_read_from_tail ( fname , dòng ):
        bufsize  =  8192
        fsize  =  os . stat ( fname ). kích thước
        lặp lại  =  0
        với  mở ( fname ) như  f :
            nếu  bufize  >  fsize :
                bufsize  =  fsize - 1
                dữ liệu  = []
                trong khi  Đúng :
                    lặp lại  + = 1
                    f . tìm kiếm ( fsize - bufsize * iler )
                    dữ liệu . mở rộng ( f . readline ())
                    nếu  len ( dữ liệu ) > =  dòng  hoặc  f . nói () ==  0 :
                        in ( '' . tham gia ( dữ liệu [ - dòng :]))
                        phá vỡ
file_read_from_tall ( 'test.txt' , 2 )
