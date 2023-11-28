# app/devices/network_device.py
class NetworkDevice:
    def __init__(self, name):
        self.name = name
        self.data_buffer = []

    def send_data(self, data):
        print(f"{self.name}: Sending data - {data}")
        self.data_buffer.append(data)
        print(f"{self.name}: Data sent")

    def receive_data(self):
        if self.data_buffer:
            received_data = self.data_buffer.pop(0)
            print(f"{self.name}: Received data - {received_data}")
            return received_data
        else:
            print(f"{self.name}: No data available")
            return None

    def process_data(self, data):
        print(f"{self.name}: Processing data - {data}")
        processed_data = f"{self.name}: Processed - {data.upper()}"
        print(f"{self.name}: Data processing complete")
        return processed_data

    @property
    def status(self):
        return f"{self.name}: Online"
