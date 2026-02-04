Binary Search – Voter Lookup
This mini project implements a binary search algorithm in Python to simulate a voter lookup system.

Motivation
During election processes, people often search manually through long alphabetical lists to find voter numbers.  
This project demonstrates how binary search can optimize that process by reducing search time significantly from O(n) to O(log n).

How it works
The program performs a binary search over a list of Costa Rican residents that is pre-sorted alphabetically by full name (first last name format, similar to real voter registries) and returns the index (voter number) if the person is found.

Design notes
This project models a simplified election lookup scenario. A future improvement would be replacing or complementing the list with a dictionary to allow constant-time verification, for example tracking whether a person is registered or has already voted.

Algorithm Used
Binary Search:
- Requires a sorted list
- Time complexity: O(log n)
- Efficient for large datasets

Binary Search Walkthrough (visual step-by-step example)
![BinarySearch](https://github.com/user-attachments/assets/32eadc48-f45f-4d07-a7d5-7baf2c68d802)
