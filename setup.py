from setuptools import setup, find_packages


requirements = [l.strip() for l in open('requirements.txt').readlines()]


    install_requires = ['Django>=1.9.0', "django-uni-form>=0.8.0"],
    include_package_data = True,
setup(
    name="oauth2app",
    version="0.3.0",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,

    # metadata for upload to PyPI
    author="John Wehr",
    author_email="johnwehr@gmail.com",
    description="Django OAuth 2.0 Server App",
    license="MIT License",
    keywords="django oauth2 oauth app server",
    url="https://github.com/david/oauth2app",
)
