import setuptools

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="distributions",
    version="0.0.1",
    description="Probability distributions package",
    url="",
    author="Kelvin Wahome",
    author_email="kevowahome@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    zip_safe=False,
)
