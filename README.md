# Wordle Curdle

A tool to generate fake Wordle scores, because you're a great big cheat.

[Available here.](https://share.streamlit.io/ewandennis/wordle-curdle/main/wordle-curdle.py)

## How To Run Locally

### Dependencies
 - python 3
 - [streamlit.io](https://streamlit.io/)

### Steps
1. Clone repo: `git clone https://github.com/ewandennis/wordle-curdle.git`
1. Optional: create a virtual environment for wordle-curdle: `python -m venv wordle-curdle`
  - Activate your new virtual environment: `cd wordle-curdle && . bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Start local streamlit server: `streamlit run wordle-curdle.py`
  - Wordle Curdle is now available at [http://localhost:8501/](http://localhost:8501/)

Warning: Streamlit collects anonymous usage stats by default. You can disable that using [these instructions](https://docs.streamlit.io/library/advanced-features/configuration). The config flag is named `gatherUsageStats`.

