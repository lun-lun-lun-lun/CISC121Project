import gradio as gr  # type: ignore
import pandas as pd  # type: ignore
import time
import random

def merge_sort(number_list: list[float], visualize=None):
    #if a visualization callback exists, show the current list state
    if visualize:
        visualize(number_list)

    #base case 1, single element, already sorted
    if len(number_list) == 1:
        return number_list

    # Base case 2 (i dont need this i just want to visualize it)
    if len(number_list) == 2:
        result = [min(number_list), max(number_list)]
        if visualize:
            visualize(result)  #show sorted pair
        return result

    #recursive case, split my list in half
    mid_id = len(number_list) // 2
    list_left = merge_sort(number_list[mid_id:], visualize)
    list_right = merge_sort(number_list[:mid_id], visualize)

    #prep for merging the 2 sorted halves
    total_len = len(list_left) + len(list_right)
    left_start = 0
    right_start = 0
    new_list = []

    #repeatedly take the smallest next element
    while len(new_list) < total_len:
        #if left list is exhausted, append  remaining right list
        if left_start > len(list_left) - 1:
            new_list = new_list + list_right[right_start:]
            break

        #if right list is exhausted, append the remaining left list
        if right_start > len(list_right) - 1:
            new_list = new_list + list_left[left_start:]
            break

        #comparison step for merge sort
        if list_left[left_start] <= list_right[right_start]:
            new_list.append(list_left[left_start])
            left_start += 1
        else:
            new_list.append(list_right[right_start])
            right_start += 1

        #visualize each merge step
        if visualize:
            visualize(new_list)

    #final visualization for this merge completion
    if visualize:
        visualize(new_list)

    return new_list


input_list_indexes = []
input_list_values = []

def add_number(new_number):
    """
    adds a number to the user's unsorted list
    also returns a DataFrame for the visualization
    """
    input_list_indexes.append(len(input_list_indexes))
    input_list_values.append(new_number)

    return pd.DataFrame({
        "Index": input_list_indexes,
        "Value": input_list_values,
    })


def reset_list():
    """
    clears stored list
    """
    input_list_indexes.clear()
    input_list_values.clear()

    return pd.DataFrame({
        "Index": [],
        "Value": [],
    })


def visualize_step(current_list):
    """
    converts the current list state into a DataFrame
    so the Gradio BarPlot can display it
    """
    return pd.DataFrame({
        "Index": list(range(len(current_list))),
        "Value": current_list,
    })


def submit_unsorted_list():
    """
    runs merge sort on the input list and yields
    each visualization frame (with a delay)
    """
    frames = []

    #captures each visualization step produced by merge sort function
    def capture(frame):
        frames.append(visualize_step(frame))

    #run merge sort (this will populate frames)
    merge_sort(input_list_values, visualize=capture)

    #stream each frame to the Gradio BarPlot
    for df in frames:
        yield df
        time.sleep(0.3)

    #MAKE SURE my final frame is shown again at the end
    if frames:
        yield frames[-1]
        return frames[-1]
    else:
        return visualize_step([])


with gr.Blocks() as demo:
    gr.Markdown("## Merge Sort Visual")

    input_number = gr.Number(label="Enter A Number", maximum=99)
    reset_button = gr.Button("Reset List")
    submit_number = gr.Button("Submit Number")
    sort_unsorted_list = gr.Button("Submit List of Numbers")
    
    #BarPlot automatically reads Index and Value columns from my dataFrames
    list_visual = gr.BarPlot(
        value=None,
        x="Index",
        y="Value",
        title="Merge Sort Visual",
        x_lim=[0, 20]
    )

    #add number button updates the displayed list
    submit_number.click(
        fn=add_number, 
        inputs=input_number, 
        outputs=list_visual
    )

    #sort button streams on every merge sort step
    sort_unsorted_list.click(
        fn=submit_unsorted_list, 
        inputs=[], 
        outputs=list_visual
    )
    
    #reset button just resets the list.
    reset_button.click(
        fn=reset_list, 
        inputs=[], 
        outputs=list_visual
    )

demo.launch()