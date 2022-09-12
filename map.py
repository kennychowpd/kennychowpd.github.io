def main():
    yell(["Top", "of", "the", "morning", "to", "you", "lad!"])
    
    
def yell(words):
    ## for loop generator
    #     uppercased = []
    #     for word in words:
    #     uppercased.append(word.upper())
    ## list comprehension
    # uppercased = [word.upper() for word in words]
    ## map
    uppercased = map(str.upper, words)
    print(*uppercased)
