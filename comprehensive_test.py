#!/usr/bin/env python3
"""
Comprehensive test for the gdb_version property fix
"""

import re
from typing import Tuple, List, Any

class MockGdb:
    """Mock GDB class for testing"""
    VERSION = "13.1"

class TestBase:
    """Base test class"""
    def __init__(self):
        self._gdb = MockGdb()
    
    @property
    def gdb_version_original(self) -> Tuple[int, int]:
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

def test_type_consistency():
    """Test type consistency between annotation and return value"""
    test = TestBase()
    
    # Check original implementation
    original_version = test.gdb_version_original
    print(f"Original implementation returns: {original_version} of type {type(original_version)}")
    print(f"Is it a tuple as annotated? {isinstance(original_version, tuple)}")
    
    # Check fixed implementation
    fixed_version = test.gdb_version_fixed
    print(f"Fixed implementation returns: {fixed_version} of type {type(fixed_version)}")
    print(f"Is it a tuple as annotated? {isinstance(fixed_version, tuple)}")

def test_comparison_operations():
    """Test various comparison operations"""
    test = TestBase()
    
    # Define test cases: (operation, expected_result)
    test_cases = [
        ("< (14, 0)", True),
        ("> (12, 0)", True),
        ("== (13, 1)", True),
        ("!= (13, 2)", True),
        ("<= (13, 1)", True),
        (">= (13, 1)", True),
        ("< (13, 0)", False),
    ]
    
    print("\nTesting comparison operations with fixed implementation:")
    for operation, expected in test_cases:
        try:
            # Dynamically evaluate the comparison
            result = eval(f"test.gdb_version_fixed {operation}")
            print(f"  test.gdb_version_fixed {operation} = {result} (Expected: {expected})")
            assert result == expected, f"Unexpected result for {operation}"
        except Exception as e:
            print(f"  Error with operation '{operation}': {e}")
    
    print("\nTesting comparison operations with original implementation:")
    for operation, expected in test_cases:
        try:
            # This should fail with TypeError for all operations
            result = eval(f"test.gdb_version_original {operation}")
            print(f"  test.gdb_version_original {operation} = {result} (Expected TypeError)")
            print("  ERROR: The original implementation should have failed with TypeError")
        except TypeError as e:
            print(f"  Expected error with operation '{operation}': {e}")

if __name__ == "__main__":
    print("=== Testing gdb_version property fix ===\n")
    test_type_consistency()
    test_comparison_operations()
    print("\n=== All tests completed ===")