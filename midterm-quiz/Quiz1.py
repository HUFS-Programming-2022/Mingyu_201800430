on_off_switch = True
while on_off_switch == True:
    # 1. 메뉴 제시
    mode_select = input(
        """
  구구단 출력기
  ----------------------------------------------------------------------
      1) n단 출력    2) n단까지 출력   3) n ~ m단 출력   q) 나가기
  ----------------------------------------------------------------------
  메뉴를 선택하세요 > 
  """
    )
    # 2. 각 메뉴에 맞는 출력물 프린트
    # 2 - 조건1. 0 < n < 10
    correct_n = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "q"]
    if mode_select == "1":
        mode1_switch = True
        mode1_func = False
        while mode1_switch:
            n = input("몇 번째 단을 출력하시겠습니까? (exit:q)")
            if n not in correct_n:
                print("1부터 9까지의 자연수 혹은 q를 입력해주세요.")
                continue
            elif n == "q":
                print("1번 모드의 수행을 종료합니다.")
                mode1_switch = False
                break
            else:
                mode1_func = True
                mode1_switch = False
                break
        if mode1_func:    
            print(f"--- {n}단 ---")
            i = 1
            while i < 10:  # 1 := 1 바다코끼리 연산자를 활용하려 했으나 i += 1을 해줘도 while 조건문에서 i = 1로 overwrite 시켜버리기 때문에 무한 loop가 발생함
                print(f"{n} x {i} = {int(n) * i}")
                i += 1
            print("수행이 완료되었습니다.")
    elif mode_select == "2":
        mode2_switch = True
        mode2_func = False
        while mode2_switch:
            n = input("몇단까지 출력하시겠습니까? (exit:q)")
            if n not in correct_n:
                print("1부터 9까지의 자연수 혹은 q를 입력해주세요.")
                continue
            elif n == "q":
                print("2번 모드의 수행을 종료합니다.")
                mode2_switch = False
                break
            else:
                mode2_switch = False
                mode2_func = True
                break
        if mode2_func:
            for i in range(1, int(n) + 1):
                print(f"--- {i}단 ---")
                for j in range(1, 10):
                    print(f"{i} x {j} = {i * j}")
            print("수행이 완료되었습니다.")
    elif mode_select == "3":
        mode3_switch = True
        mode3_func = False
        while mode3_switch:
            n1 = input("구구단을 시작할 숫자를 입력하세요. 종료하시려면 q를 입력해주세요.")
            n2 = input("구구단 종료 숫자를 입력하세요. 종료하시려면 q를 입력해주세요.")
            if len(n1) != 1 or len(n2) != 1:
                print("잘못된 입력값입니다. 다시 입력하세요.")
                continue
            elif n1 not in correct_n or n2 not in correct_n:
                print("잘못된 입력값입니다. 1부터 9 사이의 자연수나 q를 입력하세요.")
                continue
            elif correct_n[-1] in n1 or correct_n[-1] in n2:
                while ask := input(
                    "입력값에서 'q'를 발견하였습니다. 정말로 끝내시겠습니까? 끝내시려면 'q'를, 계속하시려면 'c'를 눌러주세요."
                ):  # 여러 개 숫자를 입력하다 만약에 종료하고 싶지 않은데 q를 눌러버렸을 경우의 필터링
                    if ask == "q":
                        mode3_switch = False
                        print("3번 모드의 수행을 종료합니다.")
                        break
                    elif ask == "c":
                        break
                    else:
                        print("'q'나 'c' 중 하나만 입력해주세요.")
                        continue
            elif int(n1) > int(n2):
                while compare_2num := input(
                    "구구단을 시작할 숫자가 종료 숫자보다 큽니다. 숫자를 뒤집어 실행하시겠습니까? (y/n) (exit:q)"
                ): # 2 - 조건2. n <= m
                    if compare_2num == "y":
                        n1, n2 = n2, n1
                        mode3_func = True
                        mode3_switch = False
                        break
                    elif compare_2num == "n":
                        print("입력란으로 다시 돌아갑니다.")
                        break
                    elif compare_2num == "q":
                        print("3번 모드의 수행을 종료합니다.")
                        mode3_switch = False
                        break
                    else:
                        print("'y'나 'n' 중 하나만 입력해주세요.")
                        continue
            else:
                mode3_func = True
                mode3_switch = False
                break

        if mode3_func:
            for i in range(int(n1), int(n2) + 1):
                print(f"--- {i}단 ---")
                for j in range(1, 10):
                    print(f"{i} x {j} = {i * j}")
            print("수행이 완료되었습니다.")
    elif mode_select == "q":
        print("이용해주셔서 감사합니다.")
        on_off_switch = False
        break
    else:
        print("'1', '2', '3', 'q' 중 하나만 입력해주세요.")
        continue
    while finish_code := input("프로그램을 끝내시겠습니까? 프로그램을 끝내시려면 'y'를, 메뉴로 돌아가려면 'n'을 입력하세요."):
        if finish_code == "y":
            on_off_switch = False
            print("프로그램이 종료되었습니다.")
            print("이용해주셔서 감사합니다.") # 2 - 조건4. 
            break
        elif finish_code == "n":
            break
        else:
            print("'y'나 'n' 중 하나만 입력해주세요.")
            continue
