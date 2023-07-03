import streamlit as st
from App import Logos

st.set_page_config(page_title="Decision Tree", page_icon="📈")
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
# Decision Tree algorithm

</div>
<br><br>

### Introduction
Decision trees are machine learning models which summarize a set of rules used to split the feature space into small subspaces or regions which are then used for predictions. The structure used to describe decision tree is similar to that of a tree structure but the leaves or leaf nodes of the tree are at the bottom and the root is at the top. The root node is the starting point of a decision tree and it represents the entire feature space with no subdivisions. When we make a decision, we look at the feature space and determine that a certain value of features can be used as a threshold to make a prediction. the tree then splits into two halves based on that threshold and that split makes an internal node into the tree. The two halves either end up in leaf nodes which are the terminal nodes of the tree or bifurcate further through other internal nodes. A single parent node with one internal node is called a stump. A tree is constructed by connecting many stumps together through internal nodes.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*KZ7q0kW-IAbks0eIkDlk-g.png" alt="" width=700 />
</div>
<br>

The top left images shows a non-recurse split which is not traversable through a decision tree, top right image shows a recursive split and the bottom two images are the tree and stratified representation of the same. Image source: Intorduction to statistical learning, 2nd edition.

The decision tree algorithm is a greedy algorithm. When making a split in feature space, it looks for a split that gives the best results in that particular subspace. It does not try to find a global optimal split instead looks for the best choice locally and hopes that a lot of these optimum local choices will result in a good global optimal choice.

Decision tree splitting is recursive in nature. When we make the first split of predictor space into two regions, the next split will be made in one of the two sub regions and so on. In this way, each subspace is made by creating a split in the previous subspace and thus the subspaces recurse into smaller regions until we reach the leaf nodes after which, no further devision results in a better performance.

### How are Decision trees different from other machine learning models
Decision trees divide the feature space into various non-overlapping subspaces and then use those subspaces to make predictions on the data points that fall into those subspaces. The prediction space is divided such that it is possible to travel from one subspace to another recursively. This recursive splitting of feature space is characteristic of decision trees.

The decision boundary represents the value of the parameters which the model finds most helpful in making a clean prediction. As a prediction, it returns the mean value of the partition space in which the query data point falls.

Decision trees are simple to interpret as we only need to look at the decision boundary at each node to determine the approach of the model. However we pay a price to gain this interpretability. The predictive power of the model is reduced because of its simple design.

### The loss of predictive power in decision trees
Decision trees are simple to interpret, but this simplicity comes at a cost. They are not very good at predictions. The reason for this weak predictive power of them is the simple approach they use to learn features of the data.

Decision trees are also not robust to random changes in the data. A small change in the data can result in a completely different tree. These reasons make decision trees a weak performing algorithm.

When we are splitting the training data space, we are increasing the variance of the model as each new split will introduce a new tunable decision boundary, this makes our model prone to overfitting the training data and hence make a bad model with very high variance. We need to seek ways to keep our model’s bias and variance in check as we train the tree by tuning the decision boundary splits.

### Cost functions for regression and classification tasks.
Decision trees can be used for regression tasks in a similar way as other linear regressors. We make predictions for a given observation and then try to minimize the mean squared observations. The prediction in a regression tree is the mean value of the observations in the leaf node that our given sample falls into. The cost function is given below:

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*nsstlH7W75g3FpeaXZNjtg.png" alt="" width=400 />
</div>
<br>

Here $J$ is the total sub-spaces that are formed and $R_j$ represents one of those regions. $y_{R_j}$ is the mean response from a sub region which serves as the prediction for all observation that fall into that region.

The goal is to find splits such that the above error is minimized, but the task is not easy as there can be a lot of different ways to dissect the feature space especially if the number of features is large. Hence we take the greedy approach and try to make the most optimal local choice instead of looking at the global optimum. At each split, we move down the tree and our choice of splits are not influenced by either the past or future splits.

When we use Decision trees for classification tasks, each leaf node represents the unique class that a particular observation can take. If a leaf node has observations with different classes, then it is not a good predictor for any given observation as it can belong to any of those given classes. On the other hand, a leaf node which has observations belonging to a single class is a good predictor because if an observation falls in that leaf node, then it is highly likely that it has the given class. Gini represents the probability that two points from a leaf node belong to the same class. It ranges between 0 and 1, with 1 being the purest node with a single class observations. The formula for gini index is given below:

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*dX4kvQ_4EEG1uJDEl63n_A.png" alt="" width=400 />
</div>
<br>

Here $p(i)$ represent the probatilyt of a given class and C represents that total number of classes. The ginni impurity is given by the following formula:

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*Pw8XLHk-cZKM0b5lz9fitA.png" alt="" width=400 />
</div>
<br>

A value of 1 for ginni gives the value of 0 for ginni impurity. Ginni impurity serves as a measure to test the performance of the decision tree model as an ideal decision tree model must have the lowest amount of ginni impurity in each of its leaf nodes. A similar cost function is entropy of a node.

### Tree pruning
The next criteria to optimize is the length of the tree. Large trees with many internal nodes have high variance and are prone to overfit the data, while smaller trees have little internal nodes have low variance. Our goal is to find the optimal tree length with right amount of bias and variance. One way to achieve is to make a large tree and then work our way backward by eliminating internal nodes withouth making a significant compromize on the model accuracy. This is called tree pruning. So our resultant tree is a sub tree of the original large tree. Tree pruning cost function is described below:

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*YXCHMow44FFPrI9slXQxKQ.png" alt="" width=400 />
</div>
<br>

Here $T$ represents the number of terminal nodes in the tree and alpha is the weight associated with the number of terminal nodes. a value of 0 for alpha gives us the general **`MSE`** error with no cost associated with the length of the tree. As we increase the value of alpha, the amount of cost that we add upon increasing the length of the tree increases and hence the overall cost of the model increases with increase in the size of the tree. This puts a limit on the length of the tree imposed by the minimization of the cost function.

### Conclusion
In this article, we studied the decision tree model and how it is used to make models which are highly interpretable in terms of the feature thresholds that are used to make predictive decisions. We studied the different cost functions associated with the model and optimization techniques to get the lowest test error rate possible.

Decision trees are quite intuitive in their structure and make a good example to stude the inner workings of machine learning models. However they as a stand alone model are not very good predictors and a single decision tree is rarely used as a predictor. A cluster of decision trees is a better model as a whole and is called a random forest as it is a collection of many decision trees.
</div>

    """, unsafe_allow_html=True)

st.markdown("## Use Cases")

col_1, col_2, col_3 = st.columns([1, 1, 1])
with col_1:
    button1 = st.button('Simple Linear Regression')

if button1:
    pass


