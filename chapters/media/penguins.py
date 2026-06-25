import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
sns.scatterplot(data=df, y='flipper_length_mm', x='body_mass_g')
plt.savefig('penguins-scatter.png')

sns.lmplot(data=df, y='flipper_length_mm', x='body_mass_g')
plt.savefig('penguins-regression.png')
