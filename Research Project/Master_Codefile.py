# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:24:11 2022

@author: Nishit
"""

import pandas as pd
import os
from statistics import mean
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import geopandas
import pandas_datareader as web
from pandas_datareader import wb

#Part 0: Retrieve Irrigation data from WorldBank 

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


#Part 1: Identify districts in Madhya Pradesh using ICRISAT data

base_file = r'C:\GitHub\Data_Skills_2_project\Research Project\Datasets'
most_irrigated = ['Hoshangabad', 'Narsinghpur','Dhar', 'Guna', 'Bhopal']
most_irrigated_2 = ['Hoshangabad', 'Narsimhapur','Dhar', 'Guna', 'Bhopal']
least_irrigated = ['Balaghat', 'Damoh', 'Mandla', 'Singrauli', 'Sidhi']
driest_years = [2002,2005,2010,2001,2008]

def irr_perc(area_data, irrigate_data):
       area = pd.read_csv(os.path.join(base_file, area_data))
       irrigated = pd.read_csv(os.path.join(base_file, irrigate_data ))
       irr_perc = irrigated.merge(area, on = ['Dist Name','Year'])
       irr_perc['Gross Irrigation Area %'] = irr_perc['WHEAT IRRIGATED AREA (1000 ha)']/irr_perc['WHEAT AREA (1000 ha)']
       return irr_perc
   
def aggregate_data(data,group_name, column_name, new_column_name, district_list):
    agg_data = pd.DataFrame(columns = ['year','District Group',  new_column_name])
    for year in driest_years: 
        temp_year= data[data['Year'] == year]
        temp_year = temp_year[temp_year['Dist Name'].isin(district_list)]
        agg_data.loc[len(agg_data.index)] = [year, group_name, mean(temp_year[column_name])] 
    return agg_data

wh_total = irr_perc('wheat_irrigated.csv', 'wheat_area.csv')
irrigation = pd.read_csv(os.path.join(base_file, 'wheat_irrigated.csv' ))

#Districts chosen based on 
#1. soil type
#2. NPA/GIA %age
#3. min. wheat production quantity
#4. historical irrigation supply

#Part 2: Identify driest years in MP

rainfall = pd.read_csv(os.path.join(base_file, 'rainfall.csv' ))
west_precipitation = rainfall[rainfall['SUBDIVISION'] == 'WEST MADHYA PRADESH']
west_precipitation = west_precipitation[['YEAR','ANNUAL']]
west_precipitation = west_precipitation[west_precipitation['YEAR'] >=2000]

west_precipitation 

fig, ax = plt.subplots()
ax.plot(west_precipitation['YEAR'], west_precipitation['ANNUAL'])
ax.set_title('Annual Precipitation in Madhya Pradesh, 2000 - 2015')


yield_data = pd.read_csv(os.path.join(base_file, 'master_yield.csv' ))

#Part 3: Create two groups based on irrigation levels 


agg_yield_high = aggregate_data(data=yield_data,
                                group_name= 'high irrigation', 
                                column_name= 'WHEAT YIELD (Kg per ha)', 
                                new_column_name= 'yield',
                                district_list = most_irrigated)

agg_yield_low = aggregate_data(data=yield_data, 
                               group_name= 'low irrigation', 
                               column_name= 'WHEAT YIELD (Kg per ha)', 
                               new_column_name= 'yield',
                               district_list = least_irrigated)

agg_yield = pd.concat([agg_yield_high, agg_yield_low])

#Part 4: Find group irrigation levels for every dry year 
  
high_irr_perc = irr_perc('high_area.csv','high_irrigated.csv')
low_irr_perc = irr_perc('low_area.csv', 'low_irrigated.csv' )   

agg_irr_perc = pd.DataFrame(columns = ['year','District Group', 'gross irrigation area %'])

agg_irr_high = aggregate_data(data=high_irr_perc,
                                group_name= 'high irrigation', 
                                column_name='Gross Irrigation Area %', 
                                new_column_name= 'Gross Irrigation Area %',
                                district_list = most_irrigated)

agg_irr_low = aggregate_data(data=low_irr_perc ,
                               group_name= 'low irrigation', 
                               column_name= 'Gross Irrigation Area %',
                               new_column_name= 'Gross Irrigation Area %',
                               district_list = least_irrigated)

agg_irr_perc = pd.concat([agg_irr_high, agg_irr_low])

agg_data = agg_irr_perc.merge(agg_yield, on = ['year', 'District Group'])

#Part 5: Plot scatterplot for low and high groups 
ax = sns.scatterplot(x= 'Gross Irrigation Area %',
           y= 'yield', 
           hue= 'District Group',
           ci=None,
           data= agg_data)

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.01, point['y'], str(point['val']), fontsize=7)

label_point(agg_data[ 'Gross Irrigation Area %'], agg_data['yield'], agg_data['year'], plt.gca())  

#Part 6: Plot yield for all districts in 2015

irr_perc_2015 = irr_perc(area_data = 'area_2015.csv', irrigate_data = 'irr_2015.csv')

ax_2 = sns.regplot(x= 'Gross Irrigation Area %',
           y= 'WHEAT YIELD (Kg per ha)', 
           data= irr_perc_2015)

model = sm.OLS(agg_data['yield'], agg_data[ 'Gross Irrigation Area %']).fit()
model.summary()

updated_2015 = irr_perc_2015[(irr_perc_2015['Gross Irrigation Area %']>= 0.5) & (irr_perc_2015['Gross Irrigation Area %']<=1.1)]


ax_3 = sns.regplot(x= 'Gross Irrigation Area %',
           y= 'WHEAT YIELD (Kg per ha)', 
           data= updated_2015)


#Part 7: shape file for Maharashtra to show selected districts 

path = r'C:/GitHub/Data_Skills_2_project/Research Project/Shapefiles/shapefiles-master/state_ut/madhyapradesh/district/madhyapradesh_district/'
ward_mp = os.path.join(path, 'madhyapradesh_district.shp')

df_mp = geopandas.read_file(ward_mp)
df_select_high = df_mp.loc[df_mp['district'].isin(most_irrigated_2)]
df_select_low = df_mp.loc[df_mp['district'].isin(least_irrigated)]

from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, ax = plt.subplots(figsize=(8,8))
ax.axis('off')
divider = make_axes_locatable(ax)
df_mp.plot(ax=ax, color='white', alpha=0.5, edgecolor='black', label='Wards')
df_select_high.plot(ax=ax, color='green', alpha=0.5, edgecolor='black', label='Wards')
df_select_low.plot(ax=ax, color='red', alpha=0.5, edgecolor='black', label='Wards')
ax.set_title('Selected District Groups based on Irrigated Area %', fontsize = 12)


#Part 8: shape file for Madhya Pradesh to show variation in yield 

df_mp_new = df_mp.replace('Narsimhapur', 'Narsinghpur')
df_mp_yield = df_mp_new.merge(irr_perc_2015, left_on = 'district', right_on = 'Dist Name') 

def plot_data(col_name):
        fig, ax = plt.subplots(figsize=(8,8))
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(ax)
        cax = divider.append_axes('right', size='5%', pad=0.1)
        ax = df_mp_yield.plot(ax=ax, column=col_name, legend=True, cmap="RdYlGn", cax = cax)
        ax.axis('off')
        ax.set_title(col_name)

plot_data('WHEAT YIELD (Kg per ha)')
plot_data('Gross Irrigation Area %')


#Part 9: Sentiment analysis of World Bank document

from collections import Counter
import spacy


nlp = spacy.load("en_core_web_sm")


def export_text(location):
    temp = {}
    for location in location:
        base_path = r'C:\GitHub\Data_Skills_2_project\Research Project\Reports'
        with open(os.path.join(base_path, location + '.txt'), 'r', encoding ='utf-8') as fp:
                names_list = fp.readlines()
                names_string = ''.join(map(str,names_list))
        temp.update({location: names_string})
    return temp


def sentiment(brief):
    base_path = r'C:\GitHub\Data_Skills_2_project\Research Project\Reports'
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob');
    date = []
    sentiment = []
    for current_brief in list(brief.values()):       
        doc = nlp(current_brief) 
        date.append(list(brief.keys())[list(brief.values()).index(current_brief)])
        sentiment.append(doc._.blob.polarity)
        words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
        word_freq = Counter(words)
        common_words = word_freq.most_common(20)
        print ( common_words)
        
    data = {'Date': date, 'Polarity': sentiment}    
    senti_data = pd.DataFrame(data)
    fig,ax = plt.subplots()
    ax.plot(senti_data['Date'], senti_data['Polarity'], 'b-') 
    plt.xticks(rotation = 45)
    plt.savefig(os.path.join(base_path,'question_1_plot.png'))
    ax.set_title('Sentiment Analysis of Recent World Bank Reports On India', fontsize = 12)

    return(senti_data)

    

docs = ["6_2022",
        "3_2022",
        "11_2021",
        "7_2021",
        "5_2021",
        "3_2021"]

brief = export_text(docs)
senti_df = sentiment(brief)

#Water featured just once in the top 20 common words in the past 5 World Bank reports
#focussed on the country India 
