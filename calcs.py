def calc_area(object,dimensions):
    area=[]
    for i in range(len(object)):
        if object[i]=='rectangle':
            area.append(round(dimensions[i][0]*dimensions[i][1],6))
        elif object[i] =='circle':
            area.append((dimensions[i]**2*3.14159266,6))
        else:
            area.append(round(dimensions[i][0],4)*round(dimensions[i][1]/2,6))

    return area

def calc_moi(object,dimensions):
    moi=[]
    for i in range(len(object)):
        if object[i]=='rectangle':
            moi.append( [dimensions[i][0]*dimensions[i][1]**3/36,dimensions[i][0]**3*dimensions[i][1]/36])
        elif object [i]=='circle':
            moi.append(dimensions[i]**4*3.14159266/4)
        else:
            moi.append( [dimensions[i][0]*dimensions[i][1]**3/12,dimensions[i][0]**3*dimensions[i][1]/12])
    return moi


def calc_centroid(object, dimensions,pos):
    centroid=[]
    for i in range(len(object)):

        if object[i] == 'rectangle':
            centroid.append( [round(round(pos[i][0]+dimensions[i][0]/2,4),5),round(round(pos[i][1]+dimensions[i][1]/2,4),5)])



        elif object[i] == 'circle':
            centroid.append( [round(pos[i][0]+0,5),round(pos[i][1]+0,5)])


        elif object[i]=='triangle_1':
            centroid.append( [round(pos[i][0]+(dimensions[i][0]*2/3),5),round(pos[i][1]+(dimensions[i][1]*2/3),5)])




        elif object[i] == 'triangle_2' :
            centroid.append( [round(pos[i][0] + (dimensions[i][0] * 1 / 3),5),round( pos[i][1] + (dimensions[i][1] * 1 / 3),5)])


        elif object[i] == 'triangle_3':
            centroid.append( [round(pos[i][0] + (dimensions[i][0] * 1 / 3),5), round(pos[i][1] + (dimensions[i][1] * 2 / 3),5)])


        elif object[i] == 'triangle_4':
            centroid.append( [round(pos[i][0] + (dimensions[i][0] * 2 / 3),5),round( pos[i][1] + (dimensions[i][1] * 1 / 3),5)])

    return centroid

def composite_centroid(area,centroid):
    ax=0
    ay=0
    asum=0
    for i in range(len(area)):
        ax+=round(area[i]*centroid[i][0],8)
        ay += round(area[i] * centroid[i][1],8)
        asum+=round(area[i],5)
    return[round(ax/asum,6),round(ay/asum,6)]


def calc_Ah2(area,centroid,axis):
    ah2=[]
    for i in range(len(area)):
        ah2.append([area[i]*(centroid[i][1]-axis[1]),8,area[i]*(centroid[i][1]-axis[1])])
    return ah2

def i_composite(moi,ah2):
    i_sum=[]
    for i in range(len(moi)):
        i_sum.append([moi[i][0]+ah2[i][0],moi[i][1]+ah2[i][1]])
    return i_sum