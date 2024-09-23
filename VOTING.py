BJP,INC,SWP,BSP=int(),int(),int(),int()
while True:
    name=input("PROVIDE YOUR NAME : ")
    age=int(input("PROVIDE YOUR AGE : "))
    if (age>=18):
        print("\nELIGIBLE...\n")
        print("******** VOTING LIST**\n1. BHARTIYA JANTA PARTY(BJP)\n2. INDIAN NATIONAL CONGRESS(INC)\n3. SAMAJWADI PARTY(SWP)\n4. BHAUJAN SAMAJ PARTY(BSP)\n")
        print("#",end='')
        choice=int(input("ENTER SERIAL NUMBER OF YOUR DESIRED PARTY FOR VOTE : "))
        if(choice==1):
            BJP+=1
        elif (choice==2):
            INC+=1
        elif (choice==3):
            SWP+=1
        elif (choice==4):
            BSP+=1
        else:
            print("invalid")
            continue
    else:
        print("NOT ELIGIBLE...")
    b =input("ENTER end FOR END VOTING\n**PRESS ENETR TO CONTINUE\nENTER- ")
    if b == "end":
        print("TOTAL VOTES- ","\n1.BJP--",BJP,"\n2.INC--",INC,"\n3.SWP",SWP,"\n4.BSP",BSP,"\n")
        if BJP>INC and BJP>SWP and BJP>BSP:
            print("WINNER IS BJP*")
        elif INC>BJP and INC>SWP and INC>BSP:
            print("WINNER IS INC*")
        elif SWP>INC and SWP>BJP and SWP>BSP:
            print("WINNER IS SWP")
        elif BSP>INC and BSP>SWP and BSP>BJP:
            print("WINNER IS BSP")
        else:
            print("ELECTION ARE TIED , RE-ELECTION")
        break
    else:
        continue
