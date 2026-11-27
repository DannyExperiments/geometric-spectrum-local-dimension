"""Exact checks for geometric tail and binary cylinder examples."""
from fractions import Fraction

for ratio in (Fraction(1, 3), Fraction(4, 9), Fraction(1, 5)):
    infinite_relative_tail = ratio / (1 - ratio)
    assert infinite_relative_tail < 1
    for count in range(1, 12):
        finite_relative_tail = sum(ratio**i for i in range(1, count + 1))
        assert finite_relative_tail + ratio**count * infinite_relative_tail == infinite_relative_tail

assert Fraction(4, 9) / (1 - Fraction(4, 9)) == Fraction(4, 5)
for depth in range(1, 15):
    assert 2**depth * Fraction(1, 2**depth) == 1
    assert Fraction(1, 2**depth) == 2 * Fraction(1, 2**(depth + 1))

print("OK: exact geometric tail, q=3 worked-example coefficient and binary cylinder masses")
