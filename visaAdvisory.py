import text
import visaAdvisoryData
from fuzzywuzzy import process, fuzz


english_short_to_full = {
    'usa': 'united states of america',
    'united states': 'united states of america',
    'uk': 'united kingdom',
    'russian federation': 'russia'
}
russian_to_english_profile_search = {
    'оаэ': 'uae',
    'сша': 'united States',
    'россия': "russia",
    'рф': "russia",
    'российская федерация': 'russia',
    'сингапур': 'singapore',
    'южная корея': 'south Korea',
    'финляндия': 'finland',
    'франция': 'france',
    'германия': 'germany',
    'испания': 'spain',
    'италия': 'italy',
    'япония': 'japan',
    'швеция': 'sweden',
    'великобритания': 'united Kingdom',
    'дания': 'denmark',
    'австрия': 'austria',
    'люксембург': 'luxembourg',
    'нидерланды': 'netherlands',
    'норвегия': 'norway',
    'ирландия': 'ireland',
    'бельгия': 'belgium',
    'соединенные штаты америки': 'united States',
    'канада': 'canada',
    'португалия': 'portugal',
    'швейцария': 'switzerland',
    'австралия': 'australia',
    'мальта': 'malta',
    'новая зеландия': 'new Zealand',
    'греция': 'greece',
    'чешская республика': 'czech Republic',
    'венгрия': 'hungary',
    'польша': 'poland',
    'словакия': 'slovakia',
    'исландия': 'iceland',
    'лихтенштейн': 'liechtenstein',
    'литва': 'lithuania',
    'эстония': 'estonia',
    'словения': 'slovenia',
    'латвия': 'latvia',
    'малайзия': 'malaysia',
    'монако': 'monaco',
    'кипр': 'cyprus',
    'объединенные арабские эмираты': 'united Arab Emirates',
    'румыния': 'romania',
    'болгария': 'bulgaria',
    'хорватия': 'croatia',
    'чили': 'chile',
    'сан-марино': 'san Marino',
    'андорра': 'andorra',
    'гонконг': 'hong Kong',
    'аргентина': 'argentina',
    'бразилия': 'brazil',
    'бруней': 'brunei',
    'барбадос': 'barbados',
    'израиль': 'israel',
    'багамы': 'bahamas',
    'мексика': 'mexico',
    'сейшелы': 'seychelles',
    'ватикан': 'vatican City',
    'сент-китс и невис': 'saint Kitts and Nevis',
    'уругвай': 'uruguay',
    'сент-винсент и гренадины': 'st. Vincent and the Grenadines',
    'антигуа и барбуда': 'antigua and Barbuda',
    'тринидад и тобаго': 'trinidad and Tobago',
    'коста-рика': 'costa Rica',
    'украина': 'ukraine',
    'маврикий': 'mauritius',
    'парагвай': 'paraguay',
    'тайвань': 'taiwan',
    'доминика': 'dominica',
    'сент-люсия': 'saint Lucia',
    'гренада': 'grenada',
    'панама': 'panama',
    'перу': 'peru',
    'гондурас': 'honduras',
    'гватемала': 'guatemala',
    'сербия': 'serbia',
    'колумбия': 'colombia',
    'сальвадор': 'el Salvador',
    'соломоновы острова': 'solomon Islands',
    'самоа': 'samoa',
    'никарагуа': 'nicaragua',
    'северная македония': 'north Macedonia',
    'тувалу': 'tuvalu',
    'черногория': 'montenegro',
    'тонга': 'tonga',
    'молдова': 'moldova',
    'грузия': 'georgia',
    'кирибати': 'kiribati',
    'маршалловы острова': 'marshall Islands',
    'венесуэла': 'venezuela',
    'палау': 'palau',
    'микронезия': 'micronesia',
    'албания': 'albania',
    'босния и герцеговина': 'bosnia and Herzegovina',
    'турция': 'turkey',
    'южная африка': 'south Africa',
    'катар': 'qatar',
    'белиз': 'belize',
    'кувейт': 'kuwait',
    'восточный тимор': 'timor-leste',
    'эквадор': 'ecuador',
    'вануату': 'vanuatu',
    'фиджи': 'fiji',
    'мальдивы': 'maldives',
    'бахрейн': 'bahrain',
    'науру': 'nauru',
    'ямайка': 'jamaica',
    'ботсвана': 'botswana',
    'гайана': 'guyana',
    'оман': 'oman',
    'саудовская аравия': 'saudi Arabia',
    'папуа-новая гвинея': 'papua New Guinea',
    'беларусь': 'belarus',
    'боливия': 'bolivia',
    'намибия': 'namibia',
    'таиланд': 'thailand',
    'суринам': 'suriname',
    'казахстан': 'kazakhstan',
    'лесото': 'lesotho',
    'индонезия': 'indonesia',
    'кения': 'kenya',
    'эсватини': 'eswatini',
    'малави': 'malawi',
    'китай': 'china',
    'танзания': 'tanzania',
    'доминиканская республика': 'dominican Republic',
    'замбия': 'zambia',
    'гамбия': 'gambia',
    'армения': 'armenia',
    'азербайджан': 'azerbaijan',
    'тунис': 'tunisia',
    'кабо-верде': 'cape Verde',
    'сьерра-леоне': 'sierra Leone',
    'гана': 'ghana',
    'уганда': 'uganda',
    'зимбабве': 'zimbabwe',
    'марокко': 'morocco',
    'филиппины': 'philippines',
    'руанда': 'rwanda',
    'киргизия': 'kyrgyzstan',
    'бенин': 'benin',
    'монголия': 'mongolia',
    'сан-томе и принсипи': 'sao Tome and Principe',
    'мозамбик': 'mozambique',
    'куба': 'cuba',
    'мадагаскар': 'madagascar',
    'узбекистан': 'uzbekistan',
    'буркина-фасо': 'burkina Faso',
    'габон': 'gabon',
    'таджикистан': 'tajikistan',
    'гвинея': 'guinea',
    'того': 'togo',
    'мавритания': 'mauritania',
    'экваториальная гвинея': 'equatorial Guinea',
    'сенегал': 'senegal',
    'нигер': 'niger',
    'гвинея-бисау': 'guinea-bissau',
    'индия': 'india',
    'мали': 'mali',
    'камбоджа': 'cambodia',
    'чад': 'chad',
    'бутан': 'bhutan',
    'коморы': 'comoros',
    'цар': 'central African Republic',
    'центральная африканская республика': 'central African Republic',
    'египет': 'egypt',
    'иордания': 'jordan',
    'алжир': 'algeria',
    'ангола': 'angola',
    'вьетнам': 'vietnam',
    'джибути': 'djibouti',
    'гаити': 'haiti',
    'лаос': 'laos',
    'либерия': 'liberia',
    'туркменистан': 'turkmenistan',
    'камерун': 'cameroon',
    'конго': 'congo',
    'бурунди': 'burundi',
    'нигерия': 'nigeria',
    'эфиопия': 'ethiopia',
    'южный судан': 'south Sudan',
    'иран': 'iran',
    'ливан': 'lebanon',
    'демократическая республика конго': 'democratic Republic of the Congo',
    'судан': 'sudan',
    'мьянма': 'myanmar',
    'косово': 'kosovo',
    'шри-ланка': 'sri Lanka',
    'эритрея': 'eritrea',
    'ливия': 'libya',
    'северная корея': 'north Korea',
    'непал': 'nepal',
    'палестина': 'palestinian Territories',
    'бангладеш': 'bangladesh',
    'йемен': 'yemen',
    'сомали': 'somalia',
    'пакистан': 'pakistan',
    'ирак': 'iraq',
    'сирия': 'syria',
    'афганистан': 'afghanistan'
}
countries = [
    'russian federation',
    'singapore',
    'south korea',
    'united kingdom',
    'finland',
    'france',
    'germany',
    'spain',
    'sweden',
    'italy',
    'japan',
    'austria',
    'luxembourg',
    'netherlands',
    'denmark',
    'united states of america',
    'usa',
    'uae',
    'uk'
    'belgium',
    'canada',
    'ireland',
    'norway',
    'australia',
    'portugal',
    'malta',
    'switzerland',
    'new zealand',
    'greece',
    'hungary',
    'czech republic',
    'poland',
    'liechtenstein',
    'lithuania',
    'slovakia',
    'iceland',
    'latvia',
    'estonia',
    'slovenia',
    'malaysia',
    'monaco',
    'cyprus',
    'united arab emirates',
    'romania',
    'bulgaria',
    'croatia',
    'chile',
    'san marino',
    'andorra',
    'hong kong',
    'argentina',
    'brazil',
    'brunei',
    'barbados',
    'israel',
    'bahamas',
    'mexico',
    'seychelles',
    'vatican city',
    'uruguay',
    'saint kitts and nevis',
    'st. vincent and the grenadines',
    'antigua and barbuda',
    'trinidad and tobago',
    'costa rica',
    'ukraine',
    'mauritius',
    'paraguay',
    'taiwan',
    'dominica',
    'macao',
    'saint lucia',
    'grenada',
    'panama',
    'peru',
    'honduras',
    'serbia',
    'guatemala',
    'colombia',
    'el salvador',
    'solomon islands',
    'samoa',
    'nicaragua',
    'north macedonia',
    'tuvalu',
    'montenegro',
    'tonga',
    'moldova',
    'georgia',
    'marshall islands',
    'kiribati',
    'venezuela',
    'palau',
    'micronesia',
    'albania',
    'bosnia and herzegovina',
    'turkey',
    'russia',
    'south africa',
    'qatar',
    'belize',
    'kuwait',
    'timor-leste',
    'ecuador',
    'vanuatu',
    'fiji',
    'maldives',
    'bahrain',
    'nauru',
    'botswana',
    'jamaica',
    'guyana',
    'saudi arabia',
    'oman',
    'papua new guinea',
    'belarus',
    'bolivia',
    'namibia',
    'thailand',
    'lesotho',
    'suriname',
    'kazakhstan',
    'kenya',
    'indonesia',
    'eswatini',
    'malawi',
    'china',
    'tanzania',
    'dominican republic',
    'zambia',
    'armenia',
    'azerbaijan',
    'gambia',
    'tunisia',
    'cape verde',
    'sierra leone',
    'uganda',
    'zimbabwe',
    'ghana',
    'morocco',
    'philippines',
    'kyrgyzstan',
    'rwanda',
    'benin',
    'mongolia',
    'sao tome and principe',
    'mozambique',
    'cuba',
    'uzbekistan',
    'madagascar',
    'burkina faso',
    'gabon',
    'tajikistan',
    'guinea',
    'cote d’ivoire (ivory coast)',
    'togo',
    'mauritania',
    'equatorial guinea',
    'senegal',
    'niger',
    'mali',
    'guinea-bissau',
    'cambodia',
    'chad',
    'india',
    'bhutan',
    'comoros',
    'central african republic',
    'angola',
    'egypt',
    'vietnam',
    'jordan',
    'algeria',
    'djibouti',
    'turkmenistan',
    'laos',
    'liberia',
    'haiti',
    'cameroon',
    'congo',
    'burundi',
    'nigeria',
    'ethiopia',
    'south sudan',
    'lebanon',
    'congo (dem. rep.)',
    'iran',
    'myanmar',
    'sudan',
    'kosovo',
    'sri lanka',
    'eritrea',
    'libya',
    'north korea',
    'nepal',
    'bangladesh',
    'palestinian territories',
    'yemen',
    'somalia',
    'pakistan',
    'iraq',
    'syria',
    'afghanistan']
