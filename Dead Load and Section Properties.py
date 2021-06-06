import csv
#Positions are calculated from bottom left grid space of shape

A_sum=0
A_x=0
A_y=0
obj=[]
length=[]
height=[]
pos=[]
orient=[]
area=[]
moi=[]
center=[]
centroid=[]


with open('data/Sect.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print(row)
        obj.append((row[0]))
        length.append(float(row[1]))
        height.append(float(row[2]))
        pos.append([float(row[3]),float(row[4])])
        orient.append(float(row[5]))

class shape:
    def __init__(self,name,length,height,pos):
        self.name=name
        self.length=length
        self.height=height
        self.pos=pos

    @property
    def area(self):
        if self.name =="triangle":
            return (self.length*self.height)/2
        elif self.name == "rectangle":
            return (self.length*self.height)

    @property
    def MOI(self):
        if self.name=="triangle":
            return [((self.length * self.height**3) / 36),((self.length **3 * self.height) / 36)]
        elif self.name=="rectangle":
            return [((self.length * self.height**3) / 12),((self.length **3 * self.height) / 12)]

    @property
    def Center(self):
        if self.name == "triangle":

            return [self.length/3,self.height/3]
        elif self.name == "rectangle":
            return [self.length/2,self.height/2]

for i in range(len(obj)):
    a=shape(obj[i],length[i],height[i],pos[i])
    area.append(a.area)
    moi.append(a.MOI)
    center.append(a.Center)
    A_sum = A_sum + a.area
    if obj[i]=="triangle":
        if orient[i] == 1:
            #top right
            A_x=a.area*(pos[i][0]+length[i]-a.Center[0]) + A_x
            A_y=a.area * (pos[i][1]+height[i]-a.Center[1]) + A_y
            centroid.append([(pos[i][0]+length[i]-a.Center[0]),(pos[i][1]+height[i]-a.Center[1])])
        elif orient[i] == 2:
            #bottom left
            A_x=a.area * (pos[i][0]+a.Center[0]) + A_x
            A_y=a.area * (pos[i][1]+a.Center[1]) + A_y
            centroid.append([(pos[i][0]+a.Center[0]),(pos[i][1]+a.Center[1])])
        elif orient[i] == 3:
            #top left
            A_x=a.area * (pos[i][0]+a.Center[0])+ A_x
            A_y=a.area * (pos[i][1]+height[i]-a.Center[1]) + A_y
            centroid.append([(pos[i][0]+a.Center[0]), (pos[i][1]+height[i]-a.Center[1])])
        elif orient[i] == 4:
            #bottom right
            A_x = a.area * (pos[i][0] + length[i] - a.Center[0])+ A_x
            A_y = a.area * (pos[i][1] + a.Center[1]) + A_y
            centroid.append([(pos[i][0] + length[i] - a.Center[0]),(pos[i][1] + a.Center[1])])
    elif obj[i]=="rectangle":
        A_x = a.area * (pos[i][0] + a.Center[0])+ A_x
        A_y = a.area * (pos[i][1] + a.Center[1]) + A_y
        centroid.append([(pos[i][0] + a.Center[0]), (pos[i][1] + a.Center[1])])
axes = [(A_x/A_sum),(A_y/A_sum)]
# print(A_sum)
print (axes)
I_x=0
I_y=0
for i in range(len(obj)):
    h_x = int((centroid[i][0]-axes[0]))
    h_y= abs((centroid[i][1] - axes[1]))
    I_x=area[i]*h_x**2 + I_x
    I_y = area[i] * h_y ** 2 + I_y
print ("The principal moment of inertia of section about centroidal (x,y) axes:",axes," is ",[I_x,I_y])

Dead_Loads=A_sum*25
print("Dead load per m length is:",Dead_Loads)
