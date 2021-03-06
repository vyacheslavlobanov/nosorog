class BaseProtectMeta(type):

    @property
    def one_obj(cls):
        return lambda func: cls(func=func, protection_method='block_if_not_self')

    def one_method(cls, method):
        return lambda func: cls(func=func, attrs=method, protection_method='block_if_wrong_method')

    def call_from(cls, methods):
        return lambda func: cls(func=func, attrs=methods, protection_method='block_if_not_in_list')
