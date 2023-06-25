import streamlit as st

# from LinearRegression.linear_regression_explication import linear_regression

st.set_page_config(
    page_title="Machine Learning Algorithms | Home",
    page_icon=":computer:",

)

st.markdown("""
<style>

    .css-h5rgaw.e1g8pov61 {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


def Logos():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image('https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/fsjest.jpg',
                 width=100)

    with col2:
        st.image('https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/logo.png', width=300)

    with col3:
        st.image('https://raw.githubusercontent.com/elghallali/my-images/master/Faculty%20Official/uae.png', width=150)


Logos()
st.markdown("""
    ---
    """)
st.markdown(
    """
    <div style="text-align: justify;">
    
    <div align="center">
    
    # Machine Learning Project
    
    <br><br>
    </div>
    
    ## Abstract
    ---
    
    </div>
""", unsafe_allow_html=True
)
