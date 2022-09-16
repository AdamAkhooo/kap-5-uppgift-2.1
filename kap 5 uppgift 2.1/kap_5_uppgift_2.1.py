
pris=int(input("Bensinpris (kr/liter)"))

if pris < 10:
    print('det var billigt')

elif pris > 10 and pris < 15:
    print('Tanka full tank')

elif pris > 15 and pris <  20:
    print('Tanka 10 liter')

elif pris > 20:
    print('Nu saljer jag bilen och cyklar istallet') # 
