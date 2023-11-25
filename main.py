import asyncio

class NetworkDevice:
    def __init__(self, name):
        self.name = name
        self.data_buffer = []

    async def process_data(self, data):
        print(f"{self.name}: Processing data - {data}")
        await asyncio.sleep(1)
        print(f"{self.name}: Data processing complete")

class NetworkController:
    def __init__(self, devices):
        self.devices = devices

    async def send_data(self, data):
        print(f"Controller: Sending data - {data}")
        for device in self.devices:
            device.data_buffer.append(data)
        print("Controller: Data sent")

    async def process_data_real_time(self):
        tasks = []
        for device in self.devices:
            if device.data_buffer:
                data_to_process = device.data_buffer.pop(0)
                task = asyncio.ensure_future(device.process_data(data_to_process))
                tasks.append(task)
        await asyncio.gather(*tasks)

async def main():
    # Створення пристроїв на базі ARM
    device1 = NetworkDevice("Device 1")
    device2 = NetworkDevice("Device 2")

    # Створення контролера та призначення пристроїв
    controller = NetworkController(devices=[device1, device2])

    # Відправлення даних асинхронно на контролер
    data_to_send = ["Data 1", "Data 2", "Data 3"]
    await controller.send_data(data_to_send)

    # Оптимізація ресурсів у режимі реального часу
    await controller.process_data_real_time()

if __name__ == "__main__":
    asyncio.run(main())
