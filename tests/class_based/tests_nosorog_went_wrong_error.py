import unittest

from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError
from nosorog.exceptions.nosorog_wrong_place_call_error import NosorogWrongPlaceCallError
from nosorog.exceptions.nosorog_mangled_name_error import NosorogMangledNameError
from nosorog.exceptions.nosorog_type_error import NosorogTypeError
from nosorog.exceptions.nosorog_fake_error import NosorogFakeError
from nosorog.exceptions.nosorog_split_access_exception import NosorogSplitAccessException


class TestNosorogWentWrongError(unittest.TestCase):

    def test_exception_method_subclasses_list(self):
        self.assertEqual(set(NosorogWentWrongError.subclasses_tuple), {NosorogMangledNameError, NosorogTypeError,
                                                                       NosorogWrongPlaceCallError, NosorogFakeError,
                                                                       NosorogSplitAccessException})
