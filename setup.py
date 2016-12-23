from setuptools import setup

setup(
    name="electrum-moon-server",
    version="0.9",
    scripts=['run_electrum_moon_server','electrum-moon-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrummoon':'src'
        },
    py_modules=[
        'electrummoon.__init__',
        'electrummoon.utils',
        'electrummoon.storage',
        'electrummoon.deserialize',
        'electrummoon.networks',
        'electrummoon.blockchain_processor',
        'electrummoon.server_processor',
        'electrummoon.processor',
        'electrummoon.version',
        'electrummoon.ircthread',
        'electrummoon.stratum_tcp',
        'electrummoon.stratum_http'
    ],
    description="Doge Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/electrumalt/electrum-moon-server/",
    long_description="""Server for the Electrum Lightweight Dogecoin Wallet"""
)


