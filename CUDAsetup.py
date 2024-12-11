import os
import torch
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"  # Ensure consistent GPU ordering
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Select the GPU to use (0 = first GPU)
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version: {torch.version.cuda}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"Number of GPUs: {torch.cuda.device_count()}")
print("Current Device:", torch.cuda.current_device())
print("Device Name:", torch.cuda.get_device_name(torch.cuda.current_device()))