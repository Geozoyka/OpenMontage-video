import numpy as np, cv2
from PIL import Image
im = cv2.cvtColor(cv2.imread('../images/23.jpg'), cv2.COLOR_BGR2RGB).astype(np.float32)
centers = {'smile':(259,211),'joy':(687,209),'worried':(1117,209),'sad':(259,577),'sleepy':(691,574),'wink':(1115,577)}
R = 168
for name,(cx,cy) in centers.items():
    crop = im[cy-R:cy+R, cx-R:cx+R].copy()
    if name=='sad':  # cloud sticks out lower-left; widen crop
        pass
    h,w,_ = crop.shape
    mn = crop.min(axis=2)
    # background: near-white connected to border
    near = (mn > 225).astype(np.uint8)
    ff = near.copy(); mask = np.zeros((h+2,w+2),np.uint8)
    bg = np.zeros((h,w),bool)
    for seed in [(0,0),(w-1,0),(0,h-1),(w-1,h-1)]:
        m = np.zeros((h+2,w+2),np.uint8)
        cv2.floodFill(ff.copy(), m, seed, 2, 0, 0, flags=4|(1<<8)|cv2.FLOODFILL_MASK_ONLY)
        bg |= m[1:-1,1:-1].astype(bool)
    # soft alpha in and near the background: colour-to-alpha against white
    a_ctw = np.clip((255 - mn) / 255 * 1.0, 0, 1)
    a_ctw = np.clip(a_ctw*2.2, 0, 1)
    ring = cv2.dilate(bg.astype(np.uint8), np.ones((3,3),np.uint8)).astype(bool)
    alpha = np.ones((h,w),np.float32)
    alpha[ring] = a_ctw[ring]
    # unpremultiply against white
    a3 = np.maximum(alpha[...,None],1e-3)
    rgb = np.clip((crop - 255*(1-a3))/a3, 0, 255)
    out = np.dstack([rgb, alpha*255]).astype(np.uint8)
    Image.fromarray(out,'RGBA').save(f'sun/sun_{name}.png')
print('ok')
