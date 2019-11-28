import pandas as pd
a=pd.DataFrame({"Student":['Ice Bear','Panda','Grizzly'],
                "Math":[80,95,79]})
b=pd.DataFrame({"Student":['Ice Bear','Panda','Grizzly'],
                "Electronics":[85,81,83]})
c=pd.DataFrame({"Student":['Ice Bear','Panda','Grizzly'],
                "GEAS":[90,79,93]})
d=pd.DataFrame({"Student":['Ice Bear','Panda','Grizzly'],
                "ESAT":[93,89,88]})

e=pd.merge(a,b,how='right', on='Student')
f=pd.merge(e,c,how='right', on='Student')
g=pd.merge(f,d,how='right', on='Student')

melted = pd.melt(g, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
FinalMelt = melted.rename(columns = {'variable' : 'Subject', 'value' : 'Grades'})