k = mở ( 'D: / k = opent (a.txt' , 'r' )
char , wc , lc = 0 , 0 , 0
cho  dòng  trong  k :
    cho  k  trong  phạm vi ( 0 , len ( dòng )):
        char  + = 1
        if ( dòng [ k ] == '' ):
            wc + = 1
        if ( dòng [ k ] == ' \ n ' ):
            wc , lc = wc + 1 , lc + 1
print ( "Các ký tự no.of là% d \ n Các từ no.of là% d \ n Các dòng no.of là% d" % ( char , wc , lc ))
