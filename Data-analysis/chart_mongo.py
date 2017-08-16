
import pandas as pd
import matplotlib.pyplot as plt

raw_data = {'language': ['hindi','eng','french','spanish'],
            'value': [100,200 , 300,400],
            }
df = pd.DataFrame(raw_data, columns=['language', 'value'])
print(df)
# Create a list of colors (from iWantHue)
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

# Create a pie chart
plt.pie(
    # using data total)arrests
    df['value'],
    # with the labels being officer names
    labels=df['language'],
    # with no shadows
    shadow=False,
    # with colors
    colors=colors,
    # with one slide exploded out
    #explode=(0, 0, 0, 0, 0.15),
    # with the start angle at 90%
    startangle=90,
    # with the percent listed as a fraction
    autopct='%1.1f%%',
    )

# View the plot drop above
plt.axis('equal')

# View the plot
plt.tight_layout()
plt.show()