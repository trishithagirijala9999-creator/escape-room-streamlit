import streamlit as st
import random

# ----------------------------
# Game Setup
# ----------------------------
MAX_LIVES = 3

if "lives" not in st.session_state:
    st.session_state.lives = MAX_LIVES

if "badges" not in st.session_state:
    st.session_state.badges = set()

if "game_over" not in st.session_state:
    st.session_state.game_over = False


# ----------------------------
# UI Header
# ----------------------------
st.title("🧩 Python Escape RoomV2")
st.write("Solve puzzles, unlock doors, and escape!")

st.write(f"❤️ Lives: {st.session_state.lives}")
st.write(f"🏆 Badges: {list(st.session_state.badges)}")


# ----------------------------
# Helpers
# ----------------------------
def lose_life():
    st.session_state.lives -= 1
    if st.session_state.lives <= 0:
        st.session_state.game_over = True


def add_badge(*badges):
    st.session_state.badges.add(random.choice(badges))


# ----------------------------
# GAME OVER SCREEN
# ----------------------------
if st.session_state.game_over:
    st.error("💀 Game Over! You ran out of lives.")
    if st.button("🔄 Restart Game"):
        st.session_state.lives = MAX_LIVES
        st.session_state.badges = set()
        st.session_state.game_over = False
    st.stop()


# ----------------------------
# Door Selection
# ----------------------------
st.subheader("🚪 Choose a Door")

door = st.selectbox(
    "Select a door",
    ["Select", "Math Door", "Pattern Door", "Lucky Door"]
)


# ----------------------------
# DOOR 1 - MATH
# ----------------------------
if door == "Math Door":
    st.write("🧠 What is 7 * 6 + 8 ?")

    answer = st.number_input("Enter answer", step=1)

    if st.button("Submit Door 1"):
        if answer == 50:
            st.success("Correct! Door unlocked 🔓")
            add_badge("Logic Master", "Math Whiz")
        else:
            st.error("Wrong answer ❌")
            lose_life()


# ----------------------------
# DOOR 2 - PATTERN
# ----------------------------
elif door == "Pattern Door":
    st.write("🔐 Guess the secret word (hint: mystery)")

    guess = st.text_input("Enter word").lower()

    if st.button("Submit Door 2"):
        if guess == "mystery":
            st.success("Correct! Door unlocked 🔓")
            add_badge("Pattern Pro", "Code Breaker")
        else:
            st.error("Wrong answer ❌")
            lose_life()


# ----------------------------
# DOOR 3 - LUCKY
# ----------------------------
elif door == "Lucky Door":
    st.write("🍀 Guess the lucky number (1 to 5)")

    if "lucky" not in st.session_state:
        st.session_state.lucky = random.randint(1, 5)

    guess = st.number_input("Enter number", min_value=1, max_value=5, step=1)

    if st.button("Submit Door 3"):
        if guess == st.session_state.lucky:
            st.success("Lucky hit! Door unlocked 🔓")
            add_badge("Lucky Star", "Risk Taker")
            st.session_state.lucky = random.randint(1, 5)
        else:
            st.error("Wrong guess ❌")
            lose_life()


# ----------------------------
# RESET BUTTON
# ----------------------------
st.divider()

if st.button("🔄 Reset Game Anytime"):
    st.session_state.lives = MAX_LIVES
    st.session_state.badges = set()
    st.session_state.game_over = False
    st.session_state.lucky = random.randint(1, 5)
    st.success("Game reset successfully!")