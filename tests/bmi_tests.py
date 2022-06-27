import unittest
from src.bmi_calculator import *
from src import *


class TestBMICalculator(unittest.TestCase):
    """
    Unit test cases for bmi_calculator.py
    """

    def test_overweight_count(self):
        """
        Test case for the calculation of overweight people count.
        """
        test_bmi = BMI(TEST_JSON_DATA_FILE)
        test_bmi.read_bmi_data()
        test_bmi.get_bmi_category_health_risk()
        self.assertEqual(test_bmi.get_overweight_count(), 1, "Incorrect overweight count")


    def test_invalid_filename(self):
        """
        Test case for verifying that the script throws an exception if the JSON
        data file wasn't found.
        """
        with self.assertRaises(FileNotFoundError):
            BMI(TEST_JSON_NOT_PRESENT)


    def test_empty_file(self):
        """
        Test case for verifying that the script throws an exception if the JSON
        data file was empty or contained invalid JSON data.
        """
        with self.assertRaises(InvalidBMIDataError):
            test_bmi = BMI(TEST_INVALID_JSON_DATA_FILE)
            test_bmi.read_bmi_data()


    def test_bmi_calculation(self):
        """
        Test case for verifying that the BMI calculation was accurate.
        """
        test_bmi = BMI(TEST_JSON_DATA_FILE)
        test_bmi.read_bmi_data()
        test_bmi.get_bmi_category_health_risk()
        calculated_bmi_values = [round(bmi_row["BMI"], 3) for bmi_row in test_bmi.bmi_data]
        actual_bmi_values = [33.178, 32.489, 23.183, 21.368, 31.25, 29.21]
        self.assertCountEqual(calculated_bmi_values, actual_bmi_values)


    def test_category_calculation(self):
        """
        Test case for verifying that the BMI Category calculation was accurate.
        """
        test_bmi = BMI(TEST_JSON_DATA_FILE)
        test_bmi.read_bmi_data()
        test_bmi.get_bmi_category_health_risk()
        calculated_category_values = [bmi_row["BMICategory"] for bmi_row in test_bmi.bmi_data]
        actual_category_values = ["Moderately obese", "Moderately obese", "Normal weight",
                            "Normal weight", "Moderately obese", "Overweight"]
        self.assertCountEqual(calculated_category_values, actual_category_values)


    def test_health_risk_calculation(self):
        """
        Test case for verifying that the Health risk calculation was accurate.
        """
        test_bmi = BMI(TEST_JSON_DATA_FILE)
        test_bmi.read_bmi_data()
        test_bmi.get_bmi_category_health_risk()
        calculated_health_risk_values = [bmi_row["HealthRisk"] for bmi_row in test_bmi.bmi_data]
        actual_health_risk_values = ["Medium risk", "Medium risk", "Low risk",
                            "Low risk", "Medium risk", "Enhanced risk"]
        self.assertCountEqual(calculated_health_risk_values, actual_health_risk_values)


if __name__ == "__main__":
    unittest.main()
