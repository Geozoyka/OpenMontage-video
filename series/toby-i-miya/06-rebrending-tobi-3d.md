# Ребрендинг: Тоби в объёмном стиле (карточка персонажа)

Решение: весь мир сериала переводится в объёмный пушистый 3D-стиль по образцу, который выбрали вы с женой. Имена остаются: Тоби, Мия, их мамы. Сначала утверждаем Тоби, затем по нему делаем Мию, мам, двор и солнышко.

## Карточка Тоби

**Кто он:** щенок 3–4 месяцев. Быстрый, любопытный, добрый. Сначала делает, потом думает.

**Стиль:** объёмная 3D-анимация для малышей, мягкая и тёплая. Короткая пушистая шерсть, видны мягкие ворсинки. Мягкий рассеянный свет, никаких резких теней.

**Пропорции**
- Голова крупная, почти половина роста, круглая, с пухлыми щеками.
- Тело маленькое, округлое, пухлое.
- Четыре коротких толстых лапы с крупными мягкими подушечками. Всегда стоит на четырёх лапах.
- Хвост короткий, пушистый, загнут вверх.

**Цвета (коды для промптов)**
- Основная шерсть: светло-васильковая голубая, #7FA3E6. Мягкий переход к более светлому на животе, #A9C4F2.
- Белое, #F7FAFF: вся мордочка вокруг носа и рта, полоса от лба к носу, грудка и живот, все четыре лапки («носочки»).
- Уши: висячие, мягкие, тёмно-синие, #3B4E9C.
- Пятна: ровно три тёмно-синих круглых пятна, #3B4E9C, всегда на одних местах: большое на спине, среднее на левом заднем бедре, маленькое на правой передней лапе.
- Кончик хвоста тёмно-синий, #3B4E9C.
- Нос чёрный, блестящий. Язык и румянец нежно-розовые, #F4A9B4.

**Лицо**
- Глаза крупные, блестящие: тёмно-синяя радужка, #2B3F8F, большой зрачок, по два белых блика в каждом глазу.
- Брови — короткие мягкие тёмные дуги.
- Нос чёрный, овальный.
- Рот широкий, улыбчивый, с розовым языком.
- Круглый розовый румянец на щеках.

**Примета:** белый пушистый хохолок на макушке (три пучка шерсти). Он есть на каждом рисунке.

**Аксессуар:** мягкий шарфик солнечно-жёлтого цвета, #F7C33B, с оранжевыми полосками на концах, #F59A3A, завязан свободно. Медальона нет.

**Эмоции:** радость, смех, любопытство (голова набок), удивление, грусть, испуг, сонливость, подмигивание.

**Чего у Тоби быть не должно**
- Медальона с лапкой и любых знаков, похожих на «Щенячий патруль».
- Надписей, логотипа, текста на листе.
- Позы на двух лапах, как у человека.
- Лишних пятен или пятен на других местах.

## Ошибки, которые закрыты в промптах

1. Нейросеть перерисует лист с надписями, как на образце → «страница содержит только щенка на однотонном фоне».
2. Медальон вернётся из образца → прямо сказано заменить ошейник и медальон шарфиком.
3. Пятна «гуляют» → ровно три пятна с постоянным местом.
4. Хохолок пропадёт → примета на каждом рисунке.
5. Шарф сольётся с голубым щенком → солнечно-жёлтый вместо голубого.
6. Щенок встанет на задние лапы → «всегда на четырёх лапах».
7. Разный размер рисунков → «одинаковый размер во всех рисунках».

---

## Промпт А — ChatGPT, с загрузкой вашей картинки (рекомендую)

ChatGPT нарисовал образец, поэтому он лучше всех сохранит понравившийся облик.

