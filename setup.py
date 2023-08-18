from setuptools import setup

with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()

setup(
    name="coderedcms-bootstrap4",
    version="2.0.0",
    author="CodeRed LLC",
    author_email="info@coderedcorp.com",
    url="https://github.com/coderedcorp/coderedcms-bootstrap4",
    description="Bootstrap 4 compatibility theme for Wagtail CRX.",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="BSD license",
    include_package_data=True,
    packages=["coderedcms_bootstrap4"],
    python_requires=">=3.7",
    install_requires=[
        "django-bootstrap4==22.2",
    ],
    classifiers=[
        "Framework :: Wagtail",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
