"""
Sample data for Roots & Recipes application.
Includes 3 dishes, 3 ingredients, 3 regions, and sample occasions.
"""

# Regions data
REGIONS = [
    {
        "id": 1,
        "name": "Dhaka Division",
        "name_bn": "ঢাকা বিভাগ",
        "latitude": 23.8103,
        "longitude": 90.4125,
        "description": "The capital region, known for its diverse culinary traditions and street food culture.",
        "description_de": "Die Hauptstadtregion, bekannt für ihre vielfältigen kulinarischen Traditionen und Straßenessenskultur.",
        "description_bn": "রাজধানী অঞ্চল, এর বৈচিত্র্যময় রন্ধনশৈলী এবং রাস্তার খাবার সংস্কৃতির জন্য পরিচিত।"
    },
    {
        "id": 2,
        "name": "Chittagong Division",
        "name_bn": "চট্টগ্রাম বিভাগ",
        "latitude": 22.3569,
        "longitude": 91.7832,
        "description": "Coastal region famous for seafood, especially hilsa fish and spicy curries.",
        "description_de": "Küstenregion, berühmt für Meeresfrüchte, besonders Hilsa-Fisch und scharfe Currys.",
        "description_bn": "উপকূলীয় অঞ্চল যা সামুদ্রিক খাবার, বিশেষত ইলিশ মাছ এবং ঝাল তরকারির জন্য বিখ্যাত।"
    },
    {
        "id": 3,
        "name": "Sylhet Division",
        "name_bn": "সিলেট বিভাগ",
        "latitude": 24.8949,
        "longitude": 91.8687,
        "description": "Tea country with unique culinary traditions, known for aromatic rice and distinctive spice blends.",
        "description_de": "Teeland mit einzigartigen kulinarischen Traditionen, bekannt für aromatischen Reis und besondere Gewürzmischungen.",
        "description_bn": "চা দেশ যার অনন্য রন্ধন ঐতিহ্য রয়েছে, সুগন্ধি চাল এবং বিশেষ মসলার মিশ্রণের জন্য পরিচিত।"
    }
]

