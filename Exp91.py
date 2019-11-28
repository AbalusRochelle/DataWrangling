import pandas as pd
a=pd.DataFrame({"Box":["Box1","Box1","Box1","Box2","Box2","Box2"],
"Dimension":["Length","Width","Height","Length","Width","Height"],
"Value":[6,4,2,5,3,4]})

tidy=a.pivot_table(index=['Box'],columns='Dimension',values='Value').reset_index()

tidy['Volume']=tidy.Length*tidy.Width*tidy.Height
