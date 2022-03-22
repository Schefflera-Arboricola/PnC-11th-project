'''NAME : ADITI JUNEJA
CLASS : XI A
ROLL NO. : 04
PROJECT : Calculate the number of and show all permutations or combinations of a given string with some common conditions'''

from itertools import permutations,combinations

def remove(lt):         #to remove repeating permutations
    d=[]
    for i in lt:
        for j in lt:
            if i==j:
                z= lt[lt.index(j)]
                d+=[z]
    for i in d:
        c=lt.count(i)
        while c!=1:
            del lt[lt.index(i)]
            c=lt.count(i)
    l=[]
    for k in (lt):
        r=""
        for j in k:
            r+=str(j)
        l+=[r]
    
    return l    
def comremove(lt):                #to remove repeating combinations
    d=[]
    for i in lt:
        i1=list(i)
        i1.sort()
        d+=[i1]
    l=remove(d)
    return (l)

def per_fix_let(lt,ph):         #Permutations with some letters fixed
    d=[]
    for i in lt:
        if ph not in i:
            d+=[i]
    for j in d:
        if j in lt:
            del lt[lt.index(j)]
    return lt
def notogether(l,ph):           #Permutations without some specific letters 
    d=[]
    for i in l:
        if ph in i:
            d+=[i]
    for k in d:
        if k in l:
            del l[l.index(k)]
    return l
def fix_pos(l,e,u):            #Permutations with some letters at fixed positions
    d=[]
    for i in e:
        for j in l:
            if j[e[i]]!=u[i]:
                d+=[j]
    for k in d:
        if k in l:
            del l[l.index(k)]
    return l

def com_fix_let(lt,ph):          #Combinations with some letters fixed
    p=list(ph)
    d=[]
    d2=[]
    for i in lt:
        i1=list(i)
        d+=[i1]
    for k in d:
        m=0
        d1=[]
        for k1 in k:
            if k1 in p and k1 not in d1:
                m+=1
                d1+=[k1]
        if m<len(p):
            d2+=[k]
    for t in d2:
        if t in d:
            del d[d.index(t)]
    lt=[]
    for h in d:
        r=''
        for h1 in h:
            r+=h1
        lt+=[r] 
    return lt
def com_ab(l,ph):            #Combinations without some specific letters
    d=[]
    d1=[]
    d2=[]
    for i in l:
        i1=list(i)
        d+=[i1]
    for k in d:
        for k1 in ph:
            if k1 in k:
                d1+=[k]
    for l1 in d1:
        if l1 in d:
            del d[d.index(l1)]
    for f in d:
        r=''
        for f1 in f:
            r+=f1
        d2+=[r]
    return d2
e1=str(input("Enter the word : "))                                    #STRING
pc=int(input("\nDo you want to work with (1)Combinations OR (2)Permutations? "))
if pc==1:                                                                   #COMBINATION
    f2=int(input("Enter how many words taken at a time for Combination : "))
    c=int(input("\nDo you want to work with (1)Simple Combinations OR (2)Complex Combinations? "))
    c1=list(combinations(e1,f2))
    if c==2:                                                    #Complex Combinations
        op=int(input("\nDo you want to\n(1)some fixed letter(s) present\n(2)some fixed letter(s) absent\n(3)BOTH ? "))
        if op==1:                                               #some fixed letter(s) present
            ph1=str(input("Enter letters (in continuity) : "))
            print("\nCombinations:")
            j=comremove(lt=c1)
            j1=com_fix_let(lt=j,ph=ph1)
            print(j1)
            print("\nNo of Combinations:",len(j1))
        elif op==2:                                             #some fixed letter(s) absent
            ph1=str(input("\nEnter letters (in continuity) : "))
            print("\nCombinations:")
            j=comremove(lt=c1)
            j1=com_ab(l=j,ph=ph1)
            print(j1)
            print("\nNo of Combinations:",len(j1))
        elif op==3:                                             #BOTH
            ph1=str(input("\nEnter letters (in continuity for (1)) : "))
            j=comremove(lt=c1)
            j1=com_fix_let(lt=j,ph=ph1)
            ph1=str(input("\nEnter letters (in continuity for (2)) : "))
            print("\nCombinations:")
            j2=com_ab(l=j1,ph=ph1)
            print(j2)
            print("\nNo of Combinations:",len(j2))
        else:                                                     #SIMPLE COMBINATION
            print("\nCombinations:")
            j=comremove(lt=c1)
            print(j)
            print("\nNo of Combinations:",len(j))
    else:
            print("\nCombinations:")
            j=comremove(lt=c1)
            print(j)
            print("\nNo of Combinations:",len(j))
