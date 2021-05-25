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

def computeDisparities(imgL, imgR):
    # disparity range is tuned for 'aloe' image pair
    window_size = 10
    min_disp = 16
    num_disp = 16*20-min_disp
    stereo = cv.StereoSGBM_create(
        minDisparity = min_disp,
        numDisparities = num_disp,
        blockSize = 15,
        P1 = 8*3*window_size**2,
        P2 = 32*3*window_size**2,
        disp12MaxDiff = -1,
        uniquenessRatio = 10,
        speckleWindowSize = 150,
        speckleRange = 2
    )
    

    print('computing disparity...')
    return stereo.compute(imgL, imgR).astype(np.float32) / 16.0, min_disp, num_disp

def write_ply(fn, verts, colors):
    ply_header = '''ply
format ascii 1.0
element vertex %(vert_num)d
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
end_header
'''
    verts = verts.reshape(-1, 3)
    colors = colors.reshape(-1, 3)
    verts = np.hstack([verts, colors])
    with open(fn, 'wb') as f:
        f.write((ply_header % dict(vert_num=len(verts))).encode('utf-8'))
        np.savetxt(f, verts, fmt='%f %f %f %d %d %d ')

def generate_point_cloud(img0, disp):
    size = np.array(img0.shape[1::-1]) // 2
    img0 = cv.resize(img0, size)
    disp = cv.resize(disp, size)

    print('generating 3d point cloud...',)
    h, w = img0.shape[:2]
    f = 0.8*w                          # guess for focal length
    Q = np.float32([[1, 0, 0, -0.5*w],
                    [0,-1, 0,  0.5*h], # turn points 180 deg around x-axis,
                    [0, 0, 0,     -f], # so that y-axis looks up
                    [0, 0, 1,      0]])
    points = cv.reprojectImageTo3D(disp, Q)
    colors = cv.cvtColor(img0, cv.COLOR_BGR2RGB)
    mask = disp > disp.min()
    out_points = points[mask]
    out_colors = colors[mask]
    out_fn = 'out.ply'
    write_ply(out_fn, out_points, out_colors)
    print('%s saved' % out_fn)


def main():
    recording = 'test-data/forward'
    frames = (8, 13)
    
    img0, img1 = [cv.imread(f'{recording}/{f}.png') for f in frames]

    with open(f'{recording}/{frames[0]}.json') as f:
        meta0 = FrameMeta.fromJson(json.load(f))
        cameraMatrix = meta0.intrinsics
    
    F = estimateFundamentalMat(cameraMatrix, img0, img1)
    
    pr, img0, img1 = computeRectification(F, img0, img1)

    polar0 = remap(img0, pr.forward_map(0))
    polar1 = remap(img1, pr.forward_map(1))

    disp, min_disp, num_disp = computeDisparities(polar0, polar1)
    polar_disp = disp
    disp = remap(disp, pr.get_reverse_map(0))

    cv.imshow('polar_disp', (polar_disp-min_disp)/num_disp)
    cv.imshow('disparity', (disp-min_disp)/num_disp)
    cv.imshow('left', img0)
    print('have a look')

    # cv.imwrite('disp/polar.png', polar0)
    # cv.imwrite('disp/polar_disp.png', polar_disp)
    # cv.imwrite('disp/left.png', img0)
    # cv.imwrite('disp/left_disp.png', disp)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()