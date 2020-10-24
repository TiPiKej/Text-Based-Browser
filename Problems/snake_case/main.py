def to_snake_case(camel):
    snake = ""
    for ch in camel:
        if ch.islower():
            snake += ch
        else:
            snake += "_" + ch.lower()
    return snake


word = input()

print(to_snake_case(word))
