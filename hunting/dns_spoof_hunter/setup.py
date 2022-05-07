from setuptools import setup

setup(
    install_requires=["kube-hunter", "kube-hunter-arp-spoof", "scapy>=2.4.3"],
    entry_points={"kube_hunter": ["dns_spoof = kube_hunter_dns_spoof"]},
    py_modules=["kube_hunter_dns_spoof"],
)