# -*- coding: utf-8 -*-
"""Генератор посадочных страниц под коммерческие запросы (SEO + реклама)."""
import json, os, io

OUT = r"C:\Users\Admin\skupaishop"
PHONE1 = "+7 (900) 021-88-83"
PHONE1_TEL = "+79000218883"
PHONE2 = "+7 (952) 512-92-01"
PHONE2_TEL = "+79525129201"
ENDPOINT = "https://script.google.com/macros/s/AKfycbyMx4qMQkPSdvttttlLEtDAI48TXySSoIBQVHIfd-hL9d20SKHZ_3k14u5GWWQxYN7q/exec"
METRIKA = "113939222"

CSS = """
:root{--primary:#22c55e;--primary-dark:#16a34a;--dark:#111827;--text:#1f2937;--muted:#6b7280;--line:#e5e7eb;--soft:#f9fafb}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Roboto,Arial,sans-serif;color:var(--text);line-height:1.6;background:#fff}
a{color:var(--primary-dark);text-decoration:none}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header{background:var(--dark);color:#fff;padding:14px 0}
header .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.logo{font-weight:900;font-size:20px;color:#fff;letter-spacing:.5px}
.logo span{color:var(--primary)}
header .phones{display:flex;gap:14px;flex-wrap:wrap;font-weight:700}
header .phones a{color:#fff}
.hero{background:linear-gradient(135deg,#111827,#1f2937);color:#fff;padding:48px 0 40px}
.hero h1{font-size:30px;line-height:1.25;margin-bottom:14px}
.hero p{color:#d1d5db;font-size:17px;max-width:720px;margin-bottom:18px}
.badges{display:flex;gap:10px;flex-wrap:wrap;margin-top:8px}
.badge{background:rgba(34,197,94,.15);border:1px solid rgba(34,197,94,.5);color:#bbf7d0;padding:6px 12px;border-radius:999px;font-size:13px}
main{padding:36px 0 10px}
h2{font-size:23px;margin:32px 0 14px;line-height:1.3}
h3{font-size:17px;margin:20px 0 8px}
p{margin-bottom:12px}
ul{margin:0 0 14px 20px}
li{margin-bottom:6px}
table{width:100%;border-collapse:collapse;margin:14px 0 20px;font-size:15px}
th,td{border:1px solid var(--line);padding:10px 12px;text-align:left}
th{background:var(--soft);font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:18px 0}
.card{border:1px solid var(--line);border-radius:14px;padding:16px;background:#fff}
.card h3{margin-top:0}
.form-card{background:var(--dark);color:#fff;border-radius:16px;padding:26px;margin:26px 0}
.form-card h2{color:#fff;margin-top:0}
.form-card p.sub{color:#9ca3af;margin-bottom:16px}
label.fl{display:block;font-size:14px;font-weight:600;margin:14px 0 6px}
input[type=text],input[type=tel],select{width:100%;padding:12px 14px;border-radius:10px;border:1px solid #374151;background:#1f2937;color:#fff;font-size:15px}
input::placeholder{color:#6b7280}
.cond{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.cond label{border:1px solid #374151;border-radius:999px;padding:8px 12px;font-size:13px;cursor:pointer;color:#d1d5db}
.cond input{margin-right:6px}
.policy{display:flex;gap:8px;align-items:flex-start;font-size:13px;color:#9ca3af;margin:14px 0}
button.submit{width:100%;padding:15px;border:0;border-radius:12px;background:var(--primary);color:#06210f;font-weight:800;font-size:16px;cursor:pointer;margin-top:6px}
button.submit:disabled{opacity:.6;cursor:default}
.msg{margin-top:12px;font-size:14px;display:none;padding:12px;border-radius:10px}
.msg.err{display:block;background:#7f1d1d;color:#fecaca}
.msg.ok{display:block;background:#14532d;color:#bbf7d0}
.faq dt{font-weight:700;margin-top:14px}
.faq dd{color:#374151;margin:4px 0 0}
.links{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}
.links a{border:1px solid var(--line);border-radius:999px;padding:8px 14px;font-size:14px}
footer{background:var(--dark);color:#9ca3af;padding:26px 0;margin-top:36px;font-size:14px}
footer a{color:#fff}
.cta-line{background:var(--soft);border:1px solid var(--line);border-radius:14px;padding:18px;margin:22px 0}
.cta-line strong{font-size:17px}
"""

