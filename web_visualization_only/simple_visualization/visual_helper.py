# 1
import pandas as pd
# 23
from sklearn.preprocessing import normalize 
# 25
import plotly.graph_objects as go
# 26
import plotly.express as px
# 27
import plotly.offline as opy

import os

def graphics():
    # 1
    dir_path = os.path.dirname(os.path.realpath(__file__))

    excel_path = os.path.join(dir_path,"Base_Persona_V2.xlsx")
    excel = pd.ExcelFile(excel_path)
    excel.sheet_names

    # 2
    help(excel.parse)

    # 3
    labels = excel.parse(sheet_name=excel.sheet_names[-1], header=1)
    # 4
    labels
    
    # 5
    structured_data = excel.parse(sheet_name=excel.sheet_names[:-1], header=1)
    
    # 6
    excel.sheet_names

    # 7
    print("--- LOSS in data cleaning ---")
    cleaned_data = {} 
    for key in excel.sheet_names[:-1]:
        cleaned_data.update({key:structured_data[key].dropna()})
        loss = len(structured_data[key])-len(cleaned_data[key])
        print(f"sheet name: {key}")
        print(f"loss: {loss}")
        
    # 8
    print('--- Times in the Research the Name was Cited ---')
    print(
    cleaned_data['Março 2019']['Celebridade'].value_counts()
        )

    # 9
    print("\n".join(list(cleaned_data['Março 2019'].columns)))

    # 10
    print("--- LOSS in data cleaning ---")
    for key in excel.sheet_names[:-1]:
        cleaned_data.update({key:cleaned_data[key][cleaned_data[key]['Gênero'] == 2]})
        loss = len(structured_data[key])-len(cleaned_data[key])
        remaining = len(cleaned_data[key])
        print(f"sheet name: {key}")
        print(f"loss: {loss}")
        print(f"remaining: {remaining}")

    # 11
    average_age = cleaned_data['Março 2019']['Idade'].mean()

    # 12
    average_age

    # 13
    print("--- LOSS in data cleaning ---")
    for key in excel.sheet_names[:-1]:
        cleaned_data.update({key:cleaned_data[key][cleaned_data[key]['Idade'] > average_age]})
        loss = len(structured_data[key])-len(cleaned_data[key])
        remaining = len(cleaned_data[key])
        print(f"sheet name: {key}")
        print(f"loss: {loss}")
        print(f"remaining: {remaining}")

    # 14
    cleaned_data[key][cleaned_data[key]['Idade'] > average_age]

    # 15
    cleaned_data['Março 2019'].groupby(['Celebridade']).mean()

    # 16
    cleaned_data['Março 2019'].columns == cleaned_data['Julho 2019'].columns 

    # 17
    cleaned_data['Julho 2019'].columns == cleaned_data['Dezembro 2019'].columns

    # 18
    data_sheet_names = list(cleaned_data.keys()) 
    data_agregated = cleaned_data[data_sheet_names[0]].groupby(['Celebridade']).mean()
    data_sheet_names = data_sheet_names[1:]
    for data_sheet_name in data_sheet_names:
        data_agregated += cleaned_data[data_sheet_name].groupby(['Celebridade']).mean()
    
    # 19
    data_agregated

    # 20
    data_agregated_cleaned = data_agregated.dropna()

    # 21
    data_agregated_cleaned = data_agregated_cleaned.drop(columns=['Idade','Gênero'])

    # 22
    data_agregated_cleaned

    # 23

    # 24
    data_normalized = normalize(data_agregated_cleaned)

    # 25
    colorscale=[[0.0, "rgb(255,255,255)"],
                    [1.0, "rgb(255,125,0)"]]

    colorbar=dict(
            tick0=0,
            dtick=1
        )

    fig = go.Figure(data=go.Heatmap(
                        z=data_normalized,
                        y=list(data_agregated_cleaned.index),
                        x=list(range(len(data_agregated_cleaned.columns))),
                        colorscale=colorscale,
                        colorbar=colorbar
    ))
    heatmap = fig
    #fig.show() 
    
    # 26
    fig = px.scatter(
        y=list(data_agregated_cleaned.index),
        x=list(data_agregated_cleaned.T.sum()))
    scatter = fig
    
    # 27
    # import

    # 28
    scatter_to_render = opy.plot(scatter, auto_open=False, output_type='div')
    heatmap_to_render = opy.plot(heatmap, auto_open=False, output_type='div')

    #fig.show()
    data_index = list(data_agregated_cleaned.columns)
    return heatmap_to_render, scatter_to_render, data_index, 
