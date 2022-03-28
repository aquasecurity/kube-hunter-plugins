from setuptools import setup

setup(
    name="kube-hunter-arp-spoof",
    install_requires=["kube-hunter", "scapy>=2.4.3"],
    entry_points={"kube_hunter": ["arp_entrypoint = arp_entrypoint"]},
    py_modules=["kube_hunter_arp_spoof"],
)