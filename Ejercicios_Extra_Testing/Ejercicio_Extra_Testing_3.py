import unittest
import unittest.mock

def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

class TestReadLines(unittest.TestCase):
    
    def test_read_lines_returns_expected_lines(self):
        # Mock the open function to return predefined lines without creating a real file
        expected_lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
        mocked_open = unittest.mock.mock_open(read_data="""Line 1
Line 2
Line 3
""")
        
        with unittest.mock.patch('builtins.open', mocked_open):
            lines = read_lines('dummy_path.txt')
            self.assertEqual(lines, expected_lines)
    
    def test_read_lines_raises_file_not_found_error(self):
        # Mock the open function to raise FileNotFoundError
        with unittest.mock.patch('builtins.open', side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_lines('nonexistent_file.txt')

if __name__ == '__main__':
    unittest.main()