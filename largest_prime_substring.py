# --------------------------- Largest Prime Substring ---------------------------
"""
Problem: Largest Prime Substring

A prime number is a number greater than 1 that is divisible only by 1 and itself. 
Write a function that takes a string consisting solely of digits. Validate that 
the string has 10 or fewer digits, and output the largest prime number that 
exists as a substring of the input. This may include the input itself.

Examples:
- Input: "1931695" → Output: 93169
- Input: "1062352" → Output: 23

Constraints:
- Input string consists solely of digits
- String must have 10 or fewer digits
- Must implement custom prime checking function (no built-in functions)
- Return the largest prime number found as a substring
- If no prime found, return -1 or handle appropriately

"""

from math import sqrt


def is_prime(n) -> bool:
    """
    Check if a number is prime using custom implementation.
    
    Args:
        n: int - Number to check for primality
    
    Returns:
        bool - True if prime, False otherwise
    """
    if n < 2:
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False
    return True

def is_integer(n) -> bool:
    try:
        int(n)
        return True
    except:
        return False

def largest_prime_substring(digit_string):
    """
    Find the largest prime number that exists as a substring of the input.
    
    Args:
        digit_string: str - String consisting solely of digits (≤10 characters)
    
    Returns:
        int - The largest prime number found as substring, or -1 if none found
    """

    if not is_integer(digit_string):
        return -1

    # ensure number has len <= 10
    if len(digit_string) > 10:
        return -1
    
    longest_prime = -1
    for i in range(len(digit_string)):
        for j in range(i+1, len(digit_string)+1):
            if is_prime(int( digit_string[i:j] )):
                longest_prime = max( longest_prime, int(digit_string[i:j]) )
    return longest_prime

# --------------------------- Test Cases ---------------------------
import unittest

class TestLargestPrimeSubstring(unittest.TestCase):
    
    def test_example_1(self):
        """Test case from example 1."""
        input_str = "1931695"
        expected = 93169
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """Test case from example 2."""
        input_str = "1062352"
        expected = 23
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_single_digit_prime(self):
        """Test with single digit prime."""
        input_str = "7"
        expected = 7
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_single_digit_non_prime(self):
        """Test with single digit non-prime."""
        input_str = "4"
        expected = -1
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_all_primes(self):
        """Test string where all digits are prime."""
        input_str = "2357"
        expected = 2357
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_no_primes(self):
        """Test string with no prime substrings."""
        input_str = "4680"
        expected = -1
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_multiple_primes_same_length(self):
        """Test string with multiple primes of same length."""
        input_str = "1234"
        # Primes: 2, 3, 23
        expected = 23
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_leading_zeros(self):
        """Test string with leading zeros in substrings."""
        input_str = "102"
        # Should handle "02" -> 2, "01" -> 1
        expected = 2
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_max_length(self):
        """Test with maximum allowed length (10 digits)."""
        input_str = "1234567890"
        result = largest_prime_substring(input_str)
        # Should find some prime in this string
        self.assertGreater(result, 0)
    
    def test_empty_string(self):
        """Test with empty string."""
        input_str = ""
        expected = -1
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    
    def test_invalid_input_too_long(self):
        """Test with string longer than 10 digits."""
        input_str = "12345678901"  # 11 digits
        # Should handle validation error appropriately
        result = largest_prime_substring(input_str)
        # Could return -1 or raise exception depending on implementation
    
    def test_invalid_input_non_digits(self):
        """Test with non-digit characters."""
        input_str = "12a34"
        # Should handle validation error appropriately
        result = largest_prime_substring(input_str)
        # Could return -1 or raise exception depending on implementation
    
    def test_large_prime(self):
        """Test with a known large prime."""
        input_str = "97"  # 97 is prime
        expected = 97
        result = largest_prime_substring(input_str)
        self.assertEqual(result, expected)
    

class TestIsPrime(unittest.TestCase):
    
    def test_small_primes(self):
        """Test small prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))
    
    def test_small_non_primes(self):
        """Test small non-prime numbers."""
        non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for non_prime in non_primes:
            with self.subTest(non_prime=non_prime):
                self.assertFalse(is_prime(non_prime))
    
    def test_edge_cases(self):
        """Test edge cases for prime checking."""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))  # Smallest prime
        self.assertFalse(is_prime(-5))  # Negative number
    
    def test_larger_numbers(self):
        """Test larger numbers."""
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(101))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(99))

def run_tests():
    """Run all tests and display results."""
    unittest.main(verbosity=2)

if __name__ == "__main__":
    run_tests()
