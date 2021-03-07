duration = 48
time = 5
rslt = duration+time

nbD = 0
while rslt > 24:
    rslt-=24
    nbD+=1

rslt-=12
print(nbD, rslt)
