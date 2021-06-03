def has_method(o, name):
    return callable(getattr(o, name, None))
