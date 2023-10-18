import subprocess

def check_service_status(service_name):
    try:
        subprocess.run(['systemctl', 'is-active', '--quiet', service_name])
        print(f"{service_name} is running.")
    except subprocess.CalledProcessError:
        print(f"{service_name} is not running.")

service_name = input("Enter service name: ")
check_service_status(service_name)
