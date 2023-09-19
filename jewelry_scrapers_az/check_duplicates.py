import pandas as pd

df = pd.read_excel('combined.xlsx')
#duplicateRows = df[df.duplicated(['Names', 'Adresses', 'Phones'])]
#print(df)
#print(df[df.duplicated(subset=['Names','Adresses','Phones'], keep=False)])

#df[df.duplicated(subset=['Names','Adresses','Phones'], keep=False)]
#df = df[df.duplicated(subset=['Names','Adresses','Phones'], keep=False)]
df = df.drop_duplicates(subset=["Names", "Adresses", 'Phones'], keep='first')
print(df)
df.to_excel(r'combined_scraped.xlsx', index=False)