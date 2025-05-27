import streamlit as st

# Add custom CSS for vivid background with semi-transparent content
def set_background():
    st.markdown(
        """
        <style>
        /* Vibrant diagonal stripe pattern */
        .stApp {
            background: linear-gradient(45deg, #e0f7fa 25%, #80deea 25%, #80deea 50%, 
                          #e0f7fa 50%, #e0f7fa 75%, #80deea 75%, #80deea 100%);
            background-size: 56.57px 56.57px;
            background-attachment: fixed;
        }
        
        /* Semi-transparent content area */
        .main .block-container {
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-top: 2rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        /* Question cards with glass effect */
        .stRadio > div {
            background-color: rgba(255, 255, 255, 0.7) !important;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255,255,255,0.4);
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%) !important;
            color: white !important;
            font-weight: bold !important;
            border: none !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        
        /* Title styling */
        h1 {
            color: #2575fc !important;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background
set_background()
# Define the multiple-choice questions and answers
questions = [
    {
    'question': "What is the primary objective of this project?",
    'options': [
        "Classifying individuals based on the presence or absence of Alzheimer's disease",
        "Predicting the risk of developing Alzheimer's disease",
        "Performing regression analysis to estimate the probability of having the disease",
        "Clustering individuals based on medical or cognitive features"
    ],
    'correct_answer': "Predicting the risk of developing Alzheimer's disease"
    }
    ,
    {
        'question': "Which machine learning model was the best performing in the project?",
        'options': ["Gradient Boosting", "Decision Tree", "Random Forest", "K-Nearest Neighbors"],
        'correct_answer': "Gradient Boosting"
    },
    {
        'question': "Which social factor is not included in our dataset?",
        'options': ["Age", "Salary", "Marital Status", "Smoking Status"],
        'correct_answer': "Salary"
    },
    {
        'question': "Which regularization method was used?",
        'options': ["Data Augmentation", "Dropout", "All of the above", "No regularization applied"],
        'correct_answer': "All of the above"
    },
    {
        'question': "What is a challenge faced in data collection?",
        'options': ["Realibility", "Outliers", "Missing Data", "Sex Imbalance"],
        'correct_answer': "Sex Imbalance"
    },
    {
        'question': "What biomedical data preprocessing method was used?",
        'options': ["Normalization", "Scaling", "One-Hot Encoding", "Imputation"],
        'correct_answer': "One-Hot Encoding"
    },
    {
        'question': "What evaluation metric was used for model performance?",
        'options': ["Accuracy", "Precision", "Recall", "F1-Score","All of the above"],
        'correct_answer': "All of the above"
    },
    {
        'question': "How can this model be used in the real world?",
        'options': ["Disease Diagnosis", "Consulting Part of Diagnosis Pipeline", "Web Marketing", "None of the above"],
        'correct_answer': "Consulting Part of Diagnosis Pipeline"
    }
]

# Set up the Streamlit app layout
st.title("Alzheimer Prediction Multiple-Choice Game")
st.write("Test your knowledge on Alzheimer's prediction using this multiple-choice game!")

# Initialize an empty dictionary to store answers
answers = {}

# Display each multiple-choice question and capture answers
for idx, question in enumerate(questions):
    st.write(f"**{idx + 1}. {question['question']}**")
    
    user_answer = st.radio(
        f"Select an answer for question {idx + 1}",
        options=question['options'],
        key=f"q_{idx}",
    )
    
    # Store the user's answer
    answers[idx] = user_answer

# Button to submit answers and show results
if st.button("Submit Answers"):
    correct = 0
    # Check if answers are correct
    for idx, user_answer in answers.items():
        if user_answer == questions[idx]['correct_answer']:
            correct += 1
    
    # Display the score
    st.write(f"Your score: {correct}/{len(questions)}")
    
    # Provide correct answers for feedback
    st.write("### Correct Answers:")
    for idx, question in enumerate(questions):
        st.write(f"**{idx + 1}. {question['question']}**")
        st.write(f"Correct Answer: {question['correct_answer']}")

    # Link to continue to the main site
    st.markdown("""
        <br>
        <a href="https://alzheimer-ece-ntua-healthcare.streamlit.app/" target="_blank">
            <button style='background-color:#2575fc; color:white; padding:10px 20px;
                    border:none; border-radius:5px; font-size:16px; cursor:pointer;'>
                Go to Alzheimer Healthcare App
            </button>
        </a>
    """, unsafe_allow_html=True)

    # Collect feedback
    st.subheader("We value your feedback!")
    feedback = st.text_area("Please share any thoughts, suggestions, or impressions you have about the quiz:")
    
    if st.button("Submit Feedback"):
        if feedback.strip():
            st.success("Thank you for your feedback!")
            # Optional: Save to file, database, or email (requires backend integration)
        else:
            st.warning("Feedback cannot be empty. Please enter your comments.")
