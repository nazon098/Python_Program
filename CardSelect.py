import random
class SameCardError(Exception):
  pass
Att=1
Ice_Cream=0
print("1에서 10까지의 무작위 숫자를 찍어서 맞춰 보세요!")
print("맞추면 아이스크림 사줌")
ID=input("먼저 이름을 입력하세요: ")
if ID == "":
  ID="(공백)"
if ID.lower() == 'nazon':
 print(f"환영합니다 {ID} 님!")
else:
 print(f'환영합니다 {ID} 님')
while True:
 while True:
  try:
   SelectedCard = int(input("숫자를 선택하세요."))
   if SelectedCard>=1 and SelectedCard<=10:
     break
   else:
     print("1~10사이의 숫자를 입력하세요")
  except ValueError:
     print("'숫자'를 입력하세요")
 RandCard = random.randint(1,10)
 if ID.lower()=="nazon":
   if random.randint(1,10)>=6:
     if Att > 2:
       RandCard=SelectedCard
 else:
   if Att == random.randint(60,100):
       RandCard = SelectedCard
   while RandCard==SelectedCard:
     try:
       RandCard=random.randint(1,10)
       if RandCard==SelectedCard:
         raise SameCardError
     except SameCardError:
       continue
 print(f'내가고른카드:{SelectedCard}')
 print(f'무작위의 카드:{RandCard}')
 if RandCard!=SelectedCard:
   print('안타깝네요!')
 else:
   print('아이스크림 당첨!!')
   Ice_Cream+=1
 response=input('다시 할까요? ')
 if response == '네' or response=='예' or response == "":
   Att += 1
   continue
 else:
   print(f"{ID} 님의 기록")
   print(f'총 시도:{Att}')
   print(f'얻은 아이스크림:{Ice_Cream}')
   break