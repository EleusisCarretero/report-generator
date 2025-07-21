# 1 manager
from basic_report import BasicReport, ReportTypes

class JestReporter(BasicReport):
    TYPE = ReportTypes.JEST

    def __init__(self, **kwars):
        super().__init__(self.TYPE)
        self.global_results = kwars["global_results"] # cake grafic

    def generate_global_result(self):
        # 1 Generate cake grafic
        self.generate_cake_grafic(**self.global_results)
