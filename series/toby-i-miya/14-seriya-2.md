# Серия 2. «Зайчик на двоих» (3D, пряничный мир)

Урок: одна игрушка — играем вместе, и весело обоим. Второй урок: столкнулись — остановись и подумай, а не хватай.
Длительность: около 3 мин 45 с, 43 кадра по 3–7 с.
Рамка сериала: кадры 1–4 и 43 — те же видео, что в серии 1.
Зайчик в этой серии ничей: это луч солнца сквозь листву дерева. Его никто не «даёт». Солнышко только смотрит и переживает, но ничего не решает.
Бабочки голубая и розовая — подсказка. Они не учат малышей, просто летают вместе, а малыши сами догадываются.

Названия:
- RU: Тоби и Мия — Зайчик на двоих ☀️ Мультик для малышей без слов
- EN: Toby & Mia — One Sparkle for Two ☀️ Wordless Cartoon for Toddlers
- ES: Toby y Mía — Un rayito para dos ☀️ Dibujos sin palabras para bebés

---

## Что загружать

- **[T]** лист Тоби · **[M]** лист Мии · **[MD]** лист мамы-собаки · **[MC]** лист мамы-кошки · **[S]** лист солнышка · **[Б]** бабочки (обе, голубая и розовая)
- Фоны (готовы, папка `art/`): **[Сад]** bg_sad_v1 · **[Вечер]** bg_vecher_v1 · **[ДС]** собачий домик bg_ds_v1 · **[ДК]** кошачий домик bg_dk_v1
- Двое персонажей в кадре — вместо двух листов загружать готовую склейку из `art/combo/`.

Загружать только тех, кто в кадре, плюс фон. Каждый кадр — новый чат.

## Как делается кадр

Четыре вида кадров:
1. **Обычный.** Картинка в ChatGPT: загрузить образцы → вставить ШАБЛОН + текст кадра. Потом видео в Hailuo: загрузить картинку (JPG) → вставить движение + ХВОСТ.
2. **Повтор из серии 1.** Ничего не делать: беру готовое видео серии 1.
3. **«Картинку делает Claude».** В этой серии таких нет.
4. **«Делает Claude».** Ничего генерировать не нужно.

Повторов 13 из 43. Это кадры рамки, солнышко крупным планом, двери, мамы и засыпание. Для малышей повторяющийся ритуал утра и вечера — плюс, а не минус.

Звук сервиса не нужен, весь звук ставит Claude.

**Солнышко.** Генератор его не рисует. В кадрах, где видно небо, я сам ставлю маленькое солнышко слева вверху с нужным настроением. Если генератор всё же нарисовал солнце — кадр переделать.

**ШАБЛОН картинки** (ставить перед текстом кадра):
```
Using the attached images as exact references for the characters and the location, keep every character's design, colors, size and accessories identical, in a soft 3D plush animated-film style with fluffy fur and warm gentle light. Toby is a light cornflower-blue puppy with a white face stripe, navy ears, a white tuft on his head and a plain orange bandana. Mia is a pink-peach kitten with a golden tuft on her head and a pink collar with a heart-shaped golden bell. Their mothers are about one and a half times taller and wear dusty rose. The sky shows only what is in the attached location image: its colors, clouds or stars. One frame of a gentle wordless preschool cartoon, horizontal 16:9, with no text:
```

**ХВОСТ движения** (ставить после движения):
```
Keep the characters' design, colors and the soft 3D plush style exactly the same. The sky and background stay exactly as in the picture. Gentle, simple movement in real time, no slow motion. One continuous shot, the camera stays still, no cuts. No morphing, no extra legs or paws, no new characters or objects, no text, no speech, no music.
```

---

## Сцена 1. Восход (0:00–0:18)

**1–4. 0:00–0:18. Рамка.** Ночь, солнышко тянет себя из-за холма, утро, заставка «Toby & Mia».
Повтор кадров 1–4 из серии 1.

## Сцена 2. Утро: скорее к другу (0:18–0:48)

