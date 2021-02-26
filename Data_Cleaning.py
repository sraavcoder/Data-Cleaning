import pandas as pd
import csv

data = pd.read_csv("Data.csv")

del data["Right_Ascension"]
del data["Declination"]
del data["Spectral_Type"]
del data["Bayer_Designation"]
del data["Spectral_class"]
del data["Luminosity"]

headers = []
for header in data.columns:
    headers.append(header)

for x in headers:
    data = data[data[x].notna()]


data = data.rename({
                'Brown_Dwarf': "Brown_Dwarf_Name",
                'Distance.1': "Distance_Star", 
                'Distance': "Distance_BrownDwarf", 
                'Mass.1': "Mass_Star", 
                'Mass': "Mass_BrownDwarf", 
                'Radius.1': "Radius_Star", 
                'Radius': "Radius_BrownDwarf", 
                'App_mag': "Apparent_Magnitude"
            }, axis='columns')

data.to_csv('Cleaned_Data.csv') 