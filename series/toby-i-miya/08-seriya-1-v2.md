# Серия 1. «Солнечный зайчик» — версия 3 (3D, пряничный мир)

Урок: сделать первый шаг к знакомству. Второй урок: мир большой, но мама рядом.
Длительность: около 3 мин 50 с, 43 кадра по 3–7 с.
Рамка сериала: в начале солнышко вылезает из-за левого холма и просыпается, в конце зевает и садится за тот же холм. Кадры 1–4 и 43 делаются один раз и идут в каждой серии.
Зайчик в этой серии всегда один. Столкновение носами — во 2-й серии.

Названия:
- RU: Тоби и Мия — Солнечный зайчик ☀️ Мультик для малышей без слов
- EN: Toby & Mia — The Sunny Sparkle ☀️ Wordless Cartoon for Toddlers
- ES: Toby y Mía — El rayito de sol ☀️ Dibujos sin palabras para bebés

---

## Что загружать

- **[T]** лист Тоби · **[M]** лист Мии · **[MD]** лист мамы-собаки · **[MC]** лист мамы-кошки · **[S]** лист солнышка · **[Б]** бабочки
- Фоны (готовы, папка `art/`): **[Сад]** bg_sad_v1 · **[Ночь]** bg_noch_v1 · **[Вечер]** bg_vecher_v1 · **[ДС]** собачий домик bg_ds_v1 · **[ДК]** кошачий домик bg_dk_v1

Загружать только тех, кто в кадре, плюс фон. Каждый кадр — новый чат.

## Как делается кадр

Три вида кадров:
1. **Обычный.** Картинка в ChatGPT / Nano Banana: загрузить образцы → вставить ШАБЛОН + текст кадра. Потом видео в Seedance: загрузить картинку → вставить движение + ХВОСТ.
2. **«Картинку делает Claude».** Я присылаю готовую первую картинку с солнышком. Ты загружаешь её в Seedance и вставляешь движение + ХВОСТ.
3. **«Делает Claude».** Ничего генерировать не нужно.

Звук сервиса не нужен, весь звук ставит Claude.

**Солнышко.** Генератор его не рисует никогда (кроме кадра 2). В кадрах, где видно небо, я сам ставлю маленькое солнышко слева вверху с нужным настроением. Если генератор всё же нарисовал солнце — кадр переделать.

**ШАБЛОН картинки** (ставить перед текстом кадра):
```
Using the attached images as exact references for the characters and the location, keep every character's design, colors, size and accessories identical, in a soft 3D plush animated-film style with fluffy fur and warm gentle light. Toby is a light cornflower-blue puppy with a white face stripe, navy ears, a white tuft on his head and a plain orange bandana. Mia is a pink-peach kitten with a golden tuft on her head and a pink collar with a heart-shaped golden bell. Their mothers are about one and a half times taller and wear dusty rose. The sky shows only what is in the attached location image: its colors, clouds or stars. One frame of a gentle wordless preschool cartoon, horizontal 16:9, with no text:
```

**ХВОСТ движения** (ставить после движения):
```
Keep the characters' design, colors and the soft 3D plush style exactly the same. The sky stays exactly as in the picture. Gentle, simple, slow movement. The camera stays still. No text, no speech.
```

---

## Сцена 1. Восход (0:00–0:18)

**1. 0:00–0:05. Ночь.** Спящий сад, из-за левого холма шевелятся кончики лучиков. Звук: сверчки, тихая колыбельная.
Картинку делает Claude.
- Движение: `The tips of the golden rays behind the hill on the left wiggle as if someone is waking up. Stars twinkle softly.`

**2. 0:05–0:10. Солнышко тянет себя.** Ручки цепляются за край холма, щёки надуты, солнышко выпрыгивает.
Звук: «пых-пых», смешной «чпок».
[Ночь] + [S] — единственный кадр, где солнце рисует генератор. Прислать мне на сверку с листом.
- Кадр: `Close-up of the top of the tall hill on the left at night before dawn: one single sun character, exactly like the attached sun reference, grips the edge of the hill with both little hands and pulls itself up, cheeks puffed with effort, only its top half visible above the hill. Small stars in the sky.`
- Движение: `The sun pulls itself up with effort and pops up over the hill with a little bounce.`

