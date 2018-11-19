#range

range(5)        #[0,1,2,3,4]
range(1,4)      #[1,2,3]
range(1,10,3)   #[1,4,7]
range(10,1,-4)  #[10,6,2]

#通常用在需要重複印出的時候
for i in range(5):
    print ("Hello")

import random
#隨機產生亂數10次
#抽獎活動
r_list = []
for i in range(6):
    r = random.randint(1,49)
    r_list.append(r)
    print ("第", i + 1, "組中獎號碼是:", r)
print ("本次中獎號碼依序為:", r_list)

