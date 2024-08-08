# -- 项目信息 -----------------------------------------------------

project = "KiraKira 用户手册"
copyright = "2024, Linko (Website: KiraKira☆Douga)"
author = "Linko"
release = "0.0.1"

# -- 基础配置 ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx_markdown_tables",
    # "sphinx_togglebutton",  # https://studynotes.readthedocs.io/zh/main/struct/extend/togglebutton.html
    # "sphinx_tabs.tabs",  # https://studynotes.readthedocs.io/zh/main/struct/extend/tab.html
    "sphinx.ext.todo",
]

todo_include_todos = True

# 配置 myst_parser
myst_enable_extensions = [
    "colon_fence",
]

# 如果你想显式声明支持的文件类型，可以添加以下行
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = []

language = "zh_CN"

# -- HTML 配置 -------------------------------------------------

html_theme = "pydata_sphinx_theme"
# html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
