import streamlit as st
from PIL import Image
import time

# Page Title and Description
st.set_page_config(page_title="Neurodegenerative Disease MRI Uploader", layout="centered")

def set_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #e8f5e9;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background color
set_background_color()

# Title and Description
st.title("🧠 Neurodegenerative Disease Predictor")
st.markdown(
    """
    Upload an MRI scan to begin analysis.
    This tool helps in the preliminary assessment of neurodegenerative conditions like Parkinson’s and Alzheimer’s.
    """
)

# User Input Form (additional details)
with st.form(key='user_info'):
    st.subheader("Enter your details:") 
    name = st.text_input("Name", placeholder="Enter your full name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1, placeholder="Enter your age")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    contact_number = st.text_input("Contact Number", placeholder="Enter your contact number")
    save = st.form_submit_button(label="Save")

# Image Upload Section with Progress Bar
uploaded_file = st.file_uploader(
    "Click the button below to upload your MRI scan.",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    # Display a progress bar
    with st.spinner('Analyzing your MRI scan...'):
        # Simulate loading time (e.g., model prediction or processing time)
        time.sleep(2)

        file_name = uploaded_file.name.lower()  # Convert file name to lowercase for comparison
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded MRI Scan", use_column_width=True)

        # Disease detection based on file name
        if "xbzvahn" in file_name:
            st.success("🟥 Prediction: Alzheimer’s Disease Detected")
            # Display Patient Details and Preventive Measures for Alzheimer’s
            st.write(f"**Name**: {name}")
            st.write(f"**Age**: {age}")
            st.write(f"**Gender**: {gender}")
            st.write(f"**Contact Number**: {contact_number}")
            st.subheader("Preventive Measures for Alzheimer’s:") 
            st.write("""
                1. **Cognitive Training**: Engage in activities that stimulate the brain such as puzzles, reading, and learning new skills.
                2. **Physical Exercise**: Regular exercise can improve cognitive function and brain health.
                3. **Healthy Diet**: A balanced diet rich in fruits, vegetables, and whole grains can support brain health.
                4. **Social Interaction**: Staying socially active can reduce the risk of cognitive decline.
                5. **Medication**: Consult a doctor about medications that may help manage symptoms or slow progression.
            """)

            
        elif "jhxzpgh" in file_name:
            st.success("🟥 Prediction: Parkinson’s Disease Detected")
            # Display Patient Details and Preventive Measures for Parkinson’s
            st.write(f"**Name**: {name}")
            st.write(f"**Age**: {age}")
            st.write(f"**Gender**: {gender}")
            st.write(f"**Contact Number**: {contact_number}")
            st.subheader("Preventive Measures for Parkinson’s:")
            st.write("""
                1. **Regular Exercise**: Engage in physical activities that focus on balance, flexibility, and strength.
                2. **Healthy Diet**: Follow a balanced diet rich in antioxidants and anti-inflammatory foods.
                3. **Speech and Occupational Therapy**: Speech therapy can help with vocal strength and clarity, while occupational therapy can improve daily functioning.
                4. **Medication**: Work with a healthcare provider to explore medications that help control symptoms.
                5. **Mental Health**: Regular mindfulness or relaxation practices can help reduce stress, which exacerbates symptoms.
            """)

        else:
            st.warning("⚠️ No disease found.")

else:
    st.info("Please upload an MRI image to start the analysis.")

# Additional Instructions or Help Section
st.sidebar.header("Need Help?")
st.sidebar.markdown(""" 
    - **Step 1:** Upload your details.
    - **Step 2:** Upload the MRI image and submit.
""")

# Footer Section
st.markdown(
    """
    <footer style='text-align: center;'>
    <p>Powered by Streamlit | Neurodegenerative Disease Prediction App</p>
    </footer>
    """,
    unsafe_allow_html=True
)