FORM_JS = """
const LEAD_ENDPOINT = '%(endpoint)s';
(function(){
  const form = document.getElementById('lead');
  const phone = form.querySelector('input[name=phone]');
  const msg = document.getElementById('msg');
  phone.addEventListener('input', function(){
    let d = this.value.replace(/\\D/g,'');
    if (!d) { this.value = ''; return; }
    if (d[0] === '8' || d[0] === '7') d = '7' + d.slice(1);
    else d = '7' + d;
    d = d.slice(0,11);
    let out = '+7';
    if (d.length>1) out += ' ('+d.slice(1,4);
    if (d.length>=5) out += ') '+d.slice(4,7);
    if (d.length>=8) out += '-'+d.slice(7,9);
    if (d.length>=10) out += '-'+d.slice(9,11);
    this.value = out;
  });
  function show(text, cls){ msg.textContent = text; msg.className = 'msg '+cls; }
  form.addEventListener('submit', async function(e){
    e.preventDefault();
    const btn = form.querySelector('button[type=submit]');
    const device = form.querySelector('input[name=device_name]').value.trim();
    const digits = phone.value.replace(/\\D/g,'');
    if (!device) return show('Укажите, что хотите продать.', 'err');
    if (digits.length !== 11) return show('Введите полный номер телефона (11 цифр).', 'err');
    btn.disabled = true; const old = btn.textContent; btn.textContent = 'Отправляем...';
    const payload = {
      form_source: '%(source)s',
      website_url: form.querySelector('input[name=website_url]').value || '',
      device_name: device,
      condition: (form.querySelector('input[name=condition]:checked')||{}).value || 'Не указано',
      phone: phone.value,
      photos: []
    };
    try{
      const r = await fetch(LEAD_ENDPOINT, {method:'POST', body: JSON.stringify(payload)});
      const j = await r.json();
      if (!r.ok || !j.ok) throw new Error(j.message || 'Ошибка отправки');
      form.reset();
      show('Заявка принята! Перезвоним в течение 5 минут — или звоните сами: %(phone)s.', 'ok');
      if (window.ym) { try { ym(%(metrika)s, 'reachGoal', 'lead_sent'); } catch(e){} }
    }catch(err){
      show('Не удалось отправить. Позвоните: %(phone)s или напишите в WhatsApp.', 'err');
    }finally{
      btn.disabled = false; btn.textContent = old;
    }
  });
})();
"""

