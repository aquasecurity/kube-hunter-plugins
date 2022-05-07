from setuptools import setup

setup(
    install_requires=["kube-hunter", "scapy>=2.4.3"],
    entry_points={"kube_hunter": ["arp_spoof = kube_hunter_arp_spoof"]},
    py_modules=["kube_hunter_arp_spoof"],
)