countries_ru = [
    'россия',
    'сша',
    'рф',
    'сингапур',
    'южная корея',
    'финляндия',
    'франция',
    'германия',
    'испания',
    'италия',
    'япония',
    'швеция',
    'великобритания',
    'дания',
    'австрия',
    'люксембург',
    'нидерланды',
    'норвегия',
    'ирландия',
    'бельгия',
    'соединенные штаты америки',
    'канада',
    'португалия',
    'швейцария',
    'австралия',
    'мальта',
    'новая зеландия',
    'греция',
    'чешская республика',
    'венгрия',
    'польша',
    'словакия',
    'исландия',
    'лихтенштейн',
    'литва',
    'эстония',
    'словения',
    'латвия',
    'малайзия',
    'монако',
    'кипр',
    'объединенные арабские эмираты',
    'румыния',
    'болгария',
    'хорватия',
    'чили',
    'сан-марино',
    'андорра',
    'гонконг',
    'аргентина',
    'бразилия',
    'бруней',
    'барбадос',
    'израиль',
    'багамы',
    'мексика',
    'сейшелы',
    'ватикан',
    'сент-китс и невис',
    'уругвай',
    'сент-винсент и гренадины',
    'антигуа и барбуда',
    'тринидад и тобаго',
    'коста-рика',
    'украина',
    'маврикий',
    'парагвай',
    'тайвань',
    'доминика',
    'сент-люсия',
    'макао',
    'гренада',
    'панама',
    'перу',
    'гондурас',
    'гватемала',
    'сербия',
    'колумбия',
    'сальвадор',
    'соломоновы острова',
    'самоа',
    'никарагуа',
    'северная македония',
    'тувалу',
    'черногория',
    'тонга',
    'молдова',
    'грузия',
    'кирибати',
    'маршалловы острова',
    'венесуэла',
    'палау',
    'микронезия',
    'албания',
    'босния и герцеговина',
    'турция',
    'российская федерация',
    'южная африка',
    'катар',
    'белиз',
    'кувейт',
    'восточный тимор',
    'эквадор',
    'вануату',
    'фиджи',
    'мальдивы',
    'бахрейн',
    'науру',
    'ямайка',
    'ботсвана',
    'гайана',
    'оман',
    'саудовская аравия',
    'папуа-новая гвинея',
    'беларусь',
    'боливия',
    'намибия',
    'таиланд',
    'суринам',
    'казахстан',
    'лесото',
    'индонезия',
    'кения',
    'эсватини',
    'малави',
    'китай',
    'танзания',
    'доминиканская республика',
    'замбия',
    'гамбия',
    'армения',
    'азербайджан',
    'тунис',
    'кабо-верде',
    'сьерра-леоне',
    'гана',
    'уганда',
    'зимбабве',
    'марокко',
    'филиппины',
    'руанда',
    'киргизия',
    'бенин',
    'монголия',
    'сан-томе и принсипи',
    'мозамбик',
    'куба',
    'мадагаскар',
    'узбекистан',
    'буркина-фасо',
    'габон',
    'таджикистан',
    'гвинея',
    'того',
    'кот-д’ивуар',
    'мавритания',
    'экваториальная гвинея',
    'сенегал',
    'нигер',
    'гвинея-бисау',
    'индия',
    'мали',
    'камбоджа',
    'чад',
    'бутан',
    'коморы',
    'цар',
    'египет',
    'иордания',
    'алжир',
    'ангола',
    'вьетнам',
    'джибути',
    'гаити',
    'лаос',
    'либерия',
    'туркменистан',
    'камерун',
    'конго',
    'бурунди',
    'нигерия',
    'эфиопия',
    'южный судан',
    'иран',
    'ливан',
    'демократическая республика конго',
    'судан',
    'мьянма',
    'косово',
    'шри-ланка',
    'эритрея',
    'ливия',
    'северная корея',
    'непал',
    'государство палестина',
    'бангладеш',
    'йемен',
    'сомали',
    'пакистан',
    'ирак',
    'сирия',
    'афганистан',
]