PAGES = [
    {
        "slug": "vykup-noutbukov",
        "title": "Выкуп ноутбуков в Челябинске — оценка за 15 минут, деньги сразу | Скупка74",
        "desc": "Выкуп ноутбуков в Челябинске: оценка по фото за 15 минут, до 90% рыночной цены, выезд к вам, оплата на месте. Asus, Lenovo, HP, Apple, MSI, Dell.",
        "h1": "Выкуп ноутбуков в Челябинске — оценка за 15 минут",
        "lead": "Скупаем ноутбуки в любом состоянии: рабочие, с разбитым экраном, не включающиеся, после залития. Оцениваем по фото и платим на месте — без комиссий и «до встречи посмотрим».",
        "badges": ["До 90% рыночной цены", "Выезд по Челябинску бесплатно", "Деньги при получении ноутбука"],
        "blocks": [
            ("Что покупаем", "<ul><li><b>Игровые:</b> Asus ROG, MSI, Acer Nitro, Lenovo Legion, HP Omen</li><li><b>Рабочие и офисные:</b> Lenovo ThinkPad, HP ProBook, Dell Latitude, Asus VivoBook</li><li><b>Apple:</b> MacBook Air, MacBook Pro (M1/M2/M3 и Intel)</li><li><b>Неисправные:</b> не включается, разбит экран, залит, не держит батарею, без зарядки</li><li><b>С запчастями:</b> отдельно берём рабочие платы, матрицы, блоки питания</li></ul>"),
            ("Сколько платим", None),
            ("Как остановить цену заранее", "<p>Пришлите 3–4 фото: экран со включённым ноутбуком, наклейка на дне с моделью, корпус с двух сторон. Добавьте пару слов: год покупки, что не работает, есть ли зарядное. Этого хватает, чтобы назвать цену в 90% случаев, а не «примерно».</p><p>Если ноутбук не включается — цену считаем по модели и состоянию корпуса, фото наклейки с моделью в этом случае важнее всего.</p>"),
        ],
        "prices": [
            ("MacBook Pro 14/16 (M1–M3)", "40 000 – 130 000 ₽"),
            ("MacBook Air M1/M2", "18 000 – 55 000 ₽"),
            ("Игровые Asus ROG / MSI / Legion", "20 000 – 90 000 ₽"),
            ("Офисные Lenovo / HP / Dell", "6 000 – 30 000 ₽"),
            ("Ноутбуки не старше 5 лет с дефектом", "3 000 – 20 000 ₽"),
            ("Старые и нерабочие (10+ лет)", "500 – 4 000 ₽"),
        ],
        "faq": [
            ("Сколько стоит сама оценка?", "Оценка бесплатная и ни к чему не обязывает. Мы называем сумму, вы решаете — продавать или оставить."),
            ("Вы приедете, если ноутбук не работает?", "Да. Выезд по Челябинску бесплатный независимо от результата. Диагностику на месте делаем сами."),
            ("Можно без паспорта?", "Для сделки нужен паспорт — это требование к любому выкупу б/у техники и защита обеих сторон от претензий."),
            ("Как быстро вы платите?", "Сразу при получении ноутбука: наличными или переводом на карту — как удобнее."),
        ],
    },
    {
        "slug": "vykup-iphone",
        "title": "Скупка iPhone в Челябинске — выкуп айфонов за 15 минут | Скупка74",
        "desc": "Скупка iPhone в Челябинске: оценим по фото за 15 минут, выкуп с разбитым экраном, неисправных, после воды. Честная цена, оплата сразу.",
        "h1": "Скупка iPhone в Челябинске — деньги за 15 минут",
        "lead": "Берём iPhone любых моделей — от 6s до 16 Pro Max. С разбитым экраном, неисправные, после воды, с неисправной батареей. Оцениваем по IMEI и фото, платим на месте.",
        "badges": ["До 90% рыночной цены", "Оценка по фото и IMEI", "Без «накрутки» при осмотре"],
        "blocks": [
            ("Что покупаем", "<ul><li>iPhone 11–16 Pro Max, 15/16 Plus, SE 2/3</li><li>С разбитым экраном и задней крышкой</li><li>Не включающиеся, после воды, с нерабочими камерами или Face ID</li><li>Заблокированные по iCloud — обсуждаем индивидуально</li><li>iPhone старых моделей от 6s — на запчасти и на восстановление</li></ul>"),
            ("Почему цена держится при осмотре", "<p>Мы фиксируем сумму после фото и IMEI — до выезда. Если при осмотре не вскроется скрытый дефект, о котором вы не сказали, цена не меняется. Скрытые дефекты — это заменённый дисплей, следы ремонта, вода; их видно сразу при проверке.</p>"),
        ],
        "prices": [
            ("iPhone 16 Pro / Pro Max", "60 000 – 105 000 ₽"),
            ("iPhone 15 / 15 Pro", "40 000 – 75 000 ₽"),
            ("iPhone 14 / 13", "22 000 – 50 000 ₽"),
            ("iPhone 12 / 11", "14 000 – 32 000 ₽"),
            ("С разбитым экраном или после воды", "5 000 – 30 000 ₽"),
            ("iPhone X и старше", "2 000 – 12 000 ₽"),
        ],
        "faq": [
            ("Покупаете заблокированные по iCloud?", "Обычно нет — такой телефон нельзя проверить и перепродать. Если блокировка снимается официально, обсуждаем отдельно."),
            ("Нужна коробка и чек?", "Нет, но с комплектом цена выше на 3–7%: оригинальное зарядное, коробка с IMEI, чек подтверждают покупку."),
            ("Как вы проверяете телефон?", "IMEI на совпадение с корпусом и коробкой, состояние аккумулятора, замену деталей по настройкам, Face ID, камеры, следы воды. Проверка занимает 5–10 минут."),
            ("Вы заберёте телефон с моими данными?", "Нет. Вы выходите из iCloud и стираете данные при нас — без этого сделку не проводим."),
        ],
    },
    {
        "slug": "vykup-pristavok",
        "title": "Выкуп игровых приставок в Челябинске — PS5, Xbox, Nintendo | Скупка74",
        "desc": "Выкуп игровых приставок в Челябинске: PlayStation 5, Xbox Series X/S, Nintendo Switch. Оценка за 15 минут, выкуп с играми и геймпадами, деньги сразу.",
        "h1": "Выкуп игровых приставок в Челябинске",
        "lead": "PlayStation 5, PS4 Pro, Xbox Series X и S, Nintendo Switch — покупаем с играми, геймпадами и аксессуарами. Оценка за 15 минут, оплата при получении.",
        "badges": ["PS5 и Xbox Series", "Забираем с играми", "Оценка по фото за 15 минут"],
        "blocks": [
            ("Что покупаем", "<ul><li>PlayStation 5 (включая Slim и Pro), PS4 Pro / Slim</li><li>Xbox Series X, Series S, Xbox One X / S</li><li>Nintendo Switch, Switch OLED, Lite</li><li>С играми, вторыми геймпадами, дисками, зарядными станциями</li><li>С дефектами: шумит, выключается, не читает диски, есть перегрев</li></ul>"),
            ("Что добавляет к цене", "<p>Второй геймпад +3 000–6 000 ₽, набор из 3+ игр +2 000–8 000 ₽, оригинальная коробка и чек +5%. Комплект целиком оценивается выгоднее, чем приставка отдельно.</p>"),
        ],
        "prices": [
            ("PlayStation 5 Slim / Pro", "35 000 – 65 000 ₽"),
            ("PlayStation 5 (базовая)", "28 000 – 45 000 ₽"),
            ("Xbox Series X / S", "22 000 – 45 000 ₽"),
            ("Nintendo Switch OLED / Lite", "12 000 – 26 000 ₽"),
            ("PlayStation 4 Pro", "10 000 – 18 000 ₽"),
            ("Приставки с дефектами", "4 000 – 20 000 ₽"),
        ],
        "faq": [
            ("Покупаете с аккаунтом и цифровыми играми?", "Нет, аккаунт остаётся у вас: цифровые покупки к приставке не переходят. Диски и картриджи оцениваем отдельно."),
            ("Приставка шумит и перегревается — возьмёте?", "Возьмём. Цена учитывает стоимость чистки и замены термопасты, но выкуп возможен."),
            ("Проверяете при встрече?", "Да: включение, выход в интернет, чтение диска или картриджа, состояние портов и геймпадов. 10 минут."),
            ("Можно продать только геймпад или игры?", "Да, берём аксессуары и игры отдельно — цена ниже, чем в комплекте."),
        ],
    },
    {
        "slug": "vykup-instrumenta",
        "title": "Выкуп электроинструмента в Челябинске — Bosch, Makita, DeWalt | Скупка74",
        "desc": "Выкуп электроинструмента в Челябинске: перфораторы, шуруповёрты, болгарки, пилы. Bosch, Makita, DeWalt, Metabo, Milwaukee. Оценка за 15 минут.",
        "h1": "Выкуп электроинструмента в Челябинске",
        "lead": "Покупаем профессиональный и бытовой инструмент: перфораторы, шуруповёрты, УШМ, пилы, отбойные молотки. Рабочий и с дефектами, с кейсом и без.",
        "badges": ["Bosch, Makita, DeWalt", "Берём с дефектами", "Выезд и оценка бесплатно"],
        "blocks": [
            ("Что покупаем", "<ul><li>Перфораторы и отбойные молотки Bosch, Makita, Hilti, DeWalt</li><li>Шуруповёрты и гайковёрты, в том числе аккумуляторные с зарядкой</li><li>УШМ (болгарки), лобзики, циркулярные и торцовочные пилы</li><li>Сварочные инверторы, компрессоры, мойки высокого давления</li><li>С дефектами: не включается, искрит, клинит, износ щёток</li></ul>"),
            ("Как оцениваем", "<p>Профессиональный инструмент держит цену лучше бытового: бренд, серия, год выпуска и состояние патрона важнее внешнего вида. Смазанный корпус и потёртости цены не снижают — снижает износ механики и сгоревший двигатель.</p>"),
        ],
        "prices": [
            ("Перфораторы Bosch GBH / Makita HR", "5 000 – 25 000 ₽"),
            ("Аккумуляторные шуруповёрты с зарядкой", "3 000 – 18 000 ₽"),
            ("УШМ и пилы профсерии", "2 500 – 15 000 ₽"),
            ("Сварочные инверторы", "3 000 – 20 000 ₽"),
            ("Мойки высокого давления", "2 000 – 14 000 ₽"),
            ("Инструмент с дефектами", "700 – 8 000 ₽"),
        ],
        "faq": [
            ("Берёте инструмент без документов?", "Да, паспорт нужен только ваш — документы на инструмент не обязательны."),
            ("Что с инструментом, который не включается?", "Оцениваем по модели и внешнему состоянию. Иногда такой инструмент стоит дороже рабочего — если дело в расхожей запчасти."),
            ("Выкупаете набором?", "Да, набор из нескольких единиц оценивается выгоднее — забираем одним выездом."),
            ("Работаете с организациями?", "Да, выкупаем инструмент у компаний с закрывающими документами, оплата на счёт."),
        ],
    },
    {
        "slug": "vykup-bytovoy-tehniki",
        "title": "Выкуп бытовой техники в Челябинске — холодильники, стиральные машины | Скупка74",
        "desc": "Выкуп бытовой техники в Челябинске: холодильники, стиральные машины, телевизоры, посудомойки. Вывоз и оплата на месте, оценка за 15 минут.",
        "h1": "Выкуп бытовой техники в Челябинске",
        "lead": "Холодильники, стиральные и посудомоечные машины, телевизоры, плиты, кондиционеры. Приезжаем, проверяем, вывозим и платим на месте — вывоз наш.",
        "badges": ["Вывоз за наш счёт", "Наличными или на карту", "Работаем ежедневно"],
        "blocks": [
            ("Что покупаем", "<ul><li>Холодильники и морозильные камеры (включая двухкамерные и Side-by-Side)</li><li>Стиральные и посудомоечные машины, сушильные машины</li><li>Телевизоры (в том числе с разбитой матрицей — на запчасти)</li><li>Плиты, варочные панели, вытяжки, кондиционеры</li><li>Мелкая техника: пылесосы, микроволновки, кофемашины</li></ul>"),
            ("Как проходит выкуп", "<p>Вы присылаете фото и модель — мы называем цену. Дальше приезжаем, проверяем работу, отключаем технику, вывозим и платим. Для крупногабарита нужен свободный проход и лифт — об этом лучше сказать сразу, чтобы привезти нужное число людей.</p>"),
        ],
        "prices": [
            ("Холодильники Side-by-Side", "8 000 – 40 000 ₽"),
            ("Холодильники обычные", "3 000 – 18 000 ₽"),
            ("Стиральные машины", "2 500 – 20 000 ₽"),
            ("Телевизоры 4K 50–75\"", "4 000 – 30 000 ₽"),
            ("Посудомоечные машины", "2 000 – 15 000 ₽"),
            ("Техника с дефектами", "500 – 7 000 ₽"),
        ],
        "faq": [
            ("Кто оплачивает вывоз?", "Мы. Вывоз входит в сделку, отдельно за него не платите."),
            ("Техника не работает — заберёте?", "Да, берём неисправную технику на запчасти. Цена ниже, но вывоз и утилизация — на нас."),
            ("Нужно ли самому отключать технику?", "Лучше, чтобы к нашему приезду техника была отключена от воды и электричества — так быстрее и безопаснее."),
            ("Выкупаете технику из съёмной квартиры?", "Да, но потребуется паспорт и подтверждение, что техника ваша."),
        ],
    },
]


