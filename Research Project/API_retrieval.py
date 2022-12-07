import matplotlib.pyplot as plt
from pandas_datareader import wb

#Retrieve Irrigation data from WorldBank 

indicator = 'AG.LND.IRIG.AG.ZS'
country = 'IN'
india_data = wb.download(indicator = indicator, country = country, start=2000, end = 2020)
india_data.reset_index(inplace = True)
india_data = india_data.sort_values(by='year', ascending = True )
fig, ax = plt.subplots()
ax = india_data.plot( x ='year', y='AG.LND.IRIG.AG.ZS', color='red' )
ax.legend(labels= '% Irrigated Area', loc = 'best')
ax.set_ylabel("% Irrigated Land")
ax.set_title("% Irrigated Land Area in India")
