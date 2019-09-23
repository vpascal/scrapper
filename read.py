import pandas as pd 
import glob


files = glob.glob("*.txt")
appended_data = []

for file in files:
    with open(file) as x:
        firstLine = x.readline().rstrip()
        col3 = [line.split('\n')[0] for line in x]
        names = col3[::2]
        vals = col3[1::2]
        vals =[float(x.strip('%')) for x in vals]
        firstLine = [firstLine]*len(names)
        df = pd.DataFrame(list(zip(names, vals,firstLine)), columns =['name', 'val','date']) 
        df['name']= df['name'].astype(str)
        df['date'] =  pd.to_datetime(df['date'])
        appended_data.append(df)

appended_data = pd.concat(appended_data)
#print(appended_data.tail())
appended_data.to_csv('final.csv',index=False)