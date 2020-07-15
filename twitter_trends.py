import pandas as pd
import os

data=pd.DataFrame(data=["1,","2","3"])

if not os.path.exists("./data"):
    os.makedirs("./data")

data.to_csv("./data/sample.csv")