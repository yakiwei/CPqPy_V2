# CPqPy_V2
A fully Python-based, modular and reproducible framework for reactive transport modeling in Soil and Groundwater 

CPqPy_V2: Coupled COMSOL-PHREEQC in Python
CPqPy_V2 is a modular, reproducible Python-based framework designed for fully coupled reactive transport modeling (RTM) in soil and groundwater systems.

By integrating the multiphysics capabilities of COMSOL with the geochemical precision of PHREEQC, this framework allows for automated, bidirectional data exchange at each time-step. Unlike its predecessor, CPqPy_V2 is entirely independent of the MATLAB environment, offering a more accessible and streamlined workflow for the scientific community.

🚀 Key Features
Python-Native: Complete independence from MATLAB, improving portability and reducing licensing hurdles.

Modular Architecture: Functional components are decoupled, allowing users to easily swap or extend geochemical modules or physical solvers.

Bidirectional Coupling: Seamless data exchange between COMSOL (physics/transport) and PHREEQC (chemistry) at the time-step scale.

Validated Accuracy: Proven numerical consistency against benchmark cases (Cation Exchange and Pesticide Transport).

Reproducible Research: Designed with an emphasis on open-source accessibility and automated workflows.

🛠 Architecture
The framework is built on a modular design to ensure that the physical simulation and chemical reaction components can be maintained and updated independently.

Transport Engine: Handles spatial discretization and fluid flow (COMSOL Multiphysics).

Chemical Engine: Manages complex aqueous speciation and mineral kinetics (PHREEQC).

Interface Layer: Python-based automation that synchronizes time-stepping and data mapping.

📋 Prerequisites
To run CPqPy_V2, you will need:

Python 3.8+

COMSOL Multiphysics (with MPH interface/API enabled)

IPhreeqc (via phreeqpy or the IPhreeqc shared library)

Required Python packages: numpy, pandas, Mph (for COMSOL-Python bridging)

Proposed by Yaqiang Wei in 2026 Contact: yakiwei@yahoo.com
