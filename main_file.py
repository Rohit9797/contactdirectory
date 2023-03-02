'''
Main file
=========
'''
#===========function For Use====================

def validate_mob(x):
    if x.isdigit() and len(x)==10:
        return 1
    else:
        return 0

###############2
    
def create_contact():
        fp=open('data.txt','a')
        n=input("Enter Name:")
        mn=input("Enter Mobile Number:")
        res=validate_mob(mn)#validation
        #print(res)
        if res==1:
            a,b=searchmob(mn)
            if b==1:
                print("Number Already Exist")
            else:    
                d=n+":"+mn+"\n"
                fp.write(d)
                fp.close()
                print("Contact Created Successfully!!")
        else:
            print("Please Enter Valid mobile number")


    
############3
            
def display():
    fp=open('data.txt','r')
    d=fp.read()
    print("======Contact Directory========")
    print()
    print(d)
    print("========")

####################
def searchname():
        print("Search Contact Number By Name:")
        ns=input("Enter Name")
        fp=open('data.txt','r')
        data=fp.readlines()
        #print(data)
        flag=0
        for x in data:
           # print(x)
            l=x.split(":")
           # print(l)
           # print(l[0])
            if ns.upper()==l[0].upper():
               print(x)
               flag=1
        if flag==0:
            print("Contact Not Found")
    
        fp.close()

###############
def searchmob(n):
        fp=open('data.txt','r')
        data=fp.readlines()
        for x in data:
            l=x.split(":")
            if int(n)==int(l[1]):
                #print("Contact Found")
                #print(x)

                return x,1
        else:
               return '',0


    
print("Welcome to Contact Console Application")

while True:
    print()
    print("1.Create Contact")
    print("2.View Contact")
    print("3.Search By Name")
    print("4.Search By Mobile Number")
    print("5.Exit")
    ch=int(input("Enter Your Choice:"))

    if ch==1:
        create_contact()#function is used for reduce code
        pass
    
    elif ch==2:
        display()
        pass
    
    elif ch==3:
        searchname()
        
        pass

    elif ch==4:
        ms=input("Enter Mobile Number To be Search:")
        a,b=searchmob(ms)
        #print(a)
        #print(b)
        if b==1:
            print("Contact Found")
            print(a)
        else:
            print("Not Found")
    
    
    elif ch==5:
        break
    else:
        print("Please Enter Valid Option!!!")


print("Thank You For Using Application")

    
