#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    package_data={"sample_data/*": ["*.nc, *.csv, *.yaml, *.xlsx, *.geojson, "
                                    "*.zip"]}
)

