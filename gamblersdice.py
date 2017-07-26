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
        probs = self._rolls_since_last_hit / float(total_rolls)
        return probs

    def _update_roll_counter(self, result):
        """
        Increment each side's roll count, except for the most recent roll which
        is set back to 1.
        """
        self._rolls_since_last_hit += 1
        self._rolls_since_last_hit[result] = 1
        return None

    def roll(self):
        """ Roll the die and return the result. """
        result = np.random.choice(
            range(self.sides),
            p=self._weights
        )
        self._update_roll_counter(result)
        result += 1  # Account for zero-indexing
        return result
