import os
from enum import Enum
import matplotlib.pyplot as plt
from utils.json_utils import JsonUtilsException, read_json_file

class ReportTypes(str, Enum):
    JEST = "JEST"

class BasicReport():

    DEFAULT_CAKE_PARAMS = {
        'autopct': "%1.1f%%",
        'startangle': 110,
        'shadow': {
            'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9
        },
        'frame': True,
        'pctdistance': 0.5,
        'labeldistance': 1.1,
        'textprops': {
            'fontsize': 10, 'color': 'black', 'weight': "bold"
        },
        'wedgeprops': {
            'edgecolor': "black", 'linewidth': 2
        },
        'colors': ["green", "red", "gray", "orange"],
        'explode': (0, 0.2)
    }

    def __init__(self, type_report):
        self.type_report = type_report
        self.absolute_folder_report = os.path.abspath(os.path.join(os.path.dirname( __file__ ), type_report.lower(), 'results'))
    
    def generate_cake_grafic(
            self,
            source_path:str,
            graph_name:str,
            title:str,
            fields:list,
            total:int=None,
            new_fields:list=[],
            **kwargs
            ):
        try:
            json_value = read_json_file(source_path)
        except JsonUtilsException as e:
            print(f"Json file does not have a valid value: {e}")
    
        total = total or sum([v for k, v in json_value.items() if k in fields])
        kwargs = kwargs or self.DEFAULT_CAKE_PARAMS
        porcentages = {}
        if not new_fields:
            for field in fields:
                porcentages[field] = (json_value[field] / total) * 100
        else:
            for field, new_field in zip(fields, new_fields):
                porcentages[new_field] = round((json_value[field] / total) * 100, 2)
        print(f"Fields extracted with theri values: {porcentages}")
        # creates grafi c
        plt.pie(list(
            porcentages.values()),
            labels=list(porcentages.keys()),
            **kwargs
        )
        #Title
        plt.title(title)
        plt.savefig(os.path.join(self.absolute_folder_report, f"{graph_name}.png"))

       