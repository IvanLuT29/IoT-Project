# app/data_processor.py
class DataProcessor:
    def __init__(self):
        self.processed_data = []

    def process_data(self, data):
        processed_result = f"Processed: {data}"
        self.processed_data.append(processed_result)
        return processed_result

# app/main.py
from devices.network_device import NetworkDevice
from controller.network_controller import NetworkController
from data_processor import DataProcessor
import asyncio

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

    # Додавання обробки даних
    processor = DataProcessor()
    for data in data_to_send:
        processed_data = processor.process_data(data)
        print(f"Data Processor: {processed_data}")

if __name__ == "__main__":
    asyncio.run(main())
