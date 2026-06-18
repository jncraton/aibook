# Reflexive Agents

An **intelligent agent** is a system that is able gather input (perceptions) from its environment and act on that environment via actuators. The simplest form of an agent is one that selects an action based only on its current view of the environment with no memory or stored model of the larger world.

![Reflex-based agent](https://upload.wikimedia.org/wikipedia/commons/9/91/Simple_reflex_agent.png)

A robotic vacuum could be implemented a simple reflex-based agent, though it would not be especially efficient.

![A robotic vacuum](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Roomba_original.jpg/330px-Roomba_original.jpg)

## Project

https://github.com/jncraton/vacuum

```python
def agent(percepts, available_actions, previous_actions, state):
    """Handle one agent turn

    :param percepts: dictionary of current percepts (sensor data)
    :param available_actions: List of valid actions
    :param previous_actions: List of all previous actions (most recent last)
    :param state: Initially empty dictionary that can be used to store
    state between calls to the agent function

    Percept descriptions

    - "obstructed" will be True if the path forward is blocked
    - "facing" will be the current direction as one of ["n", "s", "e", "w"]
    - "temp" will be a value between 1 and 100. It will increase by
    1 on each move and decrease 1 on each rest.

    Action descriptions

    "forward" will move forward 1 space
    "left" will turn to the left
    "right" will turn to the right
    "rest" will do nothing. Temperature will decrease by 1

    Returns exactly one action from list of valid actions
    """
```