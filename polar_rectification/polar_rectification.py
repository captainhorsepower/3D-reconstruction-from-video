#%%
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def find_matches(img1, img2):
    # surf (fast) keypoints detector
    detector = cv.xfeatures2d.SURF_create(
        hessianThreshold=100,
        nOctaves=2,
        nOctaveLayers=1,
        extended=False,
        upright=True
    )

    # from py_matcher.markdown. Need to find more about algorithm indecies.
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary

    # keypoints matcher
    matcher = cv.FlannBasedMatcher(index_params,search_params)
    
    kp1, des1 = detector.detectAndCompute(img1, None)
    kp2, des2 = detector.detectAndCompute(img2, None)

    matches = matcher.knnMatch(des1,des2,k=2)

    def only_good_matches():
        for (m, n) in matches:
            if m.distance < 0.7*n.distance:
                yield (m, n)
            
    return list(only_good_matches())

    # with this can dray keypoints to verify it works.
    # # Need only good matches, so create a mask
    # matchesMask = [[0,0] for i in range(len(matches))]

    # # ratio test as per Lowe's paper
    # for i,(m,n) in enumerate(matches):
    #     if m.distance < 0.7*n.distance:
    #         matchesMask[i]=[1,0]
    # draw_params = dict(matchColor = (0,255,0),
    #                 singlePointColor = (255,0,0),
    #                 matchesMask = matchesMask,
    #                 flags = cv.DrawMatchesFlags_DEFAULT)

    # img3 = cv.drawMatchesKnn(
    #     images[0],kp1,images[1],
    #     kp2,matches,
    #     None,**draw_params)

    # plt.imshow(img3)
    # plt.show()


#%%
# cameraMatrix: {
#  +721.537700       +0.000000     +609.559300
#    +0.000000     +721.537700     +172.854000
#    +0.000000       +0.000000       +1.000000
# }
camera_matrix = np.array([
    [721.5377, 0.0, 609.559300],
    [0, 721.5377, 172.654],
    [0, 0, 1.0]
])

images = [cv.imread(img) for img in ['input0.png', 'input1.png']]
# %%

good_matches = find_matches(*images)
len(good_matches)

# %%
cv.remap?
# %%
