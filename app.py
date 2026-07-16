main_money = 0
store = int(input("จำนวนร้านที่ต้องไปเก็บ : "))

for i in range(store) :
    money = int(input("จำนวนเงินที่ต้องเก็บ  : "))
    main_money += money
print(f"เก็บได้ {store} ร้าน ได้เงินมาทั้งหมด {main_money} บาท ได้คนละ {peplo} บาท")