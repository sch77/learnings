#hello.py file contents
print("Hello World!")
print("Hello Again!!")

answer = 42
pi = 3.147


print("answer is", answer)

""" this is a
python multi line comment"""

print ("hello".capitalize())
print("hello".replace("l","X"))

print("this is a sentence to split".split())
print("ondu,eradu,mooru".split(","))

name= "Adhrit"
machine = "AndroidBot"
message = "Nice to meet you {0} . I am {1}".format(name,machine)
print(message)

number= -1
if number:
    print ("number is defined!")
else:
    print ("number is not defined!!")


myName = "Adhrit"

if myName:
    print ("myName is ", myName)
else:
    print("myName is not defined!! or is not assigned value")


student_names = ["kallappa","mallappa","rangappa"]
print(student_names[1])
student_names[2]="Hanumappa"
print(student_names[2])

member_names = []
member_names.append("Santosh")
member_names.append("Sohan")
member_names.append("Sandeep")

print(member_names)

if "Mark" in member_names == True:
    print ("Found your mark!")
else:
    print("No marks!!")

print(len(member_names  ))

for member in member_names:
    print("current member is :",member)

for member in range(2):
    print(member_names[member])

for i in range(3,10,2):
    print("i is :", i)

for name in member_names:
    if name == "Santosh":
        continue
    print("testing ", name)

x = 0
while x < 10:
    print("count is {0}".format(x))
    x += 1


hamsa = {
    "units": 245,
    "location": "Kothnur",
    "disputed": True
}

print(hamsa)

print(hamsa.keys())
print(hamsa.values())
# del hamsa["disputed"]
hamsa["disputed"] = "";
print(hamsa)

try :
    print(hamsa["since"])
except KeyError:
    print("Erro finding the since");

print("reached here!!!")

print(set([1,2,4,4,5,5]))
