from getpass import getpass
import hashlib

def showMenu():
    print('1. 사기 2. 팔기 3. 재고상황 4. 비밀번호변경 5. 종료')

def loadInfo():
    global money, inventory
    print("FILE LOAD ..")
    f = open('inventory.txt', 'r')

    global f_id, f_pw
    f_id = f.readline().split()[2]
    f_pw = f.readline().split()[2]

    while True:
        id = input('Insert UserName : ')
        if id == f_id:
            pw = hashlib.sha256(
                getpass('Insert PassWord : ').encode()).hexdigest()
            if pw == f_pw:
                print('Hello, '+id)
                break
            else:
                print('Invalid PW')
        else:
            print('Invalid ID')

    money = int(f.readline().split()[2])

    inventory = {'apple': 0, 'banana': 0}
    inventory['apple'] = int(f.readline().split()[2])
    inventory['banana'] = int(f.readline().split()[2])
    f.close()

def saveInfo(pw=''):
    global money, inventory
    print("FILE SAVED ..")
    f = open('inventory.txt', 'w')
    f.writelines('id : {}\n'.format(f_id))
    if pw == '':
        f.writelines('pw : {}\n'.format(f_pw))
    else:
        f.writelines('pw : {}\n'.format(pw))
    f.writelines('money : {}\n'.format(money))
    f.writelines('apple : {}\n'.format(inventory['apple']))
    f.writelines('banana : {}'.format(inventory['banana']))
    f.close()

def buy():
    global money, inventory
    select = input('1. 사과(5000) 2. 바나나(7000)')

    if select == '1':
        if money < 5000:
            print('돈이 부족합니다.({})'.format(money))
            return 
        inventory['apple'] += 1
        money -= 5000

    elif select == '2':
        if money < 7000:
            print('돈이 부족합니다.({})'.format(money))
            return 
        inventory['banana'] += 1
        money -= 7000

    else:
        print('없는 메뉴 입니다.')

def sell():
    global money, inventory
    select = input('1. 사과(5000) 2. 바나나(7000)')
    if select == '1':
        if inventory['apple'] == 0:
            print('재고가 부족합니다.({})'.format(inventory))
            return 
        inventory['apple'] -= 1
        money += 5000

    elif select == '2':
        if inventory['banana'] == 0:
            print('재고가 부족합니다.({})'.format(inventory))
            return 
        inventory['banana'] -= 1
        money += 7000

    else:
        print('없는 메뉴 입니다.')

def showInventory():
    global money, inventory
    print('잔고 : {}'.format(money))
    print('재고 : {}'.format(inventory))

def changePassword():
    print("FILE LOAD ..")
    f = open('inventory.txt', 'r')
    f.readline()
    f_pw = f.readline().split()[2]
    p_pw = hashlib.sha256(
        getpass('Insert Previous PW : ').encode()).hexdigest()
    if f_pw == p_pw:
        n_pw = hashlib.sha256(getpass('Insert New PW : ').encode()).hexdigest()
        if n_pw == hashlib.sha256(getpass('Insert New PW again : ').encode()).hexdigest():
            saveInfo(n_pw)
            print('PassWord has changed !')
        else:
            print("PassWord is not matched !")

    else:
        print('Invalid PassWord')

if __name__ == "__main__":
    global money, inventory
    loadInfo()
    print()
    showInventory()

    while True:
        showMenu()
        select = input('')
        if select == '1':
            buy()
        elif select == '2':
            sell()
        elif select == '3':
            showInventory()
        elif select == '4':
            changePassword()
        elif select == '5':
            saveInfo()
            print("BYE")
            break

        else:
            print('없는 메뉴 입니다.')
        print()