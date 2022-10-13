import warnings


def warn(fn):
    def wrapper(*args, **kwargs):
        warnings.warn('Message')
        return fn(*args, **kwargs)
    return wrapper


@warn
def foo():
    return 0
