def name_to_phrase():
    import sys
    
    with open('/Users/Kwak/dictionary.txt', 'r', encoding = 'utf-8') as file :
        dict_list = file.read().lower().split()
        dict_list += ['i', 'a']
        dict_list = [w[:-1] if not w.isalpha() else w for w in dict_list] 
        
    

    while True:
        # 2번. choose_word()함수 돌리기 전까지의 과정
        name = input('full name을 입력하세요: ')
        name_dic = {ch: name.count(ch) for ch in name.lower() if ch.isalpha()}
        extracted_words = [word for word in dict_list if set(word).issubset(name_dic) and len(word) <= len(name)]
        
        user_word_list = []
        while True:
            
            choosen_words = choose_word(extracted_words, name_dic) # 2번 완성
            if not choosen_words:
                quit_or_not = input('더이상 만들 수 있는 단어가 없습니다. 선택하십시오 - 1) 다른 이름으로 반복하기 2) 그만두기 ')
                if quit_or_not == '1':
                    break
                elif quit_or_not == '2':
                    sys.exit()
            print(f'남은 단어 : {choosen_words}')
            # 3번. user_input이 choosen_words 안에 있는 값인지 판별
            user_word = check_input(choosen_words)
            if user_word == 'quit':
                sys.exit()
            # user가 고른 word를 name_dic에서 차감시킴
            delete_word(user_word, name_dic)
            # 4번. user가 고른 word 연결한 구문과 남은 단어 출력
            user_word_list.append(user_word)
            print(f'선택 단어: {" ".join(user_word_list)}')
            # 5번.
            

def choose_word(extracted_words, name_dic):
    result = []
    for word in extracted_words:
        alpha_count = 0
        for alpha in word:
            if alpha in name_dic.keys() and word.count(alpha) <= name_dic.get(alpha):
                alpha_count += 1
        if alpha_count == len(word):
            result.append(word)
    extracted_words = result
    return extracted_words

def check_input(word_list):
    while True:
        user_word = input('현재 단어 중 하나를 선택하세요: ')
        if user_word == "quit" or user_word in word_list:
            return user_word
        elif user_word not in word_list:
            print('잘못된 입력 값입니다. 다시 입력하세요.')
            continue
                
def delete_word(user_word, name_dic):
    for alpha in user_word:
        name_dic[alpha] = name_dic.get(alpha) - 1



name_to_phrase()

