# /// script
# dependencies = [
#     'seaborn',
# ]
# ///

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
sns.scatterplot(data=df, x='body_mass_g', y='flipper_length_mm')
plt.savefig('penguins-scatter.png')

sns.lmplot(data=df, x='body_mass_g', y='flipper_length_mm')
plt.savefig('penguins-regression.png')
