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
for line_item in checklist[step]:
    st.subheader(line_item)

    # Input code snippet
    st.text_area(f"Write code for: {line_item}", key=f"code_{line_item}")

    # Upload code snippet
    uploaded_file = st.file_uploader(
        f"Upload code snippet for: {line_item}", type=["py"], key=f"upload_{line_item}"
    )

    # Display uploaded code (if any)
    if uploaded_file:
        code_content = uploaded_file.read().decode("utf-8")
        st.code(code_content, language="python")
    
    # Optional: Execute snippet
    execute = st.checkbox(f"Execute {line_item}", key=f"execute_{line_item}")
    if execute and uploaded_file:
        exec_globals = {}
        try:
            exec(code_content, exec_globals)
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
                file.write(f"# {item}\n{code}\n\n")
    st.sidebar.success("Code exported successfully!")
