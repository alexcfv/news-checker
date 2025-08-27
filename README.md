# 📰 Fake News Classifier Bot

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)](https://scikit-learn.org/)
[![pandas](https://img.shields.io/badge/pandas-1.5%2B-lightblue)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)

---

### WORK ONLY FOR RUSSIAN LANG

## 📖 About the Project
This project is a **Telegram bot** that classifies news headlines as **true** or **fake**.  
The bot evaluates credibility **offline**, based entirely on historical data, without accessing the internet.

This leads to an interesting effect:  
> For example, a headline like  
> *"The heir was killed, a war may start"*  
> may be classified as highly probable, because historically such events often led to wars (e.g., WWI).  
> As a result, overly dramatic news may appear “true” to the model.

---

## 🔍 Key Features
- Built with **Python** using:
  - `pandas` for data preprocessing
  - `scikit-learn` for machine learning
- Works through a simple **Telegram bot interface**
- Trained on a **small dataset** with only two labels:
  - ✅ `True` — reliable news  
  - ❌ `False` — fake news
- No large-scale Russian dataset with multi-class labels (e.g., *propaganda*, *manipulation*, *clickbait*) is currently available.

---

## 🛠️ Tech Stack
| Technology           | Purpose                              |
|----------------------|-------------------------------------|
| Python               | Core programming language          |
| pandas               | Data processing                    |
| scikit-learn         | ML model training and evaluation   |
| python-telegram-bot  | Telegram Bot API integration       |

---

## 📊 How It Works
1. A user sends a news headline to the bot.
2. The bot:
   - Preprocesses and tokenizes the text
   - Converts it into numerical features
3. The trained model predicts:
   - `True` or `False`

---

## 💡 Future Ideas
Add additional labels (propaganda, manipulation, clickbait, etc.)

Use larger and more diverse datasets

Experiment with modern NLP models (e.g., transformers)

Explore fact-checking with external APIs

## ⭐ Contributing
This project is primarily a showcase.
Feel free to leave a star or open a pull request with suggestions!

## 📬 Contact
Open an issue or reach out if you'd like to discuss improvements.

---

## 📖 Author note
The idea was to create a bot that determines whether news is fake or not.
In fact, the big problem is the correctness of its judgments,
the algorithm does not have access to the Internet, it determines the news based on historical data and that's the whole catch.
In fact, the news may be fake, but too "harsh" like, for example: "the heir was killed, there may be a war",
if you think like an algorithm, then the probability of the event "war" when the event "the heir was killed" occurred is very high (this is how the First World War began).
A lot of other things depend on the quality of historical data, in my case there is a rather small dataset and it only has 2 classes (true and false),
if there were also, for example, such classes as: propaganda, manipulation, etc., the algorithm would determine this quite well, since it can track down such psychological manipulations in the text
But alas, there is no such high-quality dataset in Russian yet (at least I have not found it)