```
Use the attached image only as the reference for this puppy's look: his soft 3D plush animation style, fluffy fur, colors, spots, face, eyes and proportions. Create a new, clean character model sheet of the same puppy, named Toby, for a gentle wordless preschool animated series. The page contains only the puppy drawings on a plain very light blue-white background, with no lettering, logo, color swatches, icons or frames. Make these changes: replace the collar and the round medallion with a soft sunny yellow scarf (#F7C33B) with orange stripes at its ends (#F59A3A), tied loosely around his neck; he has exactly three round dark navy spots (#3B4E9C) that always stay in the same places: a large one on his back, a medium one on his left hind thigh and a small one on his right front leg. Keep everything else from the reference: light cornflower blue fur (#7FA3E6), a white muzzle, a white stripe from forehead to nose, a white chest and belly, four white paws, soft floppy dark navy ears (#3B4E9C), a short fluffy tail with a dark navy tip, a shiny black nose, big glossy eyes with dark navy-blue irises and two white highlights each, pink blush on the cheeks, and a fluffy white tuft of fur on top of his head, which appears in every drawing. Toby is a real four-legged puppy and always stands, sits or lies on four paws. Every drawing shows the same puppy at the same size, with identical colors, spots, tuft and scarf. Top row, full body standing on four legs: facing the viewer, three-quarter view facing right, side view facing right, seen from behind. Middle row, head and shoulders: laughing with eyes closed happily, curious with his head tilted, surprised, sad with eyebrows raised in the middle and ears drooping, frightened with wide eyes, sleepy with half-closed eyes. Bottom row, full body: running happily with his ears flying, and lying on his tummy asleep with a small smile. Soft warm diffused light, friendly and calm for toddlers. Wide landscape format.
```

## Промпт Б — без картинки (Krea, Nano Banana и другие)

```
A clean character model sheet for a gentle wordless preschool animated series in soft 3D plush animation style, like a modern feature-animation film for toddlers. The page contains only the puppy drawings on a plain very light blue-white background, with no lettering, logo, color swatches, icons or frames. The character is Toby, a small, round, chubby four-legged puppy about three months old. His head is big and round with chubby cheeks, almost half his total height; his body is small, round and soft; he has four short thick legs with big soft paws and a short fluffy upturned tail; he always stands, sits or lies on four paws. His short fluffy fur shows soft visible fibers. Colors: light cornflower blue fur (#7FA3E6) that gets slightly lighter on the belly (#A9C4F2); pure soft white (#F7FAFF) on the whole muzzle, a stripe from his forehead down to his nose, his chest, his belly and all four paws; soft floppy dark navy ears (#3B4E9C); a dark navy tip on his tail; and exactly three round dark navy spots (#3B4E9C) that always stay in the same places: a large one on his back, a medium one on his left hind thigh and a small one on his right front leg. His face: big glossy eyes with dark navy-blue irises (#2B3F8F), large pupils and two white highlights in each eye; short soft dark eyebrows; a shiny black oval nose; a wide friendly mouth with a pink tongue; round pink blush on his cheeks (#F4A9B4). His signature is a fluffy white tuft of fur on top of his head, which appears in every drawing. He wears a soft sunny yellow scarf (#F7C33B) with orange stripes at its ends (#F59A3A), tied loosely around his neck. Every drawing shows the same puppy at the same size, with identical colors, spots, tuft and scarf. Top row, full body standing on four legs: facing the viewer, three-quarter view facing right, side view facing right, seen from behind. Middle row, head and shoulders: laughing with eyes closed happily, curious with his head tilted, surprised, sad with eyebrows raised in the middle and ears drooping, frightened with wide eyes, sleepy with half-closed eyes. Bottom row, full body: running happily with his ears flying, and lying on his tummy asleep with a small smile. Soft warm diffused light, friendly and calm for toddlers. Horizontal 16:9.
```

## Правки, если что-то проскочило

- Медальон вернулся: `Remove the medallion and keep only the yellow scarf with orange stripes. Keep everything else exactly the same.`
- Надписи: `Remove all text, logos and color swatches. Keep the puppy drawings exactly the same.`
- Пятна не там: `Make the spots match the first drawing exactly: one large navy spot on his back, one medium on his left hind thigh, one small on his right front leg. Keep everything else exactly the same.`

## Итог: Тоби 3D утверждён (art/toby_3d_sheet_v1.jpg)

Правило пятен ослаблено: «несколько тёмно-синих пятен на спине и лапах», места не фиксируются. Тоби узнаётся по ушам, хохолку, белой полосе и жёлтому шарфу.

Необязательная правка яркости:
```
Make the puppy's fur a brighter, cheerful cornflower blue like in a sunny cartoon, and make his white areas clean bright white. In the sad face, raise the inner ends of his eyebrows so he looks sad rather than sleepy. Keep the 3D fur style, the poses, the scarf and everything else exactly the same.
```

## Мия 3D (загрузить лист Тоби 3D)

Ленточка Мии теперь лавандовая: жёлтый остаётся только у Тоби.

