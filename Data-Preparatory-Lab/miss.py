import numpy as np
import pandas as pd

data={
    'A':[1,2,None,4,5],
    'B':[10,None,20,30,None],
    'C':[None,None,None,None,50]
}

df=pd.DataFrame(data)

step1=df.dropna()
print("Output of Step1",step1)

step2=df.fillna(0)
print("Output of Step2",step2)

step3=df.fillna(df.mean())
print("Output of Step3",step3)

step4=df.fillna(method='bfill')
print("Output of Step4",step4)

step5=df.fillna(method='ffill')
print("Output of Step5",step5)

step6=df.interpolate(method='linear')
print("Output of Step6",step6)

step7=df['A'].isna().astype(int)
print("Output of Step7",step7)