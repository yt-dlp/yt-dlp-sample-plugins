from setuptools import setup, find_namespace_packages

setup(
    name='ytdlp-sample-plugins',
    packages=find_namespace_packages(include=[r'ytdlp_plugins.*'])
)
