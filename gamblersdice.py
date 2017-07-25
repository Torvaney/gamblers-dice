import numpy as np


class FallacyDie(object):
    """
    A die that respects the Gambler's fallacy. Rolling the die is more likely to
    return a result that has not been seen for a while.
    """
    def __init__(self, sides=6):
        self.sides = sides
        self._rolls_since_last_hit = np.ones(sides)

    def __repr__(self):
        return 'FallacyDie(sides={0})'.format(self.sides)

    @property
    def _weights(self):
        """
        Calculate the relative probability of each result based on the number of
        rolls since it last occurred.
        """
        total_rolls = sum(self._rolls_since_last_hit)
        probs = [r / float(total_rolls) for r in self._rolls_since_last_hit]
        return probs

    def _update_roll_counter(self, result):
        self._rolls_since_last_hit += 1
        self._rolls_since_last_hit[result] = 1

    def roll(self):
        result = np.random.choice(
            range(self.sides),
            p=self._weights
        )
        self._update_roll_counter(result)
        result += 1  # Account for zero-indexing
        return result
