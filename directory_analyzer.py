import os
def fun(l):
    for path,folder,file in os.walk(l):
                print(path)


                for j in file:
                    print("        ",j)


s =input("enter directory that you want to anlyze")
s.replace('\\','/')
fun(s)
