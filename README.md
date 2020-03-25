# Lagrangian-filtering-batch
A collection of bash and python scripts for batch submission of lagrangian filtering jobs on Gadi Cascade Lake Nodes

# qsub_multi 
is the template submission script to submit 200 zlevels and N times
(N=12 currently), over the requesite number of jobs.
Each job runs on 48 cores, and issues 48 python commands

# submit_all_levels 
will create the PBS submission scripts for each job, based on the template qsub_multi

# sub_one_level.py
Each job calls multiple instances of the core filtering script sub_one_level.py

# qsub_collation
parallel collation script which collates in z for each time (x,y) -> (x,y,z)
Once complete issues qsub qsub_collate_z command to collate all times

# qsub_collate_z
Collates (x,y,z) -> (x,y,z,t) files - output "wave.nc" single file
Slowest part of the process.

# run_concat_all (serial collation - do not recommend)
At the end of the filtering,  all output can be collate with run_concat_all
