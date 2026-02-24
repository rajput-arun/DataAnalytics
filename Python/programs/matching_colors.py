"""

Count Matching Socks


We have a box with socks of various colors. We take 2 socks of the same color and set them aside. The first pair may be red, the second green, and the third red again.

Create a function count_matching_socks that:

Takes an array of numbers colors, where each number represents a sock's color.
Returns the maximum number of pairs (two equal numbers) we can take from the box.
Examples:

count_matching_socks([10, 10])  # 1 pair of socks with color 10
count_matching_socks([2, 2, 2, 2, 2])  # 2 pairs of socks with color 2
count_matching_socks([10, 20, 30, 40, 50, 60])  # 0 pairs, all socks have different colors
count_matching_socks([10, 20, 30, 10, 20, 60])  # 2 pairs, one of color 10 and one of color 20

"""

def count_matching_socks(colors: list) -> int:
    counts={}
    pairs=0
    for color in colors:
        counts[color] = counts.get(color, 0) + 1

    for count in counts.values():
        pairs += count//2

    print(counts, pairs)

    return pairs

#count_matching_socks([1])  # 1 pair of socks with color 10
#count_matching_socks([2, 2, 2, 2, 3])
#count_matching_socks([10, 20, 30, 40, 50, 60])  # 0 pairs, all socks have different colors
count_matching_socks([10, 20, 30, 10, 20, 60])  # 2 pairs, one of color 10 and one of color 20

