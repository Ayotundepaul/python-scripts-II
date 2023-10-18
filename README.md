
---

# 🛠️ **DevOps Engineer/SRE Python Toolkit**

This repository contains a collection of Python scripts tailored for DevOps Engineers and Site Reliability Engineers to help automate and monitor various system and network tasks.

## 📜 **Contents**

1. 📊 **Disk Usage Checker**: 
    - Provides a summary of disk usage for a specified path (defaults to root).
    - Usage: `python disk_usage_checker.py`

2. 🖥️ **Memory Usage Checker**: 
    - Gives a detailed report on system memory usage.
    - Usage: `python memory_usage_checker.py`

3. 🔄 **Service Status Checker**: 
    - Checks if a specified system service is running.
    - Usage: `python service_status_checker.py`

4. 🗂️ **Bulk File Organizer**: 
    - Organizes files in a directory based on their extensions. It creates folders for each extension and moves the files into the appropriate folder.
    - Usage: `python bulk_file_organizer.py`

5. 📊 **Log Analyzer**: 
    - Analyzes a log file and reports the count of `ERROR` and `WARN` messages.
    - Usage: `python log_analyzer.py`

## 🚀 **Setup and Usage**

1. **Clone the Repository**:
    ```bash
    git clone git@github.com:Ayotundepaul/python-scripts-II.git
    cd python-scripts
    ```

2. **Run the Scripts**:
    - Each script can be run using the Python interpreter. Follow the usage instructions under each script in the **Contents** section.

3. **Dependencies**:
    - Some scripts may require additional Python libraries. Ensure you have them installed using `pip`. For example:
        ```bash
        pip install psutil
        ```

🔧 **Note**: Make sure to have the necessary permissions when running scripts that access system services or directories.

---

This README provides a clear overview of each script, its functionality, and usage instructions.