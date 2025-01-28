import streamlit as st

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

# Display step details
st.header(step)

# Iterate through line items for the selected step
for line_item in checklist[step]:
    st.subheader(line_item)

    # Input code snippet
    code_input = st.text_area(
        f"Write code for: {line_item}", 
        key=f"code_{line_item}", 
        placeholder=f"Type your Python code here for '{line_item}'"
    )

    # Optional: Execute snippet
    execute = st.checkbox(f"Execute {line_item}", key=f"execute_{line_item}")
    if execute and code_input.strip():  # Ensure there is code to execute
        exec_globals = {}
        try:
            exec(code_input, exec_globals)
            st.success("Execution Successful!")
        except Exception as e:
            st.error(f"Error: {e}")

# Save and Export
st.sidebar.title("Export Options")
if st.sidebar.button("Export Code Snippets"):
    with open("data_scientist_checklist_code.py", "w") as file:
        for step, items in checklist.items():
            file.write(f"# {step}\n")
            for item in items:
                code = st.session_state.get(f"code_{item}", "")
                if code.strip():  # Only include non-empty code snippets
                    file.write(f"# {item}\n{code}\n\n")
    st.sidebar.success("Code exported successfully!")
