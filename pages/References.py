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

## The Fast Fourier Transform
- [The Fast Fourier Transform (FFT)](https://medium.com/swlh/the-fast-fourier-transform-fft-5e96cf637c38)
</div>

    """, unsafe_allow_html=True)

