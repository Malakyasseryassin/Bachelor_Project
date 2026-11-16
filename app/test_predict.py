from app.predictor import predict_hate_speech

text = "all muslims should die"

prediction, confidence = predict_hate_speech(text)

print(prediction)
print(confidence)