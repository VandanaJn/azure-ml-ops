from transformers import RobertaForSequenceClassification
import torch

model = RobertaForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model.eval()

# Dummy input for export shape (batch size = 1, seq length = 64 for example)
dummy_input_ids = torch.randint(0, 100, (1, 64))
dummy_attention_mask = torch.ones((1, 64))

# Export to ONNX
torch.onnx.export(
    model,
    (dummy_input_ids.long(), dummy_attention_mask.long()),
    "webapp/roberta_sentiment.onnx",
    input_names=["input_ids", "attention_mask"],
    output_names=["logits"],
    dynamic_axes={"input_ids": {0: "batch_size", 1: "seq_length"},
                  "attention_mask": {0: "batch_size", 1: "seq_length"},
                  "logits": {0: "batch_size"}},
    opset_version=11
)
