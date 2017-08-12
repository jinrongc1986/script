try :
    a=input()
    if a=='1':
        raise ValueError('gg')
    else:
        print('Yes!')
except ValueError as e:
    print('in error')
    print (e)