#!/usr/bin/env python3
"""
Script to reproduce the issue with gdb_version property in tests/base.py
"""

import re
from typing import Tuple, List

def test_comparison():
    """Test comparison between list and tuple"""
    # Simulate the issue
    gdb_version_as_list = [10, 2]  # This is what's currently returned
    gdb_version_as_tuple = (11, 0)  # This is what's being compared against
    
    try:
        # This will fail with TypeError
        result = gdb_version_as_list < gdb_version_as_tuple
        print(f"Comparison result: {result}")
    except TypeError as e:
        print(f"Error: {e}")
    
    # Fix: Convert list to tuple
    gdb_version_as_tuple_fixed = tuple(gdb_version_as_list)
    result = gdb_version_as_tuple_fixed < gdb_version_as_tuple
    print(f"Fixed comparison result: {result}")

def simulate_gdb_version_property():
    """Simulate the gdb_version property in tests/base.py"""
    # Mock the regex search result
    mock_version = "10.2"
    match = re.search(r"(\d+)\D(\d+)", mock_version)
    
    # Original implementation
    res = [int(d) for d in match.groups()]
    print(f"Original result (list): {res}")
    
    # Try to compare with a tuple
    try:
        print(f"Is {res} < (11, 0)? ", end="")
        print(res < (11, 0))
    except TypeError as e:
        print(f"Error: {e}")
    
    # Fixed implementation
    res_fixed = tuple(int(d) for d in match.groups())
    print(f"Fixed result (tuple): {res_fixed}")
    
    # Compare with a tuple
    print(f"Is {res_fixed} < (11, 0)? {res_fixed < (11, 0)}")

if __name__ == "__main__":
    print("Testing comparison between list and tuple:")
    test_comparison()
    
    print("\nSimulating gdb_version property:")
    simulate_gdb_version_property()