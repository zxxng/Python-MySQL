# 클래스란? 타입을 만들어내는 도구
# int, float, str과 같이 새로운 타입을 만들 수 있다.

# 251 클래스, 객체, 인스턴스에 대해 설명해보자
# 1. 클래스는 속성을 정의한 것
# 2. 객체는 클레스로 정의된 것 ?
# 3. 인트턴스는 클래스로 생성된 것

# 252 ~ 258
from tkinter.tix import Balloon
from tokenize import blank_re


class Human:
    def __init__(self, name, age, sex):
     #   print("응애응애")
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: %s, 나이: %d, 성별: %s" % (ujaeng.name, ujaeng.age, ujaeng.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex



ujaeng = Human("don't know", 0, "don't know")
# print("이름: %s, 나이: %d, 성별: %s" % (ujaeng.name, ujaeng.age, ujaeng.sex))

ujaeng.who()
ujaeng.setInfo("jaeyyoo", 25, "women")

del(ujaeng)


class OMG:
    def print(self):
        print("Oh my god")

mystock = OMG()
mystock.print()
#OMG.print(mystock)


class Stock:
    def __init__(self, name, code, per, pbr, receive):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.receive = receive

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
    
    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr
    
    def set_receive(self, receive):
        self.receive = receive
    
    
# samsung = Stock("삼성전자", "005930")
# print(samsung.name)
# print(samsung.code)
# print(samsung.get_name())
# print(samsung.get_code())

ssm = Stock("삼성전자","005930", 15.79, 1.33, 2.83)
print(ssm.receive)

ssm.set_per(12.75)
print(ssm.per)

삼성 = Stock("삼성전지", "005930", 15.79, 1.33, 2.83)
현대 = Stock("현대차", "005380", 8.07, 0.35, 4.27)
LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stockList = []
stockList.append(삼성)
stockList.append(현대)
stockList.append(LG)

for i in stockList:
    print(i.code, i.per) # i -> Stock 클래스의 객체를 바인딩 함


# 271 Account class
import random

class Account:
    count = 0
    def __init__(self, name, balance):
        self.deposit_count=0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

        Account.count += 1

    @classmethod
    def get_account_num(cls):
        print("생성된 계좌 수 : %d" % Account.count)

    def deposit(self, money):
        if money >= 1:
            self.deposit_log.append(money)
            self.balance += money
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance += (self.balance * 0.01)

    def withdraw(self, money):
        if money <= self.balance:
            self.withdraw_log.append(money)
            self.balance -= money 
    
    def display_info(self):
        print("은행이름 : %s" % self.bank)
        print("예금주 : %s" % self.name)
        print("계좌번호 : %s" % self.number)
        print("잔고 : %d원" % self.balance)

    def withdraw_history(self):
        for money in self.withdraw_log:
            print(money)
    
    def deposit_history(self):
        for money in self.deposit_log:
            print(money)

p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)


jaeyyoo = Account("jaeyyoo", 100000000)
hanbkim = Account("hanbkim", 100000000)
jikang2 = Account("jikang", 100000)
yejinam = Account("yejinam", 100000)

accountList = []
accountList.append(jaeyyoo)
accountList.append(hanbkim)
accountList.append(jikang2)
accountList.append(yejinam)

for i in accountList:
    if i.balance >= 1000000:
        i.display_info()

jaeyyoo.withdraw(10000)
jaeyyoo.withdraw(10000)
jaeyyoo.withdraw_history()


# 281 car class

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
    def 정보(self):
        print("바퀴수 %d\n가격 %d" % (self.바퀴, self.가격))

# car = 차(2, 100)
# print("%s %s" % (car.바퀴, car.가격))

# 282 class  상속
class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 %d\n가격 %d" % (self.바퀴, self.가격))

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        #차.__init__(self, 바퀴, 가격)
        self.구동계 = 구동계

    def 정보(self):
        super().정보()
        print("구동계 %s" % self.구동계)

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

    def 정보(self):
        print("바퀴수 %d\n가격 %d" % (self.바퀴, self.가격))

car = 자동차(4, 100)
car.정보()

# 메서드 오버라이딩
class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")

나 = 자식()
나.호출()

print("\n")
# 생성자
class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")

나 = 자식()

print("\n")
# 부모클래스 생성자 호출
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

print("\n")
# 부모클래스 생성자 호출
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()