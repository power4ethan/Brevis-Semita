import arrayfire as af
## Initalize GPU(s)
af.set_backend('opencl')

# Testing 
print(af.device.info_str())

## Quantify avaliable resources based on GPU data

## Collect Processing Power of each device
deviceCount = af.device.get_device_count()
for i in range(deviceCount):


## Visualization Function to be ran in main.py loop