Сегодня малыши просыпаются раньше мам. Они уже знакомы и спешат друг к другу.

**5. 0:18–0:23. Тоби не спится.** Мама-собака ещё спит. Тоби сидит рядом, смотрит в окно и виляет хвостом.
Звук: сопение мамы, тихое «тяф?».
[ДС] + [MD] + [T]
- Кадр: `Toby's mother is still asleep on the soft blue dog bed, while little Toby is already awake and sits beside her, looking up at the round window with bright eager eyes.`
- Движение: `The mother breathes slowly in her sleep; the puppy looks at the window and wags his tail faster and faster.`

**6. 0:23–0:28. Тоби будит маму.** Лизнул маму в нос. Мама открывает один глаз и улыбается.
Звук: «чмок», сонное «вуф».
[ДС] + [MD] + [T]
- Кадр: `Little Toby gives his sleeping mother a quick lick on the tip of her nose on the blue dog bed; she opens one eye with a sleepy smile.`
- Движение: `The puppy licks his mother's nose; she opens one eye, then both, and smiles at him.`

**7. 0:28–0:33. Мие не спится.** Мама-кошка спит. Мия сидит на краю корзинки и звенит колокольчиком.
Звук: колокольчик, тихое «мяу?».
[ДК] + [MC] + [M]
- Кадр: `Mia's mother is still asleep in the soft pink cushion basket, while little Mia is already awake and sits on the edge of the basket, looking at the round window with bright eager eyes.`
- Движение: `The mother breathes slowly in her sleep; the kitten wiggles impatiently and her bell swings.`

**8. 0:33–0:38. Мия будит маму.** Трётся о мамину щёку. Мама открывает глаза и улыбается.
Звук: «мрр», колокольчик.
[ДК] + [MC] + [M]
- Кадр: `Little Mia rubs her head against her sleeping mother's cheek in the pink basket; the mother opens her eyes with a sleepy smile.`
- Движение: `The kitten rubs her cheek against her mother's; the mother opens her eyes and smiles.`

**9. 0:38–0:43. Двери открываются.** Мамы в дверях.
Повтор кадра 11 из серии 1.

**10. 0:43–0:48. Бегут навстречу.** Тоби бежит слева, Мия справа, по дорожке к середине лужайки.
Звук: топот лапок, колокольчик, тема игры.
[Сад] + [T] + [M]
- Кадр: `Wide view of the garden: little Toby runs happily from the blue-roofed cottage on the left and little Mia runs happily from the pink-roofed cottage on the right toward each other along the cobblestone path.`
- Движение: `The puppy and the kitten run toward each other along the path, ears bouncing.`

## Сцена 3. Привет (0:48–0:58)

**11. 0:48–0:53. Носик к носику.** Встречаются посреди лужайки и трутся носиками. Как в конце серии 1.
Звук: «тяф!», «мяу!», колокольчик.
[Сад] + [T] + [M]
- Кадр: `In the middle of the lawn, little Toby and little Mia gently touch noses hello, both smiling with their eyes closed happily.`
- Движение: `They touch noses, then bounce back a little and wiggle with joy; the puppy wags his tail.`

**12. 0:53–0:58. Солнышко подмигивает.**
Повтор кадра 18 из серии 1.

## Сцена 4. Зайчик в листве (0:58–1:23)

**13. 0:58–1:03. Ветерок в кроне.** Листья качаются, сквозь них пробивается тонкий золотой луч.
Звук: шелест листвы, волшебный перезвон.
[Сад]
- Кадр: `Close view of the round fluffy crown of the big tree against the blue sky: one thin golden beam of light shines down through a small gap between the leaves toward the grass.`
- Движение: `A soft breeze sways the leaves; the thin beam of light flickers between them.`

**14. 1:03–1:07. Зайчик на траве.** Под деревом дрожит яркое пятнышко света.
Звук: «блеск».
[Сад]
- Кадр: `One single small bright round spot of golden light on the green grass in the soft shade under the big tree.`
- Движение: `The bright spot of light trembles and hops a little on the grass.`

