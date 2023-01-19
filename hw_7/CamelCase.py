#import re

#def camel(underline: str):
    #sub = re.sub(r"(-\w)", lambda x: x.group(1)[1].upper(), underline)
    #return sub

#print(camel("the-stealth-warr"))

def cover_to_camel_case(array: str):
    new_array = array.replace("_", "").replace("_", "").split()
    if len(new_array) == 0:
        return "error"
    return new_array[0] + " ".join([x.capitalize()]) for x in new_array[1:]
print(cover_to_camel_case())


