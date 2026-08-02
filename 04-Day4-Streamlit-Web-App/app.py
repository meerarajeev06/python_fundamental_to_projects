import streamlit as st
import requests

# 1. Page Title & Subtitle
st.title("🌐 GitHub Profile Inspector")
st.write("Enter any GitHub username below to inspect live profile data!")

# 2. Web Input Widget
username = st.text_input("GitHub Username", value="octocat")

# 3. Interactive Button
if st.button("Fetch Profile Data"):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Layout columns in Streamlit
        col1, col2 = st.columns(2)

        with col1:
            st.image(data.get("avatar_url"), width=150)
            st.subheader(data.get("name", "N/A"))
            st.caption(f"@{data.get('login')}")

        with col2:
            st.metric(label="Public Repos", value=data.get("public_repos", 0))
            st.metric(label="Followers", value=data.get("followers", 0))

        st.success(f"Bio: {data.get('bio', 'No bio provided.')}")
    else:
        st.error(f"User '{username}' not found on GitHub!")