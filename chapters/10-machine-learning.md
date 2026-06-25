# Machine Learning

> We offer no explanation as to why these architectures seem to work; we attribute their success, as all else, to divine benevolence.
>
>  Noam Shazeer @shazeer2020glu

While it is often helpful to design algorithms to efficiently solve specific problems, it can often be helpful to allow the machine to predict outcomes by learning patterns.

## Linear Regression

What if we want to estimate the lenght of a penguin's flipper? We could measure it, but this seems a little tricky, especially if we are working with a large number of wild penguins.

![Gentoo Penguins](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/2020-11_Kerguelen_Islands_-_Gentoo_penguin_11.jpg/960px-2020-11_Kerguelen_Islands_-_Gentoo_penguin_11.jpg)

What if we could weigh them instead? Could we predict their flipper length? Perhaps we could program a computer to learn this relationship from an appropriate dataset @horst2022palmer. Here's a scatter plot showing penguin flipper length against body mass:

![Flipper length vs body mass](media/penguins-scatter.png)

In order to predict the length of a flipper when only the mass of the penguin is known, we must distill the core idea of this dataset into a formula that we could apply to compute the flipper mass. One simple formula is that of a line:

![Lines on Cartesian Plane](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Linear_Function_Graph.svg/960px-Linear_Function_Graph.svg.png)

Lines can be defined by a **slope** and a **Y-intercept**. We could attempt to manually fit a slope and intercept to our data, but it turns out that we can apply **calculus** to find the best possible line by setting up and **optimization problem** that minimizes the error between each penguins measurements and the prediction from the best fit line. This process is known as **linear regression**, and provides one the the simplest examples of machine learning.

Here's the best fit line produced from our penguin dataset:

![Flipper length vs body mass regression](media/penguins-regression.png)

We can use the properties of the best fit line to predict flipper length for any penguin after we weigh it.

## TODO

- Dot product
- Matrix multiplication
- Cosine distance
- MNIST
- word2vec
- Embeddings