**15. 1:07–1:12. Оба замечают.** Одновременно: уши торчком, смотрят вниз.
Звук: «тяф?» и «мяу?» вместе.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia stand side by side on the lawn and look down with wide delighted eyes at one single bright round spot of golden light on the grass in front of them.`
- Движение: `Both prick up their ears at the same moment and lean forward toward the spot of light.`

**16. 1:12–1:17. Солнышко смотрит.**
Повтор кадра 17 из серии 1.

**17. 1:17–1:23. Погоня вдвоём.** Зайчик бежит от дерева по лужайке к цветам. Малыши скачут за ним.
Звук: тема игры, топот.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia happily chase one single bright spot of golden light across the open lawn toward the pastel flowers at the front edge of the garden.`
- Движение: `The spot of light zigzags across the grass and the puppy and the kitten bounce after it side by side.`

## Сцена 5. Бум! (1:23–1:54)

**18. 1:23–1:27. Прыжок.** Зайчик замер у цветов. Тоби прыгает слева, Мия справа — оба в воздухе.
Звук: музыка обрывается, «вжух».
[Сад] + [T] + [M]
- Кадр: `Near the pastel flowers at the front edge of the lawn, little Toby leaps from the left and little Mia leaps from the right toward one single bright spot of golden light on the grass between them, both in mid-air with front paws forward.`
- Движение: `The puppy and the kitten leap toward the spot of light at the same moment from opposite sides.`

**19. 1:27–1:31. Бум носами.** Стукаются носами, глаза зажмурены. Зайчик выскальзывает из-под лап.
Звук: мягкий смешной «бум», «ой» у обоих.
[Сад] + [T] + [M]
- Кадр: `Close-up of little Toby and little Mia bumping noses softly, both with eyes squeezed shut, while one single bright spot of golden light slips out from under their paws onto the grass.`
- Движение: `They bump noses softly and bounce back a little; the spot of light slides away across the grass.`

**20. 1:31–1:36. Трут носы.** Сидят напротив друг друга и трут нос лапкой.
Звук: тихий писк Тоби, «мяу» Мии.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia sit on the grass facing each other, each rubbing their own nose with one paw, looking a little surprised and hurt.`
- Движение: `Both rub their noses with a paw and blink.`

**21. 1:36–1:41. Мия дуется.** Отворачивается, ушки назад, хвост стучит по траве.
Звук: обиженное «мяу».
[Сад] + [M]
- Кадр: `Little Mia sits on the grass with her head turned away and a small pout, ears slightly back, near the pink-roofed cottage side of the garden.`
- Движение: `The kitten turns her head away with a little huff; the tip of her tail taps the grass.`

**22. 1:41–1:46. Тоби грустит.** Уши опущены, смотрит на зайчика и не трогает его.
Звук: тихое скуление.
[Сад] + [T]
- Кадр: `Little Toby sits on the grass with his ears drooping, looking sadly down at one single bright spot of golden light a little way in front of him, near the blue-roofed cottage side of the garden.`
- Движение: `The puppy's ears droop lower and he looks down at the spot of light without touching it.`

**23. 1:46–1:49. Солнышко беспокоится.**
Повтор кадра 25 из серии 1.

**24. 1:49–1:54. Мамы видят и не вмешиваются.** Переглядываются спокойно: пусть сами.
Звук: тишина, одна мягкая нота.
[Сад] + [MD] + [MC]
- Кадр: `Wide view: Toby's mother in the doorway of the blue-roofed cottage and Mia's mother in the doorway of the pink-roofed cottage look toward the lawn, then calmly at each other with gentle, patient faces.`
- Движение: `Both mothers look toward the lawn, then at each other, and give a small calm nod.`

## Сцена 6. Бабочки (1:54–2:25)

