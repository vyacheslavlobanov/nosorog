import copy
import inspect


def copy_dicts(deep_copy=False):
    def decorator(func):
        def wrap(*args, **kwargs):
            copy_method = "deepcopy" if deep_copy is True else "copy"
            new_args = [getattr(copy, copy_method)(ar) if type(ar) == dict else ar for ar in args]

            try:
                new_kwargs = dict([(kwarg_name, getattr(copy, copy_method)(kwarg_item)) if type(kwarg_item) == dict else
                                   (kwarg_name, kwarg_item) for kwarg_name, kwarg_item in kwargs.items()])
            except TypeError:
                new_kwargs = kwargs
            result = func(*new_args, **new_kwargs)

            return result

        return wrap

    return decorator


def protect_ids(id_names=None):
    def decorator(func):
        def wrap(*args, **kwargs):
            if id_names and isinstance(id_names, list) and set([type(name) for name in id_names]) != {str}:
                raise TypeError("Wrong format of id_names in decorator. Must be list of str.")
            if id_names:
                try:
                    new_kwargs = dict([(kwarg_name, int(kwarg_item)) if kwarg_name in id_names else
                                       (kwarg_name, kwarg_item) for kwarg_name, kwarg_item in kwargs.items()])
                except Exception:
                    raise TypeError("Received the ids of wrong type.")
            else:
                new_kwargs = kwargs
            result = func(args, **new_kwargs)

            return result

        return wrap
    return decorator


def protect_private(allowed_list=None, silent=False):
    def decorator(func):
        def wrap(*args, **kwargs):

            fn = inspect.stack()

            if allowed_list and 'self' in allowed_list and f'self.{func.__name__}(' not in fn[1].code_context[0]:
                if silent:
                    return None
                raise Exception("This method can not be called from other object, use self instead.")
            elif allowed_list and fn[1].function not in allowed_list:
                if silent:
                    return None
                raise Exception("This method protected from not private call.")
            elif allowed_list is None:
                return None

            result = func(*args, **kwargs)

            return result

        return wrap

    return decorator


def protected_call(from_method=None, from_file=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            fn = inspect.stack()
            if from_method is not None and fn[1].function != from_method:
                raise ValueError("This method protected.")
            if from_file is not None and fn[1].filename != from_file:
                raise ValueError("This method protected.")
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator
