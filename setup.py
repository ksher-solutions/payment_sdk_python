import codecs
import os
import sys


try:
    from setuptools import setup,find_packages
except:
    from distutils.core import setup,find_packages


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
 

NAME = "ksherpay"
PACKAGES = ['hmac','hashlib','requests','urllib']
DESCRIPTION = "python implementation for Khser Payment API."
KEYWORDS = "Ksher, ksher, ksher-payment, ksher-payment-api, ksherpay"
AUTHOR = "Deemarc B"
AUTHOR_EMAIL = "deemarc.br@gmail.com"
URL = "https://github.com/ksher-solutions/payment_sdk_python"
VERSION = "1.0.0"
LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    # long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = find_packages(),
    include_package_data=True,
    zip_safe=True,
)
