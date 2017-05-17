# ==================================================================
# IMPORTANT: Make a copy of this file before you insert your values!
# ==================================================================

from __future__ import absolute_import, division, print_function

import os
import sys
#----------------------------------------------------------------------------------------------------


NNFlow_base  =
workdir_base =


#----------------------------------------------------------------------------------------------------
sys.path.append(NNFlow_base)
from preprocessing.preprocessing import merge_data_sets
#----------------------------------------------------------------------------------------------------



### The input data sets have to be provided as a dictionary in the following format:
### input_datasets = {'process_name':'filename'}
input_data_sets =


#----------------------------------------------------------------------------------------------------
path_to_inputfiles = os.path.join(workdir_base, 'HDF5_files')
path_to_merged_data_set = os.path.join(workdir_base, 'HDF5_files/data_set_merged.hdf')


#----------------------------------------------------------------------------------------------------
function_call_dict = {'input_data_sets'              : input_data_sets,
                      'path_to_inputfiles'           : path_to_inputfiles,
                      'path_to_merged_data_set'      : path_to_merged_data_set,
                      }


merge_data_sets(**function_call_dict)
