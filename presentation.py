#!python3
import cv2 as cv
import numpy as np
import json
from dataclasses import dataclass

@dataclass(frozen=True)
class FrameMeta:
    # 3x3 camera matrix
    intrinsics: np.ndarray


    @staticmethod
    def fromJson(meta: dict):
        getArray = lambda name: np.array(meta[name]).T
        return FrameMeta(
            intrinsics=getArray('intrinsics'),
        )

def estimateFundamentalMat(intrinsics, img0, img1):
    return cv.diptools.estimate_fundamental_matrix(intrinsics, img0, img1)


def remap(src, map):
        return cv.remap(src, map, None, cv.INTER_LINEAR,\
            borderMode=cv.BORDER_TRANSPARENT)

def computeRectification(F, img0, img1):
    img_size = img0.shape[1::-1]
    
    pr = cv.diptools.PolarRectification_create(F, img_size) 
    pr.compute()

    # may need to swam img0, img1 = img1, img0
    return pr, img0, img1

def main():
    recording = 'test-data/forward'
    frames = (10, 20)
    
    img0, img1 = [cv.imread(f'{recording}/{f}.png') for f in frames]

    with open(f'{recording}/{frames[0]}.json') as f:
        meta0 = FrameMeta.fromJson(json.load(f))
        cameraMatrix = meta0.intrinsics
    
    F = estimateFundamentalMat(cameraMatrix, img0, img1)
    
    pr, img0, img1 = computeRectification(F, img0, img1)

    polar0 = remap(img0, pr.forward_map(0))
    polar1 = remap(img1, pr.forward_map(1))

    cv.imshow('polar0', polar0)
    cv.imshow('polar1', polar1)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()