**25. 1:54–1:59. Бабочки над зайчиком.** Из цветов вылетают голубая и розовая бабочки и порхают над пятнышком.
Звук: тонкий перезвон бабочек.
[Сад] + [Б]
- Кадр: `Close view of the pastel flowers at the front edge of the lawn: one single bright spot of golden light lies on the grass, and just above it hover the two small butterflies from the attached reference, the pale sky-blue one and the pale peach-pink one. Only these two butterflies.`
- Движение: `The two butterflies flutter up from the flowers and hover above the spot of light.`

**26. 1:59–2:03. Малыши смотрят вверх.** Забыли обиду, головы поднимаются.
Звук: удивлённое «ой» у обоих.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia sit on the grass a little apart and both look up with wide curious eyes at something above them.`
- Движение: `Both slowly lift their heads and look up; their ears perk up.`

**27. 2:03–2:08. Зайчик гаснет.** Ветерок, листья сомкнулись — пятнышко тает. Бабочки остаются.
Звук: шелест листвы, тающий «дзынь».
[Сад] + [Б]
- Кадр: `One single bright spot of golden light on the grass near the pastel flowers, with the two small butterflies from the attached reference, the pale sky-blue one and the pale peach-pink one, fluttering just above it. Only these two butterflies.`
- Движение: `The spot of light slowly fades away and disappears; the two butterflies keep fluttering above the grass.`

**28. 2:08–2:14. Бабочки кружатся вместе.** Танцуют друг вокруг друга, весело обеим.
Звук: вальсик бабочек.
[Сад] + [Б]
- Кадр: `Close view of the two small butterflies from the attached reference, the pale sky-blue one and the pale peach-pink one, circling around each other in the air above the lawn. Only these two butterflies.`
- Движение: `The two butterflies circle around each other in a playful dance, again and again.`

**29. 2:14–2:20. Догадались.** Тоби смотрит на Мию, Мия — на Тоби. Улыбаются.
Звук: «динь» догадки, тема игры тихо.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia sit on the grass and turn to look at each other, starting to smile.`
- Движение: `They look at each other; the puppy wags his tail and the kitten's ears come up as they both smile.`

**30. 2:20–2:25. Бабочки летят к дереву.** Кружат у кроны большого дерева.
Звук: перезвон бабочек.
[Сад] + [Б]
- Кадр: `Wide view of the garden: the two small butterflies from the attached reference, the pale sky-blue one and the pale peach-pink one, flutter together near the round fluffy crown of the big tree. Only these two butterflies.`
- Движение: `The two butterflies fly together toward the crown of the tree and circle around it.`

## Сцена 7. Наперегонки (2:25–2:53)

**31. 2:25–2:29. На старт.** Плечом к плечу, припали к траве, хвосты виляют.
Звук: «тяф!», «мяу!», хихиканье.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia crouch low side by side on the lawn, ready to run, looking toward the big tree with playful faces.`
- Движение: `Both wiggle their bottoms and wag their tails, ready to run.`

**32. 2:29–2:34. Бегут.** Общий план: бегут рядом через лужайку к дереву.
Звук: тема игры в полную силу, топот.
[Сад] + [T] + [M]
- Кадр: `Wide view of the garden: little Toby and little Mia run side by side across the open lawn toward the big tree.`
- Движение: `The puppy and the kitten run side by side toward the tree, neither ahead of the other.`

**33. 2:34–2:38. Нос в нос.** Крупно: бегут вровень, уши развеваются.
Звук: колокольчик, топот.
[Сад] + [T] + [M]
- Кадр: `Close view from the front: little Toby and little Mia run side by side toward the viewer, exactly level with each other, ears flying and happy faces.`
- Движение: `They run side by side, exactly level, their ears flapping.`

**34. 2:38–2:43. Кувырок в кучу.** Прибегают к стволу вместе и кувыркаются в одну кучу.
Звук: мягкий «бух», смех.
[Сад] + [T] + [M]
- Кадр: `At the foot of the thick trunk of the big tree, little Toby and little Mia tumble together into one soft happy heap on the grass.`
- Движение: `They reach the tree at the same moment and roll over together into a happy heap.`

**35. 2:43–2:49. Смеются.** Лежат на спинках, лапки вверх, хохочут.
Звук: «трель» Мии, «тяф-тяф!» Тоби.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia lie on their backs side by side on the grass under the big tree, paws in the air, laughing with their eyes closed.`
- Движение: `Both wiggle on their backs and laugh, paws kicking happily in the air.`

