def  file_read_form_head ( fname , nlines ):
    từ  itertools  nhập  islice
    với  mở ( fname ) như  f :
        cho  dòng  trong  islice ( f , nlines ):
            in ( dòng )
        file_read_from_head ( 'test.txt' , 2 )
