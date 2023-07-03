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
# K-Nearest Neighbors (kNN) Algorithm
</div>
<br><br>

## Introduction
The abbreviation `KNN` stands for “__K-Nearest Neighbour__”. It is a supervised machine learning algorithm. The algorithm can be used to solve both 
classification and regression problem statements.

The number of nearest neighbours to a new unknown variable that has to be predicted or classified is denoted by the symbol ‘K’.

Let’s take a good look at a related real-world scenario before we get started with this awesome algorithm.

We are often notified that you share many characteristics with your nearest peers, whether it be your thinking process, working etiquettes, 
philosophies, or other factors. As a result, we build friendships with people we deem similar to us.

The KNN algorithm employs the same principle. Its aim is to locate all of the closest neighbours around a new unknown data point in order to figure 
out what class it belongs to. It’s a distance-based approach.

Consider the diagram below; it is straightforward and easy for humans to identify it as a “Cat” based on its closest allies. This operation, however, 
cannot be performed directly by the algorithm.

KNN calculates the distance from all points in the proximity of the unknown data and filters out the ones with the shortest distances to it. As a 
result, it’s often referred to as a distance-based algorithm.

In order to correctly classify the results, we must first determine the value of K (Number of Nearest Neighbours).

In the following diagram, the value of K is 5. Since there are four cats and just one dog in the proximity of the five closest neighbours, the 
algorithm would predict that it is a cat based on the proximity of the five closest neighbors in the red circle’s boundaries.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/31099Screenshot%202021-05-13%20at%208.58.28%20PM.png" alt="" width=400 />
</div>
<br>

Here, ‘K’ is the hyperparameter for KNN. For proper classification/prediction, the value of K must be fine-tuned.

##### But, How do we select the right value of K?
We don’t have a particular method for determining the correct value of K. Here, we’ll try to test the model’s accuracy for different K values. The 
value of K that delivers the best accuracy for both training and testing data is selected.

##### Note!! __`It is recommended to always select an odd value of K`__
When the value of K is set to even, a situation may arise in which the elements from both groups are equal. In the diagram below, elements from both 
groups are equal in the internal “Red” circle (k == 4).

In this condition, the model would be unable to do the correct classification for you. Here the model will randomly assign any of the two classes to 
this new unknown data.

Choosing an odd value for K is preferred because such a state of equality between the two classes would never occur here. Due to the fact that one of 
the two groups would still be in the majority, the value of K is selected as odd.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/369941_-pMkFM7U6GX22WUCLG5g2g.png" alt="" width=500 />
</div>
<br>

The impact of selecting a smaller or larger K value on the model:

- Larger K value: The case of underfitting occurs when the value of k is increased. In this case, the model would be unable to correctly learn on the 
training data.
- Smaller k value: The condition of overfitting occurs when the value of k is smaller. The model will capture all of the training data, including 
noise. The model will perform poorly for the test data in this scenario.

## How does KNN work for ‘Classification’ and ‘Regression’ problem statements?
### Classification:
When the problem statement is of ‘classification’ type, KNN tends to use the concept of “Majority Voting”. Within the given range of K values, 
the class with the most votes is chosen.

Consider the following diagram, in which a circle is drawn within the radius of the five closest neighbours. Four of the five neighbours in this 
neighbourhood voted for ‘RED,’ while one voted for ‘WHITE.’ It will be classified as a ‘RED’ wine based on the majority votes.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/525011_prEBTwv8V8BZiV-UbvXibQ.png" alt="" width=500 />
</div>
<br>

### Regression:
KNN employs a mean/average method for predicting the value of new data. Based on the value of K, it would consider all of the nearest neighbours.

The algorithm attempts to calculate the mean for all the nearest neighbours’ values until it has identified all the nearest neighbours within a 
certain range of the K value.

Consider the diagram below, where the value of k is set to 3. It will now calculate the mean (52) based on the values of these neighbours 
(50, 55, and 51) and allocate this value to the unknown data.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/89953Screenshot%202021-05-13%20at%206.53.40%20AM.png" alt="" width=500 />
</div>
<br>

## Impact of Imbalanced dataset and Outliers on KNN
### Imbalanced dataset:
When dealing with an imbalanced data set, the model will become biased. Consider the example shown in the diagram below, where the “Yes” class is 
more prominent.

As a consequence, the bulk of the closest neighbours to this new point will be from the dominant class. Because of this, we must balance our data 
set using either an “Upscaling” or “Downscaling” strategy.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/998941_RHLewL2xh2ZEfZdA7_wBkg.png" alt="" width=500 />
</div>
<br>

