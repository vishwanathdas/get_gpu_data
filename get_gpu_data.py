import GPUtil
from tabulate import tabulate

def graphics_info():
    gpus = GPUtil.getGPUs()
    gpu_list = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100:.2f}%"  # Formatting load as percentage
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature}C"
        gpu_uuid = gpu.uuid
        
        gpu_list.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory,
            gpu_used_memory, gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    headers = ["ID", "Name", "Load", "Free Memory", "Used Memory", "Total Memory", "Temperature", "UUID"]
    return str(tabulate(gpu_list, headers=headers, tablefmt="pretty"))

if __name__ == "__main__":
    print(graphics_info())