**3. 0:10–0:14. Утро.** Солнышко зевает, потягивает ручки, улыбается. Небо светлеет.
Звук: зевок-перезвон, «Солнечная тема».
Картинку делает Claude.
- Движение: `The sun character opens its eyes, yawns, stretches its little arms and smiles warmly; its rays glow brighter.`

**4. 0:14–0:18. Заставка «Тоби и Мия».** Делает Claude.

## Сцена 2. Два домика (0:18–0:48)

**5. 0:18–0:23. Собачий домик.** Мама-собака спит, обняв Тоби. Луч из окна ложится на них.
[ДС] + [MD] + [T]
- Кадр: `Toby's mother sleeps curled around little Toby on the soft blue dog bed; a warm beam of morning light from the round window falls on them.`
- Движение: `Both dogs breathe slowly in their sleep; the beam of light slowly brightens.`

**6. 0:23–0:28. Кошачий домик.** Мама-кошка спит, обняв Мию. Такой же луч.
[ДК] + [MC] + [M]
- Кадр: `Mia's mother sleeps curled around little Mia in the soft pink cushion basket; a warm beam of morning light from the round window falls on them.`
- Движение: `Both cats breathe slowly in their sleep; the beam of light slowly brightens.`

**7. 0:28–0:33. Мама будит Тоби.** Облизывает макушку, ухо дёргается, глаза открываются.
Звук: тихое «вуф-вуф», сопение.
[ДС] + [MD] + [T]
- Кадр: `Toby's mother gently licks the top of little Toby's head as he opens his eyes.`
- Движение: `The mother licks the puppy's head; his ear twitches and he opens his eyes and smiles.`

**8. 0:33–0:38. Мама будит Мию.** Облизывает щёку, Мия зевает, колокольчик звенит.
Звук: «мрр», зевок, колокольчик.
[ДК] + [MC] + [M]
- Кадр: `Mia's mother gently licks little Mia's cheek as she opens her eyes.`
- Движение: `The mother licks the kitten's cheek; the kitten opens her eyes and gives a tiny yawn, her bell swinging.`

**9. 0:38–0:43. Тоби потягивается.** Лапы вперёд, хвост вверх.
Звук: тема Тоби.
[ДС] + [T]
- Кадр: `Little Toby stretches on the blue dog bed, front paws forward and tail up.`
- Движение: `The puppy stretches with his front paws forward, then wags his tail.`

**10. 0:43–0:48. Мия потягивается точно так же.**
Звук: тема Мии.
[ДК] + [M]
- Кадр: `Little Mia stretches in the pink basket, front paws forward and tail up, exactly like a puppy would.`
- Движение: `The kitten stretches with her front paws forward, then her tail curls up.`

## Сцена 3. Первый выход в мир (0:48–1:20)

**11. 0:48–0:53. Двери открываются.** Общий план: двери обоих домиков открываются, в дверях мамы.
Звук: скрип дверей, птицы.
[Сад] + [MD] + [MC]
- Кадр: `Wide view of the garden: the round doors of both gingerbread cottages are open, with each mother standing in her doorway.`
- Движение: `Both round doors swing open at the same time and the mothers step into their doorways, smiling.`

**12. 0:53–0:58. Тоби выкатывается.** Кувыркается на траву, садится, радуется. Мама смотрит с порога.
Звук: «тяф!», мягкий «бух».
[Сад] + [T] + [MD]
- Кадр: `Little Toby tumbles out of the blue-roofed cottage onto the grass while his mother watches from the doorway.`
- Движение: `The puppy tumbles out, rolls once on the grass and sits up happily, wagging his tail.`

**13. 0:58–1:03. Тоби нюхает цветок.** Лепестки щекочут нос, Тоби трясёт головой.
Звук: обнюхивание, смешной «бдзынь».
[Сад] + [T]
- Кадр: `Close-up of little Toby sniffing a big pastel flower on the lawn.`
- Движение: `The puppy sniffs the flower, the petals tickle his nose and he shakes his head, ears flapping.`

**14. 1:03–1:08. Мия выглядывает.** Из-за дверного косяка видна только голова Мии. Мама за спиной.
Звук: тихий колокольчик.
[Сад] + [M] + [MC]
- Кадр: `Only little Mia's head peeks out from behind the doorframe of the pink-roofed cottage, her mother standing behind her.`
- Движение: `The kitten slowly peeks out, blinks, and looks around the garden with wide eyes.`

