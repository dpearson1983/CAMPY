import sys, platform, os
import numpy as np
import camb
from camb import model, initialpower
from yaml import load, dump
from astropy.io import ascii

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
    

parFile = file(sys.argv[1])
inputPars = load(parFile, Loader=Loader)
pars = camb.CAMBparams()
pars.set_cosmology(H0=inputPars['H_0'], ombh2=inputPars['Omega_bh2'], omch2=inputPars['Omega_ch2'],
                   omk=inputPars['Omega_k'], tau=inputPars['tau'])

results = camb.get_results(pars)

pars.set_dark_energy()
pars.set_matter_power(redshifts=[inputPars['z']], kmax=inputPars['k_max'])
pars.InitPower.set_params(ns=inputPars['n_s'])
pars.NonLinear = model.NonLinear_both
results.calc_power_spectra(pars)
kh, z, pk = results.get_matter_power_spectrum(minkh=inputPars['k_min'], maxkh=inputPars['k_max'], 
                                              npoints=inputPars['num_points'])

ascii.write([kh, pk[0]], inputPars['outFile'], names=['kh', 'P(k)'], overwrite=True)
