# Knowledge Representation

In order to be effective in many environments, agents need knowledge about their world. This involves the creation and curation of a **knowledge base**.

Before we can construct a method to store and access data. We need to describe data in a manner in which the computer can handle. This formal description of knowledge is known as an **ontology**.

One way to begin to construct an ontology is to consider different categories of entities using **set theory** and first-order logic. For example, here's one way categorize my shoe:

$MyShoe \in Shoes \subset Footwear \subset Clothing \subset PhysicalObjects \subset Anything$

Breaking that down from left to right, we begin by stating that $MyShoe$ is a member of ($\in$) the $Shoes$ category. $Shoes$ is then a proper subset ($\subset$) of $Footwear$. This pattern follows up a tree of entities rooted at $Anything$.

Reasoning could begin to happen via categories rather than entities. If I were to query a knowledge base to ask where I should go to replace $MyShoe$, it could provide a list of stores that sell $Clothing$.

Let's consider a self-driving car example. $Vehicles$ would certainly be a helpful category. It could be connected to the following categories:

$Vehicles \subset PhysicalObjects \subset Anything$

$Cars \subset Vehicles$

$Trucks \subset Vehicles$

$ParkedCars \subset Cars$

$MyCar \in Cars$

Mapping reality onto an ontology is an immense task. While it would be handy if a universal ontology existed, such a project is likely to be impossible to complete, there are many bits of knowledge that are true for some people and untrue for others. For an example of a project that attempts to build a large knowledge base, consider **wikidata**.

For many practical applications, a complete and universal consensus ontology is not required. A self-driving car needs to have robust knowledge about many elements of the environment, but it is likely not necessary for it to know that **Han shot first**.

Knowledge Base
--------------

- Central component of knowledge-based agents
- Stores knowledge as **sentences** in a knowledge representation language asserting facts about the world

Updates
-------

- Tell - Add new information
- Ask - query for information

Ontologies
----------

