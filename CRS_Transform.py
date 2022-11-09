def transform(deg, min, sec):
    return deg + min/60 + sec/3600

lat = [(41,44,39.59),(41,44,36.93),(41,44,27.32)]
long = [(44,44,24.07),(44,44,24.46),(44,44,17.99)]
E = []
N = []
for i in range(len(lat)):
    E.append(transform(long[i][0],long[i][1],long[i][2]))
    N.append(transform(lat[i][0],lat[i][1],lat[i][2]))
print(str(E)+'\n'+str(N))