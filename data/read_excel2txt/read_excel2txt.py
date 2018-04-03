import numpy as np
import pandas as pd

t=pd.read_excel('test2.xlsx',sheetname='temp',header=None,skiprows=1,index_col=0)

f=open('test2.dat','w')
for ii in range(t.values.shape[0]):
	for jj in range(t.values.shape[1]):
		f.write('[%i,%i,%s],'%(jj,ii,t.values[ii,jj]))
f.close()