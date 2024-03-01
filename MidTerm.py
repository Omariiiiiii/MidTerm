# def is_valid_url(param):
#     # Initialize start position for search
#     start = 0
#     # Try to find "http://" or "https://" at the start of the string
#     http_pos = param.find("http://", start)
#     https_pos = param.find("https://", start)
#
#     # Check if either "http://" or "https://" is found at the start
#     if http_pos == 0 or https_pos == 0:
#         # Determine the end of the protocol part
#         protocol_end = param.find("://", start) + 3
#
#         # Now, check if there's at least one dot after the protocol
#         if "." in param[protocol_end:]:
#             return True
#     return False
#
#
# # Example usage
# print(is_valid_url("http://google.com"))  # True
# print(is_valid_url("https://example.com"))  # True
# print(is_valid_url("example.com"))  # False
# print(is_valid_url("http://localhost"))  # False


# def find_pattern_occurrences(text):
#     # Split the text into words
#     words = text.split()
#
#     # Initialize a count for the pattern
#     pattern_count = 0
#
#     # Loop through each word in the text
#     for word in words:
#         # Check if the word starts with "C" and ends with "jeb"
#         if word.startswith('C') and word.endswith('jeb'):
#             # Increment the pattern count
#             pattern_count += 1
#
#     # Return the total count of the pattern
#     return pattern_count
#
#
# # Example usage:
# text_to_search = "Cabcjeb is a pattern, so is C123jeb but it does not match, while Cxyzjeb does."
# number_of_matches = find_pattern_occurrences(text_to_search)
# print(number_of_matches)

# my_list = [1, 2, 3]
# print("Original list:", my_list)
#
# my_list[0] = 100
# print("Modified list:", my_list)
#
# my_string = "hello"
# print("Original string:", my_string)
#
# try:
#     my_string[0] = "H"
# except TypeError as e:
#     print("Error:", e)

# def find_pattern_occurrences(text):
#     words = text.split()
#
#     pattern_count = 0
#
#     for word in words:
#         if word.startswith('C') and word.endswith('jeb'):
#             pattern_count += 1
#
#     return pattern_count
#
# text_to_search = "Cabcjeb is a pattern, so is C123jeb but it does not match, while Cxyzjeb does."
# number_of_matches = find_pattern_occurrences(text_to_search)
# print(number_of_matches)
