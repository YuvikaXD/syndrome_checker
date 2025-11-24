# syndrome_checker
## Simple Symptom Checker

A beginner-friendly Python program that allows users to enter symptoms and receive a basic wellness suggestion based on a simple scoring system.
This tool is NOT a medical diagnosis, but a small demonstration of conditional logic, user input handling, and basic program structure in Python.
## Features

1.Accepts user-entered symptoms (comma-separated)

2.Calculates a symptom severity score

3.Provides basic health guidance based on the score

4.Simple and easy to extend for more symptoms or features
## how it works
1.The user enters symptoms such as:
```bash
fever, cough, headache
```
2.The program converts them to a list and compares each symptom to a predefined set.

3.Each symptom contributes a specific number of points.

4.The final score is displayed with a wellness message.
## Symptom Scoring
```bash
| Symptom                   | Score |
| ------------------------- | ----- |
| fever                     | +2    |
| cough                     | +2    |
| body pain                 | +2    |
| headache                  | +1    |
| cold / runny nose         | +1    |
| fatigue / tired           | +1    |
| sore throat / throat pain | +1    |
```
## Wellness Guidance
```bash
| Score Range | Message                                                                              |
| ----------- | ------------------------------------------------------------------------------------ |
| 6 or more   | You might be feeling significantly unwell. Consider resting and consulting a doctor. |
| 3–5         | You may have a mild viral condition or common cold. Rest and stay hydrated.          |
| 1–2         | Very mild symptoms. Hydrate and rest.                                                |
| 0           | No noticeable symptoms. You seem okay!                                               |

```
## How to Run

1.Install Python 3 if not already installed.

2.Save the script (e.g., symptom_checker.py).

3.Run the program:
```bash
python symptom_checker.py
```
4.Enter symptoms when prompted.

## Example

```bash
=== Simple Symptom Checker ===
Enter symptoms separated by commas.
Example: fever, cough, headache

Enter symptoms: fever, body pain, headache

=== Result ===
You might be feeling significantly unwell.
Please rest and consider consulting a healthcare professional.

Note: This is not a medical diagnosis — just a simple Python-based checker.
```
## Files Included
```bash
symptom_checker.py     # Main program
README.md              # Project documentation
```
## Disclaimer

This program does not diagnose illness.
It is for educational and demonstration purposes only.
Always consult a qualified medical professional for health concerns

# AUTHOR
## YUVIKA MUKHERJEE




