from django.test import TestCase


class TestValidators(TestCase):

    def setUp(self):
        self._min = 3
        self._max = 13

    # def test_check_value_len(self):
    #     value = 'Abracadabra'
    #     self.assertEqual(check_value_len(self._min, self._max, value), True)
    #
    # def test_check_value_len_bad_min(self):
    #     value = 'Ab'
    #     with self.assertRaises(ValueError):
    #         check_value_len(self._min, self._max, value)
    #
    # def test_check_value_len_bad_max(self):
    #     value = 'Abadsfasdfasdfadf'
    #     with self.assertRaises(ValueError):
    #         check_value_len(self._min, self._max, value)
    #
    # def test_check_value_is_alpha(self):
    #     value = 'Abra-bra'
    #     self.assertEqual(check_value_is_alpha(value), True)
    #
    # def test_check_value_is_alpha_bad(self):
    #     value = 'Abra/bra'
    #     with self.assertRaises(ValueError):
    #         check_value_is_alpha(value)
    #
    # def test_check_value_is_digit(self):
    #     value = '12345678'
    #     self.assertEqual(check_value_is_digit(value), True)
    #
    # def test_check_value_is_digit_bad(self):
    #     value = 'a1234567a'
    #     with self.assertRaises(ValueError):
    #         check_value_is_digit(value)
