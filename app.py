import streamlit as st
from my_pages.first_page import the_first_page


def entry_point():
    st.title("My main entry point :D")

    "This is a string written with :violet[***magic***]"


def my_book():
    nav = st.navigation(
        [
            st.Page(entry_point, title="Entry", default=True),  # Magic works
            st.Page(the_first_page, title="First"),  # Magic does not work
            st.Page("my_pages/second_page.py", title="Second"),  # Magic works
            st.Page("my_pages/third_page.py", title="Third"),  # Magic works
        ]
    )

    nav.run()


if __name__ == "__main__":
    my_book()
