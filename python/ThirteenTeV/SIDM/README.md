Self-Interacting Dark Matter (SIDM) signal production
-----------------------------------------------------

> This is for 2018 production, taking randomized parameter points per lumi section approach.

To generate all signal points, do
```bash
python createPoints.py # this will create a `scanning_points.json` JSON to be loaded by the fragment
```

To create a CMSSW config from a fragment, do
```bash
cmsDriver.py SIDM_Scan_2018_TuneCP5_13TeV_pythia8_cff.py \
    --fileout file:SIDM_GENSIM.root \
    --mc -s GEN,SIM --era Run2_2018 --nThreads 4 \
    --conditions auto:phase1_2018_realistic \
    --beamspot Realistic25ns13TeVEarly2018Collision \
    --datatier GEN-SIM --eventcontent RAWSIM -n 10 --no_exec --python_filename SIDM_GENSIM_r_cfg.py \
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    --customise_command "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"
```

---

For SIDM model, 3 parameters are tuned:
- mass of DM bound states (`mXX`)
- mass of dark photon (self-interacting mediator, `mA`)
- `ctau` of dark photon (related with kinetic mixing parameter)

the mass points are set in madgraph gridpacks, ctau is set in pythia settings.

All scanned parameter points are summarized in the table below:

| mXX [GeV] | mA [GeV] | ctau [mm]                                             |
|-----------|----------|-------------------------------------------------------|
| 100       | 0.25     | 2.000e-02, 2.000e-01, 2.000e+00, 1.000e+01, 2.000e+01 |
| 100       | 1.2      | 9.600e-02, 9.600e-01, 9.600e+00, 4.800e+01, 9.600e+01 |
| 100       | 5        | 4.000e-01, 4.000e+00, 4.000e+01, 2.000e+02, 4.000e+02 |
|           |          |                                                       |
| 150       | 0.25     | 1.333e-02, 1.333e-01, 1.333e+00, 6.667e+00, 1.333e+01 |
| 150       | 1.2      | 6.400e-02, 6.400e-01, 6.400e+00, 3.200e+01, 6.400e+01 |
| 150       | 5        | 2.667e-01, 2.667e+00, 2.667e+01, 1.333e+02, 2.667e+02 |
|           |          |                                                       |
| 200       | 0.25     | 1.000e-02, 1.000e-01, 1.000e+00, 5.000e+00, 1.000e+01 |
| 200       | 1.2      | 4.800e-02, 4.800e-01, 4.800e+00, 2.400e+01, 4.800e+01 |
| 200       | 5        | 2.000e-01, 2.000e+00, 2.000e+01, 1.000e+02, 2.000e+02 |
|           |          |                                                       |
| 500       | 0.25     | 4.000e-03, 4.000e-02, 4.000e-01, 2.000e+00, 4.000e+00 |
| 500       | 1.2      | 1.920e-02, 1.920e-01, 1.920e+00, 9.600e+00, 1.920e+01 |
| 500       | 5        | 8.000e-02, 8.000e-01, 8.000e+00, 4.000e+01, 8.000e+01 |
|           |          |                                                       |
| 800       | 0.25     | 2.500e-03, 2.500e-02, 2.500e-01, 1.250e+00, 2.500e+00 |
| 800       | 1.2      | 1.200e-02, 1.200e-01, 1.200e+00, 6.000e+00, 1.200e+01 |
| 800       | 5        | 5.000e-02, 5.000e-01, 5.000e+00, 2.500e+01, 5.000e+01 |
|           |          |                                                       |
| 1000      | 0.25     | 2.000e-03, 2.000e-02, 2.000e-01, 1.000e+00, 2.000e+00 |
| 1000      | 1.2      | 9.600e-03, 9.600e-02, 9.600e-01, 4.800e+00, 9.600e+00 |
| 1000      | 5        | 4.000e-02, 4.000e-01, 4.000e+00, 2.000e+01, 4.000e+01 |


ctaus are set such that the mean lxy of dark photon after boost are around **[0.3, 3, 30, 150, 300] cm**.

Assume the conversion factor from l3d to lxy is 0.8, then target l3d = lxy/0.8.

boost_factor ~ mXX/2/mA;

*with* ctau * boost_factor = l3d,

ctau[mm] ~ lxy[cm] / 0.8 * 10 * 2 * mA / mXX

