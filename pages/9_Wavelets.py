import streamlit as st
from App import Logos

st.set_page_config(page_title="Wavelets", page_icon="📈")

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
# Wavelets

</div>
<br><br>

## 1. What’s a Wavelet?

A Wavelet is a wave-like oscillation that is localized in time, an example is given below. Wavelets have two basic 
properties: scale and location. Scale (or dilation) defines how “stretched” or “squished” a wavelet is. This property 
is related to frequency as defined for waves. Location defines where the wavelet is positioned in time (or space). 

<br><br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Ioee_j_s29XVULQVUN_OmA.png" alt="" width=500 />
</div>
<br>

The parameter “a” in the expression above sets the scale of the wavelet. If we decrease its value the wavelet will 
look more squished. This in turn can capture high-frequency information. Conversely, increasing the value of “a” will 
stretch the wavelet and captures low-frequency information.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*F4yPDvEePSWVLb7C9rRuag.png" alt="" width=600 />
</div>
<br>

The parameter “b” defines the location of the wavelet. Decreasing “b” will shift the wavelet to the left. Increasing 
“b” will shift it to the right. Location is important because, unlike waves, wavelets are only non-zero in a short 
interval. Furthermore, when analyzing a signal we are not only interested in its oscillations, but where those 
oscillations take place.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*QUAYlxYNrdRX0f4gRjTLtA.png" alt="" width=600 />
</div>
<br>

## 2. How does it work?
Let’s take another look at the same animation from before.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:828/1*4fXf0Yy8TMLSk7LXoZDDWw.gif" alt="" width=600 />
</div>
<br>

The **basic idea** is to **compute how much of a wavelet is in a signal** for a particular scale and location. For those 
familiar with convolutions, that is exactly what this is. A signal is convolved with a set wavelets at a variety of 
scales.

In other words, we pick a wavelet of a particular scale (like the blue wavelet in the gif above). Then, we slide this 
wavelet across the entire signal i.e. vary its location, where at each time step we multiply the wavelet and signal. 
The product of this multiplication gives us a coefficient for that wavelet scale at that time step. We then increase 
the wavelet scale (e.g. the red and green wavelets) and repeat the process.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*cjq2OLBemTeqm0FDD2WmOQ.png" alt="" width=600 />
</div>
<br>

There are two types of Wavelet Transforms: Continuous and Discrete. Definitions of each type are given in the above 
figure. The key difference between these two types is the Continuous Wavelet Transform (CWT) uses every possible 
wavelet over a range of scales and locations i.e. an infinite number of scales and locations. While the Discrete 
Wavelet Transform (DWT) uses a finite set of wavelets i.e. defined at a particular set of scales and locations.

## 3. Why wavelets?
A couple of key advantages of the Wavelet Transform are:

- **Wavelet transform** can extract local spectral **and** temporal information simultaneously
- **Variety of wavelets** to choose from

We have touched on the first key advantage a couple of times already. This is probably the biggest reason to use the 
Wavelet Transform. This may be preferable to using something like a Short-Time Fourier Transform which requires 
chopping up a signal into segments and performing a Fourier Transform over each segment.

The second key advantage sounds more like a technical detail. Ultimately, the takeaway here is if you know what 
characteristic shape you are trying to extract from your signal, there are a wide variety of wavelets to choose from 
to best match that shape. A handful of options are given in the figure below.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*mkdL9Wjoj2MjbPtkrpoZjA.png" alt="" width=700 />
</div>
<br>

### Example: Detecting R-peaks in ECG Signal

In this example, I use a type of discrete wavelet transform to help detect R-peaks from an Electrocardiogram (ECG) 
which measures heart activity. R-peaks are typically the highest peak in an ECG signal. They are part of the 
QRS-complex which is a characteristic oscillation that corresponds to the contraction of the ventricles and expansion 
of the atria. Detecting R-peaks is helpful in computing heart rate and heart rate variability (HRV). Example code can 
be found in the [GitHub repo](https://github.com/ShawhinT/YouTube-Blog/tree/main/waveletTransform).

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*m7tYdH0YdsaPBCzPB7Higw.jpeg" alt="" width=700 />
</div>
<br>

In the real world, we rarely have ECG signals that look as clean as the above graphic. As seen in this example, 
ECG data is typically noisy. For R-peak detection, simple peak-finding algorithms will fail to generalize when 
applied to raw data. The wavelet transform can help convert the signal into a form that makes it much easier for our 
peak finder function.

Here I use the maximal overlap discrete wavelet transform (MODWT) to extract R-peaks from the ECG waveform. The 
Symlet wavelet with 4 vanishing moments (sym4) at 7 different scales are used. Below the original ECG signal is 
plotted along with wavelet coefficients for each scale over time.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*R6SXRFa4Lg_QFMHJbyNCVQ.png" alt="" width=700 />
</div>
<br>

The smaller scales such as 2⁰ and 2¹ correspond to high frequencies thus predominantly consist of noise in this 
example. As we go up in scale, we see blips emerge from the noise that corresponds to R-peaks, i.e. in 2², 2³, 
and 2⁴. We then lose the signal in the larger scale coefficients i.e. 2⁵ and 2⁶, which are associated with 
low-frequency information.

We can then reconstruct the original signal with information from a subset of our wavelet scales. Here I only keep 
information from one scale, 2³. Below the original and reconstructed signals are plotted. We see the peaks in the 
reconstructed ECG (lower plot) line up reasonably well with the R-peaks. Additionally, applying a peak finder to the 
reconstructed ECG seems much more promising than to the original ECG.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8Os1HhPKpBuTcLeZ6XejJw.png" alt="" width=700 />
</div>
<br>

The final step is to apply a find peaks function to the reconstructed signal. This will approximately give the 
timestamps of each R-peak. To evaluate the performance we plot the detected R-peaks on top of the original signal.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*yZbeDuhTQSAGXRo4OqtRvw.png" alt="" width=700 />
</div>

### Conclusion

In this post, the Wavelet Transform was discussed. The key advantage of the Wavelet Transform compared to the Fourier 
Transform is the ability to extract both local spectral and temporal information. A practical application of the 
Wavelet Transform is analyzing ECG signals which contain periodic transient signals of interest. <br>

</div>

    """, unsafe_allow_html=True)


