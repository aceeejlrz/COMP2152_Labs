# Lab 03: Python Data Structures & Environment Setup

This README provides a comprehensive guide to the practical implementations and technical setup discussed during the Week 03 lecture.

---

## 📋 Student Information
* **Name:** Jezrel Dela Cruz
* **Date:** Jan 30, 2026
* **Course:** COMP2152
* **Status:** Junior Web Developer at George Brown College, Casa Loma Campus

---


## 🛠️ Lab Exercises & Logic

### Question 1: List Manipulation (Numerical)
Uses a list of grades to practice sorting and basic statistics.
* **Method:** Uses `.append()` to add grades and `.sort()` to organize them in ascending order.
* **Accessing Data:**
    * **Highest Grade:** `grades[-1]`.
    * **Lowest Grade:** `grades[0]`.
    * **Total Count:** `len(grades)`.

### Question 2: List Manipulation (Strings)
Demonstrates handling lists containing strings and duplicate entries.
* **Counting:** `.count("apple")` finds how many times an item appears.
* **Indexing:** `.index("milk")` retrieves the specific position of an item.
* **Removal:** `.remove("apple")` deletes the first occurrence from the left; `.pop()` removes the last item.

### Question 3: Tuples & Euclidean Distance
Tuples are used for immutable 2D coordinates.

* **Unpacking:** Coordinates are extracted using `x1, y1 = point1`.
* **Calculation:** Implements the formula $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ using `((x2 - x1)**2 + (y2 - y1)**2)**0.5`.

### Question 4: Set Operations
Sets store unique, unordered elements using curly braces `{}`.
* **Common Operations:**
    * **Intersection (`&`):** Elements present in both sets.
    * **Union (`|`):** All elements from either set.
    * **Difference (`-`):** Elements in the first set but not the second.
    * **Symmetric Difference (`^`):** Elements in exactly one of the sets.
    * **Subset Check (`<=`):** Returns `True` if one set is entirely contained within another.

### Question 5: Dictionaries (Key-Value Pairs)
Dictionaries map unique keys to specific values.
* **Add/Update:** `contacts["Name"] = "Number"`.
* **Deletion:** Uses the `del` keyword (e.g., `del contacts["Charlie"]`).
* **Metadata:** Accessed via `.keys()`, `.values()`, and `len()`.

---

## 📤 Submission Requirements
Submit the following for grading:
1. The **GitHub Public Repository URL**.
2. **Screenshots** of the following Git commands:
    * `git status`
    * `git commit -m "Message"`
    * `git push`

---