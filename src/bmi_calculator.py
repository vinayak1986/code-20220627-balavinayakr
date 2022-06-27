import json
from pathlib import Path
import sys
import errno
import os
from src import *


class InvalidBMIDataError(Exception):
    """
    Custom Exception for a blank/invalid JSON data file.
    """
    pass


class BMI:
    """
    BMI Class with methods to read BMI data from a JSON file, calculate
    BMI, BMI category and Health risk from it.
    """

    def __init__(self, data_file = None):
        """
        Constructor with default JSON data at 'data/data.json'. An object can
        be overridden with a different data path.
        """
        if not data_file:
            self.json_data_file = JSON_DATA_FILE
        else:
            self.json_data_file = data_file

        # Throw an error if the data path is invalid.
        if not Path(self.json_data_file).is_file():
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.json_data_file)
        self.bmi_data = None
        self.bmi_categories = BMI_CATEGORIES
        self.overweight_count = 0


    def read_bmi_data(self):
        """
        Read JSON data from the data path. Throw an error if the file was
        empty or if no valid JSON lines were present in it.
        """

        list_of_bmi_data = []
        try:
            with open(self.json_data_file, "r") as file:
                for line in file:
                    list_of_bmi_data.append(json.loads(line))
        except:
            pass
        if not list_of_bmi_data:
            raise InvalidBMIDataError("Empty/invalid BMI data file.")
        self.bmi_data =  list_of_bmi_data


    def get_bmi_category_health_risk(self):
        """
        Calculate BMI, BMI Category and Health risk for each row from
        the JSON file.
        """

        for bmi_data_row in self.bmi_data:
            # BMI = Weight (in KG) / Height (in Meter) ^ 2
            bmi = bmi_data_row["WeightKg"] / ( (bmi_data_row["HeightCm"] / 100) ** 2 )
            # Find the correct range where the calculated BMI value falls in.
            bmi_categories = tuple(filter( lambda x : bmi >= x["low"] and bmi < x["high"], self.bmi_categories))
            # Get BMI category and health risk from the correct range.
            category = bmi_categories[0]["category"]
            health_risk = bmi_categories[0]["health_risk"]
            # Store the calculated values in the JSON file.
            bmi_data_row["BMI"] = bmi
            bmi_data_row["BMICategory"] = category
            bmi_data_row["HealthRisk"] = health_risk


    def get_overweight_count(self):
        """
        Filter self.bmi_data by BMICategory = 'Overweight' to get the count
        of people who are overweight, i.e., with BMI in the 25 - 29.9 range.
        """
        filtered_overweight_data = tuple(filter(lambda x : x["BMICategory"] == "Overweight", self.bmi_data))
        self.overweight_count = len(filtered_overweight_data)
        return self.overweight_count


    def write_bmi_data_to_file(self):
        """
        Write the final BMI data to a file.
        """
        with open(JSON_OUT_FILE, "w") as file:
            for row in self.bmi_data:
                json.dump(row, file)
                file.write('\n')


if __name__ == '__main__':
    bmi = BMI(JSON_DATA_FILE)
    bmi.read_bmi_data()
    bmi.get_bmi_category_health_risk()
    print(bmi.get_overweight_count())
    bmi.write_bmi_data_to_file()
