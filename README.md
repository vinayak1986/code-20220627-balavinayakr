# BMI Calculator
A command-line Python program which calculates BMI from JSON data stored in the
*data/* folder. It also determines *BMI Category* & *Health Risk* based on the calculated
BMI value. The program prints the count of overweight people to the console, i.e.,
count of people with BMI in the range 25 - 29.9.

## Usage
Run the program by the below steps:
- git clone https://github.com/vinayak1986/code-20220627-balavinayakr.git
- cd code-20220627-balavinayakr/
- python -m src.bmi_calculator (Runs the script and writes the results to data/data_out.json)
- python -m tests.bmi_tests (Runs the unit tests)

## Design
Table 1 in the Problem Statement is represented by a Python dictionary, *BMI_CATEGORIES*,
in *src/\__init__.py*. The low and high values of the BMI ranges correspond to *low*
and *high* keys in the dictionary. The *BMI Category* and *Health risk* columns are
represented by *category* and *health_risk* keys in the dictionary. This
representation allows for easy determination of *BMI Category* and *Health risk* in
the *get_bmi_category_health_risk()* method in the *BMI* class in *src/bmi_calculator.py*.
Other methods of this class loads the JSON data from the source file and also
writes the final data to an out file.

## Testing
The *tests/bmi_tests.py* script has the test cases for the program. The
*data/test_data.json* has test data that is used by the test cases.
