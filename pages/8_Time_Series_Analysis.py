import streamlit as st
from App import Logos

st.set_page_config(page_title="Time Series", page_icon="📈")
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
# Time Series Analysis

</div>
<br><br>

## What is Time Series?

Time series is a collection of sequence of values with equally spaced time intervals. We can analyze the time series 
data to identify the underlying pattern to make the predictions.

#### Time series data is different in terms of

- Time-based dependency. Observations are not independent of each other but current observation will be dependent on 
previous observations. Today’s temperature cannot be predicted independently but is dependent on yesterday’s weather 
conditions.

- Trends that can be increasing and decreasing with time along with seasonality trends. Sale of rain jackets 
increases or decrease year on year depending on how much it rains that year and also have seasonality attached.

#### The goal of Time Series analysis is

- Identify the underlying forces that lead to a particular trend in time series pattern
- Predict future values of the time series variable

This will help to identify the patterns from the observed time-series data.

##### Identifying patterns in time series data
Time series analysis assumes that time-series data consists of some systematic pattern and some random noise.

If we remove the random noise then the systematic pattern would be more prominent. This can be done using Time Series 
Decomposition.

A systematic pattern in time series data can have a Trend or a Seasonality.

The trend in Time Series data can be linear or non-linear that changes over time and does not repeat itself within 
the known time range. There is repetition in data over systematic intervals of time.

Demand for a stationary product would steadily increase over time along with seasonality attached to the demand. 
Demand for stationary is very high during the back-to-school month.

##### Time Series decomposition:

The decomposition of time series is a statistical task that deconstructs a time series into several components. Each 
component represents one of the underlying categories of patterns.

##### Types of time series patterns:

1. **Trend(T)**: reflects the long-term progression of the series. A trend exists when there is a persistent 
increasing or decreasing direction in the data. The trend component does not have to be linear.

1. **Cyclic (C)**: reflects repeated but non-periodic fluctuations. The duration of these fluctuations is usually of at 
least two years.

1. **Seasonal(S)**: reflects seasonality present in the Time Series data, like demand for flip flops, will be highest 
during the summer season. Seasonality occurs at a fixed period of time could be weekly, monthly, quarterly, etc.

1. **Random(R)**: reflects random or irregular influences. This is residual after we have removed all other components 
from time-series data.

##### Time Series decomposition can be additive or multiplicative:

**Additive Model**: 

<div align='center'>

$$Y= T + S + C + R$$

</div>

Additive decomposition should be used when:

- The magnitude of seasonal variation around the trend cycle does not vary with the level of time series.

**Multiplicative Model**:

<div align='center'>

$$Y= T \\times S \\times C \\times R$$

</div>

Multiplicative decomposition should be used when:

- variation in trend is proportional to the level of time series.

<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*86no69_ORB-YSkkAd4MydA.png" alt="" width=600 />
</div>
<br>

### How do we forecast a time series?

Most of the time series data will be non-stationary but a common assumption in many time series technique is that the 
data is stationary. Time Series data will have some pattern or behavior over a period of time. If we understand the 
underlying pattern then we can say with a high probability that the time series will follow the same pattern in the 
future too

### Property of stationary data is that it has:

- constant mean.
- constant variance.
- autocorrelation does not change over time.

### What is stationary data? 

A stationary series is one whose statistical properties like mean, variance and 
auto-correlation is constant and does not depend on time. A data set that does not exhibit trend or seasonality and 
fluctuations in data is entirely external.

Stationary data is flat looking series, without trend, constant variance over time, a constant autocorrelation 
structure over time and no periodic fluctuations based on seasonality.

Using a stationary data set, the model can do prediction based on the fact that mean and variance will remain the 
same in the future periods

A stationarized series is easy to predict. If we understand the statistical property of the stationarized series then 
we can easily predict the future. The statistical property of the series will remain the same in future as they have 
been in the past.

### How do we know if the data is stationary?
- Visual
- Augmented Dickey-Fuller (ADF)

### Visual

<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*ltLfFhoZypScZFA6W-D8AA.png" alt="" width=600 />
</div>

**`Stationary data with constant mean and Non Stationary data with changing mean`**

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*hgP6gGCccVs7lAN5zUy5UQ.png" alt="" width=600 />
</div>

**`Non Stationary data with high variance`**

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*kTpI31cbUKptYNDfv0Okcg.png" alt="" width=600 />
</div>
<br>

### Augmented Dickey-Fuller(ADF)Test

Augmented Dickey-Fuller(ADF) is the most popular statistical method to find if the series is stationary or not. It is 
also called as Unit Root Test.

Unit Root Test determines how strongly a time series is defined by a trend

> $H_0$ : Null hypothesis for ADF test is that time series can be represented by a Unit root, that is not stationary. 
It means that time series has some time dependent structure.
> 
> $H_a$ : Alternate hypothesis is that time series is stationary

##### ADF test gives us the:

- test statistics.
- p-value.
- critical values.

<br>

> - If $\\text{test statistic} > \\text{critical value}$ : it implies that **`the series is not stationary`**.
> 
> - If $\\text{p-value}>0.05$ : then fail to reject the null hypothesis. This means that **`time series has unit root`** 
and **`is not stationary`**.
>
> - If $\\text{p-value} \\le 0.05$ : Reject the null hypothesis , **`the data does not have a unit root`** and **`is 
stationary`**.
> 

### What if the time series data is not stationary?

We can apply the different technique to make the data stationary. This technique helps generate series with constant 
location and scale

- **`Differencing`**: calculates the difference between consecutive terms or points in the data. **`Differencing is 
performed to get rid of the varying mean`**.

<div align='center'>

