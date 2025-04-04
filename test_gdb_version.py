#!/usr/bin/env python3

import re

# Simulate the current behavior
def get_gdb_version_as_list():
    # This simulates the current implementation in tests/base.py
    version_str = "12.1"
    res = [int(d) for d in re.search(r"(\d+)\D(\d+)", version_str).groups()]
    return res

# Test comparison
try:
    version_list = get_gdb_version_as_list()
    print(f"Version as list: {version_list}, type: {type(version_list)}")
    
    # This will fail with TypeError
    if version_list < (11, 0):
        print("Version is less than 11.0")
    else:
        print("Version is greater than or equal to 11.0")
except TypeError as e:
    print(f"Error: {e}")
    
# Fix: Convert list to tuple
version_tuple = tuple(get_gdb_version_as_list())
print(f"Version as tuple: {version_tuple}, type: {type(version_tuple)}")

# This should work
if version_tuple < (11, 0):
    print("Version is less than 11.0")
else:
    print("Version is greater than or equal to 11.0")