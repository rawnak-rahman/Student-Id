Enter_age=int(input("Enter your age:"))


is_eligible=(Enter_age>=18)

if is_eligible:
    print("You are eligible for an ID Card")
else: 
    print("You are not eligible for an ID Card")

name=input("Enter Name here: ")
father=input("Enter Fathers Name here: ")
mother=input("Enter Mothers Name here: ")
cls=input("Enter Class here: ")
roll=input("Enter Class Roll here: ")
bld_grp=input("Enter BLood Group here: ")
Mobile_nm=input("Enter Mobile Number here: ")

print(f"Name          :{name}")
print(f"Father's Name :{father}")
print(f"Mother's Name :{mother}")
print(f"Class         :{cls}")
print(f"Class ROll    :{roll}")
print(f"BLood Group   :{bld_grp}")
print(f"Mobile Number :{Mobile_nm}")


