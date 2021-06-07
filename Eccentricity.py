import DL_Section as dls
import LL_Combinations as lls


kerb_len=dls.length[10]
left_pos=dls.pos[10][0]
cl=dls.axes[0]-left_pos
e=[]
dist=[]
for i in range (len(lls.llc)):
    epos = 0
    for j in range (len(lls.llc[i])):
        if j == 0:
            lef_clear=150
            g=1200
            ws=1800
            for k in range(int(lls.llc[i][j])):
                epos = epos + (57 * ((kerb_len + lef_clear+k*g+k*ws) + (kerb_len + lef_clear +k*g+ (k+1)*ws)))
                lpos=(kerb_len + lef_clear +k*g+ (k+1)*ws)
        elif j == 1:
            lef_clear=1200
            g=1200
            ws=2600
            for k in range(int(lls.llc[i][j])):
                if lls.llc[i][0] > 0:
                    epos = epos + (350 * ((lpos+k*g+k*ws) + (lpos+k*g+ (k+1)*ws)))
                elif lls.llc[i][0]==0:
                    epos = epos + (57 * ((kerb_len + lef_clear + k * g + k * ws) + (kerb_len + lef_clear + k * g + (k + 1) * ws)))
        elif j == 2:
            lef_clear = 1200
            g = 1200
            ws = 2050
            for k in range(int(lls.llc[i][j])):
                if lls.llc[i][0] > 0:
                    epos = epos + (350 * ((lpos + k * g + k * ws) + (lpos + k * g + (k + 1) * ws)))
                elif lls.llc[i][0] == 0:
                    epos = epos + (57 * ((kerb_len + lef_clear + k * g + k * ws) + (
                                kerb_len + lef_clear + k * g + (k + 1) * ws)))
    e.append(cl-(epos/((57*2*lls.llc[i][0])+(350*2*lls.llc[i][1])+(350*2*lls.llc[i][2]))))
print("The eccentricities for different load combinations are:\n",e)
for i in range (len(e)):
    dist.append((1+(2/3)*e[i]/1000,1-(2/3)*e[i]/1000))
print ("The distribution factors are:\n",dist)

