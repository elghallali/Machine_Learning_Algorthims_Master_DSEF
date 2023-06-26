import streamlit as st
from App import Logos

st.set_page_config(page_title="The Fast Fourier Transform", page_icon="📈")

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
# The Fast Fourier Transform (FFT)

</div>
<br><br>

## Discrete Fourier Transform (DFT)

In some posts the Fourier Transform (FT) and some applications. In signal processing, 
this formal FT definition is not always helpful since it is rare to have functional forms of signals. To apply this 
method to real world data we need a FT definition for a discrete set of values. This is given by the Discrete Fourier 
Transform (DFT) which is the FT of a discrete sequence of values. This is derived (informally) by rewriting the 
function in the FT as a discrete sequence (vector if you like) and replacing the infinite sum, with a sum over a 
finite number of values.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*BSsOXyrKR6UhtIiz1dmmeg.png" alt="" width=600 />
</div>
<br>

Taking a closer look at the DFT expression.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:446/format:webp/1*WtMS3H-vH3FSCXOVij128A.png" alt="" width=200 />
</div>
<br>

Where, 
- $x_n$ is an element of our discrete signal, which is a column vector. 
- $f_k$ is an element of our transformed discrete signal, also a column vector. 
- $N$ is the number of elements in the vector consisting of $x_n$’s. 
- $n$ and $k$ are indexes corresponding to the original and transformed signal vectors, respectively.

Let’s introduce a new term.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*A4Fv9AUuky7gT3MYhmGBSQ.png" alt="" width=150 />
</div>
<br>

Notice that $R_{kn}$ has 2 indexes, $n$ and $k$. Therefore, we can think of it as an element of a 2 dimensional matrix. 
Substituting back into our expression for DFT.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:392/format:webp/1*k1Y4e2t0hZnbYFyrhUDrGg.png" alt="" width=200 />
</div>
<br>

For clarity, we can write the matrices corresponding to these terms.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*d_Lko0nOJbn2jiLwjuLVqQ.png" alt="" width=600 />
</div>
<br>

Finally, from the properties of matrix multiplication we can represent the DFT as a simple matrix operation. (If this 
is not immediately obvious, think about a simple case where N=K=2).

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:750/format:webp/1*Ay0YC5XpDNOy9TsFkX6Kog.png" alt="" width=400 />
</div>
<br>

My natural reaction to this sequence of steps is: “Wow, that so cool! The **DFT** can be written as matrix 
multiplication.. but so what?” If we want to code this up we still (naively) will need 2 for loops, and in the case 
where $N=K$ this gives us $O(N^2)$ time complexity. Meaning, we will have to perform on the order of $N^2$ 
computations to complete this operation. To put that into perspective, the **DFT** of your favorite 3 minute song 
would have on the order $\\big(\\frac{3min\\times 60sec}{1min\\times44100Hz}\\big)^2 \\approx 6E10^{13}$ computations!

Although things may seem hopeless, let’s take look at a concrete example of this matrix $R$. Consider the case, 
where $N=K=4$. Again, $N$ corresponds to the number of elements in input signal $x$ and $K$ is the number of elements 
in the DFT output $f$.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*80GrnZqbGnExp8mNfTleXQ.png" alt="" width=600 />
</div>
<br>

$R$ is called the Fourier Matrix. Here we have the 4 by 4 Fourier matrix whose elements were defined earlier (that “new 
term”). Notice, $R$ is symmetric meaning if we swapped the rows and columns we would have the same matrix. Note, 
we have 4 unique terms out of 16 elements i.e. $1$, $-1$, $i$, and $-i$.

We can also define any Fourier Matrix, $R$, in terms of its $n=k=1$ element, where we start counting from 0. In general, 
this is given by,

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:298/format:webp/1*5E-Ni-egevqP9rydihtvkw.png" alt="" width=150 />
</div>
<br>

We can rewrite the 4 by 4 Fourier Matrix using only this term.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:420/format:webp/1*PMn-6hmffs7CsiXmVwWpDg.png" alt="" width=200 />
</div>
<br>

Let’s take a look at a few more examples.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*2kl2eUSIEm2mttsZmsxFig.png" alt="" width=500 />
</div>
<br><br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:548/format:webp/1*lNazs_p80FPrrVbor8XSrQ.png" alt="" width=200 />
</div>
<br><br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:340/format:webp/1*hSqtAzOoPQVf8sFlnP6PkQ.png" alt="" width=150 />
</div>
<br>

