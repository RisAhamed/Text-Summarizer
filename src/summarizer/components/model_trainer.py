from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk
import tensorflow as tf
from src.summarizer.entity import ModelTrainerConfig
import os

@tf.autograph.experimental.do_not_convert
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # Load model and tokenizer with TensorFlow
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = TFAutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)

        dataset_samsum_pt = load_from_disk(self.config.data_path)

        # Prepare the datasets
        train_dataset = dataset_samsum_pt["train"].to_tf_dataset(
            columns=["input_ids", "attention_mask", "labels"],
            shuffle=True,
            batch_size=self.config.per_device_train_batch_size,
            collate_fn=lambda x: tokenizer.pad(x, return_tensors="tf"),
        )

        eval_dataset = dataset_samsum_pt["validation"].to_tf_dataset(
            columns=["input_ids", "attention_mask", "labels"],
            shuffle=False,
            batch_size=self.config.per_device_train_batch_size,
            collate_fn=lambda x: tokenizer.pad(x, return_tensors="tf"),
        )

        # Compile the model
        model.compile(
            optimizer= tf.keras.optimizers.Adam(learning_rate=3e-5),
            loss=model.compute_loss  # Model's loss function is directly used
        )

        # Train the model
        model.fit(
            train_dataset,
            validation_data=eval_dataset,
            epochs=self.config.num_train_epochs,
        )

        # Save model and tokenizer
        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
# from transformers import TrainingArguments, Trainer
# from transformers import DataCollatorForSeq2Seq
# from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
# from datasets import load_dataset, load_from_disk
# class ModelTrainer:
#     def __init__(self, config: ModelTrainerConfig):
#         self.config = config



    
#     def train(self):
#         device = "cpu"
#         tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
#         model_pegasus = TFAutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
#         seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
#         #loading data 
#         dataset_samsum_pt = load_from_disk(self.config.data_path)

#         # trainer_args = TrainingArguments(
#         #     output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
#         #     per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
#         #     weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
#         #     evaluation_strategy=self.config.evaluation_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
#         #     gradient_accumulation_steps=self.config.gradient_accumulation_steps
#         # ) 


#         trainer_args = TrainingArguments(
#             output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
#             per_device_train_batch_size=1, per_device_eval_batch_size=1,
#             weight_decay=0.01, logging_steps=10,
#             evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
#             gradient_accumulation_steps=16
#         ) 

#         trainer = Trainer(model=model_pegasus, args=trainer_args,
#                   tokenizer=tokenizer, data_collator=seq2seq_data_collator,
#                   train_dataset=dataset_samsum_pt["train"], 
#                   eval_dataset=dataset_samsum_pt["validation"])
        
#         trainer.train()

#         ## Save model
#         model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
#         ## Save tokenizer
#         tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
