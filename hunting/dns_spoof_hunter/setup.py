from setuptools import setup

setup(
    name="kube-hunter-dns-spoof",
    install_requires=["kube-hunter", "kube-hunter-arp-spoof", "scapy>=2.4.3"],
    entry_points={"kube_hunter": ["dns_entrypoint = dns_entrypoint"]},
    py_modules=["kube_hunter_dns_spoof"],
)