# tests/test_network_device.py
import pytest
from devices.network_device import NetworkDevice

def test_send_receive_data():
    device = NetworkDevice("TestDevice")
    data_to_send = "Test Data"
    
    device.send_data(data_to_send)
    received_data = device.receive_data()

    assert received_data == data_to_send

def test_process_data():
    device = NetworkDevice("TestDevice")
    data_to_process = "Test Data"
    
    processed_data = device.process_data(data_to_process)

    assert processed_data == "TestDevice: Processed - TEST DATA"

def test_status():
    device = NetworkDevice("TestDevice")
    status = device.status

    assert status == "TestDevice: Online"