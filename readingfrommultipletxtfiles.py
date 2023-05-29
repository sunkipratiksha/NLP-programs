import os
import pandas as pd
filename = os.listdir('txtfiles/')

print(filename)

files = []

for i in filename:
    f = open('txtfiles/'+i,'r')
    text=f.readlines()
    files.append(text)
    print(text)
    
df = pd.DataFrame(files)
print(df)
