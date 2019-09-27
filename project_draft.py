import pandas as pd 

data = pd.read_csv("zno_2018.csv") 


#df = pd.DataFrame(data[['Birth']]) 
# Preview the first 5 lines of the loaded data 
#data.Birth.unique()
oblast = data.REGNAME.unique()
#create an empty Data frame for mean values in different regions
meanMarkUkrObl = pd.DataFrame()
#go along all regions
for oblastCurr in oblast:
  #choose rows corresponding to the current region
  dataOblCurr = data.loc[data['REGNAME'] == oblastCurr]
  #calculate mean mark in Ukrainian
  meanMarkUkrOblCurr = dataOblCurr.loc[:,"UkrBall"].mean()
  #add new row with another region every loop cycle
  meanMarkUkrObl = meanMarkUkrObl.append({'Область':oblastCurr, 'Середній бал Укр мова':meanMarkUkrOblCurr}, ignore_index=True)

meanMarkUkrObl

#make histogram
distrib = meanMarkUkrObl.plot.bar( x='Область', y='Середній бал Укр мова', rot=90,legend=False, width=0.5,figsize=(10,5))

#distrib = meanMarkUkrObl.plot( x='Область', y='Середній бал Укр мова', rot=90, kind='bar',legend=False)
distrib.grid(zorder=0)
#distrib.legend.remove()




!sudo apt-get install libgeos-dev
!sudo pip3 install -U git+https://github.com/matplotlib/basemap.git

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None, width=2E6, height=2E6, lat_0=50, lon_0=30,)
m.etopo(scale=0.5, alpha=0.5)


