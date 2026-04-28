import unittest

class TestBubbleSort(unittest.TestCase):
    def bubble_sort(self, lst):
        # Validate parameter type
        if not isinstance(lst, list):
            raise TypeError("Parameter must be a list")

        n = len(lst)

        # Classic Bubble Sort
        for i in range(n):
            for j in range(0, n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

        return lst

    def test_small_list(self):
        """Works with a small list."""
        data = [3, 1, 2]
        result = self.bubble_sort(data)
        self.assertEqual(result, [1, 2, 3])

    def test_large_list(self):
        """Works with a large list (more than 100 elements)."""
        data = list(range(150, 0, -1))  # 150 elements in reverse order
        result = self.bubble_sort(data)
        self.assertEqual(result, list(range(1, 151)))

    def test_empty_list(self):
        """Works with an empty list."""
        data = []
        result = self.bubble_sort(data)
        self.assertEqual(result, [])

    def test_invalid_parameter(self):
        """Fails when the parameter is not a list."""
        with self.assertRaises(TypeError):
            self.bubble_sort("I am not a list")

example = TestBubbleSort()
example.test_small_list()
example.test_large_list()
example.test_empty_list()
example.test_invalid_parameter()

if __name__ == '__main__':
    unittest.main()
    
