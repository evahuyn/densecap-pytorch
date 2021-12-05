import pandas as pd

df = pd.read_json("result.json")
caps = []
for column in df:
    imgname = column.split("/")[3]
    columnSeriesObj = df[column]
    columncap = ''
    for i in range(len(columnSeriesObj)):
        columncap= columncap + columnSeriesObj[i]['cap'] + "; "
    # caps[imgname] = columncap
    caps.append(imgname + '\n')
    caps.append(columncap + '\n')

with open("densecap_result.txt", 'w') as f:
    f.writelines(caps)
#
# caps = pd.DataFrame(caps, index=[0])
# caps.to_json("densecap_result.json")