- Formal representations of knowledge in a domain
- Ontology engineering studies the methodologies for building useful ontologies
- [More info](https://en.wikipedia.org/wiki/Ontology_(information_science))

---

![Upper Ontology](media/upper-ontology.png)

Categories
----------

- Group similar objects
- Reasoning often takes place at the level of categories
- For example, a self-driving car will make decisions about pedestrians as a category without considering which individual pedestrians are nearby

First-order logic
-----------------

- Treating categories as objects in first-order logic can provide useful reasoning tools
- Membership: ${Bob} \in {Students}$
- Subcategories: ${Students} \subset {People}$

Inheritance
-----------

- Reasoning can be inherited through categories
- If we know that people have birthdates, then we know that Bob has a birthdate

Taxonomies
----------

- We can use properties of objects to create further categories

$$
\begin{gather}
Orange(x) \land Round(x) \land \\ 
Diameter(x) = 9.5 \land x \in Balls \Rightarrow \\
x \in Basketballs
\end{gather}
$$

---

What is a bird?

What is a reptile?

Disjoint subcategories
----------------------

- Set of subcategories that have no members in common
- For example, {trucks, scooters} could be defined as disjoint subcategories of vehicles

Exhaustive Decomposition
------------------------

- A set of subclasses that contain all members of the parent class
- For example, {vowel, consonant} would be an exhaustive decomposition of letters

Partition
---------

- An exhaustive decomposition that is also disjoint.
- For example, {First-years, sophomores, juniors, seniors} is a partition of undergrad students.

Physical Composition
--------------------

- In addition to subsets, it can be helpful to denote how different entities relate to one another
- For example, counties in Indiana would be a part of Indiana

Composite Objects
-----------------

- Characterized by relations among parts

Natural kinds
-------------

- Real objects are imperfect
- A logical agent may care more about understanding what is typical
- How would a logical agent tell a deformed peach from a deformed apple?

Time Intervals
--------------

- Many facts only apply when specific other qualifiers, such as time, are satisfied
- It can be useful to think of entities in the abstract, in additional to the concrete
- Who is the president of the United States?

President
---------

- When the Constitution refers to the president, it is not referring to a particular individual
- We often do want to refer to specific people who held the position

---

![View of President(USA)](media/12-3.png)

## What are Expert Systems?

- AI systems that mimic human decision making
- Use knowledge and reasoning to solve complex problems

## Key Components

- **Knowledge Base**: Stores facts and rules
- **Inference Engine**: Applies rules to facts to derive new knowledge

## History

- Developed in the 1970s and 1980s
- Pioneered by researchers like Edward Feigenbaum

## MYCIN

- Early backward chaining expert system
- Diagnosed bacterial infections
- Recommended antibiotics
- Achieved 65% accuracy, better than some human experts

## Example Rule

```lisp
(defrule 52
 if (site culture is blood)
  (gram organism is neg)
  (morphology organism is rod)
  (burn patient is serious)
 then .4
  (identity organism is pseudomonas))
```

## How They Work

- **Forward Chaining**: Start with known facts, apply rules to derive new facts
- **Backward Chaining**: Start with a goal, work backward to find supporting facts

## Forward Chaining Example

```python
rules = {
    "R1": {"if": "A", "then": "B"},
    "R2": {"if": "B", "then": "C"}
}

facts = ["A"]

def forward_chain(rules, facts):
    while True:
        new_facts = []
        for rule in rules.values():
            if rule["if"] in facts and rule["then"] not in facts:
                new_facts.append(rule["then"])
        if not new_facts:
            break
        facts.extend(new_facts)
    return facts

print(forward_chain(rules, facts))
```

## Backward Chaining Example

```python
rules = {
    "R1": {"if": "A", "then": "B"},
    "R2": {"if": "B", "then": "C"}
}

goal = "C"

def backward_chain(rules, goal, facts):
    if goal in facts:
        return True
    for rule in rules.values():
        if rule["then"] == goal:
            if backward_chain(rules, rule["if"], facts):
                return True
    return False

facts = ["A"]
print(backward_chain(rules, goal, facts))
```

---

![Backward chaining](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/BackwardChaining_David_C_England_1990_p21.gif/960px-BackwardChaining_David_C_England_1990_p21.gif)

## Limitations

- **Scalability**: Difficult to manage large knowledge bases
- **Maintenance**: Requires frequent updates and expert knowledge
- **Flexibility**: Limited to predefined rules and facts

## Modern Applications

- **Medical Diagnosis**: IBM Watson for Oncology
- **Financial Services**: Fraud detection systems
- **Customer Support**: Chatbots and virtual assistants

---

What are the key differences between expert systems and machine learning?

---

How do expert systems handle uncertainty and incomplete information?

---

What are some potential ethical concerns with using expert systems in critical domains?


## Wikidata

Wikipedia
---------

- Encyclopedia that anyone can edit
- Over 300 editions of Wikipedia in different languages
- A single factual update requires editors to change 300 pages

---

> Wikidata is a collaboratively edited multilingual knowledge graph

> document-oriented database, focused on items, which represent topics, concepts, or objects

Entities
--------

- Identified by a unique id
- Description
- Optional aliases
- Statements

Claims
------

- Map values to properties of an entity
- Organized in groups of values mapped to properties
- Qualifiers determine when claims are applicable

Statements
----------

- Claims that include references
- Include rank to distinguish between multiple claims for the same property

Snak
----

> refers to the combination of a property and either a value or one of the special cases "no value" and "unknown value". Snaks can be found in claims (then they are called main snaks) or in qualifiers as part of statements (then they are called qualifier snaks)

---

![Data Model](https://upload.wikimedia.org/wikipedia/commons/a/ae/Datamodel_in_Wikidata.svg){height=540px}

---

Database size?

---

Over 90 million entities

---

~90GB gzipped json as of 2021

More Information
----------------

- [Introduction](https://www.wikidata.org/wiki/Wikidata:Introduction)
- [Glossary](https://www.wikidata.org/wiki/Wikidata:Glossary)

API
---

- [Search example](https://www.wikidata.org/w/api.php?action=wbsearchentities&search=Anderson%20University&language=en)
- [Entity JSON example](https://www.wikidata.org/wiki/Special:EntityData/Q4754216.json)

## Application

A project to explore using **wikidata** to respond to natural language queries in a specific format is available here:

<https://github.com/jncraton/qa>
