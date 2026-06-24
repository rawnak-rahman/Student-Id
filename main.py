Enter_age=int(input("Enter your age:"))


is_eligible=(Enter_age>=18)

if is_eligible:
    print("You are eligible for an ID Card")
else: 
    print("You are not eligible for an ID Card")

Infos=[]
print("Enter your information as the following Name,Fathers Name,Mothers Name,Class,Class Roll,Blood Group,Mob Num(Press on an Empty line to finish): ")

while True:
    Info=str(input())

    if Info=="":
        break
    Infos.append(Info)

result="\n".join(Infos)
print(result)    
