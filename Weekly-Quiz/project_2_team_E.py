"""
content: 이름으로 구문 만들기.

Date: 2022.05.11
Team: E
Members: 김예지, 곽민규, 오시현, 이완희, 진주연
pylint 점수: 7.83/10
"""

"""
의사코드: 단어모음(choose)과 이름딕셔너리(name_dic)를 인자로 하는 choose_word함수:
걸러진 단어를 넣을 빈 리스트 result 를 선언한다.
	for 단어 모음에 있는 모든 단어:
		조건에 맞으면 True, 아니면 False를 저장하는 judge 변수 선언
		for 단어에 있는 모든 알파벳:
			if 단어의 알파벳 개수 > 이름딕셔너리 안에서 그 알파벳의 value값:
				judge = False
		if judge가 True:
			result에 단어를 추가한다.
	if result에 값이 있으면:
		result 반환

선택지가 없을 때 다음 활동을 고르는 함수:
	사용자로부터 1) 처음부터 시작할지 2) 그만둘지를 입력받는다.
	입력값이 1이라면:
		name_to_phrase 함수를 호출해 처음부터 시작한다.
	입력값이 2 혹은 quit라면:
		None을 반환한다.
	나머지 입력값은:
		없는 번호임을 알리고 다시 이 함수를 호출한다.
 
 
 
last_choice함수를 정의한다.
last_choice를 입력받는다
if last_choice가 1이라면
name_to_pharase()함수를 다시 호출한다.
elif last_choice가 2라면
None값을 반환한다
 
 
 
 
name_to_pharase함수를 정의한다.
sys를 import한다
name변수에 사용자가 입력한 이름을 저장한다.
 
단어사전 파일(dictionary.txt)을 file이라는 이름으로 연다.
file의 단어들을 모두 소문자로 변환하여 dict_list라는 리스트에 담는다.
(readlines를 사용하면 \n문자가 생기고 따로 제거해주어야 하므로 read 사용)
dict_list에 있는 단어 끝에 붙은 특수문자를 제거한다.
dict_list에 i,a를 추가해준다.
 
입력받은 name의 문자가 알파벳이라면, 소문자로 변환한 후 {문자: 문자 개수}의 형태로 name_dic에 저장한다.
 
extracted_words 리스트에 1차적으로 “dict_list 속 단어의 알파벳 집합”이 “name에 쓰인 알파벳(name_dic의 key부분 활용)집합”의 부분집합인 경우를 담아준다.
 
 
choose 변수를 choose_word(extracted_words, name_dic)의 반환값으로 초기화하고 출력한다
 

user_word_list를 공백문자열로 초기화한다.
 
true일 때까지 반복한다.
user_word를 입력받는다.
만약 user_word가 quit이라면
중지
만약 user_word가 choose리스트 속에 있다면
user_word_list에 user_word와 공백을 붙인다.
user_word_list를 출력한다.
user_word에서 alpha를 순회한다.
name_dic[alpha]의 값을 기존에서 1을 뺀 값으로 변경한다.
if choose_word를 실행했을 때 빈 리스트가 나온다면:
if last_choice()에서 사용자가 종료하기를 선택한다면
종료한다
else:
choose 변수를 choose_word(extracted_words, name_dic)의 반환값으로 초기화하고 출력한다
else:
"없는 단어 입니다. 다시 선택해주세요."프린트한다
 
name_to_pharase() 실행
"""
def choose_word(extracted_words, name_dic):
    """이름의 알파벳 개수에 맞는 단어 추출하는 함수."""
    result = []
    for word in extracted_words:
        judge = True
        for alpha in word:
            if word.count(alpha) > name_dic.get(alpha):
                judge = False
        if judge:
            result.append(word)
    if result:
        return result
    
def last_choice():
    """사전 단어 리스트가 비었을 때 사용자에게 진행 상태 결정하도록 하는 함수."""
    choice = input("선택지가 더 이상 없습니다. 1) 처음부터 시작하기 2) 그만두기")
    if choice == "1":
        return name_to_phrase()
    elif choice in ('2', 'quit'):
        return None
    else:
        print("없는 번호입니다. 다시 입력해주세요.")
        last_choice()
    
def name_to_phrase():
    """출력물 중 사용자 단어 입력받아 구문 만들기."""
    import sys
    name = input("이름을 입력해주세요 : ")

    with open('/Users/Kwak/dictionary.txt', 'r', encoding = 'utf-8') as file :
        dict_list = file.read().lower().split()
    dict_list = [w[:-1] if not w.isalpha() else w for w in dict_list]    
    dict_list += ['i', 'a']

    name_dic = {ch: name.count(ch) for ch in name.lower() if ch.isalpha()}
    extracted_words = [word for word in dict_list if set(word).issubset(name_dic.keys())]

    # 2. 이름으로 만들 수 있는 모든 단어를 사전에서 뽑아서 출력한다.
    print(choose := choose_word(extracted_words, name_dic))

    # 3 & 4
    user_word_list = ""
    while True:
        user_word = input("출력물 중 단어를 하나 선택해주세요 : ")
        if user_word == "quit":
            sys.exit()
        elif user_word in choose:
            user_word_list += user_word + " "
            print(user_word_list)
            for alpha in user_word:
                name_dic[alpha] = name_dic.get(alpha)-1
            # 5.
            if choose_word(choose, name_dic) is None:
                if last_choice() is None:
                    sys.exit()
            else:
                print(choose := choose_word(choose, name_dic))
        else:
            print("없는 단어 입니다. 다시 선택해주세요.")

name_to_phrase()
