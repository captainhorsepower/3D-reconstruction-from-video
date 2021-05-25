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

- [PDF] [Polar Rectificaiton](https://people.inf.ethz.ch/pomarc/pubs/PollefeysICCV99.pdf)

## Hmmmm

- [ARCore Depth Lab](https://github.com/googlesamples/arcore-depth-lab)
    - [and a PDF](https://augmentedperception.github.io/depthlab/assets/Du_DepthLab-Real-Time3DInteractionWithDepthMapsForMobileAugmentedReality_UIST2020.pdf)

- ICP: [jupyter notebook](https://nbviewer.jupyter.org/github/niosus/notebooks/blob/master/icp.ipynb), [2](https://arxiv.org/pdf/2007.07627.pdf), [source](https://www.cs.bu.edu/groups/ivc/exam/papers/besl.pdf)

- AR Cam stuff: [1](https://stackoverflow.com/questions/46131762/arkit-why-is-the-cameras-viewmatrix-position-changing-when-the-device-is-rota),

- opencv [1](https://stackoverflow.com/questions/18052337/how-to-verify-that-the-camera-calibration-is-correct-or-how-to-estimate-the-er), [2](https://stackoverflow.com/questions/33068051/how-alignregister-and-merge-point-clouds-to-get-full-3d-model), [3](https://docs.opencv.org/master/d3/d14/tutorial_ximgproc_disparity_filtering.html)

- [stereo matching algs](https://vision.middlebury.edu/stereo/taxonomy-IJCV.pdf), [SGBM tuner](https://github.com/SebastinSanty/SGBMTuner), [SGM paper](https://core.ac.uk/download/pdf/11134866.pdf)

```
В компьютерном зрении диспаратность часто рассматривается как синоним обратной глубины. Совсем недавно несколько исследователей определили диспаратность как трехмерное проекционное преобразование (коллинеацию или гомографию) трехмерного пространства (X, Y, Z). Перечисление всех возможных совпадений в таком обобщенном пространстве диспаратности может быть легко достигнуто с помощью алгоритма развертки плоскости [30, 113], который для каждого значения диспаратности d проецирует все изображения на общую плоскость с использованием перспективной проекции (гомографии).
```

- https://blog.markdaws.net/arkit-by-example-part-4-realism-lighting-pbr-b9a0bedb013e

- https://www.researchgate.net/post/How_to_properly_shift_one_view_to_match_the_other_with_known_disparity

- https://stackoverflow.com/questions/63661474/how-can-i-encode-an-array-of-simd-float4x4-elements-in-swift-convert-simd-float

- https://stackoverflow.com/questions/25452402/opencv-projection-matrices-from-fundamental-matrix-and-solvepnpransac-are-total

- https://stackoverflow.com/questions/45437037/arkit-what-do-the-different-columns-in-transform-matrix-represent

- https://medium.com/macoclock/augmented-reality-911-transform-matrix-4x4-af91a9718246

- https://stackoverflow.com/questions/47536580/get-camera-field-of-view-in-ios-11-arkit

- https://www.digitalbridge.com/blog/can-we-use-stereo-vision-with-arkit-to-estimate-floor-plans

- https://stackoverflow.com/questions/23275877/opencv-get-perspective-matrix-from-translation-rotation

- https://math.stackexchange.com/questions/336/why-are-3d-transformation-matrices-4-times-4-instead-of-3-times-3
- https://blender.stackexchange.com/questions/197447/what-is-the-meaning-of-4x4-projection-matrix

- https://cmsc426.github.io/sfm/