russian_to_english = {
    'оаэ': 'uae',
    'сша': 'united states of america',
    'россия': "russia",
    'рф': "russia",
    'российская федерация': 'russia',
    'сингапур': 'singapore',
    'южная корея': 'south korea',
    'финляндия': 'finland',
    'франция': 'france',
    'германия': 'germany',
    'испания': 'spain',
    'италия': 'italy',
    'япония': 'japan',
    'швеция': 'sweden',
    'великобритания': 'united kingdom',
    'дания': 'denmark',
    'австрия': 'austria',
    'люксембург': 'luxembourg',
    'нидерланды': 'netherlands',
    'норвегия': 'norway',
    'ирландия': 'ireland',
    'бельгия': 'belgium',
    'соединенные штаты америки': 'united states of america',
    'канада': 'canada',
    'португалия': 'portugal',
    'швейцария': 'switzerland',
    'австралия': 'australia',
    'мальта': 'malta',
    'новая зеландия': 'new zealand',
    'греция': 'greece',
    'чешская республика': 'czech republic',
    'венгрия': 'hungary',
    'польша': 'poland',
    'словакия': 'slovakia',
    'исландия': 'iceland',
    'лихтенштейн': 'liechtenstein',
    'литва': 'lithuania',
    'эстония': 'estonia',
    'словения': 'slovenia',
    'латвия': 'latvia',
    'малайзия': 'malaysia',
    'монако': 'monaco',
    'кипр': 'cyprus',
    'объединенные арабские эмираты': 'united arab emirates',
    'румыния': 'romania',
    'болгария': 'bulgaria',
    'хорватия': 'croatia',
    'чили': 'chile',
    'сан-марино': 'san marino',
    'андорра': 'andorra',
    'гонконг': 'hong kong',
    'аргентина': 'argentina',
    'бразилия': 'brazil',
    'бруней': 'brunei',
    'барбадос': 'barbados',
    'израиль': 'israel',
    'багамы': 'bahamas',
    'мексика': 'mexico',
    'сейшелы': 'seychelles',
    'ватикан': 'vatican city',
    'сент-китс и невис': 'saint kitts and nevis',
    'уругвай': 'uruguay',
    'сент-винсент и гренадины': 'st. vincent and the grenadines',
    'антигуа и барбуда': 'antigua and barbuda',
    'тринидад и тобаго': 'trinidad and tobago',
    'коста-рика': 'costa rica',
    'украина': 'ukraine',
    'маврикий': 'mauritius',
    'парагвай': 'paraguay',
    'тайвань': 'taiwan',
    'доминика': 'dominica',
    'сент-люсия': 'saint lucia',
    'гренада': 'grenada',
    'панама': 'panama',
    'перу': 'peru',
    'гондурас': 'honduras',
    'гватемала': 'guatemala',
    'сербия': 'serbia',
    'колумбия': 'colombia',
    'сальвадор': 'el salvador',
    'соломоновы острова': 'solomon islands',
    'самоа': 'samoa',
    'никарагуа': 'nicaragua',
    'северная македония': 'north macedonia',
    'тувалу': 'tuvalu',
    'черногория': 'montenegro',
    'тонга': 'tonga',
    'молдова': 'moldova',
    'грузия': 'georgia',
    'кирибати': 'kiribati',
    'маршалловы острова': 'marshall islands',
    'венесуэла': 'venezuela',
    'палау': 'palau',
    'микронезия': 'micronesia',
    'албания': 'albania',
    'босния и герцеговина': 'bosnia and herzegovina',
    'турция': 'turkey',
    'южная африка': 'south africa',
    'катар': 'qatar',
    'белиз': 'belize',
    'кувейт': 'kuwait',
    'восточный тимор': 'timor-leste',
    'эквадор': 'ecuador',
    'вануату': 'vanuatu',
    'фиджи': 'fiji',
    'мальдивы': 'maldives',
    'бахрейн': 'bahrain',
    'науру': 'nauru',
    'ямайка': 'jamaica',
    'ботсвана': 'botswana',
    'гайана': 'guyana',
    'оман': 'oman',
    'саудовская аравия': 'saudi arabia',
    'папуа-новая гвинея': 'papua new guinea',
    'беларусь': 'belarus',
    'боливия': 'bolivia',
    'намибия': 'namibia',
    'таиланд': 'thailand',
    'суринам': 'suriname',
    'казахстан': 'kazakhstan',
    'лесото': 'lesotho',
    'индонезия': 'indonesia',
    'кения': 'kenya',
    'эсватини': 'eswatini',
    'малави': 'malawi',
    'китай': 'china',
    'танзания': 'tanzania',
    'доминиканская республика': 'dominican republic',
    'замбия': 'zambia',
    'гамбия': 'gambia',
    'армения': 'armenia',
    'азербайджан': 'azerbaijan',
    'тунис': 'tunisia',
    'кабо-верде': 'cape verde',
    'сьерра-леоне': 'sierra leone',
    'гана': 'ghana',
    'уганда': 'uganda',
    'зимбабве': 'zimbabwe',
    'марокко': 'morocco',
    'филиппины': 'philippines',
    'руанда': 'rwanda',
    'киргизия': 'kyrgyzstan',
    'бенин': 'benin',
    'монголия': 'mongolia',
    'сан-томе и принсипи': 'sao tome and principe',
    'мозамбик': 'mozambique',
    'куба': 'cuba',
    'мадагаскар': 'madagascar',
    'узбекистан': 'uzbekistan',
    'буркина-фасо': 'burkina faso',
    'габон': 'gabon',
    'таджикистан': 'tajikistan',
    'гвинея': 'guinea',
    'того': 'togo',
    'мавритания': 'mauritania',
    'экваториальная гвинея': 'equatorial guinea',
    'сенегал': 'senegal',
    'нигер': 'niger',
    'гвинея-бисау': 'guinea-bissau',
    'индия': 'india',
    'мали': 'mali',
    'камбоджа': 'cambodia',
    'чад': 'chad',
    'бутан': 'bhutan',
    'коморы': 'comoros',
    'цар': 'central african republic',
    'центральная африканская республика': 'central african republic',
    'египет': 'egypt',
    'иордания': 'jordan',
    'алжир': 'algeria',
    'ангола': 'angola',
    'вьетнам': 'vietnam',
    'джибути': 'djibouti',
    'гаити': 'haiti',
    'лаос': 'laos',
    'либерия': 'liberia',
    'туркменистан': 'turkmenistan',
    'камерун': 'cameroon',
    'конго': 'congo',
    'бурунди': 'burundi',
    'нигерия': 'nigeria',
    'эфиопия': 'ethiopia',
    'южный судан': 'south sudan',
    'иран': 'iran',
    'ливан': 'lebanon',
    'демократическая республика конго': 'democratic republic of the congo',
    'судан': 'sudan',
    'мьянма': 'myanmar',
    'косово': 'kosovo',
    'шри-ланка': 'sri lanka',
    'эритрея': 'eritrea',
    'ливия': 'libya',
    'северная корея': 'north korea',
    'непал': 'nepal',
    'палестина': 'palestinian territories',
    'бангладеш': 'bangladesh',
    'йемен': 'yemen',
    'сомали': 'somalia',
    'пакистан': 'pakistan',
    'ирак': 'iraq',
    'сирия': 'syria',
    'афганистан': 'afghanistan'
}


