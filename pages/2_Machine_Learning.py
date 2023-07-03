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

You are learning python using manuals and online tutorials by following the code examples. Supervised learning is where you learn python by 
understanding its features by practicing the examples that act as labeled data and then using the knowledge acquired to write python programs for 
unseen use cases.

- __Input and output data is provided to a Supervised machine model, so supervised learning is learning by example__.

Supervised learning uses a labeled dataset, typically labeled by an external supervisor, subject matter expert(SME), or an algorithm/program. The 
dataset is split into training and test dataset for training and then validating the model. The supervised learned model is then used to generate 
predictions on previously unseen unlabeled data that belongs to the category of data the model was trained on.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*h_-5jMKtz_MYf4de5eCpZA.png" alt="" width=700 />
</div>
<br>

##### Examples of Supervised Learning are Classification and Regression. 
Classification is used in applications like Image Classification and K- Nearest Neighbors for identifying customer churn. Regression algorithms are 
used to predict sales, home prices, etc.

### 2.2. Unsupervised learning

A child playing with toys can arrange them by identifying patterns based on colors, shapes, sizes, or just based on their interests. The kid discovers 
new ways to cluster the toys without needing external supervision is similar to unsupervised learning.

- Unsupervised learning identifies hidden patterns and relationships in an unlabeled dataset by grouping data into clusters or by association

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*NaT5cMuNxfjRbcaBHOLqEQ.png" alt="" width=700 />
</div>
<br>

__Unsupervised learning is learning by reasoning__ to identify hidden patterns in an unlabeled dataset. They have no supervision like the Supervised algorithms and are hence Unsupervised.

##### Types of unsupervised algorithms
- __Clustering__ identifies hidden data patterns in an uncategorized/unlabeled dataset based on the similarities or differences in the dataset as in 
__market segmentation__.

- __Association__ rules allow you to establish associations amongst data objects inside large datasets by identifying relationships between variables 
in a given dataset, as in __market basket analysis and recommendation engines__.

- __Anomaly detection__ is an unsupervised algorithm to identify anomalous data in a dataset. __It is used for fault diagnosis, network security intrusion, 
and fraud detection__.

- The __dimensionality reduction technique__ reduces the number of features in a high-dimensional dataset to a low dimension while preserving the data 
integrity as in __Principal Component Analysis(PCA)__

### 2.3. Reinforcement learning

A chef explores different ingredients by exploring and experimenting with different recipes in the hope of creating that perfect recipe that wows 
everyone. This is similar to Reinforcement Learning, where the chef tries a variety of actions like trying different ingredients in different 
proportions to progressively favors those that appear to taste the best.

- In Reinforcement learning an agent interacts with the environment by sensing its state and learns to take actions in order to maximize long-term 
reward. As the agent takes actions it needs to maintain a balance between exploration and exploitation by performing a variety of actions using trial 
and error to favor the actions that yield the maximum reward in the future.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*A4R2aBt6sZht_OngBNhzpw.png" alt="" width=700 />
</div>
<br>

__The goal of RL is for the agent to learn to make sequential decisions in an uncertain environment by mapping the different environment states to 
actions to maximize long-term rewards__.

The two main characteristics of RL __are trial and error search and delayed rewards__ like delayed gratification.

Reinforcement learning is applied in Robotics, Self-driving cars, evaluating trading strategies and adaptive controls.

### 2.4. Difference between Supervised, Unsupervised, and Reinforcement Learning
#### Dataset
__Supervised learning requires a labeled dataset__ for training. __Unsupervised learning identifies hidden data patterns from an unlabeled dataset__, 
while __Reinforcement learning does not require data__ as it learns by interacting with the environment.

#### Learnings
__Supervised learning is instructional-based__ and needs supervision as it learns by following examples from the labeled dataset. __Unsupervised 
learning learns by reasoning__ and does not need supervision as it tries to identify hidden patterns to extract insights from the unlabeled dataset. 
__Reinforcement learning learns by experience__ as it explores and exploits different actions to maximize long-term rewards.

#### Objective
__Supervised algorithms learn only one type of task__ based on the labeled dataset. The goal is to predict outcomes for new data belonging to the same 
domain as the same model need not be applied to a different domain. In contrast, the __unsupervised algorithm's objective is to gain insights from the 
unlabeled data__ that can predict if the new data is part of the cluster or an anomaly. __Reinforcement learning is goal-oriented, and the agent aims to 
learn sequences of actions by exploration and exploitation in an uncertain environment to maximize future rewards__. Reinforcement learning can handle 
an entirely new scenario it has never encountered.

#### Training
__Training of a Supervised algorithm is offline__, whereas __training of Unsupervised and Reinforcement learning is online__ and happens in real-time.

#### Algorithms Types and Applications
- Supervised learning consists of Classification and Regression. Classification algorithms are applied to detect fraud, spam detection, and classify 
images, and Regression algorithms help predict sales, house prices, etc.

- Unsupervised learning consists of Clustering, Association, Anomaly detection, and dimensionality reduction. Unsupervised learning applications are 
customer segmentation, market basket analysis, fraud detection, network security analysis, etc.

- Reinforcement learning algorithms are either Value-based, Policy-based, or Model-based. Deep Q-Network(DQN), state-Action-Reward-State-Action(SARSA), 
Asynchronous Advantage Actor-Critic Algorithm(A3C), and Deep Deterministic Policy Gradient(DDPG) are a few Reinforcement algorithms used in Robotics, 
developing business strategies.

### 2.5. Additional ML algorithms

##### Semi-Supervised Learning
Semi-Supervised learning __combines supervised and unsupervised learning__ by training on a small number of labeled data and a large unlabeled dataset 
to capture the shape of the underlying data distribution and generalize better to new samples. This technique automates the data-labeling process with 
only a small labeled dataset.

##### Evolutionary algorithms
__Evolutionary algorithms are inspired by nature to solve problems through processes that emulate living organisms' biological evolutional behaviors__. 
The genetic algorithm is inspired by CharlesDarwin'ss theory of natural evolution. Simulated annealing is based on physical annealing to minimize the 
system's energy. Examples of EA are Genetic algorithms, Swarm Intelligence, and Ant Colony Optimization.

</div>

    """, unsafe_allow_html=True)



