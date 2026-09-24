import numpy as np, math, imageio
from PIL import Image
yard = Image.open('yard/yard_v5.png').convert('RGB')
orig = Image.open('../images/22.jpg').convert('RGB')
yard.paste(orig.crop((300,0,500,200)),(300,0))   # remove my old sun
yard.save('sun/yard_nosun.png')
names=['smile','joy','worried','sad','sleepy','wink']
suns={n:Image.open(f'sun/sun_{n}.png') for n in names}
CX,CY,SCALE=400,100,0.5
def place(img, sun, scale):
    s=sun.resize((int(sun.width*scale),int(sun.height*scale)),Image.LANCZOS)
    img.alpha_composite(s,(int(CX-s.width/2),int(CY-s.height/2)))
# per-mood grading: (r,g,b multipliers)
grade={'smile':(1,1,1),'joy':(1.05,1.02,0.93),'worried':(0.97,0.99,1.04),'sad':(0.9,0.95,1.08),'sleepy':(1.02,0.93,0.9),'wink':(1.04,1.01,0.95)}
base=np.array(yard).astype(np.float32)
def frame(a,b,t,k):
    g=np.array(grade[a])*(1-t)+np.array(grade[b])*t
    bg=Image.fromarray(np.clip(base*g,0,255).astype(np.uint8)).convert('RGBA')
    breathe=SCALE*(1+0.025*math.sin(k/7))
    la=Image.new('RGBA',bg.size,(0,0,0,0)); place(la,suns[a],breathe)
    lb=Image.new('RGBA',bg.size,(0,0,0,0)); place(lb,suns[b],breathe)
    mix=Image.blend(la,lb,t)
    bg.alpha_composite(mix)
    return np.array(bg.convert('RGB').resize((1376//2*2,768)))
w=imageio.get_writer('sun/sun_moods_demo.mp4',fps=25,codec='libx264',quality=8,macro_block_size=8)
seq=names+['smile']; k=0
for i in range(len(seq)-1):
    for _ in range(45): w.append_data(frame(seq[i],seq[i],0,k)); k+=1
    for j in range(15): w.append_data(frame(seq[i],seq[i+1],(j+1)/15,k)); k+=1
w.close()
Image.fromarray(frame('smile','smile',0,0)).save('sun/yard_with_sun.png')
print('ok',k)
