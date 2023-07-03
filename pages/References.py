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

## Support Vector Machine (SVM) Algorithm
- [Support Vector Machine — Introduction to Machine Learning Algorithms](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)

## K-Nearest Neighbors (kNN) Algorithm
- [K-Nearest Neighbour: The Distance-Based Machine Learning Algorithm](https://www.analyticsvidhya.com/blog/2021/05/knn-the-distance-based-machine-learning-algorithm/#:~:text=The%20abbreviation%20KNN%20stands%20for,by%20the%20symbol%20'K'.)
- [What is the k-nearest neighbors algorithm?](https://www.ibm.com/topics/knn#:~:text=The%20k%2Dnearest%20neighbors%20algorithm%2C%20also%20known%20as%20KNN%20or,of%20an%20individual%20data%20point.)

## Decision Tree
- [Decision Tree algorithm](https://medium.com/@goelpulkit43/decision-tree-algorithm-8a5c19d98781)

## Random Forest
- [Understanding Random Forest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)

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

