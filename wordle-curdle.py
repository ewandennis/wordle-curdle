import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import date, timedelta

smartness_scale = ('Rock', 'Horse', 'Person', '5 People', '50 People', 'Genius')

BAD = '⬛'
MISPLACED = '🟨'
GOOD = '🟩'

LINEBREAK = '\n'

bads       = [5, 3, 2, 1, 1, 0]
misplaceds = [0, 2, 2, 1, 0, 0]
goods      = [0, 0, 1, 3, 4, 5]

PUZZLE_210_DATE = date(2022, 1, 15)
PUZZLE_1_DATE = PUZZLE_210_DATE - timedelta(days=210)

def twitter_share_button(txt):
    components.html(
        f"""
        <a href="https://twitter.com/intent/tweet"
                data-text="{txt}"
                data-url=" "
                class="twitter-share-button">
                Tweet
        </a>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        """
    )

def prefix(dt, num_guesses):
    puzzle_num = (dt - PUZZLE_1_DATE).days
    return f'Wordle {puzzle_num} {num_guesses}/6'

def shuffle_string(s):
    return ''.join(random.sample(s, len(s)))

def make_guess(guess_index, num_guesses):
    start_pos = 6 - num_guesses
    seq_pos = start_pos + guess_index
    if guess_index >= num_guesses:
        raise Exception(f'guess_index must be < num_guesses')
    raw_guess = BAD * bads[seq_pos] + MISPLACED * misplaceds[seq_pos] + GOOD * goods[seq_pos]
    if guess_index < num_guesses-1:
        return shuffle_string(raw_guess)
    return raw_guess

def wordle_curdle(smartness, puzzle_date):
    """Generate a sequence of plausible guesses for the given smartness"""
    smarts_index = smartness_scale.index(smartness)
    if smarts_index < 0:
        raise Exception(f'smartness argument must be one of {smartness_scale}')
    num_guesses = 6 - smarts_index
    guesses = [make_guess(guess_index, num_guesses) for guess_index in range(num_guesses)]
    return prefix(puzzle_date, num_guesses) + LINEBREAK + LINEBREAK.join(guesses)

st.title('Wordle Curdle')
st.caption('Create a fake Wordle score because you are dishonest')

smartness = st.select_slider(label='How smart do you want to appear?', options=smartness_scale)
puzzle_date = st.date_input(
    label='What date was the puzzle you want to lie about?',
    value=date.today(),
    min_value=PUZZLE_1_DATE,
    max_value=date.today()
)

score = wordle_curdle(smartness, puzzle_date)
st.text_area(label='Here\'s your Wordle score, you big cheat:', height=150, value=score)
st.caption('Tweet it if you like to lie in public')
twitter_share_button(score)


