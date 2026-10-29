import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference data
reference = pd.DataFrame({
    "temperature": [20, 21, 22, 23, 21, 22, 20, 24, 23, 21],
    "humidity": [60, 62, 61, 63, 59, 60, 64, 62, 61, 60]
})

# Current data
current = pd.DataFrame({
    "temperature": [30, 31, 32, 29, 33, 31, 30, 32, 34, 31],
    "humidity": [75, 78, 80, 76, 79, 77, 81, 78, 80, 79]
})

# Create Evidently report
report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data=reference,
    current_data=current
)

result.save_html("evidently_report.html")

print("Evidently monitoring completed!")
print("Report saved as evidently_report.html")