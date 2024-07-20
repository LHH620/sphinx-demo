# Sphinx构建文档的使用方法

> 这里是一段引用，用来简要介绍或者说明这个文档的用途，同时也可以引用相关的内容。

```{important}
- 下面的部分内容需要安装对应的插件和开启扩展才可以实现，部分插件和扩展可能在部分主题上显示存在些许问题，所以请以**实际效果**为准。
```

## 数学符号和公式

开启公式显示和解析需要到`conf.py`文件中开启`extensions`中的`sphinx.ext.mathjax`插件。

### 使用mathjax构建公式

- 这是一个开普勒第三定律的公式：$a^3 = p^2$
  其中 $a$ 是半长轴，$p$ 是周期。

- 这是爱因斯坦质能方程：$E = mc^2$,
  其中 $E$ 是能量，$m$ 是质量，$c$ 是光速。
    

### 使用标签构建公式

Since Pythagoras, we know that {math}`a^2 + b^2 = c^2`.

```{math}
:label: mymath
(a + b)^2 = a^2 + 2ab + b^2

(a + b)^2  &=  (a + b)(a + b) \\
           &=  a^2 + 2ab + b^2
```

添加了label的公式， {eq}`mymath` is a quadratic equation.

### 使用$符号构建公式
$$
(a + b)^2  &=  (a + b)(a + b) \\
           &=  a^2 + 2ab + b^2
$$ (mymath2)

The equation {eq}`mymath2` is also a quadratic equation.

Hence, for $\alpha \in (0, 1)$,
$$
  \mathbb P (\alpha \bar{X} \ge \mu) \le \alpha;
$$
i.e., $[\alpha \bar{X}, \infty)$ is a lower 1-sided $1-\alpha$ confidence bound for $\mu$.

### 使用Latex语法构建公式

$$
\begin{gather*}
a_1=b_1+c_1\\
a_2=b_2+c_2-d_2+e_2
\end{gather*}
$$

$$
\begin{align}
a_{11}& =b_{11}&
  a_{12}& =b_{12}\\
a_{21}& =b_{21}&
  a_{22}& =b_{22}+c_{22}
\end{align}
$$

```{note}
- 当我们在这个文档里面使用Latex语法的时候，虽然可以不用将公式包裹在$符号之内，但为了保持兼容性，我们还是保留这个符号，符合约定俗成的规定。
- 支持的latex环境有以下几种：equation, multline, gather, align, alignat, flalign, matrix, pmatrix, bmatrix, Bmatrix, vmatrix, Vmatrix, eqnarray.

```

## 代码

支持代码高亮

```python
class GoogleStyle:
    '''Google注释风格

    用 ``缩进`` 分隔，
    适用于倾向水平，短而简单的文档

    Attributes:
        dividend (int or float): 被除数
        name (:obj:`str`, optional): 该类的命名
    '''

    def __init__(self, dividend, name='GoogleStyle'):
        '''初始化'''
        self.dividend = dividend
        self.name = name

    def divide(self, divisor):
        '''除法

        Google注释风格的函数，
        类型主要有Args、Returns、Raises、Examples

        Args:
            divisor (int):除数

        Returns:
            除法结果

        Raises:
            ZeroDivisionError: division by zero

        Examples:
            >>> google = GoogleStyle(divisor=10)
            >>> google.divide(10)
            1.0

        References:
            除法_百度百科  https://baike.baidu.com/item/%E9%99%A4%E6%B3%95/6280598
            
        More:
            回到主页：:doc:`index`  
        '''
        try:
            return self.dividend / divisor
        except ZeroDivisionError as e:
            return e
```

## 表格

> 表格可以添加标题

:::{table} 表格标题
:widths: auto
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
:::

## 图片

### 网络图片

语法：
```markdown
![alt text](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png "Python logo")
```
显示效果

![alt text](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png "Python logo")

### 本地图片

语法：
```markdown
![alt text](_static/logo.png)
```
显示效果
![alt text](_static/logo.png)


### 使用html语法的图片

语法：
```html
<img src="_static/logo.png" alt="alt text" width="400" height="200">
```
显示效果：
<img src="_static/logo.png" alt="alt text" width="400" height="200">

## 交叉引用

> 交叉引用是文档中非常重要的一部分，它可以帮助读者快速找到相关的内容。

交叉引用主要用于引用文档中的其他部分，包括标题、图片、表格、代码块等。

为了实现这个效果，首先需要在文档中的适当位置设置一些锚点，然后在其他地方引用这些锚点。

创建锚点主要有三种方法：
1. 用`(target)=`注释语法块
2. 使用`{#id}`属性注释语法（需要开启`attrs_block`和`attrs_inline`扩展）
3. 直接为指令添加`name`属性

```{attention}
为了实现`id`的锚点跳转功能，需要到`conf.py`中的`myst_enable_extensions`开启`attrs_block`和`attrs_inline`扩展。
```python
myst_enable_extensions = [
    ...
    "attrs_inline", # 行内属性
    "attrs_block", # 属性块
]
```


### 文档内部跳转

(heading-target)=
#### Heading

{#paragraph-target}
This is a paragraph, with an `id` attribute.

This is a [span with an `id` attribute]{#span-target}.

:::{note}
:name: directive-target

这是一个添加了  `name` 属性的段落。
:::

- [reference1](#heading-target)
- [reference2](#paragraph-target)
- [reference3](#span-target)
- [reference4](#directive-target)

### 跨文档跳转

跳转到另一个文档：[点击这里](./utils.rst)

## 一些特殊的块

> 这些特殊的块以一种更加美观突出的方式展现，可以使得文档的内容更加丰富。




```{danger}
这是一个危险块。
```

```{warning}
这是一个警告块。
```



```{error}
this is a block
```

```{hint}
this is a block
```

```{seealso}
this is a block
```

```{tip}
这是一个提示快
```

```{caution}
这里是一个警告内容
```

自定义一个块

:::{admonition} My custom title with *Markdown*!
:class: tip

This is a custom title for a tip admonition.
:::





## 任务列表
- [ ] An item that needs doing
- [x] An item that is complete




## 特殊功能

:::{admonition} 点击标题展开和折叠
:class: dropdown

This title was made into a dropdown admonition by adding `:class: dropdown` to it.
:::

```{toggle}
这是一个具有翻转功能的块，你可以点击用来查看或者隐藏！
```

## 使文档更具有设计感

只需要安装`sphinx-design`即可实现。

```bash
pip install sphinx-design
```

然后在`conf.py`里面开启扩展
```python
extensions = [
    "sphinx_design",
    # other extensions
]
```

### 效果展示
- 卡片
- 标签页

:::{card} 卡片标题
Sphinx demo
^^^
这是一个使用 `sphinx-design` 的卡片，可以更好地展示具有卡片形式的内容。
+++
感兴趣的话可以支持一下！
:::

::::{tab-set}

:::{tab-item} 唐诗
白日依山尽，黄河入海流。
欲穷千里目，更上一层楼。
:::

:::{tab-item} 宋词
众里寻他千百度，蓦然回首，那人却在灯火阑珊处。
:::

::::



