代码练兵场
=============

这里是一个虚拟的运行环境，使用 `shift+enter` 即可运行代码


目前支持的环境包括：numpy，matplotlib

.. py-config::

    splashscreen:
        autoclose: true
    packages:
    - matplotlib
    - numpy

.. py-repl::
    :output: replOutput

    import numpy as np
    import matplotlib.pyplot as plt
    

    print('currently numpy version: ', np.__version__)

    x = np.linspace(0, 10, 100)
    plt.plot(x, np.sin(x))
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Sinusoidal Function')
    plt.grid(True)
    plt.gcf()

    

.. raw:: html

    <div id="replOutput"></div>

.. py-terminal::