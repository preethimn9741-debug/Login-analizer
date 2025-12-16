import re
import pandas as pd

# 1. Pattern to match each log line: DATE TIME LEVEL MESSAGE
log_pattern = r"(\d{4}-\d{2}-\d{2}) \S+ (ERROR|WARNING|INFO) (.*)"

logs = []  # this will store each log line as a dict

# 2. Read the log file line by line
with open("app.log", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines

        match = re.match(log_pattern, line)
        if match:
            date, level, message = match.groups()
            logs.append({
                "date": date,
                "level": level,
                "message": message
            })

# 3. Convert to pandas DataFrame
df = pd.DataFrame(logs)

print("Parsed log rows:")
print(df)

# 4. Save parsed data to CSV
df.to_csv("parsed_logs.csv", index=False)
print("\nSaved parsed logs to parsed_logs.csv")

# 5. Create summary: count of each level per day
summary = df.groupby(["date", "level"]).size().reset_index(name="count")
print("\nSummary:")
print(summary)

# 6. Save summary to CSV
summary.to_csv("error_summary.csv", index=False)
print("Saved summary to error_summary.csv")

# 7. Top recurring error messages
error_only = df[df["level"] == "ERROR"]
top_errors = error_only["message"].value_counts().head(5)


print("\nTop error messages:")
print(top_errors)

# 8. Save top errors to CSV
top_errors.to_csv("top_errors.csv")
print("Saved top errors to top_errors.csv")
