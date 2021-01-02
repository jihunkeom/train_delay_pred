import pandas as pd

d06 = pd.read_csv("gagonged_data_06.csv").drop(['Unnamed: 0'], axis=1)
d09 = pd.read_csv("gagonged_data_09.csv").drop(['Unnamed: 0'], axis=1)
#print(d06.values+d09.values)
AD = pd.DataFrame(list(d06.values)+list(d09.values))
AD.to_csv("gagonged_data.csv")