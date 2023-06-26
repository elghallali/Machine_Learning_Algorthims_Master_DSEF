import streamlit as st
from App import Logos

st.set_page_config(page_title="k-Nearest Neighbors (kNN)", page_icon="📈")
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
# k-Nearest Neighbors (kNN)
</div>
<br><br>

## 1. KNN Theory
### 1.1 Type of algorithm

KNN can be used for both classification and regression predictive problems. KNN falls in the supervised learning 
family of algorithms. Informally, this means that we are given a labelled dataset consiting of training observations 
$(x,y)$ and would like to capture the relationship between  $x$ and  $y$ . More formally, our goal is to learn a 
function $h:X→Y$ so that given an unseen observation $x$ , $h(x)$ can confidently predict the corresponding output $y$.

### 1.2 Distance measure

In the classification setting, the K-nearest neighbor algorithm essentially boils down to 
forming a majority vote between the K most similar instances to a given “unseen” observation. Similarity is defined 
according to a distance metric between two data points. The k-nearest-neighbor classifier is commonly based on the 
Euclidean distance between a test sample and the specified training samples. Let  $x_i$ be an input sample with  $p$ 
features  $(x_{i1},x_{i2},...,x_{ip})$, $n$ be the total number of input samples $(i=1,2,...,n)$. The Euclidean distance 
between sample  $x_i$ and  $x_l$ is is defined as:

<div align="center">
<br>

$$d(x_i,x_l)=\\sqrt{(x_{i1}−x_{l1})^2+(x_{i2}−x_{l2})^2+...+(x_{ip}−x_{lp})^2}$$

<br>
</div>
Sometimes other measures can be more suitable for a given setting and include the Manhattan, Chebyshev and Hamming 
distance.

### 1.3 Algorithm steps
- STEP 1: Cgoose the number K of neighbors

- STEP 2: Take the K nearest neighbors of the new data point, according to your distance metric

- STEP 3: Among these K neighbors, count the number of data points to each category

- STEP 4: Assign the new data point to the category where you counted the most neighbors

## 2. Importing and preperation of data
</div>

    """, unsafe_allow_html=True)
