
import sys
import os
from ctypes import *

from mvimport.MvCameraControl_class import *

def check_devices():
    MvCamera.MV_CC_Initialize()
    deviceList = MV_CC_DEVICE_INFO_LIST()
    tlayerType = (MV_GIGE_DEVICE | MV_USB_DEVICE | MV_GENTL_CAMERALINK_DEVICE
                  | MV_GENTL_CXP_DEVICE | MV_GENTL_XOF_DEVICE)
    
    ret = MvCamera.MV_CC_EnumDevices(tlayerType, deviceList)
    if ret != 0:
        print(f"Enum devices fail! ret[0x{ret:x}]")
        return

    print(f"Find {deviceList.nDeviceNum} devices!")

    for i in range(0, deviceList.nDeviceNum):
        mvcc_dev_info = cast(deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
        if mvcc_dev_info.nTLayerType == MV_USB_DEVICE:
            print(f"\nDevice [{i}]: USB 3.0")
            model_name = ''.join([chr(c) for c in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chModelName if c != 0])
            serial_num = ''.join([chr(c) for c in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chSerialNumber if c != 0])
            print(f"  Model Name: {model_name}")
            print(f"  Serial Number: {serial_num}")
        else:
            print(f"\nDevice [{i}]: Type {mvcc_dev_info.nTLayerType}")

    MvCamera.MV_CC_Finalize()

if __name__ == "__main__":
    check_devices()
