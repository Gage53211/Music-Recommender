import pandas as pd
import sklearn
import os


path_to_data = os.path.join("data","dataset.csv")
music_df = pd.read_csv(path_to_data)
print(music_df.head())


