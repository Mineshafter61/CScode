f = lambda a,b: print(a+1, f(a+1,b)) if a < b else print()
print(f(4,123))
