import func

# 재고관리 프로그램

inventory = {"시발점":0, "뉴런":0, "수분감":0, "드릴":0, "킬캠":0}

money = int(100000)

def menu(money) : 

    i = int(input(f"실행할 항목을 선택하세요. 현재 당신의 잔액은 {money}입니다. 1.구매 2.판매 3.재고확인 4.끝내기"))

    if i == 1 : 

        buy(money)

    elif i == 2 : 

        sell(money)

    elif i == 3 : 

        inven(money)

    elif i == 4 : 
        
        print("프로그램을 종료합니다.")

    else : 

        print("잘못된 입력입니다.")

        menu(money)

def buy(money) :

    i = int(input(f"구입할 항목의 번호를 입력하세요. 현재 당신의 잔액은 {money}원 입니다. 1.시발점(1000) 2.뉴런(3000) 3.수분감(5000) 4.드릴(7000) 5.킬캠(9000)"))

    if i == 1 :
        
        if money >= 1000 :

            print("시발점을 구매합니다.")

            inventory["시발점"] += 1

            money -= 1000

            return menu(money)


        else :

            print("잔액이 부족합니다.")
        
        menu(money)

    elif i == 2 :
        
        if money >= 3000 :

            print("뉴런을 구매합니다.")

            inventory["뉴런"] += 1

            money -= 3000

            return menu(money)

        else :

            print("잔액이 부족합니다.")

        menu(money)

    elif i == 3 :
        
        if money >= 5000 :

            print("수분감을 구매합니다.")

            inventory["수분감"] += 1

            money -= 5000
            
            return menu(money)

        else :

            print("잔액이 부족합니다.")

        menu(money)

    elif i == 4 :
        
        if money >= 7000 :

            print("드릴을 구매합니다.")

            inventory["드릴"] += 1

            money -= 7000

            return menu(money)

        else :

            print("잔액이 부족합니다.")

        menu(money)

    elif i == 5 :
        
        if money >= 9000 :

            print("킬캠을 구매합니다.")

            inventory["킬캠"] += 1

            money -= 9000

            return menu(money)

        else :

            print("잔액이 부족합니다.")

        menu(money)

    else : 

        print("잘못된 입력입니다.")

        buy(money)

def sell(money) :

    i = int(input(f"판매할 항목의 번호를 입력하세요. 현재 당신의 잔액은 {money}원 입니다. 1.시발점(1000) 2.뉴런(3000) 3.수분감(5000) 4.드릴(7000) 5.킬캠(9000)"))

    if i == 1 :
        
        if inventory.get("시발점") != 0 :

            print("시발점을 판매합니다.")

            inventory["시발점"] -= 1

            money += 1000

            return menu(money)

        else :

            print("재고가 부족합니다.")

        menu(money)

    elif i == 2 :
        
        if inventory.get("뉴런") != 0 :

            print("뉴런을 판매합니다.")

            inventory["뉴런"] -= 1

            money += 3000

            return menu(money)

        else :

            print("재고가 부족합니다.")

        menu(money)

    elif i == 3 :
        
        if inventory.get("수분감") != 0 :

            print("수분감을 판매합니다.")

            inventory["수분감"] -= 1

            money += 5000

            return menu(money)

        else :

            print("재고가 부족합니다.")

        menu(money)

    elif i == 4 :
        
        if inventory.get("드릴") != 0 :

            print("드릴을 판매합니다.")

            inventory["드릴"] -= 1

            money += 7000

            return menu(money)

        else :

            print("재고가 부족합니다.")

        menu(money)

    elif i == 5 :
        
        if inventory.get("킬캠") != 0 :

            print("킬캠을 판매합니다.")

            inventory["킬캠"] -= 1

            money += 9000

            return menu(money)

        else :

            print("재고가 부족합니다.")

        menu(money)

    else : 

        print("잘못된 입력입니다.")

        sell(money)

def inven(money) :

    print(f"현재 당신의 재고 : {inventory.items()}입니다.")

    menu(money)

func.welcome()

menu(money)

