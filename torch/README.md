# Prerequisites

[Install Python3.9 on Ubuntu 16.04 LTS](https://websiteforstudents.com/how-to-install-python-3-8-on-ubuntu-18-04-16-04/)

- Manually way verified and don't mess up the installing order.

[Show graphics card:]()

'''
    lspci | grap VGA
    # or
    sudo lshw -C video
'''

[Ubuntu 16.04 LTS installing torchvision also installed torch](https://github.com/pytorch/vision)

'''
    pip3 install torchvision

    pip3 list
    Package           Version
    ----------------- -------
    numpy             1.19.4
    Pillow            8.0.1
    pip               20.2.3
    setuptools        49.2.1
    torch             1.7.1
    torchvision       0.8.2
    typing-extensions 3.7.4.3
'''

matplotlib

'''
    # optional
    # py -m pip install Pillow ?
    pip3 install Pillow

    pip3 install matplotlib
'''

# tip

Check and set pip in windows:

'''
    pip --version
'''

set path to python39/pip:

'''
    C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python39\\Scripts
'''

https://stackoverflow.com/a/65045676

## ReadTimeoutError: HTTPSConnectionPool ?

'''
    raise ReadTimeoutError(self._pool, None, "Read timed out.")
    pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
'''

Try many times, or

'''
    --default-timeout=100
'''

## Find CUDA version

- Windows 10

nvidia-smi

'''
Sun Jan 31 01:04:18 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 452.06       Driver Version: 452.06       CUDA Version: 11.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 2060   WDDM  | 00000000:01:00.0 Off |                  N/A |
| N/A   36C    P8     9W /  N/A |    164MiB /  6144MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
'''
