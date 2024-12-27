#name="arsh"
#number="ali azam"
#flot=6.8

#print(type(flot))

#print(f"my name is",name,number) #can cotination
#print(f"my name is {name} {number}") #means togther to varible, by use of "f" string

#paragraph="""my name is arsh.
#I am a programer.
#My age is 17."""

#print(paragraph)

#first_name="Arsh"

#print(f"""hi {first_name}
#u have win the ultimate prize.

#Best regard,
#Arsh""")

#[[[Modulus]]], by table if 20 is comes in 2 so answer is 0, while 21 answer is 1.

#a=23
#b=2
#result= a%b 
#print("modulus:", result)

#[[[[exponate]]]]
#num1=5
#print(num1 ** 3)

#project [[[[[[(1)]]]]]]

 #Chaand taara khan is hosting  rabri party at his home. he need to know the total amount of people attending the event and the amount of rabri (in grams and kg) he needs to prepare.
 
 #There are 12 faculty members.
 #There are 4 administrative staff members.
 #There are 100 students in the institute.
 #There are 15 people absent.
 #Per person rabri is 250g
 
faculty = 12
admin = 4
students = 100
absent = 15
per_person_rabri=250
#total_rabri_in_gram=25250 #second way to solve
total_members = faculty + admin +students
#print(f"total member is {total_members}")
 
total_present_members=total_members -absent
print(f"total present members: {total_present_members} ")

print(f"total rabri in grams:{total_present_members * per_person_rabri}g")

#print(f"total rabri in kg:{total_rabri_in_gram //1000}kg") # second way to solve

total_rabri_g=total_present_members * per_person_rabri
print(f"total rabri in kg:{total_rabri_g //1000}kg")