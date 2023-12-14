"""
This module defines the is_same_class function for checking exact class matches.

Why no imports:

- Showcases a self-contained solution without external dependencies.

Function:

- is_same_class(obj, a_class): Returns True if obj is an exact instance of a_class, False otherwise.

"""

def is_same_class(obj, a_class):
    return isinstance(obj, a_class) and obj.__class__ == a_class
    #theh eu hu  uy u u huyg
#dyu gki  7e 

