#!/usr/bin/env python
import json

parampts = [
    (100, 0.25, [2.000e-02, 2.000e-01, 2.000e00, 1.000e01, 2.000e01]),
    (100, 1.2, [9.600e-02, 9.600e-01, 9.600e00, 4.800e01, 9.600e01]),
    (100, 5, [4.000e-01, 4.000e00, 4.000e01, 2.000e02, 4.000e02]),
    (150, 0.25, [1.333e-02, 1.333e-01, 1.333e00, 6.667e00, 1.333e01]),
    (150, 1.2, [6.400e-02, 6.400e-01, 6.400e00, 3.200e01, 6.400e01]),
    (150, 5, [2.667e-01, 2.667e00, 2.667e01, 1.333e02, 2.667e02]),
    (200, 0.25, [1.000e-02, 1.000e-01, 1.000e00, 5.000e00, 1.000e01]),
    (200, 1.2, [4.800e-02, 4.800e-01, 4.800e00, 2.400e01, 4.800e01]),
    (200, 5, [2.000e-01, 2.000e00, 2.000e01, 1.000e02, 2.000e02]),
    (500, 0.25, [4.000e-03, 4.000e-02, 4.000e-01, 2.000e00, 4.000e00]),
    (500, 1.2, [1.920e-02, 1.920e-01, 1.920e00, 9.600e00, 1.920e01]),
    (500, 5, [8.000e-02, 8.000e-01, 8.000e00, 4.000e01, 8.000e01]),
    (800, 0.25, [2.500e-03, 2.500e-02, 2.500e-01, 1.250e00, 2.500e00]),
    (800, 1.2, [1.200e-02, 1.200e-01, 1.200e00, 6.000e00, 1.200e01]),
    (800, 5, [5.000e-02, 5.000e-01, 5.000e00, 2.500e01, 5.000e01]),
    (1000, 0.25, [2.000e-03, 2.000e-02, 2.000e-01, 1.000e00, 2.000e00]),
    (1000, 1.2, [9.600e-03, 9.600e-02, 9.600e-01, 4.800e00, 9.600e00]),
    (1000, 5, [4.000e-02, 4.000e-01, 4.000e00, 2.000e01, 4.000e01]),
]

lxypts = [0.3, 3, 30, 150, 300]

finalstates = ["4Mu", "2Mu2E"]

gridpackloc = "https://wsi.web.cern.ch/wsi/mc/gridpacks/SIDM_XXTo2ATo{0}_mXX-{1}_mA-{2}_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz"
configDescription = "SIDM_XXTo2ATo{0}_mXX-{1}_mA-{2}_ctau-{3}_lxy-{4}"


if __name__ == "__main__":

    points = []

    for fs_ in finalstates:
        for mxx_, ma_, ctaus_ in parampts:

            mxx_ = str(mxx_)
            ma_ = str(ma_).replace(".", "p")
            gridpack = gridpackloc.format(fs_, mxx_, ma_)

            for ctau_, lxy_ in zip(ctaus_, lxypts):

                ctau_s = str(ctau_).replace(".", "p")
                lxy_s = str(lxy_).replace(".", "p")
                description = configDescription.format(fs_, mxx_, ma_, ctau_s, lxy_s)

                points.append(
                    dict(
                        name=description,
                        weight=1.0,
                        gridpack=gridpack,
                        procParam=[
                            "ParticleDecays:tau0Max = 1000.1",
                            "LesHouches:setLifetime = 2",
                            "32:tau0 = {0:g}".format(ctau_),
                        ],
                    )
                )

    with open("scanning_points.json", "w") as f:
        f.write(json.dumps(points, indent=4))

