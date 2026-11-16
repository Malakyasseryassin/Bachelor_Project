import streamlit as st
from predictor import predict_hate_speech


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Hate Speech Detector",
    page_icon="🛡️",
    layout="wide"
)


# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Hide Streamlit Branding */
header {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Main Container */
.block-container {
    padding-top: 0.5rem;
    padding-left: 3rem;
    padding-right: 3rem;
    padding-bottom: 0rem;
}

/* Background */
.stApp {
    background: linear-gradient(
        180deg,
        #334b91 0%,
        #1f3477 100%
    );
}

/* Title */
.main-title {
    color: white;
    font-size: 48px;
    font-weight: 300;
    margin-top: 25px;
    margin-bottom: 10px;
}

/* Image */
img {
    border-radius: 16px;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.30);
}

/* Input Label */
.input-label {
    color: white;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    margin-top: 10px;
}

/* Text Area */
textarea {
    background-color: rgba(255,255,255,0.92) !important;
    color: black !important;
    border-radius: 16px !important;
    font-size: 20px !important;
    padding: 16px !important;
}

/* Placeholder */
textarea::placeholder {
    color: rgba(0,0,0,0.4) !important;
}

/* Analyze Button */
.stButton button {
    background-color: rgba(255,255,255,0.14);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    height: 48px;
    transition: 0.2s ease;
}

.stButton button:hover {
    background-color: #4f8cff;
    color: white;
}

/* Result Safe */
.safe-box {
    background-color: rgba(80, 200, 120, 0.20);
    border: 2px solid rgba(80, 200, 120, 0.45);
    padding: 16px;
    border-radius: 16px;
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    margin-top: 18px;
}

/* Result Hate */
.hate-box {
    background-color: rgba(255, 80, 80, 0.20);
    border: 2px solid rgba(255, 80, 80, 0.50);
    padding: 16px;
    border-radius: 16px;
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    margin-top: 18px;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# TOP SECTION
# =====================================

col1, col2 = st.columns([3.5, 1.3])

with col1:

    st.markdown(
        '<div class="main-title">🛡️ Hate Speech Detector</div>',
        unsafe_allow_html=True
    )

with col2:

    st.image(
        "assets/gen_image.png",
        width=300
    )


# =====================================
# INPUT SECTION
# =====================================

st.markdown(
    '<div class="input-label">Enter text to analyze:</div>',
    unsafe_allow_html=True
)

user_input = st.text_area(
    "",
    placeholder="Type or paste text here...",
    height=140
)

analyze = st.button(
    "Analyze Text",
    use_container_width=True
)


# =====================================
# PREDICTION
# =====================================

if analyze:

    if user_input.strip() == "":

        st.warning("Please enter text.")

    else:

        label, confidence = predict_hate_speech(user_input)

        if label == "Hate Speech":

            st.markdown(
                f"""
                <div class="hate-box">
                    ⚠️ Hate Speech Detected<br><br>
                    Confidence: {confidence:.2%}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="safe-box">
                    ✅ Non-Hate Speech<br><br>
                    Confidence: {confidence:.2%}
                </div>
                """,
                unsafe_allow_html=True
            )