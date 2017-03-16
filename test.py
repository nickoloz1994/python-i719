import unittest
from port import scanport

class TestScanPortCase(unittest.TestCase):
	def test_port_scan_ok(self):
		result = scanport("8.8.8.8", 53)
		self.assertEqual(result, 1)

	def test_port_scan_fail(self):
		result = scanport("8.8.8.8", 23)
		self.assertEqual(result, 0)