# Ingredients data
INGREDIENTS = [
    {
        "id": 1,
        "name": "Mustard Oil",
        "name_de": "Senföl",
        "name_bn": "সরিষার তেল",
        "image": "/images/ingredients/mustard-oil.jpg",
        "flavor_notes": "Pungent, sharp, slightly bitter with a distinctive heat. The cornerstone of Bengali cooking.",
        "flavor_notes_de": "Scharf, stechend, leicht bitter mit charakteristischer Schärfe. Der Grundstein der bengalischen Küche.",
        "flavor_notes_bn": "তীব্র, ঝাঁঝালো, সামান্য তিক্ত একটি স্বতন্ত্র তাপ সহ। বাংলা রান্নার ভিত্তি।",
        "origin": "Extracted from mustard seeds, a staple in Bengal for over a thousand years. The oil is 'tempered' by heating until it smokes, mellowing its sharp flavor.",
        "origin_de": "Aus Senfsamen gewonnen, seit über tausend Jahren ein Grundnahrungsmittel in Bengalen. Das Öl wird durch Erhitzen bis zum Rauchen 'temperiert', wodurch sein scharfer Geschmack gemildert wird.",
        "origin_bn": "সরিষার বীজ থেকে নিষ্কাশিত, বাংলায় এক হাজার বছরেরও বেশি সময় ধরে একটি প্রধান উপাদান। তেলটি ধোঁয়া না হওয়া পর্যন্ত গরম করে 'টেম্পার' করা হয়, যা এর তীক্ষ্ণ স্বাদকে নরম করে।",
        "description": "The soul of Bengali cuisine, mustard oil brings a unique pungency and depth to dishes. When heated properly, it transforms from sharp to nutty and aromatic.",
        "description_de": "Die Seele der bengalischen Küche, Senföl verleiht Gerichten eine einzigartige Schärfe und Tiefe. Bei richtiger Erhitzung verwandelt es sich von scharf zu nussig und aromatisch.",
        "description_bn": "বাঙালি রন্ধনশিল্পের আত্মা, সরিষার তেল খাবারে একটি অনন্য তীব্রতা এবং গভীরতা নিয়ে আসে। সঠিকভাবে গরম করলে এটি তীক্ষ্ণ থেকে বাদামী এবং সুগন্ধযুক্ত হয়ে যায়।",
        "substitutions": ["Vegetable oil (less flavor)", "Canola oil + mustard powder", "Sesame oil (different flavor)"],
        "allergens": ["Mustard"]
    },
    {
        "id": 2,
        "name": "Green Chili",
        "name_de": "Grüne Chili",
        "name_bn": "কাঁচা মরিচ",
        "image": "/images/ingredients/green-chili.jpg",
        "flavor_notes": "Bright, grassy heat with a fresh, vegetal quality. More about flavor than just fire.",
        "flavor_notes_de": "Helle, grasige Schärfe mit frischer, pflanzlicher Qualität. Mehr Geschmack als nur Feuer.",
        "flavor_notes_bn": "তাজা, ঘাসের মতো ঝাল একটি সতেজ, উদ্ভিজ্জ গুণ সহ। শুধু আগুন নয় স্বাদের বিষয়ে আরও বেশি।",
        "origin": "Indigenous to Bangladesh, these slender chilies are picked young for their fresh, bright heat. Different from dried red chilies, they add vibrancy to dishes.",
        "origin_de": "Heimisch in Bangladesch, werden diese schlanken Chilis jung gepflückt für ihre frische, helle Schärfe. Anders als getrocknete rote Chilis verleihen sie Gerichten Lebendigkeit.",
        "origin_bn": "বাংলাদেশের স্থানীয়, এই পাতলা মরিচগুলি তাদের তাজা, উজ্জ্বল ঝালের জন্য অল্প বয়সে সংগ্রহ করা হয়। শুকনো লাল মরিচের থেকে ভিন্ন, এগুলি খাবারে প্রাণবন্ততা যোগ করে।",
        "description": "Essential for authentic Bengali flavor, green chilies provide heat, yes, but also a fresh, bright note that balances rich, oily dishes.",
        "description_de": "Wesentlich für authentischen bengalischen Geschmack, grüne Chilis bieten Schärfe, ja, aber auch eine frische, helle Note, die reichhaltige, ölige Gerichte ausgleicht.",
        "description_bn": "প্রামাণিক বাঙালি স্বাদের জন্য অপরিহার্য, কাঁচা মরিচ ঝাল দেয়, হ্যাঁ, কিন্তু একটি তাজা, উজ্জ্বল নোটও দেয় যা সমৃদ্ধ, তৈলাক্ত খাবারের ভারসাম্য রক্ষা করে।",
        "substitutions": ["Serrano peppers", "Jalapeños (milder)", "Thai bird chilies (hotter)"],
        "allergens": []
    },
    {
        "id": 3,
        "name": "Hilsa Fish",
        "name_de": "Hilsa-Fisch",
        "name_bn": "ইলিশ মাছ",
        "image": "/images/ingredients/hilsa-fish.jpg",
        "flavor_notes": "Rich, oily, intensely flavorful with a delicate texture. The 'king of fish' in Bengali cuisine.",
        "flavor_notes_de": "Reich, ölig, intensiv aromatisch mit zarter Textur. Der 'König der Fische' in der bengalischen Küche.",
        "flavor_notes_bn": "সমৃদ্ধ, তৈলাক্ত, নরম গঠন সহ তীব্রভাবে স্বাদযুক্ত। বাঙালি রন্ধনশিল্পে 'মাছের রাজা'।",
        "origin": "Anadromous fish that migrates from the Bay of Bengal up rivers to spawn. Considered the national fish of Bangladesh and deeply embedded in Bengali culture.",
        "origin_de": "Wanderfisch, der vom Golf von Bengalen flussaufwärts wandert, um zu laichen. Gilt als Nationalfisch von Bangladesch und ist tief in der bengalischen Kultur verwurzelt.",
        "origin_bn": "স্যালমন জাতীয় মাছ যা বঙ্গোপসাগর থেকে নদীতে ডিম পাড়ার জন্য স্থানান্তরিত হয়। বাংলাদেশের জাতীয় মাছ হিসাবে বিবেচিত এবং বাঙালি সংস্কৃতিতে গভীরভাবে প্রোথিত।",
        "description": "Hilsa is more than food in Bangladesh—it's culture, poetry, and passion. Its silver scales, numerous bones, and incomparable flavor make it a challenge and a treasure.",
        "description_de": "Hilsa ist in Bangladesch mehr als nur Essen – es ist Kultur, Poesie und Leidenschaft. Seine silbernen Schuppen, zahlreichen Gräten und unvergleichliche Geschmack machen es zu einer Herausforderung und einem Schatz.",
        "description_bn": "ইলিশ বাংলাদেশে শুধু খাবার নয়—এটি সংস্কৃতি, কবিতা এবং আবেগ। এর রূপালী আঁশ, অসংখ্য কাঁটা এবং অতুলনীয় স্বাদ এটিকে একটি চ্যালেঞ্জ এবং একটি সম্পদ করে তোলে।",
        "substitutions": ["Mackerel (similar oiliness)", "Sardines (smaller)", "Shad (closest relative)"],
        "allergens": ["Fish"]
    }
]

# Occasions data
OCCASIONS = [
    {
        "id": 1,
        "name": "Pohela Boishakh",
        "name_de": "Pohela Boishakh",
        "name_bn": "পহেলা বৈশাখ",
        "description": "Bengali New Year celebration, marked by traditional foods and festivities.",
        "description_de": "Bengalisches Neujahrsfest, gekennzeichnet durch traditionelle Speisen und Festlichkeiten.",
        "description_bn": "বাংলা নববর্ষ উদযাপন, ঐতিহ্যবাহী খাবার এবং উৎসব দ্বারা চিহ্নিত।",
        "date_type": "fixed",
        "month": 4,
        "day": 14,
        "season": None
    },
    {
        "id": 2,
        "name": "Eid-ul-Fitr",
        "name_de": "Eid-ul-Fitr",
        "name_bn": "ঈদুল ফিতর",
        "description": "Festival marking the end of Ramadan, celebrated with elaborate feasts.",
        "description_de": "Fest zum Ende des Ramadan, gefeiert mit aufwendigen Festmahlen.",
        "description_bn": "রমজানের সমাপ্তি চিহ্নিত করা উৎসব, বিস্তৃত ভোজের সাথে উদযাপন করা হয়।",
        "date_type": "lunar",
        "month": None,
        "day": None,
        "season": None
    },
    {
        "id": 3,
        "name": "Monsoon Season",
        "name_de": "Monsunzeit",
        "name_bn": "বর্ষাকাল",
        "description": "Rainy season when comfort foods like khichuri are most enjoyed.",
        "description_de": "Regenzeit, in der Wohlfühlessen wie Khichuri am meisten genossen werden.",
        "description_bn": "বর্ষাকাল যখন খিচুড়ির মতো আরামদায়ক খাবার সবচেয়ে বেশি উপভোগ করা হয়।",
        "date_type": "seasonal",
        "month": None,
        "day": None,
        "season": "monsoon"
    }
]

