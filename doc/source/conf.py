# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# 增加代码文件目录
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'sphinx demo'
copyright = '2024, Mobius'
author = 'Mobius'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# 扩展插件
extensions = [
    'sphinx.ext.autodoc',   # Sphinx 扩展：根据代码自动生成文档
    'sphinx.ext.napoleon',  # Sphinx 扩展：支持 Google 和 NumPy 风格的 docstring
    'sphinx.ext.doctest',   # Sphinx 扩展：支持文档中的测试，运行 doctest 代码块
    'sphinx.ext.intersphinx',   # Sphinx 扩展：链接到其他项目的文档
    'sphinx.ext.todo',      # Sphinx 扩展：支持待办事项的管理和显示
    'sphinx.ext.coverage',  # Sphinx 扩展：生成文档覆盖率报告
    'sphinx.ext.mathjax',   # Sphinx 扩展：支持使用 MathJax 渲染数学公式
    'myst_parser',           # MyST-Parser 插件：支持 Markdown 语法
    'sphinx_togglebutton',  # Sphinx-Togglebutton 插件：支持折叠和展开内容
    'sphinx_design',        # Sphinx-Design 插件：提供高级设计元素
    'sphinx_copybutton',    # Sphinx-Copybutton 插件：为代码块增加复制按钮
    'sphinx.ext.viewcode',  # Sphinx 扩展：在文档中显示源代码按钮，可以直接跳转到源代码
    'sphinx_pyscript',      # Sphinx-PyScript 插件：在网页中执行代码（需要安装 pip install sphinx-pyscript）
]


templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "dollarmath",   # 解析使用 $ 或者 $$ 包裹的公式
    "amsmath",      # 解析使用 LaTeX 环境的公式
    "deflist",      # 开启定义某个项的功能（definition lists），一般很少使用
    "html_admonition",  # 解析 HTML 风格的告示块（admonitions），用于提示、警告等
    "html_image",   # 解析 HTML 格式的图像标签
    "colon_fence",  # 解析以冒号开头并围起来的代码块，类似 Markdown 的围栏代码块
    "smartquotes",  # 自动转换普通引号为对应的开合引号
    "replacements", # 解析文本替换功能，允许定义简短的替换语法
    "linkify",      # 自动将纯文本的 URL 转换为超链接
    "substitution", # 启用文本替换功能，允许在文档中插入替换变量
    "tasklist",     # 解析任务列表（task lists），即带复选框的列表项
    "attrs_inline", # 行内属性，允许通过 {#id} 和 {.class} 定义锚点和 CSS 类
    "attrs_block",  # 属性块，允许为整个块元素定义属性
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': '__init__',
    'inherited-members': True,
    'show-inheritance': True,
    'exclude-members': '__weakref__',
    'show-module-summary': False,  # 不显示模块摘要
}


# 解析行内公式，部分复杂的行内公式，
# 例如 $[\alpha \bar{X}, \infty)$ is a lower 1-sided $1-\alpha$ confidence bound for $\mu$.
# 会无法解析，因此需要开启
myst_dmath_double_inline = True # default: False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 设置主题选项
html_theme_options = {
    'canonical_url': '',  # 规范 URL，指定页面的规范 URL
    'analytics_id': 'UA-XXXXXXX-1',  # 分析 ID，例如 Google Analytics ID
    'logo_only': False,  # 如果为 True，仅显示 logo 而不显示项目名称
    'display_version': True,  # 显示项目的版本
    'prev_next_buttons_location': 'bottom',  # 上一页和下一页按钮的位置，选择 'bottom', 'top', 或 'both'
    'style_external_links': False,  # 外部链接样式，是否应用特定样式
    'vcs_pageview_mode': 'edit',  # 版本控制系统页面视图模式，例如 'edit' 或 'view'
    'style_nav_header_background': '',  # 导航头背景颜色
    # Toc options
    'collapse_navigation': True,  # 折叠导航栏，点击父标题时折叠子标题
    'sticky_navigation': True,  # 固定导航栏，在页面滚动时始终显示
    'navigation_depth': 3,  # 导航栏深度，显示到第几级标题
    'includehidden': True,  # 包含隐藏的 toc 项
    'titles_only': False,  # 仅显示标题而不显示内容
}

