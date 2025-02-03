import os
import json
import platform
from datetime import datetime

env_data = {
    "Test Execution Time": str(datetime.now()),
    "OS": platform.system(),
    "OS Version": platform.version(),
    "Python Version": platform.python_version(),
    "JMeter Version": "5.5",
    "Taurus Version": "1.16.8",
    "Machine Name": platform.node(),
    "Processor": platform.processor(),
}

with open("reports/allure-results/environment.json", "w") as f:
    json.dump(env_data, f, indent=4)

print("✅ Allure environment details and execution logs generated successfully.")
