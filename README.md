# CPS Co-simulation Optimizations
## Summary
This project aims to integrate multiple simulators from different domains and optimize the interactions required for the co-simulation. We utilize MOSAIK as the co-simulation framework, and NS-3, OpenDSS, and other custom constructs as the simulators to create the sample scenarios. The applications currently being simulated are as follows:
* **Tap-Control:** A smart-grid network simulating a feedback loop to control the voltage of the transformer providing power to the network.
* **DSE:** A distributed state estimator running on a larger smart-grid network.

Our contribution is to modify the created simulators (and wrappers) to improve synchronization and thus greatly reduce execution time of the simulations.

## Instructions
While the original project has been tested on both Ubuntu 18.04 LTS and Ubuntu 20.04 LTS, this project is mostly run on Ubuntu 24.04 LTS. However, it may run on any Ubuntu LTS systems with some minor changes to the installation scripts. The steps to execute the simulation are as follows:

* Clone the repository: `git clone https://github.com/talhaibnaziz/CPSCosim.git`
* Run the installation script: `cd CPSCosim/codes/ && ./install.sh`
* Run the application: `cd SmartGridMain && ./smartgrid_run.sh`

The application selection is done within the code in `simulator_demo.py`. For more details, check the section below.

## Configuration

### Dependencies
* Check the required dependencies from the installation script `install.sh`.
* The NS-3 application (not simulator) configurations are in the make file (`./NS3Mosaik/Makefile`)
* The OpenDSS configurations are in the Python file: `opendssdirect3.7/setup.py`

### `./SmartGridMain/simulator_demo.py` - master simulation file
* To change between `MOSAIK` versions, edit line 25 of this file.
* To change between the two simulated scenarios, edit line 29 of the file.
* To increase or decrease the number of scalable simulators, edit line 32 of the file.

### Network Simulator 3
* The NS-3 modes (debug vs optimized) can be changed in the installation script - some sample configurations are commented out for reference.
* The default is optimized with python disabled. To change, edit the `./waf` lines and run the installation script again.
* The NS-3 filtering modes (the comments above the code detail the modes) can be changed in line 36 of file `./NSMosaik/mosaik_api/NS3Netsim.h`. Once changed, run `make clean && make` from the `NS3Mosiak` folder for the changes to take effect.

## Publication
We are currently in the process of submitting our work to the IEEE Systems Journal. The tex files are located in the "publication" folder. Furthermore, the revisions (from the reviewers) and relevant info are also in the same folder.

# Acknowledgements

**Note:** This project has been forked from the original, even though the goals of this project are different.

The original project aims to simulate smart-grid applications: https://github.com/sustainable-computing/co_sim_platform