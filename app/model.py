import torch
import torch.nn as nn
from transformers import BertModel


class BERT_CNN_MultiKernel(nn.Module):

    def __init__(
        self,
        bert_model_name='bert-base-uncased',
        num_classes=2,
        dropout=0.3
    ):
        super(BERT_CNN_MultiKernel, self).__init__()

        self.bert = BertModel.from_pretrained(bert_model_name)

        self.convs = nn.ModuleList([
            nn.Conv1d(
                in_channels=768,
                out_channels=128,
                kernel_size=k
            )
            for k in [2, 3, 4, 5]
        ])

        self.relu = nn.ReLU()

        self.dropout = nn.Dropout(dropout)

        self.fc = nn.Linear(128 * 4, num_classes)

    def forward(self, input_ids, attention_mask):

        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        x = outputs.last_hidden_state

        x = x.permute(0, 2, 1)

        conv_outputs = []

        for conv in self.convs:

            c = self.relu(conv(x))

            pooled = torch.max(c, dim=2)[0]

            conv_outputs.append(pooled)

        x = torch.cat(conv_outputs, dim=1)

        x = self.dropout(x)

        logits = self.fc(x)

        return logits