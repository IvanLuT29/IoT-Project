# app/controller/network_controller.py
import asyncio

class NetworkController:
    def __init__(self, devices):
        self.devices = devices

    async def send_data(self, data):
        print("Controller: Sending data")
        for device in self.devices:
            device.send_data(data)
        print("Controller: Data sent")

    async def process_data_real_time(self):
        print("Controller: Processing data in real-time")
        tasks = [asyncio.ensure_future(device.receive_data()) for device in self.devices]
        await asyncio.gather(*tasks)
        print("Controller: Real-time data processing complete")
