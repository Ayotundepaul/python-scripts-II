def analyze_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        error_count = sum(1 for line in lines if "ERROR" in line)
        warn_count = sum(1 for line in lines if "WARN" in line)
    print(f"ERROR count: {error_count}")
    print(f"WARN count: {warn_count}")

file_path = input("Enter path to log file: ")
analyze_log(file_path)
