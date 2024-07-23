import json
from django.test import TestCase
from myapp.app import is_unique_subset, find_minimal_unique_subset, list_to_csv_string, main

class MyAppTests(TestCase):

    def setUp(self):
        self.entities = [
            {"name": "Alice", "age": "25", "city": "New York"},
            {"name": "Bob", "age": "30", "city": "Los Angeles"},
            {"name": "Charlie", "age": "35", "city": "Chicago"},
            {"name": "Dave", "age": "40", "city": "New York"} 
        ]
        self.attributes = {"name": 4, "age": 4, "city": 3}

    def test_is_unique_subset(self):
        self.assertTrue(is_unique_subset(self.entities, ["name"]))
        self.assertTrue(is_unique_subset(self.entities, ["name", "age"]))
        self.assertFalse(is_unique_subset(self.entities, ["city"]))

    def test_find_minimal_unique_subset(self):
        result = find_minimal_unique_subset(self.entities, self.attributes)
        self.assertIn("name", result)
        self.assertEqual(len(result), 1)

    def test_list_to_csv_string(self):
        lst = ["name", "age", "city"]
        csv_str = list_to_csv_string(lst)
        expected_csv = "name\nage\ncity\n"
        self.assertEqual(csv_str.replace("\r\n", "\n"), expected_csv)

    def test_main(self):
        json_string = json.dumps(self.entities)
        csv_result = main(json_string)
        expected_csv = "name\n"
        self.assertEqual(csv_result.replace("\r\n", "\n"), expected_csv)
