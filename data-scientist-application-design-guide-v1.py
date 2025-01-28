import streamlit as st
import json
import pandas as pd
from fpdf import FPDF

# Checklist steps and line items
checklist = {
    "Problem Identification": [
        "Define the purpose of the web application.",
        "Identify questions to answer using data."
    ],
    "Data Analysis": [
        "Find patterns and trends in datasets.",
        "Improve the quality of data or product offerings."
    ],
    "Model Development": [
        "Create algorithms and data models.",
        "Apply machine learning techniques."
    ],
    "Tool Deployment": [
        "Develop using Streamlit framework.",
        "Host on cloud platforms like Streamlit Cloud."
    ],
    "Visualization and Reporting": [
        "Create interactive visualizations.",
        "Use charts and maps for insights."
    ]
}

st.title("Data Scientist Web Application Checklist")

# Sidebar navigation
step = st.sidebar.selectbox("Select Step", list(checklist.keys()))

# Collect user inputs
user_inputs = {}

st.header(step)
for line_item in checklist[step]:
    st.subheader(line_item)

    # Input code snippet
    code_input = st.text_area(
        f"Write code for: {line_item}",
        key=f"code_{line_item}",
        placeholder=f"Type your Python code here for '{line_item}'"
    )
    # Save the input in user_inputs dictionary
    user_inputs[line_item] = code_input

# Save and Export
st.sidebar.title("Export Options")

# Function to export to JSON
def export_to_json(data):
    file_name = "data_scientist_checklist.json"
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
    return file_name

# Function to export to CSV
def export_to_csv(data):
    file_name = "data_scientist_checklist.csv"
    df = pd.DataFrame([{"Task": task, "Code": code} for task, code in data.items()])
    df.to_csv(file_name, index=False)
    return file_name

# Function to export to PDF
def export_to_pdf(data):
    file_name = "data_scientist_checklist.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Data Scientist Web Application Checklist", ln=True, align="C")
    for task, code in data.items():
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, f"Task: {task}\nCode:\n{code}\n")
    pdf.output(file_name)
    return file_name

# Export options
export_format = st.sidebar.selectbox("Select Export Format", ["JSON", "CSV", "PDF"])
if st.sidebar.button("Export Code Snippets"):
    if any(user_inputs.values()):  # Ensure there's at least one input
        if export_format == "JSON":
            file_name = export_to_json(user_inputs)
        elif export_format == "CSV":
            file_name = export_to_csv(user_inputs)
        elif export_format == "PDF":
            file_name = export_to_pdf(user_inputs)
        
        with open(file_name, "rb") as file:
            st.sidebar.download_button(
                label=f"Download {export_format} File",
                data=file,
                file_name=file_name,
                mime={
                    "JSON": "application/json",
                    "CSV": "text/csv",
                    "PDF": "application/pdf"
                }[export_format]
            )
    else:
        st.sidebar.warning("Please input code snippets before exporting.")
