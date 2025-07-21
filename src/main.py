import yaml
import argparse
from basic_report import ReportTypes
from jest.jest_reporter import JestReporter


# Select type of report
def select_reporter(type):
    return {
        ReportTypes.JEST: generate_report_jest,
        
    }.get(type)


# Report genration: JEST
def generate_report_jest(jest_argumets):
    jest_reporter = JestReporter(**jest_argumets)
    jest_reporter.generate_global_result()



if __name__ == "__main__":
    parse = argparse.ArgumentParser(
        prog='ReporGenerator',
        description='This script is able to generate different types of reports',
        epilog='Report generated',
    )
    parse.add_argument("-t", "--type", help=f"Type report. Available options: {ReportTypes}", default="JEST")
    parse.add_argument("-a", "--argumets_path", help="The path to the yaml file to get argumets", default="src/jtes_args.yaml")

    args = parse.parse_args()
    report_type = args.type
    report_args_path = args.argumets_path
    with open(report_args_path, 'r') as f:
        arguments = yaml.load(f, Loader=yaml.FullLoader)
    select_reporter(report_type)(arguments)

