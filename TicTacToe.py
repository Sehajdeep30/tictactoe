def isAP(a,b,c):
    [x,y,z] = sorted([a,b,c])
    return 2*y == x+z

def turn(n):
    el = ''
    if n%2 == 0:
        el = 'O'
    else:
        el = 'X'
    return el

def isWinner(list,n):
    sub_list = []
    el = turn(n)
    
    for i in list:
        if i[0] == el:
            sub_list += [i[1]]
            

    for a in sub_list:
        
        for b in sub_list:
        
            for c in sub_list:
                
                if a != b !=c:
                
                    if isAP(a,b,c):
                        return(True)
                        break
            
            else:
                continue
            break
        
        else:
            continue
        break

#MainLoop

Gamescreen = '---\n---\n---'
rfrnc_tile = '\n123\n456\n789'
n = 0
rfrnc_keys = {1:11,2:12,3:13,4:21,5:22,6:23,7:31,8:32,9:33}
location = {1:0,2:1,3:2,4:4,5:5,6:6,7:8,8:9,9:10}
list = []
charlist = []

print('WELCOME TO THE GAME OF TIC-TAC-TOE')

while True:
    
    Gamescreen = '---\n---\n---'
    rfrnc_tile = '\n123\n456\n789'
    n = 0
    rfrnc_keys = {1:11,2:12,3:13,4:21,5:22,6:23,7:31,8:32,9:33}
    location = {1:0,2:1,3:2,4:4,5:5,6:6,7:8,8:9,9:10}
    list = []
    charlist = []


    while n < 9:

        print('\nFILL IN THE TILES WITH RESPONSES FROM 1 TO 9:-\n',
Gamescreen,'\nUSING THE GIVEN KEY AS A REFERENCE\n',rfrnc_tile,'\n',sep = '')
        char = input('Enter Your Desired Character: ')

        if char in charlist:
            print('\nTHE TILE IS ALREADY FILLED')
            continue

        n += 1
        charlist += [char]
        el = turn(n)
        key = rfrnc_keys[int(char)]
        list += [[el,key]]
        num = location[int(char)]
        Gamescreen = Gamescreen[:num] + el + Gamescreen[num+1:]
        
        if n > 4:
            if isWinner(list,n):
                print(el+' IS THE WINNER\n',Gamescreen,sep = '')
                break
    
    else:
        print('\nTHE GAME HAS ENDED IN A DRAW')

    choice = input('\nDO YOU WANT TO CONTINUE PLAYING?\n1-ALWAYS DOWN FOR MORE:)\n2-NAH,MAYBE LATER\n>')
    if choice == '1':
        continue
    
    else:
        break        



    

