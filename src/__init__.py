# Global constants
JSON_DATA_FILE = "data/data.json"
JSON_OUT_FILE = "data/data_out.json"
TEST_JSON_DATA_FILE = "data/test_data.json"
TEST_INVALID_JSON_DATA_FILE = "data/test_data2.json"
TEST_JSON_NOT_PRESENT = "data/test_data1.json"
# Table 1 in the problem statement is represented as a dictionary with the lower and
# upper values of the BMI ranges stored as 'low' and 'high' keys. 'category' and
# 'health_risk' keys are BMI Category and Health risk from Table 1.
BMI_CATEGORIES = [
{ 'low' : 0, 'high' : 18.5, 'category' : 'Underweight', 'health_risk' : 'Malnutrition risk'},
{ 'low' : 18.5, 'high' : 25, 'category' : 'Normal weight', 'health_risk' : 'Low risk'},
{ 'low' : 25, 'high' : 30, 'category' : 'Overweight', 'health_risk' : 'Enhanced risk'},
{ 'low' : 30, 'high' : 35, 'category' : 'Moderately obese', 'health_risk' : 'Medium risk'},
{ 'low' : 35, 'high' : 40, 'category' : 'Severely obese', 'health_risk' : 'High risk'},
{ 'low' : 40, 'high' : 1e10, 'category' : 'Very severely obese', 'health_risk' : 'Very high risk'}
]
