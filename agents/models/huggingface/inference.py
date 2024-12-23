from transformers import BertForSequenceClassification, BertConfig

# Load model and config
model = BertForSequenceClassification.from_pretrained("path_to_model_directory")
config = BertConfig.from_pretrained("path_to_model_directory")

print(config)