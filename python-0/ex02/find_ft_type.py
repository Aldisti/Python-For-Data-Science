
def all_thing_is_obj(object: any) -> int:

    clzz = object.__class__

    print(f"{clzz.__name__.capitalize()}: {clzz}")

    return 42

