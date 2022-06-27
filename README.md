# BMI Calculator
A command-line Python program which calculates BMI from JSON data stored in the
'data/' folder. It also determines BMI Category & Health Risk based on the calculated
BMI value.

## Usage
Run python -m src.bmi_calculator to execute the program by using 'data/data.json'
as the source data file and to write the results to 'data/data_out.json'. The
program also prints the count of overweight records to the console.
Run python -m tests.bmi_tests to execute the unit test-cases for the script.

## Design
Table 1 in the Problem Statement is represented by a Python dictionary, BMI_CATEGORIES,
in 'src/__init__.py'. The low and high values of the BMI ranges correspond to 'low'
and 'high' keys in the dictionary. The BMI Category and Health risk columns are
represented by 'category' and 'health_risk' keys in the dictionary. This
representation allows for easy determination of BMI Category and Health risk in
the get_bmi_category_health_risk() method in the BMI class in bmi_calculator.py.
Other methods of this class loads the JSON data from the source file and also
writes the final data to an out file.

## Testing
The 'tests/bmi_tests.py' script has the test cases for the program. The
'data/test_data.json' has test data that is used by the test cases.
