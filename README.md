# Quantum Optimization Algorithms

This is the companion code to the quantum approximate optimization algorithm (QAOA) chapter of the Springer Quantum Optimization book. You can find the whole code as discussed in the QAOA chapter in the file `qaoa.py`. The implementation is based on the QAOA MaxCut functions from Pennylane [1] and the graph tools from NetworkX [2].

## Usage
We recommend executing this code in a virtual environment using Python version `3.11.5`. You can check you Python version in the terminal with:
```[sh]
python -V

//> Python 3.11.5
```
Create a virtual environment (with the name "qaoa_venv" for example) with the following command:
```[sh]
python -m venv qaoa_venv
```
Activate your environment. The name of the environment will show as "(name)" to the left of your terminal line if entered successfully. Then install the recommended python packages with the PIP package manager:
```[sh]
source qaoa_venv/bin/activate

(qaoa_venv) pip install -r requirements.txt
```
With all packages installed correctly, simply run the following to reproduce the results discussed in the chapter:
```[sh]
(qaoa_venv) python qaoa.py
```

## Contributors
- Jonas Stein LMU Munich, Germany, jonas.stein@ifi.lmu.de
- Maximilian Zorn, LMU Munich, Germany, maximilian.zorn@ifi.lmu.de
- Leo Sünkel, LMU Munich, Germany, leo.suenkel@ifi.lmu.de
- Thomas Gabor, LMU Munich, Germany, thomas.gabor@ifi.lmu.de

## Other References

- [1] https://pennylane.ai/
- [2] https://networkx.org/