**36. 2:49–2:53. Солнышко хлопает в ладошки.**
Повтор кадра 36 из серии 1.

## Сцена 8. Зайчик на двоих (2:53–3:12)

**37. 2:53–2:59. Зайчик вернулся.** Ветерок, листья раздвинулись — пятнышко прыгает на траву между ними. Малыши смотрят на него, потом друг на друга. Никто не хватает.
Звук: шелест, «блеск».
[Сад] + [T] + [M]
- Кадр: `Under the big tree, little Toby and little Mia lie on their tummies facing each other, and one single bright spot of golden light lands on the grass right between them; both look at it and then at each other with a smile.`
- Движение: `The spot of light hops onto the grass between them; they look at it, then at each other, and smile.`

**38. 2:59–3:06. Играют вместе.** Зайчик прыгает с носа Мии на нос Тоби и обратно. Оба смеются.
Звук: «блеск» на каждом прыжке, смех, тема игры.
[Сад] + [T] + [M]
- Кадр: `Close view: little Toby and little Mia lie nose to nose on the grass under the big tree, laughing; one single bright spot of golden light sits on the tip of Mia's pink nose.`
- Движение: `The spot of light hops from the kitten's nose to the puppy's nose and back again; both laugh.`

**39. 3:06–3:12. Мамы улыбаются друг другу.**
Повтор кадра 38 из серии 1.

## Сцена 9. Вечер (3:12–3:44)

**40. 3:12–3:18. Домой с бабочками.** Малыши машут лапкой и расходятся. Над Тоби летит голубая бабочка, над Мией — розовая.
Звук: колокольчик, «тяф», перезвон бабочек.
[Вечер] + [T] + [M]
- Кадр: `The garden in the evening: little Toby walks toward the blue-roofed cottage on the left and little Mia walks toward the pink-roofed cottage on the right, both looking back and waving a paw; a small pale sky-blue butterfly flutters above Toby and a small pale peach-pink butterfly flutters above Mia.`
- Движение: `They wave goodbye to each other and walk home; the butterflies flutter above them.`
Если бабочки выйдут плохо — ставлю повтор кадра 40 из серии 1.

**41. 3:18–3:24. Тоби засыпает.**
Повтор кадра 41 из серии 1.

**42. 3:24–3:30. Мия засыпает.**
Повтор кадра 42 из серии 1.

**43. 3:30–3:44. Солнышко садится.**
Повтор кадра 43 из серии 1 (обе части).

---

## Солнышко по кадрам (делает Claude)

Крупные планы — все повторы из серии 1: 1, 3, 12 (=18), 16 (=17), 23 (=25), 36, 43.
Маленькое солнышко слева вверху — во всех кадрах, где видно небо:
- Сцены 2–4 (утро, привет, зайчик): улыбка.
- Сцена 5 (бум): с кадра 19 — тревога.
- Сцена 6 (бабочки): тревога до кадра 28; с кадра 29, когда малыши догадались, — улыбка.
- Сцена 7 (наперегонки): радость, лучи ярче.
- Сцена 8: обнимает себя.
- Сцена 9: сонное, низко над левым холмом.

Цвет: на радости картинка чуть теплее, на ссоре чуть холоднее.

## Итог для производства

- Новые картинки в ChatGPT: 30. Новые видео в Hailuo: 30. Повторы из серии 1: 13.
- Склейка «Тоби и Мия» нужна в 17 кадрах. Бабочки без малышей — 4 кадра.
- Бабочки вместе с малышами — только кадр 40, описаны словами. Это риск: у ChatGPT только 2 картинки.
- Новые звуки к серии 1: мягкий «бум» носами, обиженное «мяу», шелест листвы, перезвон бабочек, «вжух» прыжка, смех обоих. Остальное — из серии 1.
