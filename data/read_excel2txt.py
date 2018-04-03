import numpy as np
import pandas as pd

t=pd.read_excel('/home/xyzheng/data/radar/test.xlsx',sheetname='pH',header=None,skiprows=1,index_col=0)
print t.values[0,0]
f=open('/home/xyzheng/data/radar/pH.dat','w')
for ii in range(t.values.shape[0]):
	for jj in range(t.values.shape[1]):
		f.write('%i,%i,%s\n'%(ii,jj,t.values[ii,jj]))
f.close()