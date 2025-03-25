# An Artificial Intelligence Model for Nuclear Grading of Clear Cell Renal Cell Carcinoma Using Whole Slide Images: A Retrospective Multicentre Study	
# Pre-requisites:
Python (3.8.13)
h5py (3.6.0)
openslide (version 3.4.1)
opencv (version 4.5.5)
pillow (version 6.2.1)
Pytorch (version 1.12.1)
scikit-learn (version 1.0.2)
matplotlib (version 3.5.2)
seaborn (version 0.11.2)

# Data prepare
The first step is to prepare training dataset. The WSI data should be first segmented to several patches (ROI in ROAM, size is 2048×2048). Patches are then cropped from each ROI and put into pre-trained model to extract features. All the features of patches within a WSI form a bag for training.

WSI data and corresponding detailed information (.csv file) shoule be ready. The format of digitized whole slide image data should be standard formats (.svs,.tiff etc.) that can be read with openslide (version 3.4.1).

1.WSI segmentation and patching
The first step is to segment the tissue and crop patches from the tissue region. We referenced CLAM's WSI processing method. CLAM provide a robust WSI segmentation and patching implementation. You can refer to CLAM for more detailed information.
* python create_patches_fp.py --source DATA_DIRECTORY --datainfo DATA_INFO_DIRECTORY --patch_size 4096 --step_size 4096 --save_dir PATCH_DIRECTORY --patch_level 0 --seg --stitch --patch
