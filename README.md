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

### Package requirements:
Some packages need to be installed on demand, such as [Pymatgen](https://pymatgen.org/), [Xenonpy](https://github.com/yoshida-lab/XenonPy), [scikit-learn](https://scikit-learn.org/stable/), [BayesianOptimization](https://github.com/bayesian-optimization/BayesianOptimization).

## Try the desired parts of the project:

### Code in the HTPS4HTTEMOs folder
**1_data4PF**: Power factor (PF) data collection and initial descriptor creation.
- 1_MP_api_features: Descriptors retrieved from the MP database
- 2_Xenonpy_features: Descriptors retrieved from Xenonpy
- 3_data4PF: The PF data and initial descriptor.

**2_featurefiltering**: Feature down-selection process.
- 1_lowvar: Descriptors retrieved from the MP database
- 2_corfilter: Descriptors retrieved from Xenonpy

**3_featurecreation_bySR**: Power factor (PF) data collection and initial descriptor creation.
- 1_PC: Descriptors retrieved from the MP database
- 2_SC: Descriptors retrieved from Xenonpy
- 3_DC: Descriptors retrieved from Xenonpy

**4_PFmodel**: Power factor (PF) data collection and initial descriptor creation.
- 1_XG: Descriptors retrieved from the MP database
- 2_RF: Descriptors retrieved from Xenonpy
- 3_MLP: Descriptors retrieved from Xenonpy

**5_SHAPanalysis**: Power factor (PF) data collection and initial descriptor creation.

**6_meltingpointAPI**: Power factor (PF) data collection and initial descriptor creation.
- 1_lowvar: Descriptors retrieved from the MP database
- 2_corfilter: Descriptors retrieved from Xenonpy

**7_HTP_virtualscreening**: Power factor (PF) data collection and initial descriptor creation.
- 1_lowvar: Descriptors retrieved from the MP database
- 2_corfilter: Descriptors retrieved from Xenonpy

**8_TE_results**: Power factor (PF) data collection and initial descriptor creation.
- 1_lowvar: Descriptors retrieved from the MP database
- 2_corfilter: Descriptors retrieved from Xenonpy

## Authors

| **AUTHORS** |Shengluo Ma, Shenghong Ju            |
|:-------------:|--------------------------------------------------|
| **VERSION** | V1.0 / November,2023                               |
| **EMAILS**  | shenghong.ju@sjtu.edu.cn                         |
| **GROUP HOME**  | https://ju.sjtu.edu.cn/en/                         |

## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.
