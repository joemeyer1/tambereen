#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. MIT License.

from pythonosc.udp_client import SimpleUDPClient

OSC_IP = "127.0.0.1"
OSC_PORT = 7004

class OscHandler:
    def __init__(self):
        self.osc = SimpleUDPClient(OSC_IP, OSC_PORT)
        self.address = "/emb"
