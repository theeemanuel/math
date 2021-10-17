hours=int(input("Enter the number of hours: "))

hour=0
fsec=0
fmsec=0
fminute=0

for i in range(1,hours+1):
    hour+=1
    if(hour==13):
        hour=1
    for minute in range(0,60):
        minerror=0.1
        for sec in range(0,60):
            for msec in range(0,100):
                angle=abs(((6*minute)+(0.1*sec)+(0.001*msec))-((30*hour)+(0.5*minute)+(sec/120)+(msec/1200)))
                if (abs(angle-180)<=minerror):
                    minerror=abs(angle-180)
                    fmsec=msec
            angle=abs(((6*minute)+(0.1*sec)+(0.001*fmsec))-((30*hour)+(0.5*minute)+(sec/120)+(fmsec/1200)))
            if(abs(angle-180)<=minerror):
                minerror=abs(angle-180)
                fsec=sec
        angle=abs(((6*minute)+(0.1*fsec)+(0.001*fmsec))-((30*hour)+(0.5*minute)+(fsec/120)+(fmsec/1200)))
        if(abs(angle-180)<=minerror):
                minerror=abs(angle-180)
                fminute=minute
    angle=abs(((6*fminute)+(0.1*fsec)+(0.001*fmsec))-((30*hour)+(0.5*fminute)+(fsec/120)+(fmsec/1200)))
    print(hour,":",fminute,":",fsec,":",fmsec," with an index error of ",abs(angle-180))
