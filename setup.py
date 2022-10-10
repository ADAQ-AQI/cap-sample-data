#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    # ...,
    packages=find_packages(where="cap_sample_data"),
    package_dir={"": "sample_data"},
    package_data={"sample_data/*": ["*.nc, *.csv, *.yaml, *.xlsx, *.geojson, "
                                    "*.zip"]}
)

