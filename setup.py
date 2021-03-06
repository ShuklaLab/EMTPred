import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='EMTPred',
    version='1.0.0',
    author='Bodhayan Prasad',
    author_email='bodhayan@live.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ShuklaLab/EMTPred',
    project_urls = {
        "Bug Tracker": "https://github.com/ShuklaLab/EMTPred/issues"
    },
    license='MIT',
    packages=['EMTPred'],
    install_requires=['numpy','pandas','sklearn','xgboost','pickle'],
)