def price_block(rows):
    tr = "".join(f"<tr><td>{a}</td><td><b>{b}</b></td></tr>" for a, b in rows)
    return ("<table><tr><th>Модель / категория</th><th>Сумма выкупа</th></tr>"
            f"{tr}</table><p style=\"font-size:14px;color:#6b7280\">Диапазоны ориентировочные: точная сумма зависит от модели, года и состояния. "
            "Итоговую цену называем до выезда — по фото и модели.</p>")


def faq_block(faq):
    items = "".join(f"<dt>{q}</dt><dd>{a}</dd>" for q, a in faq)
    ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
    }
    return f'<h2>Частые вопросы</h2><dl class="faq">{items}</dl>', ld


def build(p, others):
    blocks = ""
    for h, body in p["blocks"]:
        if body is None:
            body = price_block(p["prices"])
        blocks += f"<h2>{h}</h2>{body}"
    faq_html, faq_ld = faq_block(p["faq"])
    links = "".join(f'<a href="/{o["slug"]}.html">{o["h1"].split(" в Челябинске")[0]}</a>'
                    for o in others)
    other_slugs = [o["slug"] for o in others]
    if "vykup" not in other_slugs:
        links += '<a href="/">Скупка техники в Челябинске — главная</a>'

    url = f"https://skupaishop.ru/{p['slug']}.html"
    ld_service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": p["h1"],
        "serviceType": p["h1"].split(" в Челябинске")[0],
        "areaServed": {"@type": "City", "name": "Челябинск"},
        "provider": {
            "@type": "LocalBusiness",
            "name": "Скупка74",
            "telephone": PHONE1_TEL,
            "address": {"@type": "PostalAddress", "streetAddress": "ул. Худякова, 4",
                        "addressLocality": "Челябинск", "addressRegion": "Челябинская область",
                        "postalCode": "454000", "addressCountry": "RU"},
            "url": "https://skupaishop.ru/",
        },
        "url": url,
    }
    ld_bread = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Главная", "item": "https://skupaishop.ru/"},
            {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url},
        ],
    }

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{url}">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld_service, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ld_bread, ensure_ascii=False)}</script>
</head>
<body>
<header><div class="wrap">
  <a class="logo" href="/">СКУПКА<span>74</span> · Челябинск</a>
  <div class="phones">
    <a href="tel:{PHONE1_TEL}">{PHONE1}</a>
    <a href="tel:{PHONE2_TEL}">{PHONE2}</a>
  </div>
