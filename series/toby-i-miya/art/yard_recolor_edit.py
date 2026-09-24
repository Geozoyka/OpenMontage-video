import numpy as np, cv2
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
import math

src = np.array(Image.open('../../images/22.jpg').convert('RGB')).astype(np.float32)/255
H,W,_ = src.shape
hsv = cv2.cvtColor(src, cv2.COLOR_RGB2HSV)  # H in [0,360], S,V in [0,1]
h,s,v = hsv[...,0],hsv[...,1],hsv[...,2]

yy,xx = np.mgrid[0:H,0:W]
wood = (h>=16)&(h<=36)&(s>0.25)

region = np.zeros((H,W),bool)
region |= (yy>=392)&(yy<=548)&(xx<=1145)
region &= ~((xx>=1085)&(yy>=500)&(xx<=1145))
region |= (yy>=392)&(yy<=632)&(xx>=40)&(xx<=350)   # doghouse
region &= ~((xx>=832)&(xx<=870)&(yy<=470))         # rope

# trunk: connected light area containing seed, bounded by dark outlines
light = (v>0.55)&wood
lab,_ = ndi.label(light)
trunk_ids = {lab[450,740], lab[500,730], lab[380,735]} - {0}
trunk = np.isin(lab, list(trunk_ids))
trunk = ndi.binary_fill_holes(trunk)
trunk_zone = ndi.binary_dilation(trunk, iterations=5)
region &= ~trunk_zone

mask = wood & region
mask = ndi.binary_closing(mask, iterations=1) & region & (s>0.15)

nh = np.where(mask, 204.0, h)
ns = np.where(mask, np.clip(s*0.36,0,0.32), s)
nv = np.where(mask, v*0.94, v)
out = cv2.cvtColor(np.dstack([nh,ns,nv]).astype(np.float32), cv2.COLOR_HSV2RGB)
out8 = (np.clip(out,0,1)*255).astype(np.uint8)

# move doormat: inpaint old spot
mat_box = (1026,598,1192,668)
mat = Image.fromarray((src*255).astype(np.uint8)).crop(mat_box)
mm = np.zeros((H,W),np.uint8)
poly = np.array([[1030,604],[1146,600],[1190,660],[1060,668],[1026,640]],np.int32)
cv2.fillPoly(mm,[poly],255)
mm = cv2.dilate(mm, np.ones((9,9),np.uint8))
out8 = cv2.inpaint(out8, mm, 9, cv2.INPAINT_TELEA)

img = Image.fromarray(out8)
matp = mat.resize((122,22), Image.LANCZOS)
img.paste(matp,(1136,566))

# sun, supersampled
S=4; cx,cy,r = 400,95,44
layer = Image.new('RGBA',(W*S,H*S),(0,0,0,0)); d=ImageDraw.Draw(layer)
for i in range(12):
    a = math.radians(i*30+15)
    x1,y1 = cx+(r+12)*math.cos(a), cy+(r+12)*math.sin(a)
    x2,y2 = cx+(r+30)*math.cos(a), cy+(r+30)*math.sin(a)
    d.line([(x1*S,y1*S),(x2*S,y2*S)], fill=(232,160,58,255), width=11*S)
    d.line([(x1*S,y1*S),(x2*S,y2*S)], fill=(255,207,88,255), width=6*S)
d.ellipse([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S], fill=(232,160,58,255))
r2=r-3
d.ellipse([(cx-r2)*S,(cy-r2)*S,(cx+r2)*S,(cy+r2)*S], fill=(255,210,90,255))
layer = layer.resize((W,H), Image.LANCZOS)
img = Image.alpha_composite(img.convert('RGBA'), layer).convert('RGB')
img.save('yard_v3.png')
Image.fromarray((mask*255).astype(np.uint8)).save('mask.png')
print('done', mask.sum())
