from shiny import App, render, ui
import pandas as pd
import os
import geopandas
import matplotlib.pyplot as plt
import matplotlib

base_file = r'C:\GitHub\Data_Skills_2_project\Research Project\Datasets\2005_to_2015_yield'

def irr_perc(area_data, irrigate_data):
       area = pd.read_csv(os.path.join(base_file, area_data))
       irrigated = pd.read_csv(os.path.join(base_file, irrigate_data ))
       irr_perc = irrigated.merge(area, on = ['Dist Name','Year'])
       irr_perc['Gross Irrigation Area %'] = irr_perc['WHEAT IRRIGATED AREA (1000 ha)']/irr_perc['WHEAT AREA (1000 ha)']
       return irr_perc
   

path = r'C:\GitHub\Data_Skills_2_project\Research Project\Shapefiles\shapefiles-master\state_ut\madhyapradesh\district\madhyapradesh_district'
ward_mp = os.path.join(path, 'madhyapradesh_district.shp')

df_mp = geopandas.read_file(ward_mp)
df_mp_new = df_mp.replace('Narsimhapur', 'Narsinghpur')

df_yield = df_mp_new
df_yield = df_yield.rename(columns = { "district" : "Dist Name"})

years = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]
for year in years:
    name = "yield_" + year
    file = pd.read_csv(os.path.join(base_file, name + ".csv"))
    file.rename(columns = {"WHEAT YIELD (Kg per ha)": year}, inplace = True)
    file = file[['Dist Name',year]]
    df_yield = df_yield.merge(file, on = 'Dist Name')
   

app_ui = ui.page_fluid(
    ui.h2("This is the change in yield based on years in the State of Maharashtra!"),
    ui.input_slider(id = "n", label = "Choose a year", min = 2005, max = 2017, value =2010, sep="" ),
    ui.output_plot("plot_data"),
)


def server(input, output, session):
    @output
    @render.plot
    def plot_data():
        fig, ax = plt.subplots(figsize=(8,8))
        from mpl_toolkits.axes_grid1 import make_axes_locatable
        divider = make_axes_locatable(ax)
        cax = divider.append_axes('right', size='1%', pad=0.1)
        norm = matplotlib.colors.Normalize(vmin= 0, vmax = 5000)
        ax = df_yield.plot(ax=ax, column= str(input.n()), legend=True, cmap="RdYlGn", cax=cax, norm = norm)
        ax.legend()
        ax.axis('off')
       

app = App(app_ui, server)
