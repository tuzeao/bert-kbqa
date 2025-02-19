#!/usr/bin/env sh

python="/ssd/exec/tuzeao/anaconda3/envs/baike/bin/python"

mkdir -p output_bert-crf

$python NER_main.py \
  --data_dir=./input/data/ner_data \
  --vob_file=./input/config/bert-base-chinese-vocab.txt \
  --model_config=./input/config/bert-base-chinese-config.json \
  --output_dir=./output_bert-crf \
  --pre_train_model=./input/config/bert-base-chinese-model.bin \
  --max_seq_length=64 \
  --do_train \
  --train_batch_size=64 \
  --eval_batch_size=256 \
  --num_train_epochs=50
  
  

