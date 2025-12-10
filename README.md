---
title: CISC 121 Project
emoji: 🏢
colorFrom: red
colorTo: yellow
sdk: gradio
sdk_version: 6.0.2
app_file: app.py
pinned: false
license: apache-2.0
short_description: Merge Sort Visualization
---

# Algorithm Name: 
Merge Sort

## Demo video/gif/screenshot of test: 
https://streamable.com/ik2a0t

## Problem Breakdown & Computational Thinking: 
Decomposition:
- accept a list of numbers from the user
- continue dividing the list into two halves until each sub-list has length 1 (my base case here)
- start merging pairs of smaller sorted lists into bigger sorted lists.
- during merges repeatedly compare the first elements of each list and append the smaller one
- continue merging upward until the entire list becomes one big sorted list
- at significant steps, show it to the user using some visualization function

Pattern Recognition:
- every list is treated the same independent of the size
- split -> recursively sort the halves -> merge halves
- merge sort process stays the same: compare left[0] and right[0], choose the smaller one of the 2, remove it, append to the result

Abstraction:
- the user just puts in a random lsit of numbers and gets out a sorted list. 
- They dont have to sort anything themselves
- they only see the numbers they want to put in, their unsorted list, the steps the algorithm took to sort the list, and the sorted list

 
Algorithm Design:
-  Input: finite list of numbers
-  Processing: put the list of numbers into the merge sort algorithm
-  Output: Sorted list of numbers

## Steps To Run:
1. Enter 1-10 integers.
2. Press the run button.
3. Watch the algorithm sort your list of numbers from least to greatest.

## Hugging Face Link:
https://huggingface.co/spaces/QCISCProject/CISC-121-Project


## Author And Acknoledgement:
Laeron Lewis

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