</div></header>

<section class="hero"><div class="wrap">
  <h1>{p['h1']}</h1>
  <p>{p['lead']}</p>
  <div class="badges">{''.join(f'<span class="badge">{b}</span>' for b in p['badges'])}</div>
</div></section>

<main><div class="wrap">
{blocks}

<div class="form-card">
  <h2>Узнать цену за 15 минут</h2>
  <p class="sub">Заполните два поля — назовём точную сумму до выезда.</p>
  <form id="lead" novalidate>
    <input type="hidden" name="website_url" value="">
    <label class="fl">Что хотите продать?</label>
    <input type="text" name="device_name" placeholder="Например: iPhone 13 Pro 256 ГБ, MacBook Air M1, PS5 Slim" maxlength="400" required>
    <label class="fl">Состояние</label>
    <div class="cond">
      <label><input type="radio" name="condition" value="Новое" checked>Новое</label>
      <label><input type="radio" name="condition" value="Хорошее">Хорошее</label>
      <label><input type="radio" name="condition" value="Плохое">Плохое</label>
      <label><input type="radio" name="condition" value="Неисправное">Неисправное</label>
    </div>
    <label class="fl">Телефон для связи</label>
    <input type="tel" name="phone" placeholder="+7 (___) ___-__-__" required>
    <div class="policy"><input type="checkbox" name="policy" checked required>
      <span>Согласен с <a href="/privacy.html" target="_blank" rel="noopener" style="color:#bbf7d0">политикой конфиденциальности</a></span>
    </div>
    <button type="submit" class="submit">Узнать стоимость</button>
    <div class="msg" id="msg"></div>
  </form>
