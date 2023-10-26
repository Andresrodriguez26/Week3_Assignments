# Given a string of characters, find the starting and ending position of a given character.
# If character is not found in the string, return [-1, -1].

# Example 1:
# Input: string = 'howdy yall how are you', character = 'h'
# Output: [0, 11]

# Example 2:
# Input: string = 'well would you just look at it', character = 'r'
# Output: [-1, -1]


def characters(string, character):
    result=[]
    for i, x in enumerate(string):
        if character == x:
            result.append(i)
    if result==[]:
        return([-1, -1])
    else:
        return(result)
print(characters('howdy yall how are you', character = 'h'))