# Some info in a markdown file

This is a markdown file. Inline equation $a = 2 + 2$.

$$
y = mx + c
$$

This is a bare URL which has auto been turned into a link with the `linkify` MyST syntax extension... www.google.com

This is some more maths in a `$$` code block

$$
   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}
$$

Below is direct latex with no `$$` :)

\begin{align*}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align*}

:::{note}
This is an admonition box. This text is **standard** _Markdown_
:::

Below is a code block

```python
import numpy as np
x = np.random.rand(12)
```