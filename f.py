with open("input.txt","r") as f3:
    with open("input1.txt", "w") as f2:
        for line in f3:
            f2.write(line)
        f2.write("\n")
        f2.write("-")
'''with open("input1.txt", "a") as f1:              
    f1.write("\n")
    f1.write("-")'''
with open("input1.txt", "r") as file: 
    data = file.readlines() # 
#print(data)
with open("output.txt", "w") as f:  
    f.write("") 
l1=[]
edc=ck=ck_c=rdqs=rdqs_c=st=s=''
for line in data :
    for i in line :
        if(i=='-'):
            s=line
            for j in l1:
                #print(type(j))
                d = j.split()
                #print(data)
                # Checking if edc,ck etc.,. exists in list  
                for k in d: 
                    if(k == 'edc') : 
                        edc = j
                    if(k=='ck'):
                        ck=j
                    if(k=='ck_c'):
                        ck_c=j
                    if(k=='rdqs'):
                        rdqs=j
                    if(k=='rdqs_c'):
                        rdqs_c=j
                #break
            with open("output.txt", "a") as f:  
                f.write(st)
            #    f.write("\n")
                f.write(edc)
             #   f.write("\n")
                f.write(rdqs)
              #  f.write("\n")
                f.write(rdqs_c)
               # f.write("\n")
                f.write(ck)
                #f.write("\n")
                f.write(ck_c)
                f.write("\n")
            print(st,edc,rdqs,rdqs_c,ck,ck_c)
            
            st=s
            l1=[]
            #print (i)
            #print(line)
    l1.append(line)
#print(l1)
