import sys
import numpy as np


d = float(sys.argv[1])


p = np.array(
    [[0.00, 0.00, 0.00],
     [0.50, 0.50, 0.50],
     [0.25, 0.25, 0.25],
     [0.75, 0.75, 0.25],
     [0.75, 0.25, 0.75],
     [0.25, 0.75, 0.75]])/d

l = np.copy(p)


for x in range(int(d)):
    for y in range(int(d)):
        for z in range(int(d)):
            if x+y+z==0:
                continue
            else:
                temp = np.copy(l).T
                temp[0]+=x/d
                temp[1]+=y/d
                temp[2]+=z/d
                p = np.r_[p,temp.T]


n = np.array([['O', '\n'],
              ['O', '\n'],
              ['Cu', '\n'],
              ['Cu', '\n'],
              ['Cu', '\n'],
              ['Cu', '\n']]*int(d**3)).T


a = np.c_[n[0],p.astype(str),n[1]]


s=''
for r in a:
    for i in r:
        s+=str(i)+' '
    s=s[:-1]


lat = 4.176*d
data ="""%block lattice_abc
{lat:.4f} {lat:.4f} {lat:.4f}
90 90 90
%endblock lattice_abc

%block positions_frac
{s}
%endblock positions_frac

kpoint_mp_grid 7 7 7

symmetryGenerate""".format(lat=lat, s=s)

with open(sys.argv[2], "w") as f:
    f.write(data)

