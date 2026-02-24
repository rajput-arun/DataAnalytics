"""
Bob has a row of stones on his table:

R for red
G for green
B for blue
Help Bob determine the minimum number of stones to remove so that no two adjacent stones are the same color.

color_stones("RRGB") == 1  # Remove 1 "R"; Result: "RGB"
color_stones("RRGGB") == 2  # Remove 1 "R" and 1 "G"; Result: "RGB"
color_stones("RRRRGB)") == 3  # Remove 3 "R"; Result: "RGB"
color_stones("RGBRGBRGGB") == 1  # Remove 1 "G"; Result: "RGBRGBRGB"
color_stones("RGGRGBBRGRR") == 3  # Remove 1 "G", 1 "B", and 1 "R"; Result: "RGRGBRGR"
color_stones("RRRRGGGGBBBB") == 9  # Remove 3 "R", 3 "G", and 3 "B"; Result: "RGB"

"""
def color_stones(stones: str) -> int:
    all_stones = {}
    prev_color = None
    i=ctr=0
    for stone in stones:
        #print(prev_color, stone)
        if stone ==prev_color:
            ctr+=1
        prev_color = stone
    print (ctr)
    return(ctr)

color_stones("RGGRGBBRGRR")
#color_stones("RRGB")
# == 1  # Remove 1 "R"; Result: "RGB"
#color_stones("RRRRGGGGBBBB")
 #== 9)  # Remove 3 "R", 3 "G", and 3 "B"; Result: "RGB"





