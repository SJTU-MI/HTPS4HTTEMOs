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
- 1_lowvar: Screening features through variance.
- 2_corfilter: Screening features through correlation coefficient.

**3_featurecreation_bySR**: Feature creation process by symbolic regression (SR).
- 1_PC: Feature creation based on Pearson correlation (PC).
- 2_SC: Feature creation based on Spearman correlation (SC).
- 3_DC: Feature creation based on Distance correlation (DC).

**4_PFmodel**: PF prediction model training.
- 1_XG: XGBoost model training.
- 2_RF: Random Forest model training.
- 3_MLP: Multi-Layer Perceptron model training.

**5_SHAPanalysis**: SHAP analysis for the PF prediction model.

**6_meltingpointAPI**: API for the [melting point prediction model](https://www.pnas.org/doi/10.1073/pnas.2209630119).
- 1_prepare4API: Prepare the API json file from MP database for melting point prediction.
- 2_meltingpoint_predict:
- 3_meltingpoint_result: 

**7_HTP_virtualscreening**: 
- 1_lowvar: 
- 2_corfilter: 

**8_TE_results**: 
- 1_lowvar: 
- 2_corfilter: 

## Authors

| **AUTHORS** |Shengluo Ma, Shenghong Ju            |
|:-------------:|--------------------------------------------------|
| **VERSION** | V1.0 / November,2023                               |
| **EMAILS**  | shenghong.ju@sjtu.edu.cn                         |
| **GROUP HOME**  | https://ju.sjtu.edu.cn/en/                         |

## Attribution
This work is under BSD-2-Clause License. Please, acknowledge use of this work with the appropiate citation to the repository and research article.
