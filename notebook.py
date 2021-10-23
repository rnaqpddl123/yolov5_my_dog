import torch
import tensorflow as tf
import torch

print(torch.cuda.device_count())
print(torch.version.cuda)
print(torch.version)
print(torch.cuda.is_available())

print("-----------------------------")
torch.zeros(1).cuda()