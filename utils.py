import ipywidgets as widgets
import os 
import sys

dataset_selector = widgets.Dropdown(
    options=os.listdir('./data/Univariate_ts'),
    description='Dataset:',
    disabled=False,
)

