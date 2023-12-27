class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

#드랍쉽
dropship = FlyableUnit() #Unit 생성자로 받음. flyableunit class의 아규먼트 순서를 바꾸면 flyable이 생성자가 됨.


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()

#Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

#총 3대의 매물이 있습니다.
#강남 아파트 매매 10억 2010년
#마포 오피스텔 전세 5억 2007년
#송파 빌라 월세 500/50 2000년

#[코드]
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
              , self.price, self.completion_year)
        
houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
