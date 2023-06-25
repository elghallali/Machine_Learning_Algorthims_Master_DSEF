import streamlit as st

from App import Logos

st.set_page_config(page_title="Machine Learning", page_icon="📈")

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
    <div style="text-align: center">
    
---
# Machine Learning
</div>
    <br><br>
    <div style="text-align: justify;">

## 1. What Is Machine Learning ?    

Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data 
and algorithms to imitate the way that humans learn, gradually improving its accuracy.

Over the last couple of decades, the technological advances in storage and processing power have enabled some 
innovative products based on machine learning, such as Netflix’s recommendation engine and self-driving cars.

Machine learning is an important component of the growing field of data science. Through the use of statistical 
methods, algorithms are trained to make classifications or predictions, and to uncover key insights in data mining 
projects. These insights subsequently drive decision making within applications and businesses, ideally impacting key 
growth metrics. As big data continues to expand and grow, the market demand for data scientists will increase. They 
will be required to help identify the most relevant business questions and the data to answer them.

Machine learning algorithms are typically created using frameworks that accelerate solution development, 
such as TensorFlow and PyTorch.

## 2. Types of Machine Learning

<br>
<div align='center'>
<img src="https://static.javatpoint.com/tutorial/machine-learning/images/machine-learning-algorithms.png" alt="" width=600 />
</div>
<br>


### 2.1. Supervised learning

Supervised learning is a type of Machine learning in which the machine needs external supervision to learn. The 
supervised learning models are trained using the labeled dataset. Once the training and processing are done, 
the model is tested by providing a sample test data to check whether it predicts the correct output.

The goal of supervised learning is to map input data with the output data. Supervised learning is based on 
supervision, and it is the same as when a student learns things in the teacher's supervision. The example of 
supervised learning is **spam filtering**.

Supervised learning can be divided further into two categories of problem:

- **Classification**
- **Regression**

### 2.2. Unsupervised learning

It is a type of machine learning in which the machine does not need any external supervision to learn from the data, 
hence called unsupervised learning. The unsupervised models can be trained using the unlabelled dataset that is not 
classified, nor categorized, and the algorithm needs to act on that data without any supervision. In unsupervised 
learning, the model doesn't have a predefined output, and it tries to find useful insights from the huge amount of 
data. These are used to solve the Association and Clustering problems. **Hence further, it can be classified into two 
types**:

- **Clustering**
- **Association**

### 2.3. Reinforcement learning

In Reinforcement learning, an agent interacts with its environment by producing actions, and learn with the help of 
feedback. The feedback is given to the agent in the form of rewards, such as for each good action, he gets a positive 
reward, and for each bad action, he gets a negative reward. There is no supervision provided to the agent. **Q-Learning 
algorithm** is used in reinforcement learning.

### List of Popular Machine Learning Algorithm
1. Linear Regression Algorithm
1. Logistic Regression Algorithm
1. Decision Tree
1. SVM
1. Naïve Bayes
1. KNN
1. K-Means Clustering
1. Random Forest
1. Apriori
1. PCA


</div>

    """, unsafe_allow_html=True)



