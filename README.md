[![Open in GitHub Codespaces](
  https://img.shields.io/badge/Open%20in%20GitHub%20Codespaces-333?logo=github)](
  https://codespaces.new/dwave-training/graph-isomorphism-example?quickstart=1)

# Graph Isomorphism
The [Graph Isomorphism](https://en.wikipedia.org/wiki/Graph_isomorphism) problem asks whether two given graphs
are isomorphic, that is, if a bijection (one-to-one mapping) of vertices between the graphs exists such that
the adjacency structure is preserved.

# Set up your environment
You can run this example without installation in cloud-based IDEs that support 
the [Development Containers specification](https://containers.dev/supporting)
(aka "devcontainers").

For development environments that do not support ``devcontainers``, install 
requirements:

    pip install -r requirements.txt

If you are cloning the repo to your local system, working in a 
[virtual environment](https://docs.python.org/3/library/venv.html) is 
recommended.

# Usage
A [supported IDE](https://docs.dwavequantum.com/en/latest/leap_sapi/dev_env.html) must be [authorized](https://docs.dwavequantum.com/en/latest/ocean/leap_authorization.html#authorizing-access-to-the-leap-service) and [configured](https://docs.dwavequantum.com/en/latest/ocean/sapi_access_basic.html) to access the Leap service.

To run this demo locally, open up Jupyter Lab with a terminal.
Run this command:
```
jupyter lab
```

In Jupyter Lab, you can open the notebook by clicking on the 
``Graph_Isomorphism_Lecture.ipynb`` file in VS Code-based IDEs. 

# Code Overview
The notebook provided covers encoding the objective and constraints of the Graph Isomorphism problem
with our open source D-Wave Ocean tools.

# References
Wiki page on [Graph Isomorphism](https://en.wikipedia.org/wiki/Graph_isomorphism).\
Circuit Equivalence example in [dwave-examples](https://github.com/dwave-examples/circuit-equivalence).

# License
Released under the Apache License 2.0. See [license](LICENSE) here.
