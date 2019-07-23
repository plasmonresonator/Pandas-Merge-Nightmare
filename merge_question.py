import pandas as pd
file = 'old.xlsx'
file2 = 'new.xlsx'
desired = 'oldnewfinal.xlsx'

old = pd.read_excel(file)
new = pd.read_excel(file2)
final= pd.read_excel(desired)
print('Here is the old file...\n')
print(old.head())
print('\nHere is the new file...\n')
print(new.head())

print('\nThis is what I am trying to work towards...\n')

print(final.head(10))

print("\n\nHere are some things that I've tried so far...\n")

new['Account_corrected'] = new['Account_Zip'].str.lower()
new['Account_corrected'].replace('_','', regex=True,inplace=True)
old['Account_corrected'] = old['Account_Zip'].str.lower()
old['Account_corrected'].replace('_','', regex=True,inplace=True)

by_cust = old.groupby(by=['Account_corrected']).agg({'Ship_ID1':'first',
													'Account_Zip':'first',
													'Sales':'sum',
													'Old_Sales_Person':'first'}).reset_index()

new_by_cust = new.groupby(by=['Account_corrected']).agg({'Ship_ID1':'first',
														'Account_Zip':'first',
														'Projections':'first',
														'Old_Sales_Person':'first',
														'New_Sales_Person':'first',
														'Territory_ID':'first'}).reset_index()

print(by_cust.head())
print('\n\n')
print(new_by_cust.head())

merged = pd.merge(by_cust, new_by_cust, how='outer', on=['Account_corrected'], indicator='str')
print('\n\n')
print(merged)