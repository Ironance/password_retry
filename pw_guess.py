login_pw = 'a123'
trail = 3

while trail > 0:
    trail = trail - 1
    pw = input('Please input the password:')
    if pw == login_pw:
        print('Login Successfully!')
        break
    else:
        print('Wrong password!')
        if trail > 0:
            print(trail, 'chance left')
        else:
            print('Fail to login! Account is blocked!')




