"""setup.py file"""

import uuid
import setuptools
try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

__author__ = 'Steffen Walter <steffen.walter@atos.net>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.requirement) for ir in install_reqs]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='napalm_flexfabric',  
    version='0.2',
    packages=setuptools.find_packages(),
    author="Steffen Walter",
    author_email="steffen.walter@atos.net",
    description="Network Automation and Programmability Abstraction Layer (NAPALM) FlexFabric driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firefly-serenity/napalm-flexfabric/",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
)
