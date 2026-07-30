# test_opensync.py
"""
Tests for OpenSync module.
"""

import unittest
from opensync import OpenSync

class TestOpenSync(unittest.TestCase):
    """Test cases for OpenSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OpenSync()
        self.assertIsInstance(instance, OpenSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OpenSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
