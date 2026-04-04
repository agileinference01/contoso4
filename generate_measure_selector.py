#!/usr/bin/env python3
"""
Generate Measure Selector DAX code from _MeasureCatalog data
"""

# Metric names from _Metrics.tmdl
metrics = [
    "Sales - Actual",
    "Sales - Goal (FactSalesQuota)",
    "Sales - Goal Achievement %",
    "Sales - Strategic Plan Goal",
    "Sales - vs Strategic Plan %",
    "Units - Actual",
    "Units - Goal (FactSalesQuota)",
    "Units - Goal Achievement %",
    "Units - Store",
    "Units - Online",
    "Gross Profit - Actual",
    "Gross Profit - Goal",
    "Gross Profit - Goal Achievement %",
    "Gross Margin %",
    "Sales - Store Channel",
    "Sales - Online Channel",
    "Online Sales % of Total",
    "Store Sales % of Total",
    "Discounts - Total",
    "Discount Rate % of Sales",
    "Returns - Total",
    "Return Rate % of Sales",
    "Cost of Goods Sold",
    "Customers - Unique",
    "Avg Transaction Value",
    "Customer Lifetime Value",
    "Stores - Count",
    "Avg Sales per Store",
    "Machine - Total Downtime (Hours)",
    "Machine - Count with Downtime",
    "Machine - Avg Downtime per Machine",
    "Machine - Outage Incidents",
    "Machine - Total Maintenance Cost",
    "Machine - Preventive Maintenance Cost",
    "Machine - Emergency Maintenance Cost",
    "Machine - Preventive % of Total Cost",
    "Machine - Emergency % of Total Cost",
    "Machine - Cost per Store",
    "Machine - SLA Uptime Goal %",
    "Machine - Actual Uptime %",
    "Machine - SLA Compliance %",
    "HR - Employees Total",
    "HR - Headcount per Store",
    "HR - Sales per Employee",
    "HR - Units per Employee",
    "HR - Productivity Score",
]

def sanitize_measure_name(name):
    """Convert metric name to valid measure name"""
    # Replace special chars and spaces with underscores
    sanitized = name.replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "").replace("%", "pct").replace("&", "and").replace("/", "_")
    # Remove consecutive underscores
    while "__" in sanitized:
        sanitized = sanitized.replace("__", "_")
    return sanitized.strip("_")

# Build DAX measure selector
dax_lines = [
    "Measure Selector = ",
    "var _sel = SELECTEDVALUE('_MeasureCatalog'[Metric Name])",
    "return",
    "SWITCH(_sel,"
]

for metric in metrics:
    measure_name = "[" + sanitize_measure_name(metric) + "]"
    dax_lines.append(f'    "{metric}", {measure_name},')

# Add default case
dax_lines.append("    BLANK()")
dax_lines.append(")")

# Output
print("\n".join(dax_lines))
