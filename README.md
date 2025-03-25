# An Artificial Intelligence Model for Nuclear Grading of Clear Cell Renal Cell Carcinoma Using Whole Slide Images: A Retrospective Multicentre Study	
# Pre-requisites:
* Python (3.8.13)
* h5py (3.6.0)
* openslide (version 3.4.1)
* opencv (version 4.5.5)
* pillow (version 6.2.1)
* Pytorch (version 1.12.1)
* scikit-learn (version 1.0.2)
* matplotlib (version 3.5.2)
* seaborn (version 0.11.2)

# Abstract
The pathological assessment of International Society of Urological Pathology (ISUP) nuclear grading is crucial for the management of clear cell renal cell carcinoma (ccRCC). The study aimed to develop an artificial intelligence (AI)-based, high-efficiency, and high-accuracy ccRCC ISUP Grading Diagnostic System (RIGDAS) and evaluate its clinical application value. A total of 5,697 slides from 1,807 ccRCC patients were collected and digitized for training and validating RIGDAS. Across the training and validation datasets, RIGDAS achieved an AUC ranging from 0.943 (95% CI, 0.927–0.971) to 0.980 (0.960–1.989). In the human-AI comparison and collaboration study, RIGDAS achieved an 0.930 accuracy that was 3.3-4.3% higher than the accuracy of two junior pathologists (0.897, P = 0.004; 0.887, P = 0.001) and was comparable to the accuracy of two senior pathologists (0.960 and 0.970, both P > 0.05). Furthermore, RIGDAS significantly improved the diagnostic accuracy of the two junior pathologists to the level of the senior pathologists and greatly reduced the slide review time for all four pathologists by 20.5-45.1%. RIGDAS demonstrated decent ability in diagnosing ISUP nuclear grading in ccRCC, reducing the likelihood of misdiagnosis by pathologists, and decreasing the time required for pathological slide review, highlighting its potential for clinical application.

![Fig2](https://github.com/zqy396/RIGDAS/blob/main/Fig/Fig2.jpg)

# Data prepare
The first step is to prepare training dataset. The WSI data should be first segmented to several patches (ROI in ROAM, size is 2048×2048). Patches are then cropped from each ROI and put into pre-trained model to extract features. All the features of patches within a WSI form a bag for training.

WSI data and corresponding detailed information (.csv file) shoule be ready. The format of digitized whole slide image data should be standard formats (.svs,.tiff etc.) that can be read with openslide (version 3.4.1).

# 1.WSI segmentation and patching
The first step is to segment the tissue and crop patches from the tissue region. We referenced CLAM's WSI processing method. CLAM provide a robust WSI segmentation and patching implementation. You can refer to CLAM for more detailed information.

```python create_patches_fp.py --source DATA_DIRECTORY --datainfo DATA_INFO_DIRECTORY --patch_size 4096 --step_size 4096 --save_dir PATCH_DIRECTORY --patch_level 0 --seg --stitch --patch```

# 2.Patch feature extraction
For each ROI (patch with size of 2048×2048), you need extract features of patches (usually 256×256) within each ROI at three distinct magnification levels (20x,10x,5x). Then the fearures can be put into the ROAM model for training.

Run the following commond in ./data_prepare/ directory for feature extraction:

```python extract_feature_patch.py --data_h5_dir PATCH_DIRECTORY --data_slide_dir DATA_DIRECTORY --csv_path DATA_INFO_DIRECTORY --feat_dir FEAT_DIRECTORY --pretrained_model ImageNet --is_stain_norm```


# 3.Generate splits
RIGDAS employs a 5-fold cross validation on the training dataset, followed by testing the ensemble of the 5 trained models on the test dataset. The format of splits data is .npy file. The file contains the training and validation set splits for each fold.

We provide examples of splits in ./data_prepare/data_split/ and reference code in ./data_prepare/create_splits.ipynb.

# 4.Training RIGDAS model

```python main.py configs/ccRCC.ini s1 exp_code```

# 5.Test

```python main.py configs/ccRCC.ini s1``` 

# 6.Visualization

Run the following commond to generate roi-level visualization resutls:

```python gen_visheatmaps_roi_batch.py visheatmaps/roi_vis/configs/ccRCC.ini s1```

![Fig2](https://github.com/zqy396/RIGDAS/blob/main/Fig/Fig4.jpg)


