# Gambler's Fallacy Dice

A Python port of [xori/gamblers-dice](https://github.com/xori/gamblers-dice):

> > The term Gambler's fallacy refers to a misconception about statistics. [...] In statistics, a random event has a certain probability of occurring. The fallacy is that if the event has occurred less frequently in the past, it will be more frequent in the future. -Wikipedia
>
> Well no longer is this a fallacy my friends, these dice are real! If you roll a 20 sided die, and you haven't seen a 20 in a while it is statistically more likely to show up in the next roll with these dice. And the best part, it's still uniformly random for large sample sets!

## How do I use it?

Don't!

## But if I *really* want to?

```python
from gamblersdice import FallacyDie

die = FallacyDie(20)  # 20-sided die

print(die.roll())  # A number from 1 to 20
print(die.roll())  # Keep using the same die
```
