#모듈
# import theatre_module
# theatre_module.price(3) #명이서 영화 보러 갔을 때 가격
# theatre_module.price_morning(4)
# theatre_module.price_soldier(5)

# import theatre_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theatre_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theatre_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7) error남

# from theatre_module import price_soldier as price
# price(5)

#패키지 (모듈의 집합)
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#__all__
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))