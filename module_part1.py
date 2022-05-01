import os
from os import stat
from pwd import getpwuid
import pwd

def printFirstRepeatingElement(vector1, vector2):
    """
    function that given 2 vectors of integers finds the first repeated number
    :param vector1: vector
    :type vector1: list
    :param vector2: vector
    :type vector2: list
    :return: verdict, element
    :rtype tuple
    :return: verdict, msg
    :rtype tuple
    """
    if type(vector1) != list or type(vector2) != list or len(vector1) < 1 or len(vector2) < 1:
        return False, "input vectors must be non empty list"
    if not all(isinstance(x, int) for x in vector1):
        return False, "input vector 1 should contain only int values"
    if not all(isinstance(x, int) for x in vector2):
        return False, "input vector 2 should contain only int values"
    for element in vector1:
        if element in vector2:
            return True, element
    return False, "there is no repeated number"


def find_first_file_with_requirements(path_of_file_system):
    """
    function that given a path of the file system finds the first file that meets the following requirements:
    -The file owner is admin
    -The file is executable
    -The file has a size lower than 14*2^20
    :param path_of_file_system: directory path
    :type path_of_file_system: str
    :return: verdict, file
    :rtype tuple
    :rturn: verdict, msg
    :rtype tuple
    """
    if not os.path.exists(path_of_file_system):
        return False, "The directory does not exist"
    if not os.path.isdir(path_of_file_system):
        return False, "This is not a path of a folder"
    content = os.listdir(path_of_file_system)
    os.chdir(path_of_file_system)
    liste_files = [f for f in content if os.path.isfile(f)]
    for file in liste_files:
        file_owner = getpwuid(stat(file).st_uid).pw_name
        admin_name = pwd.getpwuid(os.getuid())[0]
        if os.path.getsize(file) < 14 * 2 ^ 20 and os.access(file, os.X_OK) and file_owner == admin_name:
            return True, file
    return False, "No file found that meet the conditions: executable, size less than 14*2^20 and admin owner"




def find_zero_pos(liste, index):
    """
    function used to find the index of the first 0 occurrence on a slice of list
    starting by a given index
    this function will be called in the  function find_minimum_quantity_of_permutations
    """
    for i in liste[index:]:
        if i == 0:
            return index
        else:
            index += 1

def find_one_pos(liste, index):
    """
    function used to find the index of the first 1 occurrence on a slice of list
    starting by a given index
    this function will be called in the  function find_minimum_quantity_of_permutations
    """
    for i in liste[index:]:
        if i == 1:
            return index
        else:
            index += 1

def find_minimum_quantity_of_permutations(sequence):
    """
    A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
    minimum quantity of permutations so that the sequence ends interspersed. For
    example, given the sequence 0,1,1,0 how many changes are needed so that the
    result is 0,1,0,1

    :param sequence: sequence of coin flips
    :type sequence: list
    :return: verdict, permutation_number
    :rtype tuple
    :return: verdict, msg
    :rtype tuple
    """
    if type(sequence) != list or len(sequence) < 1:
        return False, "input sequence must be non empty list"
    for value in sequence:
        if value not in [0, 1]:
            return False, "Sequence must be a list of 0 and 1 elements"

    if sequence.count(1) != sequence.count(0):
        return False, "Number of 1 elements must be equal to number of 0 elements"

    permutation_number = 0
    i = 0
    while i+1 < len(sequence):
        if sequence[i] == 0:
            index = find_one_pos(sequence, i+1)
            if sequence[i+1] != 1:
                aux=sequence[i+1]
                sequence[i+1] = sequence[index]
                sequence[index] = aux
                permutation_number += 1
        if sequence[i] == 1:
            index = find_zero_pos(sequence, i+1)
            if sequence[i+1] != 0:
                aux = sequence[i+1]
                sequence[i+1] = sequence[index]
                sequence[index] = aux
                permutation_number += 1
        i += 1
    return True, permutation_number
