name=["a","b","c","d","e","f","g","h"]
passed=["a","b","c"]

def convert_to_set(data):
    return set(data)

nameset=convert_to_set(name)
passedset=convert_to_set(passed)

failed=nameset.difference(passedset)
print(failed)

