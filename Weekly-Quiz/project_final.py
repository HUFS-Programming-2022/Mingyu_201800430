"""추상클래스를 위한 추상메소드 모듈, 데이터클래스 모듈, random 모듈 임포트."""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import random

class StoreGuideline(metaclass=ABCMeta):
    """
    편의점 클래스의 추상 클래스.

    각 함수에 대한 내용은 의사코드 참조
    """

    @abstractmethod
    def add_customer(cls, new_customer):
        """고객 명단에 새 고객을 추가하는 메소드."""
        pass

    @abstractmethod
    def add_stock(self, *args):
        """재고 목록에 새 제품을 추가하는 메소드."""
        pass

    @abstractmethod
    def update_stock(self, **kargs):
        """고객이 구매한 뒤 빠져나간 재고를 최신화하는 메소드."""
        pass

    @abstractmethod
    def calc_basket(self, **kargs):
        """고객의 장바구니에 담긴 제품들 가격을 계산하는 메소드."""
        pass

# -------------Store abstract class--------------

class PersonGuideline(metaclass=ABCMeta):
    """
    사람 클래스의 추상 클래스.

    각 함수에 대한 내용은 의사코드 참조
    """

    @abstractmethod
    def choose_item(self, store, *args):
        """편의점에서 물건을 장바구니에 담는 메소드."""
        pass

    @abstractmethod
    def buy_product(self, store, point = False):
        """장바구니에 담은 물품들을 구매하는 과정을 담은 메소드."""
        pass

# -------------Person abstract class--------------

@dataclass
class Product:
    """
    데이터 클래스로 정의한 상품 클래스.

    상품명과 가격을 받음.
    """

    name: str
    price: int

class MyException(Exception):
    """사용자 예외 처리 클래스."""

    pass

