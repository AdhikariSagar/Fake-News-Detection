import sys
print (sys.version)
import torch

print(torch.cuda.device_count(), torch.cuda.get_device_name(0), torch.cuda.is_available())