**15. 1:08–1:14. Бабочка.** Мия выходит на траву, рядом садится розовая бабочка, Мия замирает от восторга.
Звук: тема Мии.
[Сад] + [M] + [Б]
- Кадр: `Little Mia stands on the grass in front of her cottage, watching with wide eyes the small peach-pink butterfly from the attached reference sitting on a flower. Only this one butterfly.`
- Движение: `The kitten takes two careful steps; the butterfly flutters its wings and the kitten watches, amazed.`

**16. 1:14–1:20. Каждый в своём углу.** Тоби слева, Мия справа, между ними дерево. Друг друга не видят.
[Сад] + [T] + [M]
- Кадр: `Wide view of the garden: little Toby on the left near the blue-roofed cottage and little Mia on the right near the pink-roofed cottage, far apart, the big tree between them.`
- Движение: `The puppy sniffs the grass on the left; the kitten watches a flower on the right.`

## Сцена 4. Солнышко (1:20–1:38)

**17. 1:20–1:25. Солнышко смотрит.** Переводит глаза на Тоби, потом на Мию.
Картинку делает Claude.
- Движение: `The sun character slowly looks to the left, then to the right, with a soft curious smile; its rays sway gently.`

**18. 1:25–1:30. Солнышко подмигивает.**
Картинку делает Claude.
- Движение: `The sun character smiles wider and gives a playful wink, waving one little hand; its rays glow.`

**19. 1:30–1:35. Лучик.** Золотой лучик приходит из левого верхнего угла, колокольчик Мии вспыхивает.
Звук: волшебный перезвон.
[Сад] + [M]
- Кадр: `Closer view of little Mia on the grass, with only the lawn and her cottage behind her: a thin golden beam of light comes in from the top left corner of the picture and touches the heart-shaped golden bell on her collar, which shines brightly.`
- Движение: `The golden beam slowly reaches the bell; the bell flashes with a soft sparkle and the kitten looks down at it, surprised.`

**20. 1:35–1:38. Зайчик прыгает.** С колокольчика соскакивает яркое пятнышко и бежит по траве к Тоби.
Звук: «блеск».
[Сад]
- Кадр: `One single small bright round spot of golden light on the grass of the lawn, near the big tree.`
- Движение: `The bright spot of light hops quickly across the grass from right to left.`

## Сцена 5. Зайчик и стеснение (1:38–2:12)

**21. 1:38–1:44. Зайчик у Тоби.** Пятнышко пляшет перед лапами, Тоби наклоняет голову.
Звук: «тяф?».
[Сад] + [T]
- Кадр: `Little Toby looks down in surprise at one single bright round spot of golden light dancing on the grass in front of his paws.`
- Движение: `The spot of light wiggles; the puppy tilts his head and paws at it.`

**22. 1:44–1:50. Погоня.** Тоби гоняется за зайчиком вокруг дерева.
Звук: тема игры.
[Сад] + [T]
- Кадр: `Little Toby runs happily around the big tree chasing one single bright spot of golden light on the grass.`
- Движение: `The spot of light zigzags around the tree and the puppy chases it, jumping and turning.`

**23. 1:50–1:56. Тоби видит Мию.** Зайчик выводит его на сторону Мии. Тоби останавливается и виляет хвостом.
[Сад] + [T] + [M]
- Кадр: `Little Toby stops on the lawn and sees little Mia near the pink-roofed cottage; he wags his tail.`
- Движение: `The puppy stops, ears up, and wags his tail at the kitten in the distance.`

**24. 1:56–2:02. Мия убегает к маме.** Прячется за маму на пороге.
Звук: быстрый колокольчик, музыка стихает.
[Сад] + [M] + [MC]
- Кадр: `Little Mia hides behind her mother in the doorway of the pink-roofed cottage, peeking out shyly.`
- Движение: `The kitten runs to her mother and hides behind her, then slowly peeks out.`

**25. 2:02–2:05. Солнышко беспокоится.**
Картинку делает Claude.
- Движение: `The sun character presses its little hands together and looks down with worry; its rays droop slightly and dim.`

**26. 2:05–2:12. Мама подталкивает.** Обнимает Мию хвостом, потом мягко подталкивает носом вперёд.
Звук: колыбельная мам, «мрр».
[Сад] + [MC] + [M]
- Кадр: `Mia's mother wraps her fluffy tail around little Mia in the doorway and smiles gently.`
- Движение: `The mother cat unwraps her tail and gently nudges the kitten forward with her nose.`

