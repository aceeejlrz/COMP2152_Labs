# Lab 04: Python Functions and Iteration

## 📋 Student Information
* **Name:** Jezrel Dela Cruz
* **Date:** Feb 06, 2026
* **Course:** COMP2152

---

## 📖 Lesson Overview
This lab focuses on the practical application of Python fundamentals, specifically how to structure code using functions and how to process data using various iteration techniques.

### Core Concepts
* **Function Definition:** Created using the `def` keyword, followed by the function name, parentheses for parameters, and a colon `:`.
* **Return Values:** Functions use the `return` keyword to send data back to the caller. Note that returned values are not displayed unless printed.
* **Indentation:** In Python, indentation defines the scope of code blocks like loops and functions.
* **Iteration:** For loops allow you to iterate over elements in a list, using a temporary variable to hold each item during the cycle.

---

## 🛠️ Lab Questions & Logic

### Question 1: Robot Return to Origin
**Scenario:** A robot starts at $(0, 0)$ on a 2D grid. Given a string of moves, determine if it returns to the starting point.

* **Logic:** * Initialize `x = 0, y = 0`.
    * Loop through the moves string.
    * Update coordinates: `U` (Up: $y + 1$), `D` (Down: $y - 1$), `L` (Left: $x - 1$), `R` (Right: $x + 1$).
* **Example:** `moves = "UD"` returns `True`.

### Question 2: Two Sum
**Scenario:** Find two numbers in a list that add up to a specific target and return their indices.
* **Brute Force Approach:** Uses nested loops to check every possible pair, resulting in $O(n^2)$ complexity.
* **Optimized Approach:** Uses a dictionary to store previously seen numbers. It checks if the `needed` value ($target - current$) exists in the dictionary, resulting in $O(n)$ complexity.
* **Example:** `numbers = [2, 7, 11, 15], target = 9` returns `[0, 1]`.

### Question 3: Shuffle the Array
**Scenario:** Given an array of length $2n$, rearrange it from $[x_1, x_2, ..., y_1, y_2, ...]$ into $[x_1, y_1, x_2, y_2, ...]$.
* **Logic:** * Split the list using slicing: `first_half = nums[:n]` and `second_half = nums[n:]`.
    * Interleave them by appending alternating elements to a new list within a loop.
* **Example:** `nums = [2, 5, 1, 3, 4, 7], n = 3` returns `[2, 3, 5, 4, 1, 7]`.

### Question 4: First Unique Character
**Scenario:** Find the index of the first character in a string that does not repeat.
* **Logic:**
    * **Step 1:** Use a dictionary to count the frequency of every character in the string.
    * **Step 2:** Loop through the string again and check the dictionary. Return the index of the first character with a count of 1.
* **Example:** `"leetcode"` returns index `0` because 'l' is the first unique character.

---

## 📁 Repository Instructions
* **Tooling:** This lab was developed using **VS Code**.


