# CAMPY
This repository will house a simple python script to generate the nonlinear matter power spectrum for a given cosmology using the CAMB python package.

## Dependencies
The following python packages are required
* numpy
* camb
* pyyaml
* astropy

## Usage
The program uses parameters entered into a YAML file to set the cosmology for the power spectrum calculation, as well as set the output file name. See the included parameters.yaml file for an example (or just modify that file to use the values that you want). The program is then run by entering the following command on a Linux system:

```
$ python campy.py parameters.yaml
```

You can create different parameter files for generating different power spectra. Keeping those files around is a good way to keep track of the cosmological parameters used to create a particular power spectrum. To use a different parameter file, simply replace parameters.yaml in the above command with the name of the parameter file you want to use.
