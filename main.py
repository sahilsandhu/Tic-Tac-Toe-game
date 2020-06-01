
def condition(array,num1):
    if array[1]==array[2]==array[3]==num1 or array[4]==array[5]==array[6]==num1 or  array[1]==array[4]==array[7]==num1 or array[2]==array[5]==array[8]==num1 or array[3]==array[6]==array[9]==num1 or array[1]==array[5]==array[7]==num1 or array[3]==array[5]==array[7]==num1:
        print('player is winner ')
        return False
    else:
        
        return True
        
def show(array):
    print('the array after update is')
    print(array[1]+'|'+array[2]+'|'+array[3]+'|')
    print(array[4]+'|'+array[5]+'|'+array[6]+'|')
    print(array[7]+'|'+array[8]+'|'+array[9]+'|')
    
    
def position(num1,array):
    pos=int(input('enter the position '))
    for i in range(len(array)):
        array[pos]=num1
        
def who_start_game():
    import random
    a=random.randint(0,1)
    return a
    
def enter():
    print("lemme tell,whether the player 1 will chosse O or X ")
    entx=input('enter your choice')
    if entx=='X':
        print('player 2 will play with O')
        return ("X","O")
    else:
        print('player 2 will play with X')
        return ('O','X')
        
    
print('welcome to the tic tac toe game')
array=[' ']*10
num= True
while num:
    j=0
    num1,num2=enter()
    print('lemme check who will start the game')
    a=who_start_game()
    if a==1:
        print('player one will start the game')
    else:
        print("player 2 will start the game")
    bata=input('are you ready to play')
    if bata=='y':
        taf= True
        for j in range(len(array)):
        
         if taf==True:
           if j%2==0:
             
             position(num1,array)
             show(array)
             taf=condition(array,num1)
            
           else:
             position(num2,array)
             show(array)
             taf=condition(array,num1)
          
        break
    if taf==False:
        num= False