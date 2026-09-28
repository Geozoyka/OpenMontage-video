# Тест видеосервисов — какой брать

Цель: за один вечер бесплатно понять, какой сервис лучше оживляет Тоби и Мию. Потом купить только его.

## Что нужно заранее

Две картинки из папки с кадрами:
- `05 Собачий домик` — один сюжет, двое спят (проверка меха и спокойного движения);
- `29 Ку-ку!` — двое выглядывают из-за ствола (проверка двух персонажей и мордочек).

Два текста (одинаковые во всех сервисах):

**Для 05:**
```
Both dogs breathe slowly in their sleep; the puppy's ear twitches once; the beam of warm light from the window slowly brightens. Keep the characters' design, colors and the soft 3D plush style exactly the same. Gentle, simple, slow movement. The camera stays still. No text, no speech, no music.
```

**Для 29:**
```
The puppy and the kitten peek out from behind the tree trunk at the same moment, see each other, blink with wide surprised eyes and their ears twitch. Keep the characters' design, colors and the soft 3D plush style exactly the same. Gentle, simple, slow movement. The camera stays still. No text, no speech, no music.
```

Настройки везде: image-to-video, 16:9, 5–6 секунд, 720p/768p, звук выключен (если есть).

## Шаг 1. Hailuo

1. Открыть https://hailuoai.video и войти через Google.
2. Выбрать **Image to Video**, модель **Hailuo 2.3** (если есть — ещё раз на **H3**).
3. Загрузить картинку `05`, вставить текст для 05, нажать Generate.
4. То же для `29`.
5. Скачать видео, назвать: `hailuo_05.mp4`, `hailuo_29.mp4`.

## Шаг 2. Freepik

1. Открыть https://www.freepik.com, войти через Google.
2. В меню **AI → Video Generator** (или **Generate video**).
3. Выбрать модель **Kling 2.5**, загрузить `05`, вставить текст, сгенерировать. Затем `29`.
4. Повторить на модели **MiniMax Hailuo Fast** (если бесплатных кредитов хватит).
5. Назвать: `freepik_kling_05.mp4`, `freepik_kling_29.mp4`, `freepik_hailuofast_05.mp4`, `freepik_hailuofast_29.mp4`.

## Шаг 3 (если останутся силы). Kling напрямую

1. Открыть https://app.klingai.com/global и войти.
2. **AI Videos → Image to Video**, та же схема.
3. Назвать: `kling_05.mp4`, `kling_29.mp4`.

Бесплатные видео в мультик не идут (нет коммерческих прав). Они только для сравнения.

## Шаг 4. Прислать Claude

Все видео одним сообщением. Claude разберёт кадры и поставит оценки.

## Как оцениваем (каждое видео, 0–2 балла за пункт)

1. **Персонаж тот же до конца** — морда, цвета, косынка, колокольчик не меняются.
2. **Мех не «плывёт»** — нет каши, мерцания, пятен.
3. **Нет брака** — лишних лап, слияния двух персонажей, скачков фона.
4. **Движение как просили** — спокойно, без самовольных действий.
5. **Стиль остался мультяшным** — не стал реалистичнее.

Максимум 10 за видео, 20 за сервис.

## Как решаем

- Покупаем сервис с наибольшим баллом.
- Если разница 2 балла или меньше — берём более дешёвый на нашу серию:
  - Freepik Premium+ помесячно (безлимит на Kling 2.5 и Hailuo Fast, если подтвердится);
  - Hailuo Standard $14.99 + докупка кредитов (~$31 за серию);
- Первый месяц — только помесячная оплата. Годовая — когда серия реально собрана.
- Звук: сначала пробуем звуки в Freepik (если он выбран). ElevenLabs Starter $6 — только если «тяф/мяу» там не выходят.
