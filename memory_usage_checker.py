import psutil

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    print(f"Total Memory: {memory_info.total // (2**30)} GB")
    print(f"Available Memory: {memory_info.available // (2**30)} GB")
    print(f"Used Memory: {memory_info.used // (2**30)} GB")
    print(f"Memory Percentage Used: {memory_info.percent}%")

check_memory_usage()
