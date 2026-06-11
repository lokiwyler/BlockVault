# test_blockvault.py
"""
Tests for BlockVault module.
"""

import unittest
from blockvault import BlockVault

class TestBlockVault(unittest.TestCase):
    """Test cases for BlockVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockVault()
        self.assertIsInstance(instance, BlockVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