### Outliers:
__Outliers are the points that differ significantly from the rest of the data points__.

The outliers will impact the classification/prediction of the model. The appropriate class for the new data point, according to the following 
diagram, should be “Category B” in green.

The model, however, would be unable to have the appropriate classification due to the existence of outliers. As a result, removing outliers before 
using KNN is recommended.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/202961_56MmutHmr4WzDJrufP8kug.png" alt="" width=500 />
</div>
<br>

## Importance of scaling down the numeric variables to the same level
Data has 2 parts: 
> 1. Magnitude
> 1. Unit

For instance; if we say 20 years then “20” is the magnitude here and “years” is its unit.
Since it is a distance-dependent algorithm, KNN selects the neighbours in the closest vicinity based solely on the magnitude of the data.  Have a 
look at the diagram below; the data is not scaled, so it can not find the closest neighbours correctly.  As a consequence, the outcome will be 
influenced.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/95189OCUmI.png" alt="" width=500 />
</div>
<br>

The data values in the previous figure have now been scaled down to the same level in the following example. Based on 
the scaled distance, all of the closest neighbours would be accurately identified.

<br>
<div align='center'>
<img src="https://editor.analyticsvidhya.com/uploads/22708Screenshot%202021-05-14%20at%207.16.28%20PM.png" alt="" width=500 />
</div>
<br>

## Compute KNN: distance metrics
To recap, the goal of the k-nearest neighbor algorithm is to identify the nearest neighbors of a given query point, so that we can assign a class 
label to that point. In order to do this, KNN has a few requirements:

### Determine your distance metrics

In order to determine which data points are closest to a given query point, the distance between the query point and the other data points will 
need to be calculated. These distance metrics help to form decision boundaries, which partitions query points into different regions. You commonly 
will see decision boundaries visualized with Voronoi diagrams.

While there are several distance measures that you can choose from, this article will only cover the following:

__Euclidean distance (p=2)__: This is the most commonly used distance measure, and it is limited to real-valued vectors. Using the below formula, it 
measures a straight line between the query point and the other point being measured.

<br>
<div align='center'>
<img src="https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/cdp/cf/ul/g/3c/fb/EuclideanDistance.component.complex-narrative-l.ts=1653407891085.png/content/adobe-cms/us/en/topics/knn/jcr:content/root/table_of_contents/body/complex_narrative/items/content_group_610921119/image" alt="" width=500 />
</div>
<br>

__Manhattan distance (p=1)__: This is also another popular distance metric, which measures the absolute value between two points. It is also referred to 
as taxicab distance or city block distance as it is commonly visualized with a grid, illustrating how one might navigate from one address to another 
via city streets.

<br>
<div align='center'>
<img src="https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/cdp/cf/ul/g/26/80/ManhattanDistance.component.complex-narrative-l.ts=1653407891178.png/content/adobe-cms/us/en/topics/knn/jcr:content/root/table_of_contents/body/complex_narrative/items/content_group_443822816/image" alt="" width=500 />
</div>
<br>

__Minkowski distance__: This distance measure is the generalized form of Euclidean and Manhattan distance metrics. The parameter, p, in the formula 
below, allows for the creation of other distance metrics. Euclidean distance is represented by this formula when p is equal to two, and Manhattan 
distance is denoted with p equal to one.

<br>
<div align='center'>
<img src="https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/cdp/cf/ul/g/9e/a8/MinkowskiDistance.component.complex-narrative-l.ts=1653407891320.png/content/adobe-cms/us/en/topics/knn/jcr:content/root/table_of_contents/body/complex_narrative/items/content_group_1376261523/image" alt="" width=500 />
</div>
<br>

__Hamming distance__: This technique is used typically used with Boolean or string vectors, identifying the points where the vectors do not match. 
As a result, it has also been referred to as the overlap metric. This can be represented with the following formula:

<br>
<div align='center'>
<img src="https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/cdp/cf/ul/g/43/3a/HammingDistance.component.complex-narrative-l.ts=1653407891468.png/content/adobe-cms/us/en/topics/knn/jcr:content/root/table_of_contents/body/complex_narrative/items/content_group/image" alt="" width=500 />
</div>
<br>

</div>

    """, unsafe_allow_html=True)

st.markdown("## Examples")

col_1, col_2, col_3 = st.columns([1, 1, 1])
with col_1:
    button1 = st.button('kNN example 1')

with col_2:
    button2 = st.button('kNN example 2')

with col_3:
    button3 = st.button('kNN example 3')

if button1:
    pass
