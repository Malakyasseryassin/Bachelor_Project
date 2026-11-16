import torch
from transformers import BertTokenizer
from app.model import BERT_CNN_MultiKernel


# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Load tokenizer
tokenizer = BertTokenizer.from_pretrained(
    "saved_model/tokenizer"
)


# Load model
model = BERT_CNN_MultiKernel()

model.load_state_dict(
    torch.load(
        "saved_model/bert_cnn_model.pt",
        map_location=device
    )
)

model.to(device)

model.eval()


def predict_hate_speech(text):

    encoding = tokenizer(
        text,
        truncation=True,
        padding='max_length',
        max_length=128,
        return_tensors='pt'
    )

    input_ids = encoding['input_ids'].to(device)

    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():

        outputs = model(input_ids, attention_mask)

        probabilities = torch.softmax(outputs, dim=1)

        prediction = torch.argmax(probabilities, dim=1).item()

        confidence = probabilities[0][prediction].item()

    # Convert numerical label to text
    if prediction == 1:
        label = "Hate Speech"
    else:
        label = "Non-Hate Speech"

    return label, confidence