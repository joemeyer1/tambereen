#!/usr/bin/env python3
# Copyright (c) 2024 Joseph Meyer. All Rights Reserved.


import os


def install_requirements():

    # Do the following 2 commands from Terminal, not here (so they're commented out)
    # os.system("virutalenv env_tmp --python=python3.8")
    # os.system("source env_tmp/bin/activate")

    os.system("pip install -r requirements.txt")  # install all requirements except torch
    # this will install typing_extensions==4.5.0 which tensorflow==2.13.1 depends on

    # then install torch after reinstalling typing_extensions==4.12.2 which torch==2.2.2 depends on
    os.system("pip install typing_extensions==4.12.2")  # torch and tensorflow depend on different versions of this
    os.system("pip install torch==2.2.2")
    os.system("pip install mediapipe")
    os.system("pip install opencv-python==4.11.0.86")


if __name__ == '__main__':
    install_requirements()
