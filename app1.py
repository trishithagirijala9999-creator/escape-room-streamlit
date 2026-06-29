import streamlit as st
import random

# ----------------------------
# PAGE CONFIG (PRO UI)
# ----------------------------
st.set_page_config(
    page_title="Escape Room Game",
    page_icon="🧩",
    layout="wide"
)

# ----------------------------
# SESSION STATE
# ----------------------------
MAX_LIVES = 3

if "level" not in st.session_state:
    st.session_state.level = 1

if "lives" not in st.session_state:
    st.session_state.lives = MAX_LIVES

if "badges" not in st.session_state:
    st.session_state.badges = set()

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "lucky" not in st.session_state:
    st.session_state.lucky = random.randint(1, 5)

# ----------------------------
# FUNCTIONS
# ----------------------------
def lose_life():
    st.session_state.lives -= 1
    if st.session_state.lives <= 0:
        st.session_state.game_over = True


def add_badge():
    rewards = ["Logic Master", "Code Breaker", "Lucky Star", "Escape Pro"]
    st.session_state.badges.add(random.choice(rewards))


def next_level():
    st.session_state.level += 1


# ----------------------------
# SIDEBAR (GAME MENU)
# ----------------------------
with st.sidebar:
    st.title("🎮 Game Panel")

    st.markdown("### 📊 Status")
    st.write(f"📍 Level: {st.session_state.level}")
    st.write(f"❤️ Lives: {st.session_state.lives}")
    st.write(f"🏆 Badges: {len(st.session_state.badges)}")

    progress = st.session_state.level / 4
    st.progress(min(progress, 1.0))

    st.markdown("---")
    if st.button("🔄 Reset Game"):
        st.session_state.level = 1
        st.session_state.lives = MAX_LIVES
        st.session_state.badges = set()
        st.session_state.game_over = False
        st.session_state.lucky = random.randint(1, 5)
        st.rerun()

# ----------------------------
# HEADER (HERO STYLE)
# ----------------------------
st.title("🧩 PYTHON ESCAPE ROOM")
st.caption("A logic-based story adventure game")

st.markdown("You are trapped inside a digital escape system. Solve all levels to escape!")

st.divider()

# ----------------------------
# GAME OVER SCREEN
# ----------------------------
if st.session_state.game_over:
    st.error("💀 GAME OVER — You are trapped forever!")
    st.button("🔄 Restart Game", on_click=lambda: st.session_state.update({
        "level": 1,
        "lives": MAX_LIVES,
        "badges": set(),
        "game_over": False,
        "lucky": random.randint(1, 5)
    }))
    st.stop()

# ----------------------------
# LEVEL UI FUNCTION STYLE
# ----------------------------
def game_card(title, content, key):
    with st.container():
        st.markdown(f"### 🚪 {title}")
        st.info(content)
        return key()


# ----------------------------
# LEVEL 1
# ----------------------------
if st.session_state.level == 1:

    st.subheader("Level 1 — The Math Gate")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("🧠 Solve the ancient equation to unlock the gate")

        answer = st.number_input("What is 7 × 6 + 8 ?", step=1)

        if st.button("🔓 Submit Answer"):
            if answer == 50:
                st.success("Door unlocked! You move forward.")
                add_badge()
                next_level()
                st.rerun()
            else:
                st.error("Wrong answer!")
                lose_life()

    with col2:
        st.markdown("📜 Hint Board")
        st.info("Multiply first, then add")

# ----------------------------
# LEVEL 2
# ----------------------------
elif st.session_state.level == 2:

    st.subheader("Level 2 — The Whispering Code")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("🔐 A hidden word controls the door")

        guess = st.text_input("Enter secret word").lower()

        if st.button("🔓 Submit Word"):
            if guess == "mystery":
                st.success("Correct! Door unlocked.")
                add_badge()
                next_level()
                st.rerun()
            else:
                st.error("Wrong word!")
                lose_life()

    with col2:
        st.info("💡 Hint: It is something unknown")

# ----------------------------
# LEVEL 3
# ----------------------------
elif st.session_state.level == 3:

    st.subheader("Level 3 — The Lucky Chamber")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("🍀 Choose wisely... only luck can save you")

        guess = st.number_input("Pick number (1–5)", min_value=1, max_value=5)

        if st.button("🎯 Try Luck"):
            if guess == st.session_state.lucky:
                st.success("YOU ESCAPED THE ROOM! 🎉")
                add_badge()
                st.session_state.level = 4
                st.rerun()
            else:
                st.error("Unlucky!")
                lose_life()

    with col2:
        st.warning("⚠️ No hints available")

# ----------------------------
# WIN SCREEN
# ----------------------------
elif st.session_state.level == 4:
    st.balloons()

    st.success("🏆 YOU ESCAPED SUCCESSFULLY!")
    st.markdown("### 🎖️ Final Stats")
    st.write(f"Badges earned: {len(st.session_state.badges)}")

    st.button("🔄 Play Again", on_click=lambda: st.session_state.update({
        "level": 1,
        "lives": MAX_LIVES,
        "badges": set(),
        "game_over": False,
        "lucky": random.randint(1, 5)
    }))