# Dishes data
DISHES = [
    {
        "id": 1,
        "name": "Ilish Bhaja",
        "name_de": "Gebratener Hilsa",
        "name_bn": "ইলিশ ভাজা",
        "hero_image": "/images/dishes/ilish-bhaja-hero.jpg",
        "hero_video": None,
        "region_id": 2,  # Chittagong
        "dietary_type": "pescatarian",
        "heat_level": 3,
        "what_it_is": "Fried hilsa fish, marinated in turmeric and salt, then shallow-fried in mustard oil until crispy and golden. Served with steamed rice and dal.",
        "what_it_is_de": "Gebratener Hilsa-Fisch, mariniert in Kurkuma und Salz, dann in Senföl flach gebraten bis knusprig und golden. Serviert mit gedämpftem Reis und Dal.",
        "what_it_is_bn": "ভাজা ইলিশ মাছ, হলুদ এবং লবণে মেরিনেট করা, তারপর সরিষার তেলে অগভীর ভাজা করা হয় যতক্ষণ না এটি কুঁচকুচে এবং সোনালী হয়। ভাপানো ভাত এবং ডালের সাথে পরিবেশন করা হয়।",
        "why_it_matters": "Hilsa is the national fish of Bangladesh and a cultural icon. This simple preparation lets the fish shine, celebrating its natural oils and delicate flavor. It's tradition on every Bengali's table.",
        "why_it_matters_de": "Hilsa ist der Nationalfisch von Bangladesch und eine kulturelle Ikone. Diese einfache Zubereitung lässt den Fisch glänzen und feiert seine natürlichen Öle und den delikaten Geschmack. Es ist Tradition auf jedem bengalischen Tisch.",
        "why_it_matters_bn": "ইলিশ বাংলাদেশের জাতীয় মাছ এবং একটি সাংস্কৃতিক প্রতীক। এই সাধারণ প্রস্তুতি মাছকে উজ্জ্বল হতে দেয়, এর প্রাকৃতিক তেল এবং সূক্ষ্ম স্বাদ উদযাপন করে। এটি প্রতিটি বাঙালির টেবিলে ঐতিহ্য।",
        "how_its_made": "Clean fish pieces are rubbed with turmeric and salt, then left to marinate briefly. Heat mustard oil until it smokes (this is crucial!), reduce heat, and fry the fish until golden and crispy. The bones remain—eating hilsa is an art.",
        "how_its_made_de": "Saubere Fischstücke werden mit Kurkuma und Salz eingerieben und kurz mariniert. Senföl erhitzen bis es raucht (das ist entscheidend!), Hitze reduzieren und den Fisch goldbraun und knusprig braten. Die Gräten bleiben—Hilsa essen ist eine Kunst.",
        "how_its_made_bn": "পরিষ্কার মাছের টুকরোগুলি হলুদ এবং লবণ দিয়ে ঘষে, তারপর সংক্ষিপ্তভাবে মেরিনেট করতে রেখে দেওয়া হয়। সরিষার তেল ধোঁয়া না হওয়া পর্যন্ত গরম করুন (এটি গুরুত্বপূর্ণ!), তাপ কমিয়ে দিন এবং মাছ সোনালী এবং কুঁচকুচে না হওয়া পর্যন্ত ভাজুন। কাঁটাগুলি থেকে যায়—ইলিশ খাওয়া একটি শিল্প।",
        "taste_texture": "Crispy, salty crust gives way to tender, oily fish. The mustard oil adds a sharp, nutty undertone. Rich, indulgent, and deeply satisfying. The numerous bones are part of the experience.",
        "taste_texture_de": "Knusprige, salzige Kruste gibt weichem, öligem Fisch Platz. Das Senföl fügt einen scharfen, nussigen Unterton hinzu. Reich, genussvoll und tief befriedigend. Die zahlreichen Gräten sind Teil des Erlebnisses.",
        "taste_texture_bn": "কুঁচকুচে, নোনা ভূত্বক নরম, তৈলাক্ত মাছকে পথ দেয়। সরিষার তেল একটি তীক্ষ্ণ, বাদামী আন্ডারটোন যোগ করে। সমৃদ্ধ, আনন্দদায়ক এবং গভীরভাবে সন্তোষজনক। অসংখ্য কাঁটা অভিজ্ঞতার অংশ।",
        "how_we_eat_it": "Traditionally served with plain white rice and dal (lentil soup). Use your hands! Break off pieces carefully, navigating the bones. Squeeze fresh lime on top. Pair with a simple vegetable side.",
        "how_we_eat_it_de": "Traditionell mit einfachem weißem Reis und Dal (Linsensuppe) serviert. Verwenden Sie Ihre Hände! Brechen Sie vorsichtig Stücke ab und navigieren Sie durch die Gräten. Frischen Limettensaft darüber träufeln. Mit einer einfachen Gemüsebeilage kombinieren.",
        "how_we_eat_it_bn": "ঐতিহ্যগতভাবে সাদা ভাত এবং ডাল (মসুর স্যুপ) এর সাথে পরিবেশন করা হয়। আপনার হাত ব্যবহার করুন! সাবধানে টুকরো ভেঙে ফেলুন, কাঁটাগুলির মধ্য দিয়ে নেভিগেট করুন। উপরে তাজা লেবু চিপুন। একটি সাধারণ সবজির পাশে জোড়া লাগান।",
        "fun_facts": "• Hilsa can have over 40 tiny bones\n• Monsoon hilsa is considered the most flavorful\n• There are poems written about hilsa in Bengali literature\n• The fish is so important it appears on Bangladeshi currency",
        "fun_facts_de": "• Hilsa kann über 40 winzige Gräten haben\n• Monsun-Hilsa gilt als am schmackhaftesten\n• Es gibt Gedichte über Hilsa in der bengalischen Literatur\n• Der Fisch ist so wichtig, dass er auf bangladeschischer Währung erscheint",
        "fun_facts_bn": "• ইলিশে 40 টিরও বেশি ছোট কাঁটা থাকতে পারে\n• মৌসুমী ইলিশকে সবচেয়ে সুস্বাদু বলে মনে করা হয়\n• বাংলা সাহিত্যে ইলিশ নিয়ে কবিতা লেখা হয়েছে\n• মাছটি এত গুরুত্বপূর্ণ যে এটি বাংলাদেশী মুদ্রায় দেখা যায়",
        "allergens": ["fish"],
        "prep_time_minutes": 30,
        "map_hint": "Especially popular in the coastal regions and during monsoon season",
        "gallery": [
            {
                "url": "/images/dishes/ilish-bhaja-1.jpg",
                "type": "image",
                "caption": "Golden crispy fried hilsa",
                "caption_de": "Goldener knuspriger gebratener Hilsa",
                "caption_bn": "সোনালী কুঁচকুচে ভাজা ইলিশ"
            },
            {
                "url": "/images/dishes/ilish-bhaja-2.jpg",
                "type": "image",
                "caption": "Traditional serving with rice and dal",
                "caption_de": "Traditionelle Servierung mit Reis und Dal",
                "caption_bn": "ভাত এবং ডালের সাথে ঐতিহ্যবাহী পরিবেশন"
            }
        ],
        "ingredient_ids": [1, 2, 3],  # Mustard oil, green chili, hilsa
        "occasion_ids": [3]  # Monsoon
    },
    {
        "id": 2,
        "name": "Tehari",
        "name_de": "Tehari",
        "name_bn": "তেহারি",
        "hero_image": "/images/dishes/tehari-hero.jpg",
        "hero_video": None,
        "region_id": 1,  # Dhaka
        "dietary_type": "meat",
        "heat_level": 2,
        "what_it_is": "Fragrant yellow rice cooked with tender beef or mutton, potatoes, and warm spices. Less elaborate than biryani, but equally loved. Street food royalty.",
        "what_it_is_de": "Duftreis gelb gekocht mit zartem Rind- oder Hammelfleisch, Kartoffeln und warmen Gewürzen. Weniger aufwendig als Biryani, aber ebenso beliebt. Straßenessen-Royalty.",
        "what_it_is_bn": "সুগন্ধি হলুদ চাল নরম গরু বা খাসির মাংস, আলু এবং উষ্ণ মসলা দিয়ে রান্না করা। বিরিয়ানির চেয়ে কম বিস্তৃত, কিন্তু সমানভাবে প্রিয়। রাস্তার খাবারের রাজকীয়তা।",
        "why_it_matters": "Born in Dhaka's old city, tehari represents accessible luxury—rich flavors without the ceremony of biryani. It's the working person's celebration meal, sold from street stalls and loved by all classes.",
        "why_it_matters_de": "Geboren in Dhakas Altstadt, repräsentiert Tehari zugänglichen Luxus – reiche Aromen ohne die Zeremonie von Biryani. Es ist das Festmahl der Arbeiter, von Straßenständen verkauft und von allen Schichten geliebt.",
        "why_it_matters_bn": "ঢাকার পুরাতন শহরে জন্মগ্রহণকারী, তেহারি সহজলভ্য বিলাসিতার প্রতিনিধিত্ব করে—বিরিয়ানির অনুষ্ঠান ছাড়াই সমৃদ্ধ স্বাদ। এটি শ্রমজীবীদের উদযাপনের খাবার, রাস্তার স্টল থেকে বিক্রি হয় এবং সব শ্রেণীর দ্বারা ভালোবাসা।",
        "how_its_made": "Marinate meat in yogurt and spices. Fry potatoes until golden. Layer partially cooked rice with meat and potatoes, add saffron or turmeric for color, seal the pot, and cook on low heat (dum) until everything melds into aromatic perfection.",
        "how_its_made_de": "Fleisch in Joghurt und Gewürzen marinieren. Kartoffeln goldbraun braten. Teils gekochten Reis mit Fleisch und Kartoffeln schichten, Safran oder Kurkuma für Farbe hinzufügen, Topf versiegeln und bei niedriger Hitze (Dum) kochen bis alles zu aromatischer Perfektion verschmilzt.",
        "how_its_made_bn": "মাংস দই এবং মসলায় মেরিনেট করুন। আলু সোনালী না হওয়া পর্যন্ত ভাজুন। আংশিকভাবে রান্না করা ভাত মাংস এবং আলু দিয়ে স্তর করুন, রঙের জন্য জাফরান বা হলুদ যোগ করুন, পাত্রটি সিল করুন এবং কম আঁচে (দম) রান্না করুন যতক্ষণ না সবকিছু সুগন্ধি পূর্ণতায় মিশে যায়।",
        "taste_texture": "Each grain of rice separate, tinted yellow-gold, fragrant with cumin, cardamom, and cinnamon. Tender meat falls apart, potatoes absorb all the spices. Comfort in a bowl.",
        "taste_texture_de": "Jedes Reiskorn separat, gelb-golden getönt, duftend nach Kreuzkümmel, Kardamom und Zimt. Zartes Fleisch zerfällt, Kartoffeln absorbieren alle Gewürze. Trost in einer Schüssel.",
        "taste_texture_bn": "চালের প্রতিটি দানা আলাদা, হলুদ-সোনার আভা, জিরা, এলাচ এবং দারচিনি দিয়ে সুগন্ধি। নরম মাংস আলাদা হয়ে যায়, আলু সমস্ত মসলা শুষে নেয়। একটি বাটিতে আরাম।",
        "how_we_eat_it": "Serve hot with borhani (spiced yogurt drink), sliced onions, and green chilies. Squeeze lime over everything. Often enjoyed as a Friday lunch treat or celebration meal. No cutlery needed—use your right hand.",
        "how_we_eat_it_de": "Heiß servieren mit Borhani (würziges Joghurtgetränk), geschnittenen Zwiebeln und grünen Chilis. Limette über alles träufeln. Oft als Freitag-Mittagessen oder Festmahl genossen. Kein Besteck nötig—rechte Hand verwenden.",
        "how_we_eat_it_bn": "বোরহানি (মসলাযুক্ত দই পানীয়), কাটা পেঁয়াজ এবং কাঁচা মরিচের সাথে গরম পরিবেশন করুন। সবকিছুর উপরে লেবু চিপুন। প্রায়শই শুক্রবারের দুপুরের খাবার বা উদযাপনের খাবার হিসাবে উপভোগ করা হয়। কোন কাটলারি দরকার নেই—ডান হাত ব্যবহার করুন।",
        "fun_facts": "• Tehari originated in Old Dhaka during the Mughal period\n• Unlike biryani, the rice and meat cook together\n• Best tehari is said to come from specific street vendors who've perfected their recipe over decades\n• The yellow color comes from turmeric, not saffron (keeping it affordable)",
        "fun_facts_de": "• Tehari entstand im alten Dhaka während der Mogulzeit\n• Im Gegensatz zu Biryani kochen Reis und Fleisch zusammen\n• Das beste Tehari soll von bestimmten Straßenverkäufern kommen, die ihr Rezept über Jahrzehnte perfektioniert haben\n• Die gelbe Farbe kommt von Kurkuma, nicht Safran (hält es erschwinglich)",
        "fun_facts_bn": "• তেহারি মোগল আমলে পুরাতন ঢাকায় উৎপত্তি হয়েছিল\n• বিরিয়ানির বিপরীতে, ভাত এবং মাংস একসাথে রান্না হয়\n• সেরা তেহারি নির্দিষ্ট রাস্তার বিক্রেতাদের থেকে আসে বলে বলা হয় যারা দশক ধরে তাদের রেসিপি নিখুঁত করেছে\n• হলুদ রঙ হলুদ থেকে আসে, জাফরান নয় (এটি সাশ্রয়ী রাখে)",
        "allergens": ["dairy"],
        "prep_time_minutes": 90,
        "map_hint": "Iconic dish of Old Dhaka, now found throughout Bangladesh",
        "gallery": [
            {
                "url": "/images/dishes/tehari-1.jpg",
                "type": "image",
                "caption": "Fragrant yellow rice with tender meat",
                "caption_de": "Duftender gelber Reis mit zartem Fleisch",
                "caption_bn": "নরম মাংসের সাথে সুগন্ধি হলুদ চাল"
            },
            {
                "url": "/images/dishes/tehari-2.jpg",
                "type": "image",
                "caption": "Street vendor preparing fresh tehari",
                "caption_de": "Straßenverkäufer bereitet frisches Tehari zu",
                "caption_bn": "রাস্তার বিক্রেতা তাজা তেহারি প্রস্তুত করছেন"
            }
        ],
        "ingredient_ids": [1, 2],  # Mustard oil, green chili
        "occasion_ids": [2]  # Eid
    },
    {
        "id": 3,
        "name": "Khichuri",
        "name_de": "Khichuri",
        "name_bn": "খিচুড়ি",
        "hero_image": "/images/dishes/khichuri-hero.jpg",
        "hero_video": None,
        "region_id": 3,  # Sylhet
        "dietary_type": "vegetarian",
        "heat_level": 1,
        "what_it_is": "A comforting one-pot dish of rice and lentils cooked together until creamy, spiced with cumin, bay leaves, and ginger. Bengali soul food.",
        "what_it_is_de": "Ein tröstliches Eintopfgericht aus Reis und Linsen, zusammen gekocht bis cremig, gewürzt mit Kreuzkümmel, Lorbeerblättern und Ingwer. Bengalisches Soulfood.",
        "what_it_is_bn": "ভাত এবং ডালের একটি আরামদায়ক এক-পাত্রের খাবার একসাথে রান্না করা হয় যতক্ষণ না ক্রিমি হয়, জিরা, তেজপাতা এবং আদা দিয়ে মসলাযুক্ত। বাঙালি আত্মার খাবার।",
        "why_it_matters": "The ultimate comfort food, khichuri is what mothers make when you're sick, what you crave during monsoon rains, and what brings families together. Simple, humble, beloved.",
        "why_it_matters_de": "Das ultimative Wohlfühlessen, Khichuri ist das, was Mütter machen, wenn man krank ist, wonach man sich während des Monsunregens sehnt und was Familien zusammenbringt. Einfach, bescheiden, geliebt.",
        "why_it_matters_bn": "চূড়ান্ত আরামদায়ক খাবার, খিচুড়ি হল যা মায়েরা তৈরি করেন যখন আপনি অসুস্থ থাকেন, যা আপনি বর্ষার বৃষ্টির সময় চান এবং যা পরিবারকে একত্রিত করে। সহজ, নম্র, প্রিয়।",
        "how_its_made": "Rinse rice and lentils. Temper whole spices in ghee or oil. Add rice, lentils, ginger, and water. Cook until everything breaks down into a creamy, porridge-like consistency. The longer it cooks, the better it gets.",
        "how_its_made_de": "Reis und Linsen spülen. Ganze Gewürze in Ghee oder Öl temperieren. Reis, Linsen, Ingwer und Wasser hinzufügen. Kochen bis alles zu einer cremigen, breiartigen Konsistenz zerfällt. Je länger es kocht, desto besser wird es.",
        "how_its_made_bn": "চাল এবং ডাল ধুয়ে ফেলুন। ঘি বা তেলে পুরো মসলা টেম্পার করুন। চাল, ডাল, আদা এবং জল যোগ করুন। সবকিছু একটি ক্রিমি, পোরিজের মতো সামঞ্জস্যে ভেঙে না যাওয়া পর্যন্ত রান্না করুন। এটি যত বেশি সময় রান্না হয়, তত ভাল হয়।",
        "taste_texture": "Creamy, mild, warming. Each spoonful is a hug. The spices whisper rather than shout. Ghee adds richness. It's simplicity perfected.",
        "taste_texture_de": "Cremig, mild, wärmend. Jeder Löffel ist eine Umarmung. Die Gewürze flüstern statt zu schreien. Ghee fügt Reichhaltigkeit hinzu. Es ist Einfachheit perfektioniert.",
        "taste_texture_bn": "ক্রিমি, মৃদু, উষ্ণতা। প্রতিটি চামচ একটি আলিঙ্গন। মসলা চিৎকার না করে ফিসফিস করে। ঘি সমৃদ্ধি যোগ করে। এটি পূর্ণতা সরলতা।",
        "how_we_eat_it": "Serve piping hot with fried eggplant (begun bhaja), omelette, or crispy fried fish. A dollop of ghee on top is traditional. Perfect for rainy days, lazy Sundays, or when you need comfort. Eat with a spoon.",
        "how_we_eat_it_de": "Heiß servieren mit gebratener Aubergine (Begun Bhaja), Omelett oder knusprig gebratenem Fisch. Ein Klecks Ghee obendrauf ist traditionell. Perfekt für regnerische Tage, faule Sonntage oder wenn man Trost braucht. Mit einem Löffel essen.",
        "how_we_eat_it_bn": "ভাজা বেগুন (বেগুন ভাজা), অমলেট বা কুঁচকুচে ভাজা মাছের সাথে গরম পরিবেশন করুন। উপরে একটি চামচ ঘি ঐতিহ্যবাহী। বৃষ্টির দিনের জন্য, অলস রবিবার বা যখন আপনার আরামের প্রয়োজন তখন নিখুঁত। একটি চামচ দিয়ে খান।",
        "fun_facts": "• Khichuri is the ancestor of British 'kedgeree'\n• There's a saying: 'Bhaat-kapor-mach' (rice-clothes-fish) are life's essentials, but on rainy days, it's just 'khichuri'\n• Every family has their own secret ratio of rice to lentils\n• It's considered auspicious to eat khichuri during certain religious occasions",
        "fun_facts_de": "• Khichuri ist der Vorfahre des britischen 'Kedgeree'\n• Es gibt ein Sprichwort: 'Bhaat-kapor-mach' (Reis-Kleider-Fisch) sind die Grundlagen des Lebens, aber an regnerischen Tagen ist es nur 'Khichuri'\n• Jede Familie hat ihr eigenes geheimes Verhältnis von Reis zu Linsen\n• Es gilt als glückverheißend, Khichuri während bestimmter religiöser Anlässe zu essen",
        "fun_facts_bn": "• খিচুড়ি ব্রিটিশ 'কেজেরি' এর পূর্বপুরুষ\n• একটি প্রবাদ আছে: 'ভাত-কাপড়-মাছ' জীবনের প্রয়োজনীয় জিনিস, কিন্তু বৃষ্টির দিনে, এটি শুধু 'খিচুড়ি'\n• প্রতিটি পরিবারের চাল এবং ডালের নিজস্ব গোপন অনুপাত রয়েছে\n• নির্দিষ্ট ধর্মীয় অনুষ্ঠানে খিচুড়ি খাওয়া শুভ বলে মনে করা হয়",
        "allergens": ["dairy"],
        "prep_time_minutes": 45,
        "map_hint": "Enjoyed throughout Bangladesh, especially during monsoon season",
        "gallery": [
            {
                "url": "/images/dishes/khichuri-1.jpg",
                "type": "image",
                "caption": "Creamy khichuri with fried eggplant",
                "caption_de": "Cremiges Khichuri mit gebratener Aubergine",
                "caption_bn": "ভাজা বেগুনের সাথে ক্রিমি খিচুড়ি"
            },
            {
                "url": "/images/dishes/khichuri-2.jpg",
                "type": "image",
                "caption": "Perfect rainy day comfort",
                "caption_de": "Perfekter Regentag-Trost",
                "caption_bn": "নিখুঁত বৃষ্টির দিনের আরাম"
            }
        ],
        "ingredient_ids": [1, 2],  # Mustard oil, green chili
        "occasion_ids": [3]  # Monsoon
    },
    {
        "id": 4,
        "name": "Kacchi Biryani",
        "name_de": "Kacchi Biryani",
        "name_bn": "কাচ্চি বিরিয়ানি",
        "hero_image": "/images/dishes/kacchi-biryani-hero.jpg",
        "hero_video": None,
        "region_id": 1,  # Dhaka
        "dietary_type": "meat",
        "heat_level": 3,
        "what_it_is": "A royal layered biryani where marinated raw mutton and half-cooked fragrant basmati rice are slow-cooked together in a sealed pot using the traditional 'dum' method. The ultimate celebration dish.",
        "what_it_is_de": "Ein königliches geschichtetes Biryani, bei dem mariniertes rohes Hammelfleisch und halbgekochter duftender Basmatireis in einem verschlossenen Topf nach der traditionellen 'Dum'-Methode langsam zusammen gekocht werden. Das ultimative Festessen.",
        "what_it_is_bn": "একটি রাজকীয় স্তরযুক্ত বিরিয়ানি যেখানে মেরিনেট করা কাঁচা মাটন এবং অর্ধ-রান্না করা সুগন্ধি বাসমতি চাল ঐতিহ্যবাহী 'দম' পদ্ধতি ব্যবহার করে একটি সিল করা পাত্রে একসাথে ধীরে রান্না করা হয়। চূড়ান্ত উদযাপনের খাবার।",
        "why_it_matters": "Kacchi Biryani is the crown jewel of Bangladeshi cuisine. Reserved for weddings, Eid, and grand celebrations, it represents hospitality, abundance, and culinary mastery. Making authentic kacchi is a rite of passage for cooks.",
        "why_it_matters_de": "Kacchi Biryani ist das Kronjuwel der bangladeschischen Küche. Reserviert für Hochzeiten, Eid und große Feiern, repräsentiert es Gastfreundschaft, Überfluss und kulinarische Meisterschaft. Die Zubereitung von authentischem Kacchi ist ein Initiationsritus für Köche.",
        "why_it_matters_bn": "কাচ্চি বিরিয়ানি বাংলাদেশী রন্ধনশিল্পের মুকুট রত্ন। বিবাহ, ঈদ এবং বড় উদযাপনের জন্য সংরক্ষিত, এটি আতিথেয়তা, প্রাচুর্য এবং রন্ধন দক্ষতার প্রতিনিধিত্ব করে। খাঁটি কাচ্চি তৈরি করা রান্নার জন্য একটি দীক্ষার অনুষ্ঠান।",
        "how_its_made": "Marinate mutton in yogurt, spices, saffron, and ghee for hours. Parboil basmati rice with whole spices. Layer raw marinated meat at the bottom of a heavy pot, top with partially cooked rice, fried onions, boiled eggs, and potatoes. Seal the pot tightly and cook on very low heat (dum) for 45-60 minutes. The steam and meat juices cook everything to perfection.",
        "how_its_made_de": "Hammelfleisch stundenlang in Joghurt, Gewürzen, Safran und Ghee marinieren. Basmatireis mit ganzen Gewürzen vorkochen. Rohes mariniertes Fleisch am Boden eines schweren Topfes schichten, mit teilweise gekochtem Reis, gebratenen Zwiebeln, gekochten Eiern und Kartoffeln belegen. Den Topf fest verschließen und 45-60 Minuten bei sehr schwacher Hitze (Dum) kochen. Der Dampf und die Fleischsäfte kochen alles zur Perfektion.",
        "how_its_made_bn": "মাটনকে দই, মসলা, জাফরান এবং ঘিতে ঘন্টার জন্য মেরিনেট করুন। পুরো মসলা দিয়ে বাসমতি চাল পার্বয়েল করুন। একটি ভারী পাত্রের নীচে কাঁচা মেরিনেট করা মাংস স্তর করুন, আংশিক রান্না করা চাল, ভাজা পেঁয়াজ, সেদ্ধ ডিম এবং আলু দিয়ে শীর্ষ করুন। পাত্রটি শক্তভাবে সিল করুন এবং 45-60 মিনিটের জন্য খুব কম তাপে (দম) রান্না করুন। বাষ্প এবং মাংসের রস সবকিছু পূর্ণতায় রান্না করে।",
        "taste_texture": "Each grain of rice is separate, infused with saffron and spices. The mutton falls off the bone, incredibly tender and flavorful. Layers of crispy fried onions add texture. The potatoes absorb all the rich flavors. Aromatic, indulgent, unforgettable.",
        "taste_texture_de": "Jedes Reiskorn ist separat, durchdrungen von Safran und Gewürzen. Das Hammelfleisch fällt vom Knochen, unglaublich zart und geschmackvoll. Schichten von knusprigen gebratenen Zwiebeln fügen Textur hinzu. Die Kartoffeln absorbieren alle reichen Aromen. Aromatisch, genussvoll, unvergesslich.",
        "taste_texture_bn": "চালের প্রতিটি দানা আলাদা, জাফরান এবং মসলা দিয়ে মিশ্রিত। মাটন হাড় থেকে পড়ে যায়, অবিশ্বাস্যভাবে কোমল এবং স্বাদযুক্ত। কুঁচকুচে ভাজা পেঁয়াজের স্তর টেক্সচার যোগ করে। আলু সমস্ত সমৃদ্ধ স্বাদ শোষণ করে। সুগন্ধযুক্ত, আনন্দদায়ক, অবিস্মরণীয়।",
        "how_we_eat_it": "Serve on a large platter, garnished with fried onions, boiled eggs, and fresh coriander. Traditionally eaten with hands from a communal plate. Pair with raita (yogurt sauce), salad, and borhani (spiced yogurt drink). Save room - portions are generous!",
        "how_we_eat_it_de": "Auf einer großen Platte servieren, garniert mit gebratenen Zwiebeln, gekochten Eiern und frischem Koriander. Traditionell mit den Händen von einem gemeinsamen Teller gegessen. Mit Raita (Joghurtsauce), Salat und Borhani (gewürztes Joghurtgetränk) kombinieren. Platz lassen - die Portionen sind großzügig!",
        "how_we_eat_it_bn": "একটি বড় থালায় পরিবেশন করুন, ভাজা পেঁয়াজ, সেদ্ধ ডিম এবং তাজা ধনে পাতা দিয়ে সাজান। ঐতিহ্যগতভাবে একটি সাম্প্রদায়িক প্লেট থেকে হাত দিয়ে খাওয়া হয়। রাইতা (দই সস), সালাদ এবং বোরহানি (মসলাযুক্ত দই পানীয়) এর সাথে জোড়া লাগান। জায়গা সংরক্ষণ করুন - অংশগুলি উদার!",
        "fun_facts": "• The word 'kacchi' means 'raw' - referring to the raw meat\n• Old Dhaka is famous for the best kacchi biryani in Bangladesh\n• A proper kacchi biryani pot should never be stirred during cooking\n• The 'dum' creates a unique aroma that fills the entire house\n• Premium kacchi uses pure ghee worth its weight in gold",
        "fun_facts_de": "• Das Wort 'Kacchi' bedeutet 'roh' - bezieht sich auf das rohe Fleisch\n• Alt-Dhaka ist berühmt für das beste Kacchi Biryani in Bangladesch\n• Ein richtiger Kacchi-Biryani-Topf sollte während des Kochens niemals gerührt werden\n• Das 'Dum' erzeugt ein einzigartiges Aroma, das das ganze Haus erfüllt\n• Premium-Kacchi verwendet reines Ghee, das sein Gewicht in Gold wert ist",
        "fun_facts_bn": "• 'কাচ্চি' শব্দের অর্থ 'কাঁচা' - কাঁচা মাংসকে বোঝায়\n• পুরাতন ঢাকা বাংলাদেশের সেরা কাচ্চি বিরিয়ানির জন্য বিখ্যাত\n• একটি সঠিক কাচ্চি বিরিয়ানি পাত্র রান্নার সময় কখনও নাড়ানো উচিত নয়\n• 'দম' একটি অনন্য সুবাস তৈরি করে যা পুরো বাড়ি ভরে দেয়\n• প্রিমিয়াম কাচ্চি খাঁটি ঘি ব্যবহার করে যা এর ওজনে সোনার মূল্যবান",
        "allergens": ["dairy", "eggs"],
        "prep_time_minutes": 180,
        "map_hint": "Most famous in Old Dhaka, now beloved across all of Bangladesh",
        "gallery": [
            {
                "url": "/images/dishes/kacchi-biryani-1.jpg",
                "type": "image",
                "caption": "Aromatic layers of rice and tender mutton",
                "caption_de": "Aromatische Schichten aus Reis und zartem Hammelfleisch",
                "caption_bn": "চাল এবং কোমল মাটনের সুগন্ধযুক্ত স্তর"
            },
            {
                "url": "/images/dishes/kacchi-biryani-2.jpg",
                "type": "image",
                "caption": "Garnished with fried onions, eggs, and potatoes",
                "caption_de": "Garniert mit gebratenen Zwiebeln, Eiern und Kartoffeln",
                "caption_bn": "ভাজা পেঁয়াজ, ডিম এবং আলু দিয়ে সাজানো"
            }
        ],
        "ingredient_ids": [1],  # Uses ghee (can add more ingredients as needed)
        "occasion_ids": [2]  # Eid (can add wedding occasion if you create one)
    }
]

