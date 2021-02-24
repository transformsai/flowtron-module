# flowtron-module

Shim to allow using flowtron as a pip module

Please see https://github.com/NVIDIA/flowtron for the appropriate documentation.

This shim works by generating the `__init.py__` files required to access the flowtron, tacotron2 and waveglow directories as modules.

These shims are generated during setup.py, which executes after the repository is cloned recursively. This repository is needed because Flowtron itself uses git submodules to organize its files. It also uses `sys.path.insert(0, "tacotron2")` to manage its imports. 

# WINDOWS WARNING 

In order to use this for windows, you MUST enable longpaths on the git installation that `pip` uses.

To do this, run:

```
git config --system core.longpaths true

```
or
```
git config --glohal core.longpaths true
```

There are some repercusions to doing this. 