## Сцена 6. Ку-ку у дерева (2:12–2:45)

**27. 2:12–2:17. Мия идёт за зайчиком.** Колокольчик звенит, зайчик скачет перед ней к дереву.
Звук: тема Мии.
[Сад] + [M]
- Кадр: `Little Mia walks carefully across the lawn, her heart-shaped bell shining; one single bright spot of golden light hops on the grass in front of her toward the big tree.`
- Движение: `The kitten walks forward carefully, her bell swinging, following the spot of light as it hops toward the tree.`

**28. 2:17–2:22. Зайчик прячется за ствол.** Тоби бежит к дереву слева, Мия подходит справа.
Звук: лёгкий перезвон.
[Сад] + [T] + [M]
- Кадр: `Wide view of the garden: a small bright spot of golden light slips behind the thick trunk of the big tree; little Toby runs toward the tree from the left and little Mia comes toward it from the right.`
- Движение: `The spot of light disappears behind the trunk; the puppy runs to the tree from the left and the kitten comes from the right.`

**29. 2:22–2:26. Ку-ку!** Оба одновременно выглядывают из-за ствола — нос к носу, глаза круглые.
Звук: тишина, потом «динь».
[Сад] + [T] + [M]
- Кадр: `Close view of the thick trunk of the big tree: little Toby peeks out from the left side of the trunk and little Mia peeks out from the right side at the same moment, face to face, both with wide surprised eyes.`
- Движение: `Both peek out from behind the trunk at the same moment, see each other and freeze with wide eyes.`

**30. 2:26–2:30. Мия прячется.** Юркает за ствол, торчит только кончик хвоста. Тоби наклоняет голову.
Звук: быстрый колокольчик.
[Сад] + [T] + [M]
- Кадр: `Little Mia hides behind the right side of the thick tree trunk with only the tip of her tail showing, while little Toby watches with his head tilted.`
- Движение: `The kitten ducks quickly behind the trunk; the puppy slowly tilts his head.`

**31. 2:30–2:35. Тоби ложится.** Медленно ложится, голова на лапах, тихо виляет кончиком хвоста — чтобы не напугать.
Звук: мягкая нота.
[Сад] + [T]
- Кадр: `Little Toby lies down slowly on the grass next to the thick trunk of the big tree, his head on his paws, looking gently toward the trunk.`
- Движение: `The puppy lowers himself slowly to the grass and softly wags the tip of his tail.`

**32. 2:35–2:40. Мия выглядывает снова.** Одна голова из-за ствола, смотрит на Тоби.
Звук: тихое «мяу?».
[Сад] + [M]
- Кадр: `Little Mia slowly peeks out from behind the thick trunk of the big tree, only her head showing, looking with curiosity at something on the grass.`
- Движение: `The kitten peeks out slowly and blinks; her bell gives a tiny swing.`

**33. 2:40–2:45. Зайчик на носу.** Колокольчик качнулся — зайчик прыгает Тоби на нос, глаза Тоби сходятся к носу.
Звук: колокольчик, «блеск».
[Сад] + [T]
- Кадр: `Close-up of little Toby lying on the grass with one single bright spot of golden light on his black nose, his eyes crossing to look at it.`
- Движение: `The spot of light wiggles on the puppy's nose and his eyes cross to look at it.`

## Сцена 7. Чих и смех (2:45–3:06)

**34. 2:45–2:50. Чих!** От чиха зайчик рассыпается искорками и пропадает.
Звук: чих Тоби, «дзынь».
[Сад] + [T]
- Кадр: `Close-up of little Toby sneezing with his eyes shut tight and his ears flying, a bright spot of golden light on his nose.`
- Движение: `The puppy sneezes, his whole head bouncing and his ears flapping; the spot of light bursts into tiny golden sparkles and disappears.`

**35. 2:50–2:55. Мия смеётся.** Выходит из-за ствола, смеётся. Тоби радостно вскакивает.
Звук: «трель» Мии, «тяф-тяф!».
[Сад] + [T] + [M]
- Кадр: `Little Mia steps out from behind the tree trunk laughing with her eyes closed happily, and little Toby jumps up happily in front of her.`
- Движение: `The kitten laughs and steps forward; the puppy springs up, wagging his tail.`

