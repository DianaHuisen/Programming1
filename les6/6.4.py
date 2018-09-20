def new_password(oldpassword,newpassword):
    cijfer1=0
    for cijfers in newpassword:
        if cijfers in '0123456789':
            cijfer1=1
    if newpassword != oldpassword and len(newpassword)>= 6 and cijfer1 == 1:
        return('True')
    else:
        return('False')

oldpassword = input('Wat is je oude password: ')
newpassword = input('Wat is je nieuwe password: ')
print(new_password(oldpassword, newpassword))