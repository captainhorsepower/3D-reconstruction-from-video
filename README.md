# 3D reconstruction from video

Input:

- кадры видео
- camera motion data (с датчиков, либо восстановленная по видео)

Output

- восстановленная 3D сцена. В идеале -- файл, открываемый в каком-либо 3D viewer-е.


## WIP:

- [ ] camera calibration

- [ ] pose estimation (from AR framework)

- polar calibration, which includes:
    - [ ] find fundamental matrix
    - [ ] find epiploes
    - [ ] common region
    - [ ] forward and backward mappings (remaps)

- [ ] find disparities

- [ ] reconstruct 3D (triangulation or 'low res' depth map)


## Hot links:

- polar rectification [paper](https://people.inf.ethz.ch/pomarc/pubs/PollefeysICCV99.pdf)

- learn [SURF theory](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html)

- opencv [geometric transformations](https://docs.opencv.org/3.4/da/d54/group__imgproc__transform.html)

# References

- [PDF] Depth from Motion for Smartphone AR
- [PDF] DTAM: Dense Tracking and Mapping in Real-Time
- [PDF] Joint Projection Filling method for occlusion handling in Depth-Image-Based Rendering
- [ARCore, Android] https://developers.google.com/ar/discover/concepts
- [ARKit, iOS] https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration

## Hmmmm

- [ARCore Depth Lab](https://github.com/googlesamples/arcore-depth-lab)
    - [and a PDF](https://augmentedperception.github.io/depthlab/assets/Du_DepthLab-Real-Time3DInteractionWithDepthMapsForMobileAugmentedReality_UIST2020.pdf)