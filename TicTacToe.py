
# coding: utf-8

# In[1]:


t7 = [7]
t8 = [8]
t9 = [9]
t4 = [4]
t5 = [5]
t6 = [6]
t1 = [1]
t2 = [2]
t3 = [3]


# In[2]:


t71 = [7]
t81 = [8]
t91 = [9]
t41 = [4]
t51 = [5]
t61 = [6]
t11 = [1]
t21 = [2]
t31 = [3]


# In[3]:


global posi
posi = [1,2,3,4,5,6,7,8,9]


# In[4]:


global posi1
posi1 = []


# In[5]:


def display():
    global t7
    global t8
    global t9
    global t4
    global t5
    global t6
    global t1
    global t2
    global t3
    print("| {}".format(t7[0]) + " | {}".format(t8[0]) + " | {}".format(t9[0]) + " |")
    print("| {}".format(t4[0]) + " | {}".format(t5[0]) + " | {}".format(t6[0]) + " |")
    print("| {}".format(t1[0]) + " | {}".format(t2[0]) + " | {}".format(t3[0]) + " |")


# In[6]:


def check_true():
    global t7
    global t8
    global t9
    global t4
    global t5
    global t6
    global t1
    global t2
    global t3
    global t71
    global t81
    global t91
    global t41
    global t51
    global t61
    global t11
    global t21
    global t31
    global posi
    global posi1
    if(t7==t8==t9):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range(0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t4==t5==t6):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range(0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t1==t2==t3):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range(0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t7==t4==t1):
        print("You have won")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range (0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t8==t5==t2):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range (0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t9==t6==t3):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range (0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t7==t5==t3):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range(0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass
    if(t9==t5==t1):
        print("You have won!")
        playagain = input("Do you wish to play again? Y or N")
        if playagain == 'Y':
            t7.pop()
            t7.append(t71[0])
            t8.pop()
            t8.append(t81[0])
            t9.pop()
            t9.append(t91[0])
            t4.pop()
            t4.append(t41[0])
            t5.pop()
            t5.append(t51[0])
            t6.pop()
            t6.append(t61[0])
            t1.pop()
            t1.append(t11[0])
            t2.pop()
            t2.append(t21[0])
            t3.pop()
            t3.append(t31[0])
            for i in range(0,len(posi1)):
                posi.append(posi1[i])
            ask()
        else:
            pass


# In[7]:


def ask():
    global t7
    global t8
    global t9
    global t4
    global t5
    global t6
    global t1
    global t2
    global t3
    global t71
    global t81
    global t91
    global t41
    global t51
    global t61
    global t11
    global t21
    global t31
    global posi
    global pos
    global mylist
    player1 = input("Please select either 'X' or 'O' : ")
    print('Player 1 has selected {}'.format(player1))
    mylist = []
    if player1 == 'X':
        mylist.append('X')
        mylist.append('O')
    elif player1 == 'O':
        mylist.append('O')
        mylist.append('X')
    display()
    for i in range(1,11):
        if i%2 != 0:
            pos = input("Where do you wish to insert your symbol?")
            if int(pos) in posi:
                calling1()
                continue
            if int(pos) not in posi:
                print("This position is occupied")
                receiving1()
                continue
        if (i%2 == 0 and i != 10):
            pos = input("Where do you wish to insert your symbol?")
            if int(pos) in posi:
                calling2()
                continue
            if int(pos) not in posi:
                print("This position is occupied")
                receiving2()
                continue


# In[8]:


def calling1():
    global t7
    global t8
    global t9
    global t4
    global t5
    global t6
    global t1
    global t2
    global t3
    global pos
    global mylist
    global posi
    if pos == '7':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t7.pop()
        t7.append(mylist[0])
        display()
        check_true()
    if pos == '8':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t8.pop()
        t8.append(mylist[0])
        display()
        check_true()
    if pos == '9':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t9.pop()
        t9.append(mylist[0])
        display()
        check_true()
    if pos == '4':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t4.pop()
        t4.append(mylist[0])
        display()
        check_true()
    if pos == '5':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t5.pop()
        t5.append(mylist[0])
        display()
        check_true()
    if pos == '6':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t6.pop()
        t6.append(mylist[0])
        display()
        check_true()
    if pos == '1':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t1.pop()
        t1.append(mylist[0])
        display()
        check_true()
    if pos == '2':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t2.pop()
        t2.append(mylist[0])
        display()
        check_true()
    if pos == '3':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t3.pop()
        t3.append(mylist[0])
        display()
        check_true()


# In[9]:


def calling2():
    global pos
    global t7
    global t8
    global t9
    global t4
    global t5
    global t6
    global t1
    global t2
    global t3
    global mylist
    global posi1
    if pos == '7':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t7.pop()
        t7.append(mylist[1])
        display()
        check_true()
    if pos == '8':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t8.pop()
        t8.append(mylist[1])
        display()
        check_true()
    if pos == '9':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t9.pop()
        t9.append(mylist[1])
        display()
        check_true()
    if pos == '4':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t4.pop()
        t4.append(mylist[1])
        display()
        check_true()
    if pos == '5':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t5.pop()
        t5.append(mylist[1])
        display()
        check_true()
    if pos == '6':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t6.pop()
        t6.append(mylist[1])
        display()
        check_true()
    if pos == '1':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t1.pop()
        t1.append(mylist[1])
        display()
        check_true()
    if pos == '2':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t2.pop()
        t2.append(mylist[1])
        display()
        check_true()
    if pos == '3':
        posi.remove(int(pos))
        posi1.append(int(pos))
        t3.pop()
        t3.append(mylist[1])
        display()
        check_true()


# In[10]:


def receiving1():
    global pos
    global posi
    while True:
        pos = input("Next position please")
        if int(pos) not in posi:
            print("Wrong again")
            continue
        else:
            calling1()
            break
    return


# In[12]:


def receiving2():
    global pos
    global posi
    while True:
        pos = input("Next position please")
        if int(pos) not in posi:
            print("Wrong again")
            continue
        else:
            calling2()
            break
    return


# In[ ]:


ask()


# In[ ]:


ask()