def getVisaAdvisory(citizenship, destination, language):
    try:
        if language == 'ru':
            passport = process.extractOne(citizenship.lower(), countries_ru, score_cutoff=75, scorer=fuzz.token_sort_ratio)
            to = process.extractOne(destination.lower(), countries_ru, score_cutoff=75, scorer=fuzz.token_sort_ratio)
            print(passport, to)
            passport = russian_to_english[passport[0].strip()].strip()
            to = russian_to_english[to[0].strip()].strip()
            print(passport,to)
        else:
            passport = process.extractOne(citizenship.lower(), countries, score_cutoff=75, scorer=fuzz.token_sort_ratio)[0].lower().strip()
            to = process.extractOne(destination.lower(), countries, score_cutoff=75, scorer=fuzz.token_sort_ratio)[0].lower().strip()
            if passport in english_short_to_full.keys():
                passport = english_short_to_full.get(passport)
            if to in english_short_to_full.keys():
                to = english_short_to_full.get(to)
            print(passport,to)
    except Exception:
        return text.try_again[language]
    first = visaAdvisoryData.countries[passport.strip()]
    print(first)
    if first is not None:
        for key in first.keys():
            if to.lower() in first[key]:
                if language == "ru":
                    return text.visaAdvisory[language][key]
                return key
