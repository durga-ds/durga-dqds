# Python function to convert a CamelCase string to snake_case
def to_snake(given):
    snake = given[0].lower()
    return (snake + ''.join( '_'+l.lower() if l.isupper() else l for l in given[1:]) )