</div>

<div class="cta-line">
  <strong>Проще позвонить?</strong> {PHONE1} — отвечаем с 9:00 до 21:00, ежедневно. Или напишите в
  <a href="https://wa.me/79000218883">WhatsApp</a> и <a href="https://t.me/+79000218883">Telegram</a>.
</div>

{faq_html}

<h2>Другие направления</h2>
<div class="links">{links}</div>
</div></main>

<footer><div class="wrap">
  Скупка74 — выкуп б/у техники в Челябинске, ул. Худякова, 4. {PHONE1}, {PHONE2}.<br>
  Работаем ежедневно 9:00–21:00. <a href="/privacy.html">Политика конфиденциальности</a>
</div></footer>

<script>{FORM_JS % {'endpoint': ENDPOINT, 'source': 'Лендинг: ' + p['h1'], 'phone': PHONE1, 'metrika': METRIKA}}</script>
<!-- Yandex.Metrika counter -->
<script type="text/javascript">
(function(m,e,t,r,i,k,a){{m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
m[i].l=1*new Date();for(var j=0;j<document.scripts.length;j++){{if(document.scripts[j].src===r){{return;}}}}
k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}})
(window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");
ym({METRIKA},"init",{{clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true}});
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/{METRIKA}" style="position:absolute; left:-9999px;" alt=""></div></noscript>
<!-- /Yandex.Metrika counter -->
</body>
</html>
"""
    with io.open(os.path.join(OUT, p["slug"] + ".html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return p["slug"] + ".html", len(html)


if __name__ == "__main__":
    made = []
    for p in PAGES:
        others = [o for o in PAGES if o["slug"] != p["slug"]]
        made.append(build(p, others))
    for name, size in made:
        print(f"{name:34} {size:>7} байт")
