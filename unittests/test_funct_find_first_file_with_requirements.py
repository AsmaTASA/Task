import unittest
import os
from module_part1 import find_first_file_with_requirements
class TestFunc2(unittest.TestCase):
#unittests of function find_first_file_with_requirements
    global path
    path_unititests = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(path_unititests, os.pardir))

    def test_find_first_file_with_requirements(self):
        """
        test the nominal case
        the directory task/files_dir/correct_file_is_present contains a file that fits the requirements (correctFile_exec_size0_admin.txt)
        """
        path_files = os.path.join(path, "files_dir/correct_file_is_present")
        verdict, file_name = find_first_file_with_requirements(path_files)
        self.assertTrue(verdict)
        self.assertEqual(file_name, "correctFile_exec_size0_admin.txt")

    def test_find_first_file_with_requirements_no_file_present(self):
        """
        test the case of no file with the 3 requirements is present
        """
        path_files = os.path.join(path, "files_dir/no_correct_file_is_present")
        verdict, file_name = find_first_file_with_requirements(path_files)
        self.assertFalse(verdict)
        self.assertEqual(file_name, "No file found that meet the conditions: executable, size less than 14*2^20 and admin owner")

    def test_find_first_file_with_requirements_path_directory_NOK(self):
        """
        test the case of no error on the directory path
        """
        verdict, file_name = find_first_file_with_requirements('error_path')
        self.assertFalse(verdict)
        self.assertEqual(file_name, "The directory does not exist")

    def test_find_first_file_with_requirements_with_path_file_as_input(self):
        """
        test the case of the given path is a file path not folder
        """
        verdict, file_name = find_first_file_with_requirements(os.path.abspath(__file__))
        self.assertFalse(verdict)
        self.assertEqual(file_name, "This is not a path of a folder")

unittest.main(argv=[''],verbosity=2, exit=False)