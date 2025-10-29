# NLP Trigram Model - Text Prediction & Completion

A statistical Natural Language Processing system that predicts and completes sentences using a trigram language model trained on Persian text. (This project is also a part of the [Artificial Intelligence Course](https://github.com/zamirmehdi/Artificial-Intelligence-Course) repository.)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![NLP](https://img.shields.io/badge/NLP-Language%20Modeling-green.svg)](#)
[![Persian](https://img.shields.io/badge/Language-Persian-red.svg)](#)

<details> <summary><h2>📚 Table of Contents</h2></summary>

- [Project Overview](#-project-overview)
- [N-gram Language Models](#-n-gram-language-models)
  - [What is a Trigram?](#what-is-a-trigram)
  - [Example](#example)
  - [N-gram Types](#n-gram-types)
- [Project Structure](#️-project-structure)
- [Files Description](#-files-description)
- [Requirements](#️-requirements)
- [How to Run](#-how-to-run)
- [Input/Output](#-inputoutput)
- [Key Features](#-key-features)
- [Concepts Demonstrated](#-concepts-demonstrated)
- [Model Evaluation](#-model-evaluation)
- [Customization](#-customization)
- [Theoretical Background](#-theoretical-background)
- [Persian Language Considerations](#-persian-language-considerations)
- [References](#-references)
- [Project Information](#ℹ️-project-information)
- [Related Projects](#-related-projects)
- [Contact](#-contact)

</details>

## 📋 Project Overview

This project implements a **trigram language model** for Persian text that:
- Learns word patterns from a training corpus
- Predicts the next word given two previous words
- Completes partial sentences
- Generates coherent text based on learned probabilities

## 🧠 N-gram Language Models

### What is a Trigram?

A **trigram** is a sequence of three consecutive words. The trigram model predicts the next word based on the previous two words:

```
P(w₃ | w₁, w₂) = Count(w₁, w₂, w₃) / Count(w₁, w₂)
```

### Example
Given: "من به" (I to/at)  
Predict: "مدرسه" (school), "خانه" (home), "دانشگاه" (university), etc.

### N-gram Types

| Model | Context | Formula |
|-------|---------|---------|
| **Unigram** | No context | P(wᵢ) |
| **Bigram** | 1 previous word | P(wᵢ \| wᵢ₋₁) |
| **Trigram** | 2 previous words | P(wᵢ \| wᵢ₋₂, wᵢ₋₁) |
| **N-gram** | n-1 previous words | P(wᵢ \| wᵢ₋ₙ₊₁, ..., wᵢ₋₁) |

## 🗂️ Project Structure

```
NLP-Project/
├── main.py              # Trigram model implementation
├── Train_data.txt       # Training corpus (Persian text)
├── Test_data.txt        # Test cases
├── labels.txt           # Expected outputs for evaluation
└── Instruction NLP.pdf  # Project specification
```

## 📄 Files Description

### `main.py`
Core implementation containing:
- Text preprocessing (tokenization, normalization)
- Trigram probability calculation
- Model training
- Next word prediction
- Sentence completion
- Evaluation metrics

### `Train_data.txt`
Persian text corpus for training:
- Multiple sentences in Persian
- Used to build trigram frequency counts
- Vocabulary extraction

### `Test_data.txt`
Test cases for evaluation:
- Incomplete sentences
- Context pairs for prediction
- Evaluation scenarios

### `labels.txt`
Ground truth for testing:
- Expected predictions
- Correct completions
- Accuracy measurement

## ⚙️ Requirements

```bash
# Python 3.x
# Standard library only (no external dependencies)
```

### Optional (for enhanced features)
```bash
pip install hazm  # Persian text processing (if used)
```

## 🚀 How to Run

```bash
# Navigate to project directory
cd NLP-Project

# Run the trigram model
python main.py
```

### Program Flow
1. Load and preprocess training data
2. Build trigram frequency tables
3. Calculate probabilities
4. Load test cases
5. Make predictions
6. Compare with labels and calculate accuracy

## 📊 Input/Output

### Input
**Training Phase:**
- `Train_data.txt` - Persian sentences for model training

**Prediction Phase:**
- `Test_data.txt` - Contexts for prediction (two-word sequences)

### Output
- Predicted next words
- Probability scores
- Completed sentences
- Accuracy metrics
- Model statistics

### Example

**Input:** "من به"  
**Output:**
```
Top 3 predictions:
1. مدرسه (P = 0.35)
2. خانه (P = 0.28)
3. دانشگاه (P = 0.15)
```

## 🎯 Key Features

### 1. Text Preprocessing
- Tokenization (word splitting)
- Normalization (character standardization)
- Handling Persian-specific characters
- Stop word consideration

### 2. Trigram Extraction
- Sliding window over text
- Frequency counting
- Context-word pair storage

### 3. Probability Calculation
```python
P(w₃ | w₁, w₂) = Count(w₁, w₂, w₃) / Count(w₁, w₂)
```

### 4. Smoothing (Optional)
Handles zero-probability cases:
- Laplace smoothing (add-one)
- Add-k smoothing
- Back-off to bigram/unigram

### 5. Prediction Strategies
- **Greedy:** Select highest probability word
- **Sampling:** Random selection based on probability distribution
- **Beam search:** Multiple candidate sequences

## 🎓 Concepts Demonstrated

### Statistical NLP
- Language modeling
- Maximum likelihood estimation
- Markov assumption
- Probability distributions

### Text Processing
- Tokenization
- Normalization
- Vocabulary building
- Context windowing

### Machine Learning
- Training on corpus
- Model evaluation
- Accuracy metrics
- Overfitting considerations

### Algorithm Design
- Efficient data structures (dictionaries/hash tables)
- Probability calculations
- Text generation
- Performance optimization

## 📈 Model Evaluation

### Metrics
- **Accuracy:** Percentage of correct predictions
- **Perplexity:** Model's uncertainty (lower is better)
- **Top-K Accuracy:** Correct word in top K predictions

### Example Results
```
Test samples: 100
Correct predictions: 73
Accuracy: 73%
Average perplexity: 45.2
```

## 🔧 Customization

You can modify:
- **N-gram size** (trigram → bigram/4-gram)
- **Smoothing technique**
- **Training corpus** (add more data)
- **Prediction strategy** (greedy vs. sampling)

## 📖 Theoretical Background

### Markov Assumption
The probability of a word depends only on a fixed number of previous words:
```
P(sentence) ≈ ∏ P(wᵢ | wᵢ₋₂, wᵢ₋₁)
```

### Advantages
✅ Simple and interpretable  
✅ Fast training and prediction  
✅ Works well for short contexts  
✅ No complex neural architectures needed

### Limitations
❌ Limited context window  
❌ Data sparsity issues  
❌ No semantic understanding  
❌ Requires large corpus

## 🌐 Persian Language Considerations

### Challenges
- Right-to-left script
- Complex morphology
- Informal vs. formal variants
- Diacritics and vowel marks

### Solutions
- Proper Unicode handling
- Character normalization
- Consideration of language-specific features

## 📚 References

- **Jurafsky, D., & Martin, J. H.** (2023). *Speech and Language Processing* (3rd ed.).
- **Manning, C. D., & Schütze, H.** (1999). *Foundations of Statistical Natural Language Processing*.

## ℹ️ Project Information

**Author:** Amirmehdi Zarrinnezhad  
**Course:** Artificial Intelligence  
**University:** Amirkabir University of Technology (Tehran Polytechnic) - Spring 2020  
**GitHub:** [AI_Final_Project-NLP](https://github.com/zamirmehdi/AI_Final_Project-NLP)

## 🔗 Related Projects

This project is part of the [Artificial Intelligence Course](https://github.com/zamirmehdi/Artificial-Intelligence-Course) repository.

**Other AI Projects:**
- [Students Lineup](https://github.com/zamirmehdi/Artificial-Intelligence-Course/tree/main/Students-Lineup-Project) - Search algorithms
- [Super Mario LRTA*](https://github.com/zamirmehdi/AI-Project-Super-Mario) - Heuristic pathfinding


## 📧 Contact  
Questions or collaborations? Feel free to reach out!

**📧 Email:** amzarrinnezhad@gmail.com  
**🌐 GitHub:** [@zamirmehdi](https://github.com/zamirmehdi)


---

<div align="center">

[⬆ Back to Main Repository](https://github.com/zamirmehdi/Artificial-Intelligence-Course)

<p align="right">(<a href="#top">back to top</a>)</p>
</div>



<div align="center">

⭐ **If you found this project helpful, please consider giving it a star!** ⭐

*Amirmehdi Zarrinnezhad*

</div>
