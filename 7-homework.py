def gugudan():
    try:
        dan = int(input("2에서 9사이의 숫자를 입력해주세요: "))
        if dan > 1 and dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요!!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan()
    except:
        print("알 수 없는 에러가 발생 했습니다.")
        gugudan()
gugudan()
