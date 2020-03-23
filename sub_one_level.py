#!/usr/bin/env python3
# notes
# w is on a z-grid called ZLd000003 rather than Zmd00003; so filtering will not work directly.


import filtering
from datetime import timedelta
import numpy as np
import scipy.signal as signal
import sys
#import matplotlib.pyplot as plt
#from netCDF4 import Dataset
i=int(sys.argv[1])
ti=int(sys.argv[2])

#print( i )


ncfile_name='/scratch/v45/cjs157/gadi_short/cjs157/mitgcm/archive/SOMs_hr1_200m_2020_Goff_v2/output00*/zlevels_hourly*.nc'
ncfile_namew='/scratch/v45/cjs157/gadi_short/cjs157/mitgcm/archive/SOMs_hr1_200m_2020_Goff_v2/output00*/wvel_hourly*.nc'
#for i in range(0,200):
ncfile_out=('out_z%03i_t%03i' % (i , ti) )

filenames = {
        "U": ncfile_name, 
            "V": ncfile_name,
          "P": ncfile_name,
          "W": ncfile_namew,
            "RHO": ncfile_name
    }   
variables = {"U": "UVEL", "V": "VVEL", "P": "PHIHYD", "RHO": "RHOAnoma","W": "UDIAG1"}
dimensions = {"lon": "X", "lat": "Y", "time": "T", "depth": "Zmd000200"}
indices = {"depth": [i]}


ff = filtering.LagrangeFilter(
	ncfile_out, filenames, variables, dimensions,
	sample_variables=["U","V","P","RHO","W"], mesh="flat",
	window_size=timedelta(days=2).total_seconds(),
        indices=indices,
    highpass_frequency=1.2060e-4
)

# turn off the advection (Eulerian)
#ff.kernel = ff.sample_kernel
#ff._compile(ff.kernel)

ff.seed_subdomain(min_lon=50000,
        max_lon=200000, min_lat=50000, max_lat=200000)

# time output: in hours from window start
t1=timedelta(days=2).total_seconds()+3600*ti
ff.filter(times=[t1])
#ff.filter()
