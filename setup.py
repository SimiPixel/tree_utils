import setuptools

setuptools.setup(
    name="tree_utils",
    packages=setuptools.find_packages(),
    version="0.2.5",
    install_requires=["jax", "jaxlib", "dm-tree"],
)
