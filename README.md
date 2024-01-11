# HTPS4HTTEMOs
High-Throughput Screening for High-Temperature Thermoelectric Metal Oxides (HTPS4HTTEMOs)
## Description
In this work, we propose a screening framework combining interpretable machine learning with high-throughput calculations to identify a range of metal oxides that exhibit both high-temperature tolerance and high power factors. Aiming at the problem of weak generalization ability of small data with power factors and the challenge of model interpretation, we employ symbolic regression for feature creation. This approach enhances the robustness of the model while preserving the physical meaning of features, outperforming traditional combinations of descriptors. Next, we combine melting point prediction and power factor intersection screening to extract 33 candidate metal oxides for high-temperature thermoelectric applications from a pool of 48,694 compounds in the Materials Project database. Lastly, we apply the Boltzmann transport theory to perform DFT calculations on the electrical transport properties at 1000K. The relaxation time is approximated by employing constant electron-phonon coupling based on the deformation potential theory. Considering band degeneracy, the electron group velocity is obtained using the momentum matrix element method, yielding 28 materials with power factors greater than 50 μWcm<sup>-1</sup>K<sup>-2</sup>. 
## Installation
### Files loading:
To download, clone this repository:<br>
````
git clone https://github.com/SJTU-MI/HTPS4HTTEMOs.git
````


## Authors

| **AUTHORS** |Shengluo Ma, Shenghong Ju            |
|:-------------:|--------------------------------------------------|
| **VERSION** | V1.0 / November,2023                               |
| **EMAILS**  | shenghong.ju@sjtu.edu.cn                         |
| **GROUP HOME**  | https://ju.sjtu.edu.cn/en/                         |

## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.
