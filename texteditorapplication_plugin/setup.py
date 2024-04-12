from setuptools import setup

setup(
    name="texteditorapplication_plugin",
    install_requires="texteditorapplication",
    entry_points={"texteditorapplication": ["plugin = texteditorapplication_plugin"]},
    py_modules=["texteditorapplication_plugin"],
)