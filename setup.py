from setuptools import setup, find_namespace_packages

setup(
    name='yt-dlp-sample-plugins',
    packages=find_namespace_packages(include=[r'yt_dlp_plugins.*'])
)
