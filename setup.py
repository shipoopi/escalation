#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(
    name='escalation',
    version='0.3.2',
    author='Gregory McWhirter',
    author_email='gmcwhirt@uci.edu',
    description='Game theory simulations for escalation research',
    url='https://www.github.com/gsmcwhirter/escalation',
    license='MIT',
    packages=[
        "escalation"
    ],
    install_requires=[
        'simulations>=0.5.0'
    ],
    package_dir={
        '': 'src',
    },
    dependency_links=[
        "https://www.ideafreemonoid.org/pip/simulations"
    ],
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector',
    scripts=[
        "scripts/escalation.sim.py",
        "scripts/escalation.stats.py"
    ]
)
