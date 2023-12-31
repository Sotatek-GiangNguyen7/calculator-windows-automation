from decimal import Decimal
import decimal
import unittest
import pyautogui
import uiautomation as automation
import time
import subprocess
import xmlrunner
import HtmlTestRunner
import sys
sys.path.append('core/helper/')
sys.path.append('source/')
from calculator import Calculator
from data_programmer_mode import test_data_programmer_mode
from data_operation import test_data_standard_mode
from parameterized import parameterized
automation.uiautomation.SetGlobalSearchTimeout(15)
calculator_object = Calculator()
class CalculatorAutomationTest(unittest.TestCase):

    def setUp(self):
        # Open Windows Calculator
        pyautogui.press('win')
        pyautogui.write('Calculator')
        pyautogui.press('enter')
        calculator_object.get_windows()
        time.sleep(1)
    def tearDown(self):
        # Close the Calculator window
        pyautogui.hotkey('alt', 'f4')

    @parameterized.expand(test_data_standard_mode)
    def test_standard_mode(self, a, operator, b):
        calculator_object.click_to_navigate()
        calculator_object.click_to_mode('Standard Calculator')

        calculator_object.perform_calculation(a, operator, b)
        # Verify result
        self.assertEqual(str(eval(f"{a} {operator} {b}")), calculator_object.get_calculator_result() ,"Test Addition Failed")

    @parameterized.expand(test_data_programmer_mode)
    def test_programmer_mode(self, num):
        #navigate to programmer mode
        calculator_object.click_to_navigate()
        calculator_object.click_to_mode('Programmer Calculator')

        #input number to calculator
        calculator_object.enter_number(num)


        #verify result
        calculator_object.click_to_display_values('HEX')
        self.assertEqual(hex(num).upper()[2:], calculator_object.get_calculator_result())
        calculator_object.click_to_display_values('DEC')
        self.assertEqual(str(num), calculator_object.get_calculator_result().replace(',', ''))
        calculator_object.click_to_display_values('OCT')
        self.assertEqual(calculator_object.add_space(oct(num)[2:]), calculator_object.get_calculator_result())
        calculator_object.click_to_display_values('BIN')
        self.assertEqual(calculator_object.binary_format(num), calculator_object.get_calculator_result().replace(' ', ''))

if __name__ == '__main__':
    unittest.main()
