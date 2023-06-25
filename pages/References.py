import streamlit as st
from App import Logos

st.set_page_config(page_title="References", page_icon="📈")

st.markdown("""
<style>

    .css-h5rgaw.e1g8pov61 {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)
Logos()
c = st.container()
with c:
    st.markdown("""

    <div style="text-align: justify;">
        <div style="text-align: center">

---
# References

</div>
<br><br>

## The Wavelet Transform
- [The Wavelet Transform](https://towardsdatascience.com/the-wavelet-transform-e9cfa85d7b34)
</div>

    """, unsafe_allow_html=True)

st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)