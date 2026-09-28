import re
src=open('08-seriya-1-v2.md').read()
blocks=re.split(r'\n(?=\*\*\d+\. )',src)
D={
'T':"Toby is a light cornflower-blue puppy with a white face stripe, navy ears, a white tuft on his head, a few round navy spots and a plain orange bandana.",
'M':"Mia is a pink-peach kitten with a golden tuft on her head and a pink collar with a heart-shaped golden bell.",
'MD':"Toby's mother is a grown-up dog about one and a half times taller than Toby, a deeper denim blue, with long silky ears and a dusty rose knitted shawl.",
'MC':"Mia's mother is a grown-up cat about one and a half times taller than Mia, golden apricot, with a cream ruff and a dusty rose collar with a white flower.",
'Б':"The butterfly is the small peach-pink one from the attached reference.",
'S':"The sun character looks exactly like the attached sun reference.",
}
WHO={'T':'Toby','M':'Mia','MD':"Toby's mother",'MC':"Mia's mother",'Б':'one peach-pink butterfly','S':'one sun character'}
RU={'T':'лист Тоби','M':'лист Мии','MD':'лист мамы-собаки','MC':'лист мамы-кошки','S':'лист солнышка','Б':'бабочки',
'Сад':'фон «сад днём»','Ночь':'фон «сад ночью»','Вечер':'фон «сад вечером» (исправленный Claude)','ДС':'фон «собачий домик» (исправленный Claude)','ДК':'фон «кошачий домик»'}
BG={'Сад','Ночь','Вечер','ДС','ДК'}
out=["# Промпты картинок — серия 1\n","Каждый кадр — новый чат в ChatGPT. Загрузить 2 картинки (первой — персонажей, второй — фон), вставить текст целиком, прислать результат Claude.\n","Кадры с ✅ готовы. Кадры с 🆕 — сделать.\n"]
n=0
out.append(open('art/gen_sunsec.md').read())
import re as _r
DONE=set(_r.findall(r'- \[x\] (\d+) ',open('11-chek-list-kadrov.md').read()))
for b in blocks:
    m=re.match(r'\*\*(\d+)\. [^.]*?\d:\d\d(?:–\d:\d\d)?\. ([^*]+?)\*\*',b)
    if not m: continue
    num,title=m.group(1),m.group(2).strip().rstrip('.')
    k=re.search(r'- Кадр: `([^`]+)`',b)
    r=re.search(r'^(\[[^\n]+\])',b,re.M)
    if not k or not r: continue
    refs=re.findall(r'\[([^\]]+)\]',r.group(1).split(' — ')[0])
    chars=[x for x in refs if x not in BG]
    bgs=[x for x in refs if x in BG]
    outdoor=bgs and bgs[0] in ('Сад','Ночь','Вечер')
    desc=' '.join(D[c] for c in chars)
    who=', '.join(WHO[c] for c in chars) if chars else 'none, only the place'
    p=(("The first attached image shows the characters, the second shows the place. " if chars else "")+"Using the attached images as exact references for the characters and the location, keep every character's design, colors, size and accessories identical, in a soft 3D plush animated-film style with fluffy fur and warm gentle light. "
       +(desc+' ' if desc else '')
       +f"The only characters in the picture are: {who}. "
       +("House colors never change: Toby and his mother live in the cottage with the soft blue roof on the left side of the garden; Mia and her mother live in the cottage with the soft pink roof on the right side. Any cottage seen near or behind Toby or his mother has a soft blue roof; any cottage seen near or behind Mia or her mother has a soft pink roof. " if outdoor else "")
       +("The sky shows only what is in the attached location image: its colors, clouds or stars. " if outdoor and 'S' not in chars else '')
       +"One frame of a gentle wordless preschool cartoon, horizontal 16:9, with no text: "+k.group(1))
    COMBO={frozenset(['MD','T']):'склейка 1 «мама-собака и Тоби»',frozenset(['MC','M']):'склейка 2 «мама-кошка и Мия»',frozenset(['MD','MC']):'склейка 3 «две мамы»',frozenset(['T','M']):'склейка 4 «Тоби и Мия»',frozenset(['M','Б']):'склейка 5 «Мия и бабочка»'}
    first=COMBO.get(frozenset(chars)) if len(chars)>1 else (RU[chars[0]] if chars else None)
    up=' + '.join([x for x in [first]+[RU[b] for b in bgs] if x])
    n+=1
    mark=' ✅ готово' if num in DONE else ''
    out.append(f"\n## Кадр {num}. {title}{mark}\n\nЗагрузить: {up}\n\n```\n{p}\n```\n")
open('10-prompty-kartinok-seriya-1.md','w').write(''.join(out))
print(n)
