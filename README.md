 
# Hate Speech Detection Using Deep Learning

A deep learning-based hate speech detection system that identifies hateful and non-hateful content in social media text. This project investigates multiple neural network architectures and introduces a hybrid **BERT + Multi-Kernel Convolutional Neural Network (CNN)** model designed to combine contextual language understanding with multi-scale textual feature extraction.

The project also incorporates a data enhancement pipeline to improve robustness against noisy social media language, including obfuscation, leetspeak, slang, and implicit hate speech.

## Overview

The widespread use of social media has increased the need for reliable automated content moderation systems. However, detecting hate speech remains challenging due to informal language, spelling variations, contextual ambiguity, and implicit expressions of hostility.

This project explores different deep learning approaches to address these challenges, evaluates their classification performance, and develops a deployable hate speech detection application.

**Main objectives:**
- Investigate and compare multiple deep learning architectures.
- Evaluate the impact of raw and preprocessed text on classification performance.
- Improve robustness against obfuscated and implicit hate speech.
- Develop a hybrid BERT + Multi-Kernel CNN architecture.
- Evaluate model performance using internal and external datasets.
- Deploy the final model through an interactive Streamlit application.

## Proposed Methodology

The proposed architecture combines two complementary approaches:

**BERT (Bidirectional Encoder Representations from Transformers)**
- Generates contextualized text representations.
- Captures semantic relationships and contextual dependencies.
- Provides a deeper understanding of the input text.

**Multi-Kernel CNN**
- Extracts localized textual features.
- Captures patterns of varying lengths through multiple convolutional kernel sizes.
- Identifies discriminative linguistic patterns relevant to hate speech classification.

By combining contextual embeddings with multi-scale convolutional feature extraction, the hybrid architecture aims to improve classification performance and robustness.

## Model Architectures

The following architectures were implemented and evaluated:

| Model | Description |
|---|---|
| CNN V1 | Initial convolutional neural network |
| CNN V2 | Multi-kernel TextCNN architecture |
| CNN V3 | Enhanced CNN architecture |
| BiLSTM | Bidirectional Long Short-Term Memory network |
| BERT | Transformer-based contextual model |
| Proposed Hybrid | BERT + Multi-Kernel CNN |

## Data Enhancement Pipeline

A dedicated enhancement pipeline was developed to address common challenges in social media text classification.

The implemented techniques include:

- **Text Cleaning:** Normalization of noisy text and removal of unnecessary characters.
- **Obfuscation Handling:** Detection and normalization of intentionally modified offensive words.
- **Leetspeak Normalization:** Handling character substitutions commonly used to evade text filters.
- **Slang Normalization:** Standardization of informal social media expressions.
- **Keyword Masking:** Reducing excessive dependence on specific lexical indicators.
- **Implicit Hate Speech Augmentation:** Expanding the representation of hateful expressions that do not rely on explicit offensive vocabulary.

These enhancements were introduced to improve the model's ability to recognize different forms of hateful language.

## Dataset

The primary training dataset consists of approximately 48,199 samples, combining English-language hate speech data from multiple sources.

The dataset incorporates samples from:
- Waseem and Hovy
- Impermium
- Davidson

**Final dataset distribution:**

| Class | Samples |
|---|---:|
| Hate Speech | 27,911 |
| Non-Hate Speech | 20,288 |
| **Total** | **48,199** |

External datasets, including Davidson and TSA Analytics Vidhya, were also used to investigate cross-dataset generalization.

*Note: Dataset files are not included in this repository. Please refer to the original dataset sources and their respective usage terms.*

## Experimental Results

The proposed hybrid architecture achieved the following results on the primary test dataset:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | **89.43%** |
| Precision | **91.19%** |
| Recall | **90.44%** |
| F1-score | **90.81%** |

The model was selected based on its F1-score, providing a balanced assessment of precision and recall.

These results demonstrate the effectiveness of combining transformer-based contextual representations with multi-kernel convolutional feature extraction.

## Application Demo

The trained model was integrated into an interactive web application using Streamlit.

The application allows users to:
- Enter text for analysis.
- Run real-time hate speech classification.
- View the predicted class.
- Examine the model's prediction confidence.

### Interface
<img width="456" height="234" alt="image" src="https://github.com/user-attachments/assets/80ffb54d-d9ad-4207-8858-2fa9c9d20757" />



## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| PyTorch | Deep learning implementation |
| Hugging Face Transformers | BERT implementation |
| Scikit-learn | Dataset splitting and evaluation |
| Pandas & NumPy | Data processing |
| NLTK | Text preprocessing |
| Streamlit | Interactive web application |
| Matplotlib & Seaborn | Experimental visualization |

## Project Structure

```text
Bachelor_Project/
│
├── app/
│   ├── predictor.py
│   └── streamlit_app.py
│
├── assets/
│   └── gen_image.png
│
├── data/
│   └── improved_dataset_final.csv
│
├── saved_model/
│   ├── bert_cnn_model.pt
│   └── tokenizer/
│
├── notebooks/
│   ├── dataset_preprocessing.ipynb
│   ├── improvements.ipynb
│   └── hybrid_training.ipynb
│
├── requirements.txt
└── README.md
```

*The structure above illustrates the main project components. Adjust the directory names to match the final repository.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Bachelor_Project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
.\venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure the PyTorch installation is compatible with your hardware and CUDA configuration.

### 4. Run the application

From the project's root directory:

```bash
python -m streamlit run app/streamlit_app.py
```

The application will open in your default browser.

## Limitations

Although the proposed model demonstrates promising classification performance, certain challenges remain:

- Difficulty identifying sarcastic and humorous hate speech.
- Challenges with implicit hostility and ambiguous target references.
- Sensitivity to distribution shifts between datasets.
- Dependence on the quality and diversity of training data.
- Higher computational requirements compared to simpler classification architectures.

## Future Improvements

Potential directions for further development include:

- Exploring advanced transformer architectures such as RoBERTa and DeBERTa.
- Incorporating conversational context and discourse-level information.
- Expanding multilingual hate speech detection capabilities.
- Investigating adversarial training and advanced data augmentation.
- Developing explainable AI capabilities.
- Extending the application into a more comprehensive content moderation platform.

## Academic Context

This project was developed as part of a Bachelor of Science thesis in Media Engineering and Technology at the German University in Cairo.

**Research Title:** Hate Speech Detection Using Deep Learning

**Supervisor:** Dr. Mahmoud Ibrahim Khalil

The project explores the effectiveness of deep learning and hybrid neural network architectures for automated hate speech detection in social media environments.

## License

Please add an appropriate license before distributing or reusing this project. Ensure that the licenses and usage conditions of all third-party datasets, pretrained models, and dependencies are respected.

---

**Developed as a research project exploring more robust and context-aware approaches to automated hate speech detection.**
