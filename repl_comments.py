from hashlib import sha256


def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()


pwd_master="13a965e03bd53a70ab69c1a0d7f246afb8295c322c9cb1d9d56aab1b0a826b12"


comments=[]
while True:

    comment = input('Enter your comment: \n(for exit press 18 and enter)')

    if comment=='18':
        break
    else:
        pwd_user=input('Enter your pasword: ')

        pwd_user= create_hash(pwd_user)

        if pwd_master==pwd_user:
            comments.append(comment)
            print('Previously entered comments: ')
            count=1
            for comment in comments:
                print(str(count)+'.'+ comment )
                count=count+1

        else:
            print('Sorry i cant let you in!!')
