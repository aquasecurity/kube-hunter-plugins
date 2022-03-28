# kube-hunter-plugins
The following repo contains an official collection of kube-hunter plugins.
As well as documentations for how to create one yourselves.

## Intro
Due to the pluggable mechanism in kube-hunter (provided by the [pluggy package](https://pluggy.readthedocs.io/en/stable/))  
You can add almost _any_ additional functionality to kube-hunter without diving into 
a large codebase.
By convention plugins should be a pypi package named with the following format:  
 `kube-hunter-example-plugin`

Plugins are functionalities that should not be included in the official implementations. it is there for users who wish to uniquely serve a specific solution for their private deployment. 
If you have an idea for a new functionality. feel free to create a PR to [kube-hunter](https://github.com/aquasecurity/kube-hunter) directly. We encourage every contribution!

## Official plugins
The plugins that are featured here are:
| Name | Pypi Package Name | Details |
| --- | -- | -- | 
| hunting/arp_spoof_hunter | kube-hunter-arp-spoof | Registers a new hunter: ArpSpoofHunter|
| hunting/dns_spoof_hunter      | kube-hunter-dns-spoof | Registers a new hunter: DnsSpoofHunter |
## Develop a new plugin
#### prerequisites
* read the [pluggy](https://pluggy.readthedocs.io/en/stable/) docs
* look at the examples in this repo

### 1. setup.py
Create a setup.py for the package. containing the following:
```python
from setuptools import setup

setup(
    name="kube-hunter-your-plugin",
    install_requires=["kube-hunter", "your-requirement-package>=0.0.0"],
    entry_points={"kube_hunter": ["plugin_entrypoint = plugin_entrypoint"]},
    py_modules=["kube_hunter_your_plugin"],
)
```

### 2. plugin_entrypoint.py
Create a plugin_entrypoint.py for the package. containing the following:
```python
from kube_hunter.plugins import hookimpl

""" This function will run BEFORE argument parsing """
@hookimpl
def parser_add_arguments(parser):
    parser.add_argument('--custom-argument', help="example for your custom argument")

""" This function will run AFTER argument parsing """
@hookimpl
def load_plugin(args):
    # You can either put your implementation directly here, or:
    import your_plugin_implementation # file
```

Optional plugin types:
| Type | hook name | purpose |
| --- | -- | -- | 
| Additional Argument | parser_add_arguments | Adding an additional argument to the cli
| Generic Plugin      | load_plugin | Registering hunters / Defining new events 

### 3. Install
Install the plugin 
```bash
pip install .
```


-----
