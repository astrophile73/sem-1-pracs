import numpy as np
import pandas as pd

casestudy = pd.read_csv("Data.csv")
total = casestudy["Sub1"]+casestudy["Sub2"]
casestudy["Total"]=total




t=casestudy.values[:21].tolist()


for i in range(len(t)):
    for j in range(i+1, len(t)):
        if int(t[i][4])>int(t[j][4]):
            t[i],t[j]= t[j],t[i]

casestudy=pd.DataFrame(t)
print(casestudy)            
            

