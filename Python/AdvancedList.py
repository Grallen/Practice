#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge: Advanced List Comprehension Puzzle
# Using only one line, generate a 10x10 matrix (list of lists) filled with unique random integers between 1 and 100.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\033[H\033[J", end="")
import random
# advanced_list = list(range(1,101))
# advanced_list = random.sample(advanced_list,len(advanced_list))
# advanced_list = [random.sample(list(range(1,101)),100)[x:x+10] for x in range(0,100,10)]
# print(advanced_list)

# 1. ---

# This is only unique in each list, not across the whole matrix.
# print([random.sample(list(range(1,101)),100)[x:x+10] for x in range(0,100,10)])


# 2. ---

# Only way to get functional oneliner and be unique across the matrix is to use "tricks" to get preevaluation of the range....
# I this this challenenge is invalid.  The best possible reasable answer is above (answer 1), but the challenge would have to reworded to allow it.

# This is unique across the whole matrix, but is using VERY bad techniques / tricks to make it possible...  It definitely doesn't make you a good coder to be able to do it.
matrix = [list(nums[i*10:(i+1)*10]) for i in range(10)] if (nums := random.sample(range(1, 101), 100)) else None
print(matrix)


def is_matrix_unique(matrix):
    """Checks if all elements in a 2D matrix (list of lists) are unique.

    Args:
        matrix: The 2D matrix to check.

    Returns:
        True if all elements are unique, False otherwise.
    """
    seen = set()  # Use a set for efficient uniqueness checking
    for row in matrix:
        for element in row:
            if element in seen:
                return False  # Found a duplicate
            seen.add(element)
    return True  # All elements are unique

print(f"Unique: {is_matrix_unique(matrix)}")