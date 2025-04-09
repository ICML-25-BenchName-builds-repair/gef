#!/usr/bin/env python3
"""
Script to verify the fix for the gdb_version property in tests/base.py
"""

import re
from typing import Tuple

class MockGdb:
    """Mock GDB class for testing"""
    VERSION = "13.1"

class TestGdbVersion:
    """Test class for gdb_version property"""
    def __init__(self):
        self._gdb = MockGdb()
    
    @property
    def gdb_version(self) -> Tuple[int, int]:
        """Original implementation (returns a list)"""
        res = [int(d) for d in re.search(r"(\d+)\D(\d+)", self._gdb.VERSION).groups()]
        assert len(res) >= 2
        return res
    
    @property
    def gdb_version_fixed(self) -> Tuple[int, int]:
        """Fixed implementation (returns a tuple)"""
        res = [int(d) for d in re.search(r"(\d+)\D(\d+)", self._gdb.VERSION).groups()]
        assert len(res) >= 2
        return tuple(res)  # Convert list to tuple

def test_comparison():
    """Test comparison between gdb_version and a tuple"""
    test = TestGdbVersion()
    
    # Test original implementation
    try:
        result = test.gdb_version < (11, 0)
        print(f"Original implementation - Comparison result: {result}")
        print("ERROR: The original implementation should have failed with TypeError")
    except TypeError as e:
        print(f"Original implementation - Expected error: {e}")
    
    # Test fixed implementation
    try:
        result = test.gdb_version_fixed < (11, 0)
        print(f"Fixed implementation - Comparison result: {result}")
    except TypeError as e:
        print(f"Fixed implementation - Unexpected error: {e}")
        raise

if __name__ == "__main__":
    print(f"Testing gdb_version property fix...")
    test_comparison()
    print("All tests passed!")