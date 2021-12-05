import random

def display(room):
    print(room)

room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]

x =0
y= 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0
print("\n---> Note : 1 means dirty and 0 means clean <---\n")
print("Random dirty rooms")
display(room)
x =0
y= 0
z=0
while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print("Vaccum's location",x, y)
            room[x][y] = 0
            print("cleaned")
            z+=1
        y+=1
    x+=1
    y=0
perf= (100-((z/16)*100))
print("All Rooms are clean now")
display(room)
print('performance :',perf,'%')