**36. 2:55–2:59. Солнышко хлопает в ладошки.** Свет теплеет.
Картинку делает Claude.
- Движение: `The sun character claps its little hands happily and bounces; its rays glow brighter and sparkle.`

**37. 2:59–3:06. Играют в ку-ку.** Выглядывают друг на друга из-за ствола снова и снова, смеются.
Звук: тема игры.
[Сад] + [T] + [M]
- Кадр: `Little Toby and little Mia play peekaboo around the thick trunk of the big tree, peeking out at each other from opposite sides and laughing.`
- Движение: `The puppy and the kitten hide and peek out at each other from opposite sides of the trunk again and again, bouncing happily.`

## Сцена 8. Мамы (3:06–3:12)

**38. 3:06–3:12. Мамы переглядываются.** Обе мамы в дверях смотрят на малышей и улыбаются друг другу.
Звук: колыбельная мам поверх темы игры.
[Сад] + [MD] + [MC]
- Кадр: `Wide view: Toby's mother in the doorway of the blue-roofed cottage and Mia's mother in the doorway of the pink-roofed cottage smile at each other across the garden.`
- Движение: `Both mothers smile and nod softly to each other.`

## Сцена 9. Вечер (3:12–3:50)

**39. 3:12–3:18. Мамы зовут.** Вечер. Малыши оглядываются на свои домики.
Звук: мягкое «вуф», «мрр».
[Вечер] + [T] + [M]
- Кадр: `The garden in the evening: little Toby and little Mia sit together on the lawn and turn their heads toward their cottages.`
- Движение: `Both little ones turn their heads toward their homes, ears perked.`

**40. 3:18–3:24. До завтра.** Трутся носиками, машут лапкой и бегут домой.
Звук: колокольчик, «тяф».
[Вечер] + [T] + [M]
- Кадр: `In the evening garden, little Toby and little Mia gently touch noses goodbye on the lawn.`
- Движение: `They touch noses, each waves a paw, and they run toward their own cottages.`

**41. 3:24–3:30. Тоби засыпает.** Прижимается к маме, глаза закрываются.
Звук: вздох, колыбельная.
[ДС] + [MD] + [T]
- Кадр: `Evening inside the cottage, warm orange light in the round window: little Toby snuggles against his mother on the blue dog bed, eyes closing.`
- Движение: `The puppy snuggles closer and slowly closes his eyes; his mother rests her head over him.`

**42. 3:30–3:36. Мия засыпает.** Прижимается к маме, глаза закрываются.
Звук: мурлыканье.
[ДК] + [MC] + [M]
- Кадр: `Evening inside the cottage, warm orange light in the round window: little Mia snuggles against her mother in the pink basket, eyes closing.`
- Движение: `The kitten snuggles closer and slowly closes her eyes; her mother wraps her tail around her.`

**43. 3:36–3:50. Солнышко садится.** Две части.
- Часть 1, картинку делает Claude. Движение: `The sun character yawns widely, then gives a sleepy wink; its rays glow softly.`
- Часть 2, делает Claude: солнышко опускается за левый холм, вечер переходит в ночь, два тёплых окна, конечная заставка.

---

## Солнышко по кадрам (делает Claude)

Крупные планы (я делаю картинку, ты оживляешь): 1, 3, 17, 18, 25, 36, 43.
Маленькое солнышко слева вверху — во всех кадрах, где видно небо:
- Сцена 3 (первый выход): улыбка.
- Сцена 4: в кадрах 19–20 неба нет, солнышко не ставлю.
- Сцена 5: улыбка; с момента, когда Мия прячется за маму, — тревога.
- Сцена 6: тревога, пока Мия прячется; с момента, когда она выглядывает снова, — улыбка.
- Сцена 7: радость, лучи ярче.
- Сцена 8: обнимает себя, как мамы малышей.
- Сцена 9: сонное, низко над левым холмом.

Цвет: на радости картинка чуть теплее, на тревоге чуть холоднее.

## Итог для производства

- Фоны и бабочки: готовы (папка `art/`, промпты в файле 09).
- Картинки кадров в генераторе: 35. Видео в Seedance: 42.
- Делает Claude без генерации: заставка 4 и вторая часть кадра 43.
- Звуки: колыбельная мам, темы Тоби, Мии, игры, «Солнечная тема»; колокольчик, двери, сверчки, птицы, «блеск», «дзынь», «чпок»; голоса по файлу 07-golosa-elevenlabs.md.
