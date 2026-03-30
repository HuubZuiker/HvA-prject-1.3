import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#de data uit de excels lezen opgeslagen door de code voor dataverwerking
reverb_df_0 = pd.read_excel(r"C:\Users\huubz\HvA\Duuk Ludding - Project 1.3 groep 1\reverbs.xlsx", sheet_name="0")
reverb_df_1 = pd.read_excel(r"C:\Users\huubz\HvA\Duuk Ludding - Project 1.3 groep 1\reverbs.xlsx", sheet_name="1")

#de nagalmtijden uit de dataframes halen en reshapen voor de 4x6 grid voor de heatmap
reverb_data_0 = reverb_df_0["reverb"].values
reverb_data_0 = reverb_data_0.reshape(4,6)
reverb_data_1 = reverb_df_1["reverb"].values
reverb_data_1 = reverb_data_1.reshape(4,6)

#een functie om de figure voor de heatmap op te zetten en de data erin te zetten
def plot(reverb_data,index):
    fig, ax = plt.subplots() #de axes aanmaken en formaten om het goeie gridsysteem aan te geven
    ax.set_xticklabels(['',"F","E","D","C","B","A"])
    ax.set_yticklabels(['',1,'',2,'',3,'',4])
    ax.imshow(reverb_data, cmap="hot_r",vmin=0.1,vmax=0.8) #de data in als heatmap in de figure zetten
    for (i, j),z in np.ndenumerate(reverb_data): #de nagalmtijden zelf in het grids zetten
        ax.text(j,i,"{:0.2f}".format(z),ha="center",va="center")
    ax.invert_xaxis() #de x-as omdraaien zodat het overeen komt met de kamer zelf en dit opslaan in de project map
    plt.savefig(rf"C:\Users\huubz\HvA\Duuk Ludding - Project 1.3 groep 1\Heatmaps\Heatmap_{index}.png")
    plt.show()

plot(reverb_data_0,0)
plot(reverb_data_1,1)