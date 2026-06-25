import seaborn as sns
import matplotlib.pyplot as plt

def plot_penguins_regression():
    '''
    Load penguins dataset and plot linear regression of flipper length and body mass.

    >>> plot_penguins_regression()
    '''
    df = sns.load_dataset('penguins')
    sns.scatterplot(data=df, y='flipper_length_mm', x='body_mass_g')
    plt.savefig('penguins-scatter.png')

    sns.lmplot(data=df, y='flipper_length_mm', x='body_mass_g')
    plt.savefig('penguins-regression.png')


if __name__ == '__main__':
    plot_penguins_regression()