else:                                                                   #PERMUTATIONS
    f1=int(input("Enter how many words taken at a time for Permutation : "))
    p=int(input("\nDo you want to work with (1)Simple Permutations OR (2)Complex Permutations? "))
    p1=list(permutations(e1,f1))
    j=remove(lt=p1)
    if p==2:                                                            #Complex Permutations
        op=(input("\nDo you want to :\n(1) have a fixed letter(s)\n(2) not have a fixed letter(s)\n(3) have fixed position(s) of fixed letter(s)\n(enter indices in continuity(without space,in qoutation marks) "))
        for t in op:
            t=int(t)
            if t==1:                        #have a fixed letter(s)
                h=input("\nEnter the letter(s) you want to keep fixed: ")
                j= per_fix_let(lt=j,ph=h)
            elif t==2:                         #not have a fixed letter(s)
                h=input("\nEnter the letter(s) you don\'t want to keep : ")
                j= notogether(l=j,ph=h)
            elif t==3:                          #have fixed position(s) of fixed letter(s)
                e3={}
                print("\nEnter 0 to stop")
                x=int(input("\nEnter the letter\'s current position: "))
                while x!=0:
                    y=int(input("\nEnter the letter\'s position wanted in permutation: "))
                    e3[x-1]=y-1
                    x=int(input("\nEnter the letter\'s current position: "))
                j=fix_pos(l=j,e=e3,u=e1)    
        print("\nPermutations:")
        print(j)
        print("\nNo of Permutations:",len(j))
    else:                                    #Simple Permutations
        print("\nPermutations:")
        print(j)
        print("\nNo of Permutations:",len(j))

        
'''OUTPUTS

OUTPUT 1

Enter the word : 'PARALLEL'

Do you want to work with (1)Combinations OR (2)Permutations? 1
Enter how many words taken at a time for Combination : 4

Do you want to work with (1)Simple Combinations OR (2)Complex Combinations? 2

Do you want to
(1)some fixed letter(s) present
(2)some fixed letter(s) absent
(3)BOTH ? 3

Enter letters (in continuity for (1)) : 'LR'

Enter letters (in continuity for (2)) : 'PA'

Combinations:
['LLLR', 'ELLR']

No of Combinations: 2

========================================================================

OUTPUT 2

Enter the word : 'ARRANGE'

Do you want to work with (1)Combinations OR (2)Permutations? 2
Enter how many words taken at a time for Permutation : 3

Do you want to work with (1)Simple Permutations OR (2)Complex Permutations? 2

Do you want to :
(1) have a fixed letter(s)
(2) not have a fixed letter(s)
(3) have fixed position(s) of fixed letter(s)
(enter indices in continuity(without space,in qoutation marks) '231'

Enter the letter(s) you don't want to keep : 'A'

Enter 0 to stop

Enter the letter's current position: 6

Enter the letter's position wanted in permutation: 2

Enter the letter's current position: 0

Enter the letter(s) you want to keep fixed: ''

Permutations:
['RGR', 'RGN', 'RGE', 'NGR', 'NGE', 'EGR', 'EGN']

No of Permutations: 7

========================================================================

OUTPUTS 3

Enter the word : 'ALLAHABAD'

Do you want to work with (1)Combinations OR (2)Permutations? 2
Enter how many words taken at a time for Permutation : 4

Do you want to work with (1)Simple Permutations OR (2)Complex Permutations? 2

Do you want to :
(1) have a fixed letter(s)
(2) not have a fixed letter(s)
(3) have fixed position(s) of fixed letter(s)
(enter indices in continuity(without space,in qoutation marks) '231'

Enter the letter(s) you don't want to keep : 'LH'

Enter 0 to stop

Enter the letter's current position: 7

Enter the letter's position wanted in permutation: 1

Enter the letter's current position: 9

Enter the letter's position wanted in permutation: 4

Enter the letter's current position: 0

Enter the letter(s) you want to keep fixed: ''

Permutations:
['BLLD', 'BLAD', 'BHLD', 'BHAD', 'BALD', 'BAHD', 'BAAD']

No of Permutations: 7

========================================================================

OUTPUT 4

Enter the word : 'UMBRELLA'

Do you want to work with (1)Combinations OR (2)Permutations? 1
Enter how many words taken at a time for Combination : 4

Do you want to work with (1)Simple Combinations OR (2)Complex Combinations? 2

Do you want to
(1)some fixed letter(s) present
(2)some fixed letter(s) absent
(3)BOTH ? 3

Enter letters (in continuity for (1)) : ''

Enter letters (in continuity for (2)) : 'UEA'

Combinations:
['BLMR', 'BLLM', 'LLMR', 'BLLR']

No of Combinations: 4

========================================================================

'''
