import random
class SameCardError(Exception):
  pass
Att=1
Won=0
print("Select Random number  Cards between 1 and 10")
ID=input("First,enter your name: ")
if ID == "":
  ID="(Blank)"
if ID.lower() == 'nazon':
 print(f"Welcome {ID}!")
else:
 print(f'Welcome {ID}')
while True:
 while True:
  try:
   SelectedCard = int(input("Choose number."))
   if SelectedCard>=1 and SelectedCard<=10:
     break
   else:
     print("Enter number between 1 and 10")
  except ValueError:
     print("Enter 'Number'")
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
 print(f'Selected Card:{SelectedCard}')
 print(f'Random Card:{RandCard}')
 if RandCard!=SelectedCard:
   print('That's bad!')
 else:
   print('You won!!')
   Won+=1
 response=input('Try again? ')
 if response.lower() == 'yes' or response.lower()=='ye' or response.lower() == "" or response.lower() == 'y:
   Att += 1
   continue
 else:
   print(f"{ID}'s Information")
   print(f'Total Attempts:{Att}')
   print(f'You won:{Won}')
   break