```
Use the attached Toby model sheet as the exact reference for the rendering style, fur texture, lighting, background, page layout and character size: a soft 3D CGI animated-film render with fluffy fur, volumetric shading and gentle warm light. Create a matching clean character model sheet for his friend Mia, a small, round, fluffy four-legged kitten about three months old, the same height as Toby. The page contains only the kitten on the same plain very light blue-white background, with no lettering, logo, color swatches, icons or frames. Mia has a big round head with chubby cheeks, a small soft round body, short legs with soft paws and small pointed triangle ears. Her fluffy coat is warm creamy white (#FBF4E6), never grey, with a soft charcoal (#3A3A40) cap patch over the top of her head and her ear on the viewer's left, like a little hat tilted to one side, a round charcoal patch on her back, and a long fluffy charcoal tail that curls into a soft spiral like a question mark and ends in a white tip. Her whole face is creamy white. She has big glossy eyes with mint-green irises (#7FCBAE) and white highlights, both eyes the same color, a tiny pink nose, a small smile and pink blush. She wears a soft lavender ribbon collar (#B79CE0) with a small shiny golden bell at the front. She is a real four-legged kitten and always stands, sits or lies on four paws, the same size in every drawing. Top row, full body: standing facing the viewer, three-quarter view facing right, side view facing right, seen from behind with the cap patch, the back patch and the spiral tail visible. Middle row, head and shoulders: laughing with eyes closed happily, curious with her head tilted, surprised, sad with eyebrows raised in the middle, grumpy with eyebrows pulled down and her fur a little puffed, shy peeking over her spiral tail. Bottom row, full body: pouncing playfully at something on the ground, and curled up asleep with her tail around her. Soft warm studio light, friendly and calm for toddlers. Horizontal 16:9.
```

## Решения (25.09)
- Тоби: оранжевый однотонный платок вместо жёлтого шарфа (лапки с платка убираются).
- Мия: розово-персиковая, золотистая прядка на макушке, розовый ошейник с золотым колокольчиком, длинный пушистый хвост без спирали. Имя — Мия.
- Мир: пряничный пастельный сказочный сад (как на карточке «Пушинки»): домик-пряник, пастельные цветы, мягкий тёплый свет.
- Мамы будут переделаны под новых малышей: мама-собака в голубой гамме Тоби, мама-кошка в розовой гамме Мии, взрослее и темнее; розовые накидка/ленточка и ресницы сохраняются.

## Мия 3D — промпт для ChatGPT
Загрузить: 1 — окончательный лист Тоби, 2 — карточка «Пушинки».

```
Use the two attached images as references. Image 1, the model sheet of Toby the puppy, is the exact reference for the rendering style, fur texture, lighting, plain background, page layout and character size. Image 2 is the reference only for the kitten's look. Create a clean character model sheet of this kitten, named Mia, for a gentle wordless preschool animated series, matching image 1 so that Mia and Toby look like they come from the same animated film. The page contains only the kitten on the same plain very light background as image 1, with no lettering, name, logo, color swatches, icons, frames or scenery. Mia's colors and accessories come only from image 2 and this description. She is a small, round, fluffy four-legged kitten about three months old, exactly the same height as Toby in image 1, and she always stands, sits or lies on four paws. Soft 3D animated-film render with fluffy fur and visible soft fibers. Her fur is soft pink-peach (#F5B5AA), slightly lighter and more peach on her body (#F7C9B4). Her muzzle, chest, belly and all four paws are warm cream (#FBEFD9). Her small pointed ears are pink-peach outside and soft pink inside (#F29CA3). Her signature is a soft golden-blonde tuft of fur on top of her head (#F4D27A), which appears in every drawing. She has big glossy blue eyes (#3F63B8) with lighter blue rings and white highlights, both eyes the same color in every drawing, a tiny pink nose, a small happy mouth and pink blush on her cheeks. Her long fluffy tail curves softly upward. She wears a soft pink collar (#F08FA0) with one small shiny golden bell at the front (#E8B84A), and this bell is her only accessory. Every drawing shows the same kitten at the same size, with identical colors, tuft, collar and bell. Top row, full body: standing facing the viewer, three-quarter view facing right, side view facing right, seen from behind with the fluffy tail visible. Middle row, head and shoulders: laughing with eyes closed happily, curious with her head tilted, surprised, sad with eyebrows raised in the middle and ears lowered, grumpy with eyebrows pulled down and her fur a little puffed, shy peeking out from behind her fluffy tail. Bottom row, full body: pouncing playfully with her front paws, and curled up asleep with her tail wrapped around her. Soft warm light, friendly and calm for toddlers. Wide landscape format.
```