We can notice, that the above Fourier matrices are comprised of a few unique terms compared to the size of each 
matrix. Additionally, all three matrices seem to have elements in common. It would be nice if we could exploit this 
redundancy to reduce the number of operations needed to compute the DFT… This is exactly what the Fast-Fourier 
Transform does.

## Fast-Fourier Transform (FFT)

Often cited as one of the most important algorithms of the 20th century, the **Fast-Fourier Transform (FFT)** is 
truly what brings the idea of the Fourier Transform into practice. The FFT is **an efficient algorithm for 
computing the DFT**. The core idea behind **FFT** is re-expressing Fourier Matrices as the product of 3 (sparse) 
matrices, given below.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*f2ELOrhdr5U42CH4pxRjxQ.png" alt="" width=400 />
</div>
<br><br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:270/format:webp/1*yKSM-1LlyoFWAaiQClVRoQ.png" alt="" width=150 />
</div>
<br>

To see a concrete example, let’s return to our 4 by 4 Fourier Matrix.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*hejdRw_iN1rLqLH3tq30dg.png" alt="" width=500 />
</div>
<br><br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*z5d5EcNV6mjUAtctgvKb4w.png" alt="" width=500 />
</div>
<br>

We can take a moment to visually compare this example to the general expression. Defining some objects, $I_2$ is the 2 
by 2 identity matrix, $D_2$ is a 2 by 2 diagonal matrix consisting of the first 2 diagonal elements of the 4 by 4 
Fourier Matrix, and finally $R_2$ is the 2 by 2 Fourier Matrix.

It may not be immediately obvious why this re-expression is helpful. Let’s walk through this operation at a high 
level. First we note, that multiplying the permutation matrix by the input signal is practically free, 
as far as computation. This is equivalent to reshuffling elements in the input signal which can be done in constant 
time, $O(1)$. Next, half the terms in the middle matrix are zeroes, thus we are left with 8 non-trivial terms this 
gives $O(2N)$ time complexity. Finally, half the terms in the left-most matrix are again zero. Additionally, 
half of the non-zero terms will always be 1, so there is no need to perform a multiplication. Ultimately this leaves 
us with $O(N)$ time complexity for the left matrix.

Adding everything up, $O(1) + O(2N) + O(N) = O(3N + 1) = O(13)$. Which is an improvement from the original $O(N^2) = O(
16)$. More generally, it turns out as N goes to infinity we get $O(N log(N))$ time complexity for the FFT.

To see this, let’s take a look at one last example.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:554/format:webp/1*K27Ku5v1fB5Z3LZ1YzlXlw.png" alt="" width=300 />
</div>
<br>

Here we have the $R_{16}$ expressed in terms of $R_8$. Notice, that we can play the same game with $R_8$ and express it in 
terms of $R_4$.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*S65vYvJFWIfKkTobrk4poA.png" alt="" width=500 />
</div>
<br>

Repeating the same idea for $R_4$.

<br>
<div align='center'>
<img src="https://miro.medium.com/v2/resize:fit:1100/format:webp/1*EyRSic9gRbevgzvo6GKOIA.png" alt="" width=700 />
</div>
<br>

Notice, every time we re-express a Fourier Matrix, we pick up some zeroes and lose computations. This is what makes 
the FFT so powerful and leads to $O\\big(N log(N)\\big)$ time complexity. Using technical jargon, this is an example of a 
recursive program.

As a brief note, $N$ in the above expression must be a power of 2. In practice, this can be achieved for an arbitrary 
signal by padding it with zeroes before and after.

## Conclusion

The Fast-Fourier Transform (FFT) is a powerful tool. It makes the Fourier Transform applicable to 
real-world data. Applications include audio/video production, spectral analysis, and computational physics.

Although FFT has made a great impact on science and technology, it is limited in what information it can extract from 
a signal. Specifically, the Fourier Transform uncovers global frequency information. In many situations, 
critical information does not persist over the entirety of a signal, but rather over a short window. An alternative 
analytical tool that is better suited for such tasks is the Wavelet Transform.

</div>

    """, unsafe_allow_html=True)


