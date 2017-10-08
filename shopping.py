import sys
get_List={'iphone':7188,'bike':1200,'book':70,'foods':1000,'Telsa':200000}
salary=int(input("Please tell me the months'salary of you:"))
get_all=[]
get_end={}
count=0
print("++++++++++++++++++++")
for k,v in get_List.items():
    count+=v
    print k,v
print("++++++++++++++++++++")
while salary>0:
    get_pro=raw_input("What do you want?Please tell me :")
    if get_pro not in get_List.keys():
        print "Sorry,don't have %s!" %get_pro
    else:
        if get_List[get_pro]>salary:
            print "You don't have enough money to buy %s"%get_pro
            sys.exit()
        else:
            print "Thanks for your patronage! You haver got %s"% get_pro
            get_all.append(get_pro)
            salary=salary-get_List[get_pro]
        
        check_get=raw_input("Do you want anything else ? Please tell Yes or NO:")
        if check_get=="yes":    #check for Regx
            continue
        else:
            break

if get_all==[]:
    print "You haven't bought anything,loser!"
    sys.exit()
for l in get_all:
    get_end[l]=get_all.count(l)
print "You have got %s,and you just have %d RMB!"%(str(get_end),salary)      