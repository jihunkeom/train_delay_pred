import pandas as pd
import numpy as np

d = pd.read_csv("gagonged_data.csv").drop(['Unnamed: 0'], axis=1)

AD =[]


for item in d.values:
    a = item[6:59]
    b = item[0:6]

    # for l in range(len(a)):
    #     if np.isnan(a[l]):
    #         a[l]=0
    #     else:
    #         break
    # for l in range(len(a)-1,-1,-1):
    #     if np.isnan(a[l]):
    #         a[l]=0
    #     else:
    #         break

    ts = pd.Series(a)
    ts = ts.interpolate(method="values")
    AD.append(list(b)+list(ts.values))

AD = pd.DataFrame(AD)
AD.to_csv("gong2_data_nopad.csv")