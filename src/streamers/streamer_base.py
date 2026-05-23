#!/usr/bin/env python3
# Copyright (c) 2024-2026 Joseph Meyer. All Rights Reserved.


from run_settings import RunSettings

class StreamerBase:

    def __init__(self, run_settings: RunSettings = RunSettings()):
        self.run_settings = run_settings
