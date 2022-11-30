import sys

print("""Welcome... 
X brand computer   : 15000 TL 
Y brand computer   : 18500 TL 
Z brand computer   : 25400 TL 
------------------------------ 
Gaming RAM         : 1500  TL 
------------------------------ 
Sound System       : 957 TL \n """)

brand = input('Whıch brand do you prefer? "X", "Y" veya "Z"').upper()

total_price = 0
if (brand == ' '):
    print("You entered incorrectly.")
elif (brand == 'X'):
    total_price += 15000
elif (brand == 'Y'):
    total_price += 18500
elif (brand == 'Z'):
    total_price += 25400
else:
    print("You entered incorrectly.")
    sys.exit(0)

Gaming_RAM = input('Do you want Gaming RAM? "yes" or "no"').lower()
if Gaming_RAM == "yes":
    total_price += 1500
else:
    total_price += 0

sound_system = input('Do you want Sound System ? "yes" or "no"').lower()
if sound_system == "yes":
    total_price += 957
else:
    total_price += 0
print(f"Your total order amounts: {total_price} TL.")