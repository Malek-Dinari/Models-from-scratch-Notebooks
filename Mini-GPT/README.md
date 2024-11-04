# Mini GPT Decoder Transformer from Scratch

This repository contains a minimal implementation of a GPT-like model, built from scratch as an educational project. This small-scale transformer model is designed to process text sequences and generate outputs in an autoregressive manner, following the general architecture of Generative Pre-trained Transformers (GPT).

## Project Overview

### Goals

- **Understanding GPT Architectures:** This project dives into the core mechanics of GPT-like models, with a focus on self-attention and transformer decoding.
- **From Theory to Practice:** Implementing each component from scratch reinforces comprehension of NLP model construction, making it a great learning resource.
- **Autoregressive Text Generation:** The mini-GPT model is trained on *Shakespeare's complete works* to simulate predictive text generation.

### Dataset

The model uses a compact dataset, `tiny_shakespeare.txt`, which contains over 1,100,000 characters of text from Shakespeare and roughly ~100,000 tokens. This dataset is ideal for testing a small-scale GPT model even with the very simple Bigram Language Model due to its relatively simple language structure.

## Features

- **Transformer Decoder Architecture:** The implementation adheres to a decoder-only transformer design, typical of GPT models.
- **Self-Attention Mechanism:** Each token can attend to all previous tokens in the sequence, ensuring robust context-aware predictions.
- **Positional Encoding:** Adds sequence information, essential for transformers since they lack inherent position awareness.
- **Efficient Training Pipeline:** Optimized to run on personal machines with basic computational resources.

## File Structure

- `gpt_dev1.ipynb` - Jupyter Notebook containing the main code for the model with comments and explanattion & notes.
- `tiny_shakespeare.txt` - Training data used for generating Shakespearean-style text.
- `.ipynb_checkpoints/` - Folder for checkpointing the notebook, generated automatically.

## Installation & Setup

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/Malek-Dinari/Models-from-scratch-Notebooks.git
cd Models-from-scratch-Notebooks
