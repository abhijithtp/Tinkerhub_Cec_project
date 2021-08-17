import sqlite3
dat=[]
fh=input("Enter file name: ")#to enter the .txt file containing the people names
#opens file and read names from it and store it in the list dat.Should be present in same directory or give path as input
fn=open(fh)
for line in fn:
    line=line.rstrip()
    line=str(line)
    dat.append(line)
#function for comparing given data in dat and from database in argumet a and compare them to return the absentees count,name and 
#removes matched names to find unidentified ones
def test(a):
    absent=[]
    flag=0
    count=0
    for num in range(0,50):
        for da in dat:
            if(da==str((a[num])[1])):
                dat.remove(da)
                flag=1
            else:
                continue
        if(flag==0):
            absent.append(a[num])
            count=count+1
        else:
            flag=0
            continue
    return absent,count;
#To create a file in same directory *IN MY CASE"python_project/filename"* adjust with your path.Returns the filehandle
def filing(n):
    try:#When file is not opened yet creates a new file
        batch=open(("python_project/"+str(n)),'w')
        return batch
    except:#When file is already created  by code it will rewrite the contents
        batch=open(("python_project/"+str(n)),'x')
        return batch


    
#Readd data from database and pass the obtained list to function for processing
cn=sqlite3.connect("python_project/data.sqlite")
c=cn.cursor()
c.execute("SELECT * FROM a_batch")
a=c.fetchall()
cn.commit()
d,n=test(a)#receives absentees name and count of A batch
print('Absentees in A batch:'+str(n))
fh_a=filing("A_batch_absentees")
for ab in d:#Prints roll number and name of absent people
    print(str(ab[0])+"\t"+str(ab[1]))
    fh_a.write(str(ab[0])+"\t"+str(ab[1])+"\n")
fh_a.close()
c.execute("SELECT * FROM b_batch")
b=c.fetchall()
cn.commit()
cn.close()
e,m=test(b)#receives absentees name and count of B batch
print("\nAbsentees in B batch:"+str(m))
fh_b=filing("B_batch_absentees")
for bb in e:#Prints roll number and name of absent people
    print(str(bb[0])+"\t"+str(bb[1]))
    fh_b.write(str(bb[0])+"\t"+str(bb[1])+'\n')
fh_b.close()
print("\nUnidentified")
fh_unid=filing("Unidentified_people")
for un in dat:#prints the updated dat that contains unidentifiable entries
    print(un)
    fh_unid.write(str(un)+'\n')
fh_unid.close()



