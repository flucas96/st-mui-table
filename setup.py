import setuptools


with open('README.md') as f:
    long_desc = f.read()

setuptools.setup(
    name="st_ant_carousel",
    version="0.0.3",
    author="",
    author_email="",
    setup_requires=['wheel'],
    description="Streamlit Component for ANT Carousel",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    # url="https://github.com/flucas96/st_ant_tree",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)

