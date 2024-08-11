import unittest
from host_insights_promptify.system import collect_system_info

class TestSystemInfo(unittest.TestCase):
    
    def test_collect_system_info(self):
        system_info = collect_system_info()

        # Check if the returned value is a dictionary
        self.assertIsInstance(system_info, dict)

        # Check that all expected keys are in the dictionary
        expected_keys = [
            "OS", "OS Version", "Architecture", "Hostname", "CPU", 
            "Physical Cores", "Logical Cores", "CPU Frequency", 
            "Total Memory", "Available Memory", "Disk", "Disk Available", 
            "Disk Usage", "Disk Partitions"
        ]
        for key in expected_keys:
            self.assertIn(key, system_info)

        # Check that the values are not None or empty
        for key in expected_keys:
            self.assertIsNotNone(system_info[key])
            self.assertNotEqual(system_info[key], "")

if __name__ == "__main__":
    unittest.main()