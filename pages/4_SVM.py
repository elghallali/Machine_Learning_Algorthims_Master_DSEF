import streamlit as st
from App import Logos

st.set_page_config(page_title="Support Vector Machine (SVM)", page_icon="📈")

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
# Support Vector Machine (SVM)

</div>
<br><br>

## Introduction
I guess by now you would’ve accustomed yourself with linear regression and logistic regression algorithms. If not, I suggest you have a look at them 
before moving on to support vector machine. Support vector machine is another simple algorithm that every machine learning expert should have in 
his/her arsenal. Support vector machine is highly preferred by many as it produces significant accuracy with less computation power. Support Vector 
Machine, abbreviated as SVM can be used for both regression and classification tasks. But, it is widely used in classification objectives.

__What is Support Vector Machine?__

The objective of the support vector machine algorithm is to find a hyperplane in an N-dimensional space(N — the number of features) that distinctly 
classifies the data points.

<br>
<div align='center'>
<figure>
<img src="https://miro.medium.com/v2/resize:fit:600/format:webp/0*9jEWNXTAao7phK-5.png" alt="" width=300 />
<img src="https://miro.medium.com/v2/resize:fit:600/format:webp/0*0o8xIA4k3gXUDCFU.png" alt="" width=300 />
<figcaption>Possible hyperplanes</figcaption>
</figure>
</div>
<br>

To separate the two classes of data points, there are many possible hyperplanes that could be chosen. Our objective is to find a plane that has the 
maximum margin, i.e the maximum distance between data points of both classes. Maximizing the margin distance provides some reinforcement so that future 
data points can be classified with more confidence.

## Hyperplanes and Support Vectors

<br>
<div align='center'>
<figure>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ZpkLQf2FNfzfH4HXeMw4MQ.png" alt="" width=700 />
<figcaption>Hyperplanes in 2D and 3D feature space</figcaption>
</figure>
</div>
<br>

Hyperplanes are decision boundaries that help classify the data points. Data points falling on either side of the hyperplane can be attributed to 
different classes. Also, the dimension of the hyperplane depends upon the number of features. If the number of input features is 2, then the hyperplane 
is just a line. If the number of input features is 3, then the hyperplane becomes a two-dimensional plane. It becomes difficult to imagine when the 
number of features exceeds 3.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/0*ecA4Ls8kBYSM5nza.jpg" alt="" width=700 />
</div>
<br>

Support vectors are data points that are closer to the hyperplane and influence the position and orientation of the hyperplane. Using these support 
vectors, we maximize the margin of the classifier. Deleting the support vectors will change the position of the hyperplane. These are the points that 
help us build our SVM.

### Large Margin Intuition
In logistic regression, we take the output of the linear function and squash the value within the range of [0,1] using the sigmoid function. If the 
squashed value is greater than a threshold value(0.5) we assign it a label 1, else we assign it a label 0. In SVM, we take the output of the linear 
function and if that output is greater than 1, we identify it with one class and if the output is -1, we identify is with another class. Since the 
threshold values are changed to 1 and -1 in SVM, we obtain this reinforcement range of values([-1,1]) which acts as margin.

### Cost Function and Gradient Updates
In the SVM algorithm, we are looking to maximize the margin between the data points and the hyperplane. The loss function that helps maximize the 
margin is hinge loss.

<br>
<div align='center'>
<figure>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*3xErahGeTFnbDiRuNXjAuA.png" alt="" width=350 />
<img src="https://miro.medium.com/v2/resize:fit:1116/format:webp/1*hHlytjVk6d7O2WWvG2Gdig.png" alt="" width=300 />
<figcaption>Hinge loss function (function on left can be represented as a function on the right)</figcaption>
</figure>
</div>
<br>

The cost is 0 if the predicted value and the actual value are of the same sign. If they are not, we then calculate the loss value. We also add a 
regularization parameter the cost function. The objective of the regularization parameter is to balance the margin maximization and loss. After 
adding the regularization parameter, the cost functions looks as below.

<br>
<div align='center'>
<figure>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*GQAd28bK8LKOL2kOOFY-tg.png" alt="" width=350 />
<figcaption>Loss function for SVM</figcaption>
</figure>
</div>
<br>

Now that we have the loss function, we take partial derivatives with respect to the weights to find the gradients. Using the gradients, we can 
update our weights.

<br>
<div align='center'>
<figure>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*WUphtYLfTOAoaXQXvImBeA.png" alt="" width=500 />
<figcaption>Gradients</figcaption>
</figure>
</div>
<br>

When there is no misclassification, i.e our model correctly predicts the class of our data point, we only have to update the gradient from the 
regularization parameter.

<br>
<div align='center'>
<figure>
<img src="https://miro.medium.com/v2/resize:fit:616/format:webp/1*-nKEXrWos8Iuf-DWSv_srQ.png" alt="" width=250 />
<figcaption>Gradient Update — No misclassification</figcaption>
</figure>
</div>
<br>

When there is a misclassification, i.e our model make a mistake on the prediction of the class of our data point, we include the loss along with the 
regularization parameter to perform gradient update.

<br>
<div align='center'>
<figure>
  <img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*tnvMhAKaTUCO43diEvtTAQ.png" alt="" width=300 />
  <figcaption>Gradient Update — Misclassification</figcaption>
</figure>
</div>
<br>

</div>

    """, unsafe_allow_html=True)


