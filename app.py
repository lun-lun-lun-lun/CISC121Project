import gradio as gr  # type: ignore
import pandas as pd  # type: ignore
import time
import random

def merge_sort(number_list: list[float], visualize=None):
    if visualize:
        visualize(number_list)

    if len(number_list) == 1:
        return number_list
    if len(number_list) == 2:
        result = [min(number_list), max(number_list)]
        if visualize:
            visualize(result)
        return result

    mid_id = len(number_list) // 2
    list_left = merge_sort(number_list[mid_id:], visualize)
    list_right = merge_sort(number_list[:mid_id], visualize)

    total_len = len(list_left) + len(list_right)
    left_start = 0
    right_start = 0
    new_list = []

    while len(new_list) < total_len:
        if left_start > len(list_left) - 1:
            new_list = new_list + list_right[right_start:]
            break
        if right_start > len(list_right) - 1:
            new_list = new_list + list_left[left_start:]
            break

        if list_left[left_start] <= list_right[right_start]:
            new_list.append(list_left[left_start])
            left_start += 1
        else:
            new_list.append(list_right[right_start])
            right_start += 1

        if visualize:
            visualize(new_list)
            
    if visualize:
        visualize(new_list)

    return new_list


input_list_indexes = []
input_list_values = []

def add_number(new_number):
    input_list_indexes.append(len(input_list_indexes))
    input_list_values.append(new_number)
    return pd.DataFrame({
        "Index": input_list_indexes,
        "Value": input_list_values,
    })

def reset_list():
    input_list_indexes.clear()
    input_list_values.clear()
    return pd.DataFrame({
        "Index": [],
        "Value": [],
    })

def visualize_step(current_list):
    return pd.DataFrame({
        "Index": list(range(len(current_list))),
        "Value": current_list,
    })


def submit_unsorted_list():
    # print(input_list_values)
    # print(merge_sort(input_list_values))
    frames = []

    def capture(frame):
        frames.append(visualize_step(frame))
    merge_sort(input_list_values, visualize = capture)

    for df in frames:
        yield df
        time.sleep(0.3)

    if frames:
        yield frames[-1]

    if len(frames) > 0:
        return frames[-1]
    else:
        return visualize_step([])
 





with gr.Blocks() as demo:
    gr.Markdown("## Merge Sort Visual")

    input_number = gr.Number(label="Enter A Number", maximum=99)
    reset_button = gr.Button("Reset List")
    submit_number = gr.Button("Submit Number")
    sort_unsorted_list = gr.Button("Submit List of Numbers")
    
    list_visual = gr.BarPlot(
        value=None,
        x="Index",
        y="Value",
        title="Merge Sort Visual",
        x_lim=[0,20]
    )

    submit_number.click(
        fn=add_number, 
        inputs=input_number, 
        outputs=list_visual
    )
    sort_unsorted_list.click(
        fn=submit_unsorted_list, 
        inputs=[], 
        outputs=list_visual
    )
    
    reset_button.click(
        fn=reset_list, 
        inputs=[], 
        outputs=list_visual
    )

demo.launch()