import time

import torch
from thop import profile
from torchvision import models
from models.common import DCNv2,CoordConv,Conv
model = DCNv2(3,3,3)
img = torch.zeros((1, 3, 256, 256))
flops, params = profile(model, inputs=(img,), verbose=False)
s=time.time()
model(img)
time_s=(time.time()-s)
print(f'{model}',time_s,flops*(10**-9),params)