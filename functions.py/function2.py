def multiple_items(*args):
    print(args)
    print(type(args))
          

multiple_items("Dave", "John", "Sarah")  #tuple


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(name1="Dave", name2="John", name3="Sarah") # Dictionary

