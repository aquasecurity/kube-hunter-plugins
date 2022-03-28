import logging

from kube_hunter.plugins import hookimpl

logging.getLogger("scapy.runtime").setLevel(logging.CRITICAL)
logging.getLogger("scapy.loading").setLevel(logging.CRITICAL)

@hookimpl
def load_plugin(args):
    import kube_hunter_dns_spoof