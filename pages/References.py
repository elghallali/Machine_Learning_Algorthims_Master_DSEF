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

## The Fourier transform
- [Demystifying the Fourier transform](https://aniket-kamat.medium.com/demystifying-the-fourier-transform-a995bdb6d73a)
-[The Intuition Behind The Fourier Series and The Fourier Transform](https://medium.com/math-simplified/the-intuition-behind-the-fourier-series-and-the-fourier-transform-75e7a78d96ef)

## Time Series Analysis
- [Step by Step Time Series Analysis](https://medium.datadriveninvestor.com/step-by-step-time-series-analysis-d2f117554d7e)
- [Identification of seasonality in time series](https://www.sciencedirect.com/science/article/pii/089571779390126J#targetText=Identification%20of%20patterns%20in%20time,identify%20seasonality%20with%20greater%20confidence.)
- [Identifying the numbers of AR or MA terms in an ARIMA model](https://people.duke.edu/~rnau/411arim3.htm)

</div>

    """, unsafe_allow_html=True)

