import streamlit as st

from utils.passwordanalyser import analyze_password


# Page configuration
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="wide"
)


# Title
st.title("🔐 Password Strength Analyzer")

st.write(
    "Analyze your password strength and get suggestions "
    "for creating stronger passwords."
)


# Password input
password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Enter password here..."
)


# Analyze button
if st.button("Analyze Password"):

    if not password:
        st.warning("Please enter a password.")

    else:

        result = analyze_password(password)

        st.subheader("Analysis Result")

        # Display strength
        st.metric(
            "Password Strength",
            result["strength"]
        )

        st.write(
            f"**Password Score:** {result['score']} / 4"
        )

        # Password characteristics
        st.subheader("Password Characteristics")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("Length", result["length"])

        with col2:
            st.write(
                "✅ Uppercase"
                if result["uppercase"]
                else "❌ Uppercase"
            )

        with col3:
            st.write(
                "✅ Lowercase"
                if result["lowercase"]
                else "❌ Lowercase"
            )

        with col4:
            st.write(
                "✅ Numbers"
                if result["numbers"]
                else "❌ Numbers"
            )

        with col5:
            st.write(
                "✅ Special"
                if result["special"]
                else "❌ Special"
            )

        # Suggestions
        st.subheader("💡 Suggestions")

        for suggestion in result["feedback"]:
            st.write(f"• {suggestion}")