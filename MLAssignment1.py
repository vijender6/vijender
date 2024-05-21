Q1 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]     
ages.sort()
a = min(ages)
b = max(ages)
print(a)
print(b)
ages.append(a)
print(ages)
ages.append(b)
print(ages)
c = len(ages)
s =(c-1)//2
median1 = (ages[s] + ages[s+1])/2
print(median1)
sum1 = sum(ages)
print(sum1)
avg = sum1/c
print(avg)
range1 = b-a
print(range1)


Q2
dog = dict()
dog["name"] = "BROWNIE"
dog["color"] = "BLACK"
dog["breed"] = "GREAT DANE"
dog["legs"] = "4"
dog["age"] = "9"
print(dog)

student = dict()
student["first_name"] = "SPARSHA"
student["last_name"] = "ADURI"
student["gender"] = "FEMALE"
student["age"] = "22"
student["hobbies"] = ["CRICKET" , "MUSIC"]
student["achievements"] = "STATE CHAMPION"
student["country"] = "INDIA"
student["city"] = "PDPL"
student["ph no"] = "+91 9378762761"
print(student)
length1 = len(student)
print(length1)
print(student["hobbies"])
print(type(student["hobbies"]))
student["hobbies"].extend(["STATE CHAMPOIN"])
print(student["hobbies"])
print(student.keys())
print(student.values())

Q3

brothers = ("SUJITH", "VARSHIK", "VAMSHI");
sisters = ("SATVIKA", "SRUTHI", "VANITHA");
siblings = sisters + brothers;
print(siblings);
length1 = (siblings);
print(length1);
family_members = siblings + ("VIKAS", "KAVYA");
print(family_members);

Q4

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
print(" length:",len(it_companies))  
it_companies.update(['twitter'])
print(it_companies)  
it_companies.remove("IBM")
print(it_companies)
it_companies.update({'Blueberry'})
print(it_companies)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
X=A.union(B)
print(X)
Y=A.intersection(B)  
print(Y)
print(A&B)
print(A.issubset(B))  
print(A.isdisjoint(B)) 
print(A.symmetric_difference(B))   
X.clear()  
print(X)
age_list = [22, 19, 24, 25, 26, 24, 25, 24]
print("Age",len(age_list))
AGE_SET= set(age_list) 
print("Age",AGE_SET) 
print("Age",len(AGE_SET))

Q5

r = 30
pi = 3.14
area_of_circle = pi*r**2  
res = 'The area of circle with {} is {}'.format(str(r), str(area_of_circle))
print(res)
circum_of_circle = 2*3.14*r 
print("circumference of circle:",circum_of_circle)
user_input=float(input()) 
raaadius=20
area_of_circle=pi*raaadius**2
print(area_of_circle)

Q6
sentence="I am a teacher and I love to inspire and teach people"
unique_letter=set(sentence.split())
print("no.of unique words are ",len(unique_letter))

Q7
sequence="Name\tAge\tCountry\tCity\tASABNEH\t250\tFINLAND\tHELSINKI";
print(sequence);

Q8
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with a radius %s is %s meters square." %(radius,area))

Q9
c=0.45
v=int(input("number of students")) 
l1=[]
l2=[]
for i in range(v):
    l1.append(int(input("enter weight in lbs:"+str(i+1)+" "))) 
    l2.append(round(l1[i]*0.453,2))
print("given weights in lbs:",l1)
print("converted weights in kgs:",l2)
