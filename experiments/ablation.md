# Auriga-Agent ablations

Verification coverage on the development split.

| configuration              | verified traces | false accepts |
|----------------------------|----------------:|--------------:|
| full contract checking     |            0.94 |          0.01 |
| postcondition only         |            0.91 |          0.06 |
| no verification            |            0.88 |          0.29 |

Contract checking catches most silent tool-contract violations at a small
increase in rejected-but-valid trajectories.
