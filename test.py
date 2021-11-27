import unittest
import os
target = __import__("WordSearch", globals={"__name__": __name__})


class TestWordSearch(unittest.TestCase):
    def test_file_parser(self):
        test = target.WordSearch()
        test.file_parser('fixtures/simple.pzl')
        self.assertEqual(len(test._puzzle), 2)
        self.assertIn(['b', 'b'], test._puzzle)
        self.assertIn(['a', 'a'], test._puzzle)
        self.assertEqual(len(test._words), 1)
        self.assertIn("cc", test._words)

    def test_puzzle_explorer_found(self):
        test = target.WordSearch()
        test.file_parser('fixtures/animals.pzl')
        found = test.puzzle_explorer('DOG')
        print(test.file_outputter())
        self.assertEqual(found, "(2, 2), (2, 4)")

    def test_puzzle_explorer_not_found(self):
        test = target.WordSearch()
        test.file_parser('fixtures/lostDuck.pzl')
        found = test.puzzle_explorer('DUCK')
        self.assertEqual(found, "not found")


if __name__ == '__main__':
    unittest.main()
