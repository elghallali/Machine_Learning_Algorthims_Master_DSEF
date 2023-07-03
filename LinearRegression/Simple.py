import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

sns.set()


def SimpleLinearRegression():
    st.markdown("""

    #### 1. Import libraries

    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn import datasets, linear_model
    from sklearn.metrics import mean_squared_error, r2_score
    import seaborn as sns
    sns.set()
    
    ```

    #### 2. Import dataset from scikit-learn

    ```python
    # Load the diabetes dataset
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
    ```

    ```python
    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)
    ```

    ```python

    # The coefficients
    print(\"Coefficients: \", regr.coef_)
    # The mean squared error
    print(\"Mean squared error: %.2f\" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print(\"Coefficient of determination: %.2f\" % r2_score(diabetes_y_test, diabetes_y_pred))

    ```
    Coefficients: [938.23786125] \n
    Mean squared error: 2548.07 \n
    Coefficient of determination: 0.47

    #### 3. Visualisation

    ```python

    # Plot outputs
    fig, ax = plt.subplots()
    ax.scatter(diabetes_X_test, diabetes_y_test, color="black")
    ax.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
    plt.title('Title', size=18)
    plt.xlabel('X', size=15)
    plt.ylabel('Y', size=15)
    plt.xticks(())
    plt.yticks(())
    plt.show()

    ```
    <br>
    """, unsafe_allow_html=True)

    # Load the diabetes dataset
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)

    # The coefficients
    print("Coefficients: \n", regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

    # Plot outputs
    fig, ax = plt.subplots()
    ax.scatter(diabetes_X_test, diabetes_y_test, color="black")
    ax.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)
    plt.title('Title', size=18)
    plt.xlabel('X', size=15)
    plt.ylabel('Y', size=15)
    plt.xticks(())
    plt.yticks(())

    st.pyplot(fig)
