# Coding Test Practice

A growing collection of my LeetCode solutions. Problems are grouped by topic, and the repository will expand as I solve more challenges.

## Project Layout

```text
leetcode/                 Problem solutions, organized by topic
	array/                  Array problems
tests/
	tests_leetcode/         Tests for the LeetCode solutions
		tests_array/          Array solution tests
```

Each problem has its own Python module. Solutions currently follow LeetCode's `Solution` class format. For example, the array solutions include Two Sum and Best Time to Buy and Sell Stock.

As the collection grows, new solutions can be added under the relevant topic in `leetcode/`, with corresponding tests under `tests/tests_leetcode/`.

## Running Tests

The project uses pytest. Run the LeetCode tests from the repository root:

```bash
pytest tests/tests_leetcode
```

Problem statements can be found on [LeetCode](https://leetcode.com/problemset/).
