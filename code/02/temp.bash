mrconvert temp_AP_dwi.nii.gz temp_dwi.mif -fslgrad temp_AP.bvec temp_AP.bval
mrinfo temp_dwi.mif
mrinfo -size temp_dwi.mif | awk '{print $4}'
awk '{print NF; exit}' temp_AP.bvec
awk '{print NF; exit}' temp_AP.bval
mrview temp_dwi.mif
dwidenoise temp_dwi.mif temp_den.mif -noise noise.mif

mrcalc temp_dwi.mif temp_den.mif -subtract residual.mif

mrview residual.mif

dwidenoise temp_dwi.mif temp_dwi_denoised_7extent.mif -extent 7 -noise noise_7extent.mif

mrcalc temp_dwi.mif temp_dwi_denoised_7extent.mif -subtract residual_7extent.mif

mrview residual_7extent.mif


mrdegibbs temp_den.mif temp_den_unr.mif

mrconvert temp_AP_dwi.nii.gz PA.mif
mrconvert PA.mif -fslgrad temp_AP.bvec temp_AP.bval - | mrmath - mean mean_b0_PA.mif -axis 3

dwiextract temp_den.mif - -bzero | mrmath - mean mean_b0_AP.mif -axis 3
mrcat mean_b0_AP.mif mean_b0_PA.mif -axis 3 b0_pair.mif

dwifslpreproc temp_den.mif temp_den_preproc.mif -nocleanup -pe_dir AP -rpe_pair -se_epi b0_pair.mif -eddy_options " --slm=linear --data_is_shelled"

mrview sub-02_den_preproc.mif -overlay.load sub-02_dwi.mif