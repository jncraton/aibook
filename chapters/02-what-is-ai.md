# What is AI?

> Who can produce a single thought,  
> Knowing that we are not able to think a thing  
> About ourselves,  
> By ourselves  
>
> **Guido de Bres**, 1561 [@belgic]

**Artificial intelligence** is the science of making machines do things that would require intelligence if done by humans @minsky1968semantic.

AI is not magic. Many simple computer programs, from spell checkers to tic-tac-toe bots can be considered artificial intelligence. In popular culture, the term may mean something more. There are fears that AI will replace the work of humans. If your role involves checking spelling or playing tic-tac-toe, perhaps you should be concerned about this. Otherwise, our time may be better spent exploring and understanding this science and our human role applying it.

## Intelligence

Intelligence is a complex idea with no singular agreed upon definition.

Are plants intelligent? How would we know? They don't seem to have brains or minds, yet they can change their behaviors based on stimulus from the environment, such as via **phototropism**:

![Phototropism](https://upload.wikimedia.org/wikipedia/commons/0/05/Phototropism_in_Solanum_lycopersicum.gif)

Some plants can even trap and digest prey.

![Dionaea muscipula closing trap](https://upload.wikimedia.org/wikipedia/commons/9/9d/Dionaea_muscipula_closing_trap_animation.gif)

Are insects intelligent? How would we know? They clearly interact with their environment. They may also be able to collaborate with one another to complete larger projects.


![Ants building a bridge](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/AntBridge_Crossing_10.jpg/960px-AntBridge_Crossing_10.jpg)

Are mammals intelligent? We have been able to train mammals in various ways to improve our own lives.

![Mules working in the Grand Canyon](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Mule_train.jpg/960px-Mule_train.jpg)

Are humans intelligent? Most definitions of intelligence assume that humans reside within this category, but how and when does intelligence develop? There are surely differences between a baby, child, and an adult. How would we appropriately measure differences in intelligence?

![Sipke Ernst versus Magnus Carlsen](https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/ErnstCarlsenWijkaanZee2004.jpg/960px-ErnstCarlsenWijkaanZee2004.jpg)

Intelligence is difficult to define, and this makes it difficult to measure progress in artificial intelligence. One approach is to split AI progress into axes of performance and breadth. We can clearly outperform humans in specific areas, but it is harder for an AI to be performant in all areas. The following table is one attempt to lay this out @morris2023levels:

| | Narrow | General |
| :--- | :--- | :--- |
| Level 1: Emerging<br>below 50th percentile of skilled adults | **SHRDLU** @winograd1972understanding and **GOFAI** | Emerging AGI <br> **ChatGPT** @achiam2023gpt or **Google Gemini** @team2023gemini |
| Level 2: Competent <br> at least 50th percentile of skilled adults | **Siri** or **Alexa** | Competent **AGI**<br>Not yet achieved |
| Level 3: Expert <br> at least 90th percentile of skilled adults | spelling & grammar checkers; Imagen @saharia2022photorealistic | Expert AGI<br>Not yet achieved |
| Level 4: Virtuoso <br> at least 99th percentile of skilled adults | **Deep Blue** @campbell1999knowledge, **AlphaGo** @silver2016mastering | Virtuoso AGI<br>Not yet achieved |
| Level 5: Superhuman <br> outperforms 100% of humans | **AlphaFold** @jumper2021highly, AlphaZero @silver2018general, StockFish | **Artificial Superintelligence** (ASI)<br>Not yet achieved |

## Understanding

One challenge for the field artificial intelligence is the tendancy to project human traits onto computer programs when they do work that humans might do. This has been referred to as the **ELIZA effect** after the 1966 ELIZA chatbot @weizenbaum1966eliza. The creator of this early chatbot went on to reflect on this sort of emotional bonding and **anthropomorphism**:

> I knew of course that people form all sorts of emotional bonds to machines, for example, to musical instruments, motorcycles, and cars. And I knew from long ex-perience that the strong emotional ties many programmers have totheir computers are often formed after only short exposures to theirmachines. What I had not realized is that extremely short exposuresto a relatively simple computer program could induce powerful de-lusional thinking in quite normal people. This insight led me toattach new importance to questions of the relationship between theindividual and the computer, and hence to resolve to think about them.
>
> Joseph Weizenbaum @weizenbaum1977computer

At the core of this subject is whether or not a machine that performs tasks that a human performs necessarily understands the world as a human understands it. In his 1714 work exploring what his become known as the **Leibniz's gap**, Gottfried Leibniz framed this as follows:

> It must be confessed that perception and that which depends upon it are inexplicable on mechanical grounds, that is to say, by means of figures and motions. And supposing there were a machine, so constructed as to think, feel, and have perception, it might be conceived as increased in size, while keeping the same proportions, so that one might go into it as into a mill. That being so, we should, on examining its interior, find only parts which work one upon another, and never anything by which to explain a perception.
>
> Liebniz @leibniz1969monadology

Simply because a machine performs a task does not mean that is produces human-like understanding. This concept has been explored from various angles. Another is John Searle's **Chinese Room** thought experiement that argues for the idea that computational work does not require anything like human understanding:

> I will argue that in the literal sense the programmed computer understands what the car and the adding machine understand, namely, exactly nothing. The computer understanding is not just (like my understanding of German) partial or incomplete; it is zero.
>
> John Searle @searle1980minds

Still, it is difficult to prove that a computer is *not* thinking as humans think. As Alan Turing put it:

> May not machines carry out something which ought to be described as thinking but which is very different from what a human does?
>
> Alan Turing @turing2007computing

He proposed the **Turing test** test to determine if a machine is intelligent.

![Turing Test](https://upload.wikimedia.org/wikipedia/commons/5/55/Turing_test_diagram.png)

In the test, an evaluator is allowed to interact with a system using only text without knowing if they are interacting with a human or a computer. If the participant is unable to reliably determine if they are interacting with a human or a computer, then the computer is determined to be intelligent based on the test.

## Disciplines

Some have suggested that human intelligence can be divided into mulitple forms @gardner2011frames. We often break down artificial intelligence problems along similar lines.

Throughout this book, we will use formal language to refer to various specific aspects of artificial intelligence. In particular, we will explore the field by way of the following six more specific disciplines:

- **Natural language processing** allows machines to communicate using English or other human languages.
- **Knowledge representation** is the storage a retrieval of knowledge and information.
- **Automated reasoning** chains knowledge and facts logically to produce correct results.
- **Machine learning** allows computers to improve by explore data or the world.
- **Computer vision** give systems tools to interpret and transform visual data.
- **Robotics** allows computers to interact with and manipulate the physical world.

## Discussion Questions

- What is intelligence?
- How do we measure intelligence?
- Are there different types of intelligence?
- How do we determine if an animal is intelligent?
- How is knowledge acquired?
- Do definitions of intelligence vary between cultures?