class Store(StoreGuideline):
    """
    추상클래스를 부모로 받는 편의점 클래스.

    각 함수에 대한 내용은 의사코드 참조
    """

    customers = {}
    mandatory_stock = [Product('water', 500),\
      Product('ramen', 1000), Product('coffee', 800)]
    discount_dict = {}
    asset = [0]
    lottery_list = []

    def __init__(self, store_name, stocks = []):
        """
        편의점 초기화 함수.

        입력값 : 편의점 이름, 추가하고자 하는 재고 목록
        결과 : 공통 발주 제품 목록과 사용자가 입력한 추가 제품 목록을 {제품명 : [가격, 개수]} 형태로 초기화시킴.
        """
        self.store_name = store_name
        stocks += Store.mandatory_stock
        self.stock_dict = \
          {product.name: [product.price, 10] for product in stocks}

    def check_asset(self):
        """현재 편의점의 재산을 보여주는 메소드."""
        print(self.asset[0])

    def add_stock(self, *args):
        """튜플 형태의 (상품객체, 수량) 가변매개변수를 인자로 받아 재고목록에 추가해주는 메소드."""
        for bundle in args:
            product, quantity = bundle[0], bundle[1]
            self.stock_dict[product.name] = [product.price, quantity]
            print(f'{product.name}을 각 {quantity}개만큼 재고에 추가하였습니다')
        print('현 시점 재고목록:', end= ' ')
        self.print_stock()

    def print_stock(self):
        """
        현재 편의점에 어떤 상품이 있는지 보여주는 메소드.

        재고가 0인 경우 노출되지 않게 함.
        """
        print([f'{name} : {self.stock_dict[name][1]}' \
          for name in self.stock_dict.keys() if self.stock_dict[name][1] > 0])

    @classmethod
    def add_customer(cls, new_customer):
        """
        새로운 고객을 명단에 추가하는 메소드.

        입력값 : Person 객체
        반환값 : 편의점 클래스 customers 딕셔너리에 고객 정보 추가
        추가설명 :
            추가하려는 고객이 편의점 고객명단에 존재하지 않을 경우
            최초 회원가입으로 판단하고 적립금을 500원으로 세팅해준다.
        """
        def first_join(cls, newbie):
            new_id = new_customer.phone_num[-4:]
            if new_id not in cls.customers.keys():
                cls.customers[new_id] = [newbie.name, 500]
                print(f'최초 가입 이벤트! {newbie.name}님 500점 적립되셨습니다.')
        return first_join(cls, new_customer)

    @classmethod
    def save_point(cls, num, total_buy):
        """
        고객의 상품 구매 과정에서 포인트를 적립해주는 메소드.

        입력값 : 고객ID, 총구매금액
        결과 : 고객ID에 저장된 포인트에 총구매금액의 10%만큼 포인트 추가
        """
        cls.customers[num][1] += int(total_buy//10)
        print(f'{cls.customers[num][0]}님의 새로 적립된 포인트: {total_buy//10} 점\
          \n총 가용 포인트: {cls.customers[num][1]}점')

    @classmethod
    def use_point(cls, num, total_buy):
        """
        고객의 상품 구매 과정에서 포인트를 사용하는 과정을 담은 메소드.

        입력값 : 고객ID, 총구매금액
        반환값 : 고객ID에 저장된 포인트 전액을 소모하여 총구매금액에서 포인트 전액이 차감된 가격을 반환.
        """
        while cls.customers[num][1] > 0:
            print(f'{cls.customers[num][0]} 님의 총 가용 포인트는 {cls.customers[num][1]} 점입니다')
            total_buy -= cls.customers[num][1]
            cls.customers[num][1] = 0
            print(f'포인트 전액을 사용하여 {total_buy}원 결제 도와드리겠습니다')
        return total_buy

    @classmethod
    def alter_sale(cls, product_name, rate):
        """
        세일 품목을 추가하거나 삭제시키는 메소드.

        입력값 : 제품명, 할인비율
        결과 :
            할인비율이 0이라면 그 제품을 할인 목록에서 삭제하는 것으로 판단
            그렇지 않다면 그 제품을 할인 목록에 추가하거나 원래의 할인비율을 입력값으로 수정.
        """
        if rate == 0:
            del cls.discount_dict[product_name]
        else:
            cls.discount_dict[product_name] = rate
            print(f'할인 이벤트 수정 완료 - 현재 할인품목: {cls.discount_dict}')

    def update_stock(self, **kargs):
        """
        고객 구매과정이 모두 종료된 뒤 재고목록을 최신화하는 함수.

        입력값 : 고객 장바구니 목록 - {상품명: 수량, 상품명: 수량, ...} 형태.
        결과 : 편의점 재고목록에서 고객 장바구니에 담긴 제품 개수만큼 차감.
              이 때 제품을 장바구니에 담는 메소드에서 재고량보다 넘치게 구매하지 못하도록 처리해놓아
              해당 메소드에서는 따로 처리과정을 밟지 않음.
        """
        for product, num in kargs.items():
            stock = self.stock_dict[product]
            stock[1] -= num

    def calc_basket(self, **kargs):
        """
        고객 구매과정에서 고객이 장바구니에 담은 제품들의 바코드를 찍는 메소드.

        입력값 : 고객 장바구니 목록 - {상품명: 수량, 상품명: 수량, ...} 형태.
        반환값 : 상품명에 해당하는 제품가격 * 수량을 모두 더한 총 구매금액
               만약 제품이 할인 제품이라면 할인된 가격으로 총 구매금액 계산.
        """
        total = 0
        def check_discount(**kargs):
            nonlocal total
            for product, num in kargs.items():
                price = self.stock_dict[product][0]
                if product in Store.discount_dict.keys():
                    discount_rate = Store.discount_dict[product]
                    print(f'{product}는 {discount_rate * 100}% 행사 상품입니다')
                    discounted_price = price * (1 - discount_rate)
                    total += discounted_price * num
                else:
                    total += price * num
            print(f'구매하시는 제품의 총 금액은 {total} 원입니다')
            return total
        return check_discount(**kargs)

    @classmethod
    def payback(cls, num, *args):
        """
        우유갑이나 공병을 들고오면 소액 적립해주는 이벤트 메소드.

        입력값 : 고객ID, ((공병, 개수), (우유갑, 개수)) 튜플
        결과 : 우유갑일 경우 개당 5원씩 적립, 공병일 경우 개당 10원씩 적립.
              만약 해당하지 않은 물건을 가져오면 경고 문구와 함께 예외처리되도록 함.
        """
        for bundle in args:
            reusable, quantity = bundle[0], bundle[1]
            if reusable == "milk_carton":
                cls.customers[num][1] += quantity * 5
                print(f'{cls.customers[num][0]}님, 포인트가 {quantity*5}만큼 적립되었습니다.\
                   총 포인트 : {cls.customers[num][1]}')
            elif reusable == "empty_bottle":
                cls.customers[num][1] += quantity * 10
                print(f'{cls.customers[num][0]}님, 포인트가 {quantity*10}만큼 적립되었습니다.\
                   총 포인트 : {cls.customers[num][1]}')
            else:
                raise MyException("그 물건은 페이백이 안 됩니다..")

    @classmethod
    def lottery(cls, entry_num):
        """
        고객이 구매를 마쳤을 때 자동으로 추첨이벤트에 응모되도록 하는 메소드.

        입력값 : 고객ID
        결과 : 응모 인원이 다 찼을 경우 응모자들 중 2명 랜덤으로 추출하여 100 포인트 추가 적립,
              이후 응모 리스트 초기화
        """
        cls.lottery_list.append(entry_num)
        print('현재 응모 상황 : ', cls.lottery_list)
        if len(cls.lottery_list) == 3:
            lotteries = random.sample(cls.lottery_list, 2)
            def printing(lst:list):
                for lottery in lst:
                    yield lottery
            for i in printing(lotteries):
                cls.customers[i][1] += 100
                print(f'당첨자 {cls.customers[i][0]}({i})님께 포인트가 100만큼 적립됩니다.\
                   총 포인트 {cls.customers[i][1]}')
            cls.lottery_list = []


class Person(PersonGuideline):
    """
    추상클래스를 부모로 하는 사람 클래스.

    이름, 전화번호를 초기 설정으로 받는다.
    보유금액은 기본적으로 1000 ~ 10000원 사이의 금액으로 설정되며 사용자가 기입할 수 있다.
    각 Person 클래스마다 개별 장바구니 변수를 설정해놓고 장바구니 카트에 아이템을 담을 수 있게 해놓았다.
    각 함수는 의사코드 참조.
    """

    def __init__(self, name, phone_num, money = (random.randrange(1, 10))*1000, basket = {}):
        """
        사람 객체 초기화 함수.

        입력값 : 사람 이름, 전화번호, 재산, 장바구니
        결과 : 해당 객체에 맞게 변수 초기화.
              재산의 경우 입력값이 없다면 1,000원에서 10,000원 사이의 랜덤한 값으로 설정
        """
        self.name = name
        self.phone_num = phone_num
        self.money = money
        self.basket = basket

    def check_money(self):
        """현재 잔고 확인 메소드."""
        print(f'나의 현재 통장 잔고: {self.money}원')

    def work(self, hour):
        """
        특정 시간 동안 노동하여 임금을 받는 메소드.

        입력값 : 시간
        결과 : 시급 10,000원 기준 시급 * 시간의 결과값이 해당 사람의 재산에 추가됨.
        """
        wage = lambda hour:10000 * hour
        self.money += wage(hour)
        print(f'{hour} 시간을 노동하여 돈을 {wage(hour)}원 벌었습니다.')
        self.check_money()

    def choose_item(self, store, *args):
        """
        편의점에서 물건을 장바구니에 담는 메소드.

        입력값 : 편의점 이름, (제품명, 개수)형식의 튜플*N개
        결과 : 제품명이 올바르고, 제품 개수가 재고량보다 크지 않을 때 장바구니에 추가되도록 함.
              이 때, 이미 장바구니에 있는 물건이라면 장바구니에 있는 물건 개수와 입력받은 개수의 합을 재고량과 비교하게 됨.
              편의점 자체를 잘못 기입했을 때의 예외처리는 잘 작동하지 않음(잘 모르겠음).
        """
        assert isinstance(store, Store), "편의점의 정확한 명칭을 입력하세요."
        self.basket = {}
        stock = store.stock_dict
        for bundle in args:
            product_name, number = bundle[0], bundle[1]
            assert product_name in stock.keys(), '구매하시려는 상품이 존재하지 않습니다. 다시 입력하세요.'
            assert number or number.isdigit(), '상품의 개수를 바르게 입력하세요.'
            assert number <= stock[product_name][1], '구매하려는 수량이 재고량보다 많습니다.'
            self.basket[product_name] = number
        print(f'{self.name}님의 장바구니 : {self.basket}')

    def buy_product(self, store, point = False):
        """
        장바구니에 담은 물품들을 구매하는 과정을 담은 메소드.

        입력값 : 편의점 이름, 포인트 사용 여부(boolean)
        결과 : 장바구니가 비었을 경우 메소드 종료
              그렇지 않을 경우:
                  1. 장바구니에 담긴 물품들 총 금액 계산
                  2. 총 금액의 10%를 포인트로 적립
                  3. 고객ID에 저장된 포인트 전액을 사용하여 총 계산금액 확정
                  4. 만약 고객의 잔고가 결제할 만큼의 금액이 아닐 경우 구매과정 종료
                     그렇지 않다면 정상적으로 계산
                  5. 구매가 완료되었을 경우 편의점 재고목록 최신화
        """
        customer_id = self.phone_num[-4:]
        basket = self.basket
        assert basket, '아무것도 구매를 원하지 않으시므로 종료합니다.'
        basket_total = store.calc_basket(**basket)
        # 포인트 적립
        store.save_point(customer_id, basket_total)
        # 포인트 사용
        if point:
            final_price = store.use_point(customer_id, basket_total)
        else: final_price = basket_total
        assert self.money >= final_price, '잔액이 부족합니다. 다시 주문해주세요.'
        print(f'{self.money} 원 받았습니다')
        self.money -= final_price
        print(f'{self.money} 원 거슬러 드렸습니다. 이용해 주셔서 감사합니다.')
        store.asset[0] += final_price
        store.update_stock(**basket)
        self.basket = {}


    def check_point(self, store):
        """
        자신의 포인트가 얼마나 적립됐는지 확인하는 메소드.

        입력값 : 편의점 지점.
        출력값 : 고객의 해당 편의점 포인트 현황 출력
        """
        store_id = self.phone_num[-4:]
        print(f'현재 {self.name}의 멤버십 포인트는 {store.customers[store_id][1]}점입니다.')