$$Y= X_t - X_{t-1}$$

</div>

- **`Seasonality Differencing`**: the difference between an observation and a previous observation from the same season. 
For e.g.; sale of Chocolates is high during festival season. For seasonality differencing we take the sales of 
Chocolates last year during festival season and sales this year during festival season.

- **`Log transformation or square root or power transformation`**: helps to stabilize the non-constant variance of a 
series.

### How to reducing Random noise from Time Series data?

**`Smoothing`** is a statistical technique that can reveal the underlying trend, or seasonality or cyclic pattern 
present in the time series data. Smoothing data removes random variation and reveals trends and cyclic component.

smoothing can be applied using

- Averaging
- Exponential Smoothing methods assigns exponentially decreasing weights as the observation get older. Recent 
observations are given higher weights compared to the previous observations

#### Analyzing Trend in the Time Series:

As part of trend analysis, we remove the random noise by apply smoothing. Moving Average is the most common smoothing 
technique. It could be a simple average or weighted average. The benefit of moving average smoothing is that its 
results are less biased by outliers.

Monotonous time series data can be approximated by a linear function. For non-monotonous non-linear data, 
we apply transformations like log transformation, exponential transformation or square root transformations to remove 
the non-linearity.

### Analyzing Seasonality in Time Series:

Seasonality is a structured pattern of changes within a year. Understanding of the seasonality of data is useful to 
make a prediction for any time series data like managing right inventory levels or planning production for the right 
products.

Seasonality present in Time Series can be identified by:

- Domain knowledge of time series is helpful to understand structured patterns repeating over year
- Using a plot of the data.
- Obtaining a lagged autocorrelation function.
- ANOVA: Analysis of Variance —Used to test two groups to check the difference between them.

Now that we understand the underlying pattern of time series it is time for a prediction. We will explore ARIMA.

### ARIMA Auto Regression Integrated Moving Average

ARIMA is a statistical analysis model for time series that helps us predict future trends for time series.

**It is a form of regression analysis that evaluates the strength of the dependent variable relative to other 
changing variables.**

**Non-Seasonal ARIMA**: Prediction population of a County for infrastructure planning.

**Seasonal ARIMA**: Predicting demand for different products during different months of a year.

### ARIMA has three components

#### 1. Auto Regression: AR(p)
- Past values are used in the regression equation for the series $Y$.
- Autoregression uses dependent relationship between observation and number of lagged observations.
- The pattern of growth/decline in the data is accounted for using Autoregression.
- Auto-regressive parameter p specifies the number of lags used in the model.
- Identification of AR is best done using **`PACF`**.

<div align='center'>

$$AR(p): Y_t = \\theta + \\alpha_1Y_{t-1} + \\alpha_2Y_{t-2} + \\dots + \\alpha_pY_{t-p} + \\varepsilon_t$$

</div>

#### 2. Integrated: I(d)
- Differencing to make time-series data stationary.
- Rate of change of the growth/decline in the data is accounted.
- **`d`** represents the number of times data have to be “differenced” to produce stationary data.

#### 3. Moving Average: MV(q)

Noise between consecutive time points is accounted for by Moving Averages. The model that uses dependency between an 
observation and its residual error from a moving average model applied to lagged observations

- Represents the error of the model as a combination of previous error terms
- **`q`** represents the number of preceding or lagged values for the error term that are added or subtracted to $Y$.
- Smooth out the noise from the time series
- Identification of the MA model is done best by **`ACF`**

<div align='center'>

$$MA(q): Y_t = \\theta + \\beta_1\\varepsilon_{t-1} + \\beta_2\\varepsilon_{t-2} + \\dots + \\beta_q\\varepsilon_{t-q} + \\varepsilon_t$$

</div>

### ARIMA model is expressed as ARIMA(p,d,q). Also referred to as non-seasonal ARIMA model.

- $p$ = number of lags used in the model.

- $d$ = degree of differencing.

- $q$ = No. of error terms to include in the model.

<div align='center'>

$$ARIMA(p,d,q): Y_t = \\theta + \\alpha_1Y_{dt-1} + \\alpha_2Y_{dt-2} + \\dots + \\alpha_pY_{dt-p} + \\beta_1\\varepsilon_{t-1} + \\beta_2\\varepsilon_{t-2} + \\dots + \\beta_q\\varepsilon_{t-q} + \\varepsilon_t$$

</div>

### SARIMA -Seasonal ARIMA Auto Regression Integrated Moving Average
Seasonal ARIMA models rely on seasonal lags and differences to fit the seasonal pattern.

SARIMA model is represented by SARIMA(p,d,q)x(P,D,Q)

We have three additional terms compared to ARIMA model:

- $P$ is the number of seasonal autoregressive terms.

- $D$ is the number of seasonal differences.

- $Q$ is the number of seasonal moving-average terms.

#### How do we choose the values for $p$, $d$ and $q$, and $P$, $D$ and $Q$?
- we use Auto Correlation Function(ACF) or Partial Auto Correlation function (PACF) to find the values for $p$, $d$ and $q$ to be used in ARIMA.

- Auto Correlation tells us how correlated a time series is to its previous values. It is the correlation between observations of a time series separated by k time units.

- Partial autocorrelations measure the strength of relationship with other terms being accounted.

- We can also use pmdarima(Pyramid ARIMA) library which performs a grid search across multiple combinations of $p$, $d$ and $q$ and $P$, $D$ and $Q$. This is the most effective way to build a good ARIMA or SARIMA model.

- pmdarima library compare AIC(Akaike Information Criteria) metric to evaluate the performance of different ARIMA models.


</div>

    """, unsafe_allow_html=True)


