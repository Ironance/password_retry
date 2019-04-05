login_pw = 'a123'
trail = 3

while trail > 0:
    pw = input('Please input the password:')
    if pw == login_pw:
        print('Login Successfully!')
        break
    else:
        trail = trail - 1
        print('Wrong password!', trail, 'chance left')
        if trail == 0:
            print('Game Over!')




