import streamlit as st
import re 
import string



st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stTextInput input {
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 10px;
            width: 100%;
        }
        .strength-box {
            padding: 10px;
            border-radius: 5px;
            color: white;
            text-align: center;
            font-weight: bold;
        }
        .weak { background-color: #e74c3c; }
        .moderate { background-color: #f39c12; }
        .strong { background-color: #2ecc71; }
    </style>
""", unsafe_allow_html=True)




def password_strength(password):
    score = 0
    criteria = {
        "Length": len(password) >= 12,
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digits": any(c.isdigit() for c in password),
        "Special characters":any(c in string.punctuation for c in password),
        "No common patterns":not re.search(r"(1234|password|qwerty|abc|admin)", password, re.IGNORECASE),
    }

    score = sum(criteria.values())


    strength_levels = ["very weak", "weak", "moderate", "strong", "very strong", "extremely strong"]
    strength = strength_levels[score] if score < len(strength_levels) else "Excellent"

    return strength,criteria


st.title("🔒Password Strength Checker")
st.write("This app checks the strength of your password based on the following criteria:")

password = st.text_input("Enter your password", type="password")

if password:
    strength , criteria = password_strength(password)

    strength_class = "weak" if strength in ["very weak", "weak"] else "moderate" if strength == "moderate" else "strong"

    st.markdown(f'<div class="strength-box {strength_class}">{strength}</div>', unsafe_allow_html=True)

    st.write("Criteria:")
    for criterion, satisfied in criteria.items():
        st.write(f"- {criterion}: {'✅' if satisfied else '❌'}")

    if strength in ["very weak", "weak"]:
        st.write("Please consider using a stronger password.")

    elif strength == ["moderate", "strong"]:
        st.write("Good job! Your password is strong enough.")

    elif strength == ["very strong", "extremely strong"]:
        st.write("Excellent! Your password is very strong.")

    else:
        st.write("Please consider using a stronger password.")