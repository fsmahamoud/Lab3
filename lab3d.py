#!/usr/bin/env python3
# Author ID: 140729229
import os
import subprocess
import lab3d
def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())


