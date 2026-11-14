#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.

import threading

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

OSC_IP = "127.0.0.1"
OSC_PORT = 7004
OSC_ACK_PORT = 7005
OSC_ACK_ADDRESS = "/ack"


class OscHandler:
    def __init__(self):
        self.osc = SimpleUDPClient(OSC_IP, OSC_PORT)
        self.address = "/emb"

    def send_on_signal_and_wait(self, timeout: float = 10.0) -> None:
        acknowledgement_received = threading.Event()
        dispatcher = Dispatcher()
        dispatcher.map(OSC_ACK_ADDRESS, lambda address, *args: acknowledgement_received.set())

        with ThreadingOSCUDPServer((OSC_IP, OSC_ACK_PORT), dispatcher) as server:
            server_thread = threading.Thread(target=server.serve_forever, daemon=True)
            server_thread.start()
            try:
                self.osc.send_message("/on", 1)
                if not acknowledgement_received.wait(timeout):
                    raise TimeoutError("No ack from Max for /on")
            finally:
                server.shutdown()
                server_thread.join()
