#!/usr/bin/env python3

"""
Script to verify the fix for the gdb_version issue.
"""

import re

def test_gdb_version_comparison():
    """Test that the gdb_version property works correctly."""
    # Simulate the current implementation
    def gdb_version_list():
        return [10, 2]
    
    # Simulate the fixed implementation
    def gdb_version_tuple():
        return tuple([10, 2])
    
    try:
        # This should fail
        result = gdb_version_list() < (11, 0)
        print("ERROR: List comparison with tuple should have failed but didn't!")
        return False
    except TypeError:
        print("PASS: List comparison with tuple correctly failed with TypeError")
    
    try:
        # This should succeed
        result = gdb_version_tuple() < (11, 0)
        print(f"PASS: Tuple comparison with tuple succeeded: {result}")
        return True
    except TypeError:
        print("ERROR: Tuple comparison with tuple failed with TypeError!")
        return False

if __name__ == "__main__":
    test_gdb_version_comparison()