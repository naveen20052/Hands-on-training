import pandas as pd
import numpy as np

data={'name':['naveen','harish','karthi','ambi','ovi'],'age':[10,12,13,14,15],'salary':[10000,20000,30000,40000,50000],'dep':['it','cse','iit','aids','cse']}
df=pd.DataFrame(data)
print('database:\n')
print(df)

print('csv values:/n')
df[['name','age','salary','dep']].to_csv(('number.csv'),index=True)
f=open('number.csv','r')
print(f.read())
print('\n')

print('readcsv:\n')
updated=pd.read_csv(r'number.csv')
print(updated)


print('excel values:\n')
df[['name','age','salary','dep']].to_excel(('number.xlsx'),index=True,sheet_name='employee')
f=open('number.xlsx','r')


print('readexcel:\n')
updated=pd.read_excel(r'number.xlsx')
print(updated)

print('new database:\n')
string={'name':['ajay kumar','sudar mani','amir khan','salman khan','moeen ali'],'age':[1,2,3,4,5]}
do=pd.DataFrame(string)
print(do)

print('\n values of string:\n')
do['first']=do['name'].str.split().str[0]
print(do[['name','first']])

print('\n values of string:\n')
do['last']=do['name'].str.split().str[1]
print(do[['name','first','last']])

print('\n database values:\n')
dicto={'emp_id':[1,2,3,4],'name':['a','ab','acb','abcd']}
dp=pd.DataFrame(dicto)
print(dp)

print('\n anthoer database:\n')
dictp={'emp_id':[5,6,7,8],'age':[12,13,14,15]}
de=pd.DataFrame(dictp)
print(de)

print('\n updated one:\n')
updated_one=pd.merge(dp,de,on='emp_id')
print(updated_one)

print('\n anthoer concat:\n')
doic={'emp_id':[1,2,4,5],'age':[12,13,14,15]}
ga=pd.DataFrame(doic)
print(ga)

print('\n new one:\n')
dilp={'emp id':[3,6,7,8],'age':[12,13,14,15]}
go=pd.DataFrame(dilp)
print(go)

print('\n concat \n')
updated_new=pd.concat([ga,go],ignore_index=False)
print(updated_new)
import matplotlib.pyplot as plt
print('\n plot :\n')
num={ 'val':[10,20,30,40],'category':['a','b','c','d']}
de=pd.DataFrame(num)
print(de)

print('\n bar plot: \n')
de.plot(kind='bar',x='category',y='val',title='data anlysis')
plt.show()

print('\n line plot: \n')
de.plot(kind='line',x='category',o='marker',y='val',title='data anlysis')
plt.show()

print('\n hist plot: \n')
de.plot(kind='hist',garb=5,title='data anlysis')
plt.show()






      

                                







           
