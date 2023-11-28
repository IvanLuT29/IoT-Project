# tests/test_network_controller.py
import pytest
from devices.network_device import NetworkDevice
from controller.network_controller import NetworkController
import asyncio

@pytest.fixture
def devices():
    device1 = NetworkDevice("Device 1")
    device2 = NetworkDevice("Device 2")
    return [device1, device2]

@pytest.mark.asyncio
async def test_send_data(devices, capsys):
    controller = NetworkController(devices=devices)
    data_to_send = "Test Data"

    await controller.send_data(data_to_send)

    captured = capsys.readouterr()
    assert "Controller: Sending data" in captured.out
    assert "Device 1: Sending data - Test Data" in captured.out
    assert "Device 2: Sending data - Test Data" in captured.out
    assert "Controller: Data sent" in captured.out

@pytest.mark.asyncio
async def test_process_data_real_time(devices, capsys):
    controller = NetworkController(devices=devices)

    await controller.process_data_real_time()

    captured = capsys.readouterr()
    assert "Controller: Processing data in real-time" in captured.out
    assert "Device 1: Received data" in captured.out
    assert "Device 2: Received data" in captured.out
    assert "Controller: Real-time data processing complete" in captured.out
