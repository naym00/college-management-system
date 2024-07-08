from datetime import datetime
from datetime import date
from help.regex.validator import Validators as Regex
class Five(Regex):
    def uniqueCode(self):
            return f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"[:18]