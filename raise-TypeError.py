# Raise TypeError
numss = "abir"

if not type(numss) is int:
    raise TypeError("Only integers are allowed")