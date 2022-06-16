from nosorog.decorators.base_decorator import BaseDecorator
from nosorog.exceptions import NosorogWrongPlaceCallError, NosorogMangledNameError, NosorogTypeError


class Silent(BaseDecorator):
    __exceptions = (NosorogWrongPlaceCallError, NosorogMangledNameError, NosorogTypeError)

    def __init__(self, func, exceptions=None):
        if exceptions:
            self.__exceptions = tuple(exceptions)

        super().__init__(func=func)

    def __call__(self, obj, *args, **kwargs):
        try:
            result = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            # catch Exception, compare it with DecoratorMessages, return None if message in list
            if isinstance(ex, self.__exceptions):
                result = None
            else:
                raise ex

        return result

    @classmethod
    def include(cls, exceptions):
        exceptions = exceptions or ()
        exceptions = (*cls.__exceptions, *exceptions)
        return lambda func: cls(func, exceptions)

    @classmethod
    def exclude(cls, exceptions):
        exceptions = tuple(set(cls.__exceptions) - set(exceptions))
        return lambda func: cls(func, exceptions)
