

ci_target = "<= -49.5 gCO2/MJ"
ts_ci = float(ci_target.split()[-2].replace(',', '.'))  # Extract number

print(ts_ci)  # Output: -49.5