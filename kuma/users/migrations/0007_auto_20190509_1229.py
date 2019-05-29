# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-09 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_pytz_2018_9'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timezone',
            field=models.CharField(blank=True, choices=[('Africa', [('Africa/Abidjan', 'Abidjan (GMT+0000)'), ('Africa/Accra', 'Accra (GMT+0000)'), ('Africa/Addis_Ababa', 'Addis Ababa (GMT+0300)'), ('Africa/Algiers', 'Algiers (GMT+0100)'), ('Africa/Asmara', 'Asmara (GMT+0300)'), ('Africa/Bamako', 'Bamako (GMT+0000)'), ('Africa/Bangui', 'Bangui (GMT+0100)'), ('Africa/Banjul', 'Banjul (GMT+0000)'), ('Africa/Bissau', 'Bissau (GMT+0000)'), ('Africa/Blantyre', 'Blantyre (GMT+0200)'), ('Africa/Brazzaville', 'Brazzaville (GMT+0100)'), ('Africa/Bujumbura', 'Bujumbura (GMT+0200)'), ('Africa/Cairo', 'Cairo (GMT+0200)'), ('Africa/Casablanca', 'Casablanca (GMT+0000)'), ('Africa/Ceuta', 'Ceuta (GMT+0200)'), ('Africa/Conakry', 'Conakry (GMT+0000)'), ('Africa/Dakar', 'Dakar (GMT+0000)'), ('Africa/Dar_es_Salaam', 'Dar es Salaam (GMT+0300)'), ('Africa/Djibouti', 'Djibouti (GMT+0300)'), ('Africa/Douala', 'Douala (GMT+0100)'), ('Africa/El_Aaiun', 'El Aaiun (GMT+0000)'), ('Africa/Freetown', 'Freetown (GMT+0000)'), ('Africa/Gaborone', 'Gaborone (GMT+0200)'), ('Africa/Harare', 'Harare (GMT+0200)'), ('Africa/Johannesburg', 'Johannesburg (GMT+0200)'), ('Africa/Juba', 'Juba (GMT+0300)'), ('Africa/Kampala', 'Kampala (GMT+0300)'), ('Africa/Khartoum', 'Khartoum (GMT+0200)'), ('Africa/Kigali', 'Kigali (GMT+0200)'), ('Africa/Kinshasa', 'Kinshasa (GMT+0100)'), ('Africa/Lagos', 'Lagos (GMT+0100)'), ('Africa/Libreville', 'Libreville (GMT+0100)'), ('Africa/Lome', 'Lome (GMT+0000)'), ('Africa/Luanda', 'Luanda (GMT+0100)'), ('Africa/Lubumbashi', 'Lubumbashi (GMT+0200)'), ('Africa/Lusaka', 'Lusaka (GMT+0200)'), ('Africa/Malabo', 'Malabo (GMT+0100)'), ('Africa/Maputo', 'Maputo (GMT+0200)'), ('Africa/Maseru', 'Maseru (GMT+0200)'), ('Africa/Mbabane', 'Mbabane (GMT+0200)'), ('Africa/Mogadishu', 'Mogadishu (GMT+0300)'), ('Africa/Monrovia', 'Monrovia (GMT+0000)'), ('Africa/Nairobi', 'Nairobi (GMT+0300)'), ('Africa/Ndjamena', 'Ndjamena (GMT+0100)'), ('Africa/Niamey', 'Niamey (GMT+0100)'), ('Africa/Nouakchott', 'Nouakchott (GMT+0000)'), ('Africa/Ouagadougou', 'Ouagadougou (GMT+0000)'), ('Africa/Porto-Novo', 'Porto-Novo (GMT+0100)'), ('Africa/Sao_Tome', 'Sao Tome (GMT+0000)'), ('Africa/Tripoli', 'Tripoli (GMT+0200)'), ('Africa/Tunis', 'Tunis (GMT+0100)'), ('Africa/Windhoek', 'Windhoek (GMT+0200)')]), ('America', [('America/Adak', 'Adak (GMT-0900)'), ('America/Anchorage', 'Anchorage (GMT-0800)'), ('America/Anguilla', 'Anguilla (GMT-0400)'), ('America/Antigua', 'Antigua (GMT-0400)'), ('America/Araguaina', 'Araguaina (GMT-0300)'), ('America/Argentina/Buenos_Aires', 'Buenos Aires (GMT-0300)'), ('America/Argentina/Catamarca', 'Catamarca (GMT-0300)'), ('America/Argentina/Cordoba', 'Cordoba (GMT-0300)'), ('America/Argentina/Jujuy', 'Jujuy (GMT-0300)'), ('America/Argentina/La_Rioja', 'La Rioja (GMT-0300)'), ('America/Argentina/Mendoza', 'Mendoza (GMT-0300)'), ('America/Argentina/Rio_Gallegos', 'Rio Gallegos (GMT-0300)'), ('America/Argentina/Salta', 'Salta (GMT-0300)'), ('America/Argentina/San_Juan', 'San Juan (GMT-0300)'), ('America/Argentina/San_Luis', 'San Luis (GMT-0300)'), ('America/Argentina/Tucuman', 'Tucuman (GMT-0300)'), ('America/Argentina/Ushuaia', 'Ushuaia (GMT-0300)'), ('America/Aruba', 'Aruba (GMT-0400)'), ('America/Asuncion', 'Asuncion (GMT-0400)'), ('America/Atikokan', 'Atikokan (GMT-0500)'), ('America/Bahia', 'Bahia (GMT-0300)'), ('America/Bahia_Banderas', 'Bahia Banderas (GMT-0500)'), ('America/Barbados', 'Barbados (GMT-0400)'), ('America/Belem', 'Belem (GMT-0300)'), ('America/Belize', 'Belize (GMT-0600)'), ('America/Blanc-Sablon', 'Blanc-Sablon (GMT-0400)'), ('America/Boa_Vista', 'Boa Vista (GMT-0400)'), ('America/Bogota', 'Bogota (GMT-0500)'), ('America/Boise', 'Boise (GMT-0600)'), ('America/Cambridge_Bay', 'Cambridge Bay (GMT-0600)'), ('America/Campo_Grande', 'Campo Grande (GMT-0400)'), ('America/Cancun', 'Cancun (GMT-0500)'), ('America/Caracas', 'Caracas (GMT-0400)'), ('America/Cayenne', 'Cayenne (GMT-0300)'), ('America/Cayman', 'Cayman (GMT-0500)'), ('America/Chicago', 'Chicago (GMT-0500)'), ('America/Chihuahua', 'Chihuahua (GMT-0600)'), ('America/Costa_Rica', 'Costa Rica (GMT-0600)'), ('America/Creston', 'Creston (GMT-0700)'), ('America/Cuiaba', 'Cuiaba (GMT-0400)'), ('America/Curacao', 'Curacao (GMT-0400)'), ('America/Danmarkshavn', 'Danmarkshavn (GMT+0000)'), ('America/Dawson', 'Dawson (GMT-0700)'), ('America/Dawson_Creek', 'Dawson Creek (GMT-0700)'), ('America/Denver', 'Denver (GMT-0600)'), ('America/Detroit', 'Detroit (GMT-0400)'), ('America/Dominica', 'Dominica (GMT-0400)'), ('America/Edmonton', 'Edmonton (GMT-0600)'), ('America/Eirunepe', 'Eirunepe (GMT-0500)'), ('America/El_Salvador', 'El Salvador (GMT-0600)'), ('America/Fort_Nelson', 'Fort Nelson (GMT-0700)'), ('America/Fortaleza', 'Fortaleza (GMT-0300)'), ('America/Glace_Bay', 'Glace Bay (GMT-0300)'), ('America/Godthab', 'Godthab (GMT-0200)'), ('America/Goose_Bay', 'Goose Bay (GMT-0300)'), ('America/Grand_Turk', 'Grand Turk (GMT-0400)'), ('America/Grenada', 'Grenada (GMT-0400)'), ('America/Guadeloupe', 'Guadeloupe (GMT-0400)'), ('America/Guatemala', 'Guatemala (GMT-0600)'), ('America/Guayaquil', 'Guayaquil (GMT-0500)'), ('America/Guyana', 'Guyana (GMT-0400)'), ('America/Halifax', 'Halifax (GMT-0300)'), ('America/Havana', 'Havana (GMT-0400)'), ('America/Hermosillo', 'Hermosillo (GMT-0700)'), ('America/Indiana/Indianapolis', 'Indianapolis (GMT-0400)'), ('America/Indiana/Knox', 'Knox (GMT-0500)'), ('America/Indiana/Marengo', 'Marengo (GMT-0400)'), ('America/Indiana/Petersburg', 'Petersburg (GMT-0400)'), ('America/Indiana/Tell_City', 'Tell City (GMT-0500)'), ('America/Indiana/Vevay', 'Vevay (GMT-0400)'), ('America/Indiana/Vincennes', 'Vincennes (GMT-0400)'), ('America/Indiana/Winamac', 'Winamac (GMT-0400)'), ('America/Inuvik', 'Inuvik (GMT-0600)'), ('America/Iqaluit', 'Iqaluit (GMT-0400)'), ('America/Jamaica', 'Jamaica (GMT-0500)'), ('America/Juneau', 'Juneau (GMT-0800)'), ('America/Kentucky/Louisville', 'Louisville (GMT-0400)'), ('America/Kentucky/Monticello', 'Monticello (GMT-0400)'), ('America/Kralendijk', 'Kralendijk (GMT-0400)'), ('America/La_Paz', 'La Paz (GMT-0400)'), ('America/Lima', 'Lima (GMT-0500)'), ('America/Los_Angeles', 'Los Angeles (GMT-0700)'), ('America/Lower_Princes', 'Lower Princes (GMT-0400)'), ('America/Maceio', 'Maceio (GMT-0300)'), ('America/Managua', 'Managua (GMT-0600)'), ('America/Manaus', 'Manaus (GMT-0400)'), ('America/Marigot', 'Marigot (GMT-0400)'), ('America/Martinique', 'Martinique (GMT-0400)'), ('America/Matamoros', 'Matamoros (GMT-0500)'), ('America/Mazatlan', 'Mazatlan (GMT-0600)'), ('America/Menominee', 'Menominee (GMT-0500)'), ('America/Merida', 'Merida (GMT-0500)'), ('America/Metlakatla', 'Metlakatla (GMT-0800)'), ('America/Mexico_City', 'Mexico City (GMT-0500)'), ('America/Miquelon', 'Miquelon (GMT-0200)'), ('America/Moncton', 'Moncton (GMT-0300)'), ('America/Monterrey', 'Monterrey (GMT-0500)'), ('America/Montevideo', 'Montevideo (GMT-0300)'), ('America/Montserrat', 'Montserrat (GMT-0400)'), ('America/Nassau', 'Nassau (GMT-0400)'), ('America/New_York', 'New York (GMT-0400)'), ('America/Nipigon', 'Nipigon (GMT-0400)'), ('America/Nome', 'Nome (GMT-0800)'), ('America/Noronha', 'Noronha (GMT-0200)'), ('America/North_Dakota/Beulah', 'Beulah (GMT-0500)'), ('America/North_Dakota/Center', 'Center (GMT-0500)'), ('America/North_Dakota/New_Salem', 'New Salem (GMT-0500)'), ('America/Ojinaga', 'Ojinaga (GMT-0600)'), ('America/Panama', 'Panama (GMT-0500)'), ('America/Pangnirtung', 'Pangnirtung (GMT-0400)'), ('America/Paramaribo', 'Paramaribo (GMT-0300)'), ('America/Phoenix', 'Phoenix (GMT-0700)'), ('America/Port-au-Prince', 'Port-au-Prince (GMT-0400)'), ('America/Port_of_Spain', 'Port of Spain (GMT-0400)'), ('America/Porto_Velho', 'Porto Velho (GMT-0400)'), ('America/Puerto_Rico', 'Puerto Rico (GMT-0400)'), ('America/Punta_Arenas', 'Punta Arenas (GMT-0300)'), ('America/Rainy_River', 'Rainy River (GMT-0500)'), ('America/Rankin_Inlet', 'Rankin Inlet (GMT-0500)'), ('America/Recife', 'Recife (GMT-0300)'), ('America/Regina', 'Regina (GMT-0600)'), ('America/Resolute', 'Resolute (GMT-0500)'), ('America/Rio_Branco', 'Rio Branco (GMT-0500)'), ('America/Santarem', 'Santarem (GMT-0300)'), ('America/Santiago', 'Santiago (GMT-0400)'), ('America/Santo_Domingo', 'Santo Domingo (GMT-0400)'), ('America/Sao_Paulo', 'Sao Paulo (GMT-0300)'), ('America/Scoresbysund', 'Scoresbysund (GMT+0000)'), ('America/Sitka', 'Sitka (GMT-0800)'), ('America/St_Barthelemy', 'St Barthelemy (GMT-0400)'), ('America/St_Johns', 'St Johns (GMT-0230)'), ('America/St_Kitts', 'St Kitts (GMT-0400)'), ('America/St_Lucia', 'St Lucia (GMT-0400)'), ('America/St_Thomas', 'St Thomas (GMT-0400)'), ('America/St_Vincent', 'St Vincent (GMT-0400)'), ('America/Swift_Current', 'Swift Current (GMT-0600)'), ('America/Tegucigalpa', 'Tegucigalpa (GMT-0600)'), ('America/Thule', 'Thule (GMT-0300)'), ('America/Thunder_Bay', 'Thunder Bay (GMT-0400)'), ('America/Tijuana', 'Tijuana (GMT-0700)'), ('America/Toronto', 'Toronto (GMT-0400)'), ('America/Tortola', 'Tortola (GMT-0400)'), ('America/Vancouver', 'Vancouver (GMT-0700)'), ('America/Whitehorse', 'Whitehorse (GMT-0700)'), ('America/Winnipeg', 'Winnipeg (GMT-0500)'), ('America/Yakutat', 'Yakutat (GMT-0800)'), ('America/Yellowknife', 'Yellowknife (GMT-0600)')]), ('Antarctica', [('Antarctica/Casey', 'Casey (GMT+0800)'), ('Antarctica/Davis', 'Davis (GMT+0700)'), ('Antarctica/DumontDUrville', 'DumontDUrville (GMT+1000)'), ('Antarctica/Macquarie', 'Macquarie (GMT+1100)'), ('Antarctica/Mawson', 'Mawson (GMT+0500)'), ('Antarctica/McMurdo', 'McMurdo (GMT+1200)'), ('Antarctica/Palmer', 'Palmer (GMT-0300)'), ('Antarctica/Rothera', 'Rothera (GMT-0300)'), ('Antarctica/Syowa', 'Syowa (GMT+0300)'), ('Antarctica/Troll', 'Troll (GMT+0200)'), ('Antarctica/Vostok', 'Vostok (GMT+0600)')]), ('Arctic', [('Arctic/Longyearbyen', 'Longyearbyen (GMT+0200)')]), ('Asia', [('Asia/Aden', 'Aden (GMT+0300)'), ('Asia/Almaty', 'Almaty (GMT+0600)'), ('Asia/Amman', 'Amman (GMT+0300)'), ('Asia/Anadyr', 'Anadyr (GMT+1200)'), ('Asia/Aqtau', 'Aqtau (GMT+0500)'), ('Asia/Aqtobe', 'Aqtobe (GMT+0500)'), ('Asia/Ashgabat', 'Ashgabat (GMT+0500)'), ('Asia/Atyrau', 'Atyrau (GMT+0500)'), ('Asia/Baghdad', 'Baghdad (GMT+0300)'), ('Asia/Bahrain', 'Bahrain (GMT+0300)'), ('Asia/Baku', 'Baku (GMT+0400)'), ('Asia/Bangkok', 'Bangkok (GMT+0700)'), ('Asia/Barnaul', 'Barnaul (GMT+0700)'), ('Asia/Beirut', 'Beirut (GMT+0300)'), ('Asia/Bishkek', 'Bishkek (GMT+0600)'), ('Asia/Brunei', 'Brunei (GMT+0800)'), ('Asia/Chita', 'Chita (GMT+0900)'), ('Asia/Choibalsan', 'Choibalsan (GMT+0800)'), ('Asia/Colombo', 'Colombo (GMT+0530)'), ('Asia/Damascus', 'Damascus (GMT+0300)'), ('Asia/Dhaka', 'Dhaka (GMT+0600)'), ('Asia/Dili', 'Dili (GMT+0900)'), ('Asia/Dubai', 'Dubai (GMT+0400)'), ('Asia/Dushanbe', 'Dushanbe (GMT+0500)'), ('Asia/Famagusta', 'Famagusta (GMT+0300)'), ('Asia/Gaza', 'Gaza (GMT+0300)'), ('Asia/Hebron', 'Hebron (GMT+0300)'), ('Asia/Ho_Chi_Minh', 'Ho Chi Minh (GMT+0700)'), ('Asia/Hong_Kong', 'Hong Kong (GMT+0800)'), ('Asia/Hovd', 'Hovd (GMT+0700)'), ('Asia/Irkutsk', 'Irkutsk (GMT+0800)'), ('Asia/Jakarta', 'Jakarta (GMT+0700)'), ('Asia/Jayapura', 'Jayapura (GMT+0900)'), ('Asia/Jerusalem', 'Jerusalem (GMT+0300)'), ('Asia/Kabul', 'Kabul (GMT+0430)'), ('Asia/Kamchatka', 'Kamchatka (GMT+1200)'), ('Asia/Karachi', 'Karachi (GMT+0500)'), ('Asia/Kathmandu', 'Kathmandu (GMT+0545)'), ('Asia/Khandyga', 'Khandyga (GMT+0900)'), ('Asia/Kolkata', 'Kolkata (GMT+0530)'), ('Asia/Krasnoyarsk', 'Krasnoyarsk (GMT+0700)'), ('Asia/Kuala_Lumpur', 'Kuala Lumpur (GMT+0800)'), ('Asia/Kuching', 'Kuching (GMT+0800)'), ('Asia/Kuwait', 'Kuwait (GMT+0300)'), ('Asia/Macau', 'Macau (GMT+0800)'), ('Asia/Magadan', 'Magadan (GMT+1100)'), ('Asia/Makassar', 'Makassar (GMT+0800)'), ('Asia/Manila', 'Manila (GMT+0800)'), ('Asia/Muscat', 'Muscat (GMT+0400)'), ('Asia/Nicosia', 'Nicosia (GMT+0300)'), ('Asia/Novokuznetsk', 'Novokuznetsk (GMT+0700)'), ('Asia/Novosibirsk', 'Novosibirsk (GMT+0700)'), ('Asia/Omsk', 'Omsk (GMT+0600)'), ('Asia/Oral', 'Oral (GMT+0500)'), ('Asia/Phnom_Penh', 'Phnom Penh (GMT+0700)'), ('Asia/Pontianak', 'Pontianak (GMT+0700)'), ('Asia/Pyongyang', 'Pyongyang (GMT+0900)'), ('Asia/Qatar', 'Qatar (GMT+0300)'), ('Asia/Qostanay', 'Qostanay (GMT+0600)'), ('Asia/Qyzylorda', 'Qyzylorda (GMT+0500)'), ('Asia/Riyadh', 'Riyadh (GMT+0300)'), ('Asia/Sakhalin', 'Sakhalin (GMT+1100)'), ('Asia/Samarkand', 'Samarkand (GMT+0500)'), ('Asia/Seoul', 'Seoul (GMT+0900)'), ('Asia/Shanghai', 'Shanghai (GMT+0800)'), ('Asia/Singapore', 'Singapore (GMT+0800)'), ('Asia/Srednekolymsk', 'Srednekolymsk (GMT+1100)'), ('Asia/Taipei', 'Taipei (GMT+0800)'), ('Asia/Tashkent', 'Tashkent (GMT+0500)'), ('Asia/Tbilisi', 'Tbilisi (GMT+0400)'), ('Asia/Tehran', 'Tehran (GMT+0430)'), ('Asia/Thimphu', 'Thimphu (GMT+0600)'), ('Asia/Tokyo', 'Tokyo (GMT+0900)'), ('Asia/Tomsk', 'Tomsk (GMT+0700)'), ('Asia/Ulaanbaatar', 'Ulaanbaatar (GMT+0800)'), ('Asia/Urumqi', 'Urumqi (GMT+0600)'), ('Asia/Ust-Nera', 'Ust-Nera (GMT+1000)'), ('Asia/Vientiane', 'Vientiane (GMT+0700)'), ('Asia/Vladivostok', 'Vladivostok (GMT+1000)'), ('Asia/Yakutsk', 'Yakutsk (GMT+0900)'), ('Asia/Yangon', 'Yangon (GMT+0630)'), ('Asia/Yekaterinburg', 'Yekaterinburg (GMT+0500)'), ('Asia/Yerevan', 'Yerevan (GMT+0400)')]), ('Atlantic', [('Atlantic/Azores', 'Azores (GMT+0000)'), ('Atlantic/Bermuda', 'Bermuda (GMT-0300)'), ('Atlantic/Canary', 'Canary (GMT+0100)'), ('Atlantic/Cape_Verde', 'Cape Verde (GMT-0100)'), ('Atlantic/Faroe', 'Faroe (GMT+0100)'), ('Atlantic/Madeira', 'Madeira (GMT+0100)'), ('Atlantic/Reykjavik', 'Reykjavik (GMT+0000)'), ('Atlantic/South_Georgia', 'South Georgia (GMT-0200)'), ('Atlantic/St_Helena', 'St Helena (GMT+0000)'), ('Atlantic/Stanley', 'Stanley (GMT-0300)')]), ('Australia', [('Australia/Adelaide', 'Adelaide (GMT+0930)'), ('Australia/Brisbane', 'Brisbane (GMT+1000)'), ('Australia/Broken_Hill', 'Broken Hill (GMT+0930)'), ('Australia/Currie', 'Currie (GMT+1000)'), ('Australia/Darwin', 'Darwin (GMT+0930)'), ('Australia/Eucla', 'Eucla (GMT+0845)'), ('Australia/Hobart', 'Hobart (GMT+1000)'), ('Australia/Lindeman', 'Lindeman (GMT+1000)'), ('Australia/Lord_Howe', 'Lord Howe (GMT+1030)'), ('Australia/Melbourne', 'Melbourne (GMT+1000)'), ('Australia/Perth', 'Perth (GMT+0800)'), ('Australia/Sydney', 'Sydney (GMT+1000)')]), ('Canada', [('Canada/Atlantic', 'Atlantic (GMT-0300)'), ('Canada/Central', 'Central (GMT-0500)'), ('Canada/Eastern', 'Eastern (GMT-0400)'), ('Canada/Mountain', 'Mountain (GMT-0600)'), ('Canada/Newfoundland', 'Newfoundland (GMT-0230)'), ('Canada/Pacific', 'Pacific (GMT-0700)')]), ('Europe', [('Europe/Amsterdam', 'Amsterdam (GMT+0200)'), ('Europe/Andorra', 'Andorra (GMT+0200)'), ('Europe/Astrakhan', 'Astrakhan (GMT+0400)'), ('Europe/Athens', 'Athens (GMT+0300)'), ('Europe/Belgrade', 'Belgrade (GMT+0200)'), ('Europe/Berlin', 'Berlin (GMT+0200)'), ('Europe/Bratislava', 'Bratislava (GMT+0200)'), ('Europe/Brussels', 'Brussels (GMT+0200)'), ('Europe/Bucharest', 'Bucharest (GMT+0300)'), ('Europe/Budapest', 'Budapest (GMT+0200)'), ('Europe/Busingen', 'Busingen (GMT+0200)'), ('Europe/Chisinau', 'Chisinau (GMT+0300)'), ('Europe/Copenhagen', 'Copenhagen (GMT+0200)'), ('Europe/Dublin', 'Dublin (GMT+0100)'), ('Europe/Gibraltar', 'Gibraltar (GMT+0200)'), ('Europe/Guernsey', 'Guernsey (GMT+0100)'), ('Europe/Helsinki', 'Helsinki (GMT+0300)'), ('Europe/Isle_of_Man', 'Isle of Man (GMT+0100)'), ('Europe/Istanbul', 'Istanbul (GMT+0300)'), ('Europe/Jersey', 'Jersey (GMT+0100)'), ('Europe/Kaliningrad', 'Kaliningrad (GMT+0200)'), ('Europe/Kiev', 'Kiev (GMT+0300)'), ('Europe/Kirov', 'Kirov (GMT+0300)'), ('Europe/Lisbon', 'Lisbon (GMT+0100)'), ('Europe/Ljubljana', 'Ljubljana (GMT+0200)'), ('Europe/London', 'London (GMT+0100)'), ('Europe/Luxembourg', 'Luxembourg (GMT+0200)'), ('Europe/Madrid', 'Madrid (GMT+0200)'), ('Europe/Malta', 'Malta (GMT+0200)'), ('Europe/Mariehamn', 'Mariehamn (GMT+0300)'), ('Europe/Minsk', 'Minsk (GMT+0300)'), ('Europe/Monaco', 'Monaco (GMT+0200)'), ('Europe/Moscow', 'Moscow (GMT+0300)'), ('Europe/Oslo', 'Oslo (GMT+0200)'), ('Europe/Paris', 'Paris (GMT+0200)'), ('Europe/Podgorica', 'Podgorica (GMT+0200)'), ('Europe/Prague', 'Prague (GMT+0200)'), ('Europe/Riga', 'Riga (GMT+0300)'), ('Europe/Rome', 'Rome (GMT+0200)'), ('Europe/Samara', 'Samara (GMT+0400)'), ('Europe/San_Marino', 'San Marino (GMT+0200)'), ('Europe/Sarajevo', 'Sarajevo (GMT+0200)'), ('Europe/Saratov', 'Saratov (GMT+0400)'), ('Europe/Simferopol', 'Simferopol (GMT+0300)'), ('Europe/Skopje', 'Skopje (GMT+0200)'), ('Europe/Sofia', 'Sofia (GMT+0300)'), ('Europe/Stockholm', 'Stockholm (GMT+0200)'), ('Europe/Tallinn', 'Tallinn (GMT+0300)'), ('Europe/Tirane', 'Tirane (GMT+0200)'), ('Europe/Ulyanovsk', 'Ulyanovsk (GMT+0400)'), ('Europe/Uzhgorod', 'Uzhgorod (GMT+0300)'), ('Europe/Vaduz', 'Vaduz (GMT+0200)'), ('Europe/Vatican', 'Vatican (GMT+0200)'), ('Europe/Vienna', 'Vienna (GMT+0200)'), ('Europe/Vilnius', 'Vilnius (GMT+0300)'), ('Europe/Volgograd', 'Volgograd (GMT+0400)'), ('Europe/Warsaw', 'Warsaw (GMT+0200)'), ('Europe/Zagreb', 'Zagreb (GMT+0200)'), ('Europe/Zaporozhye', 'Zaporozhye (GMT+0300)'), ('Europe/Zurich', 'Zurich (GMT+0200)')]), ('GMT', [('GMT', 'GMT (GMT+0000)')]), ('Indian', [('Indian/Antananarivo', 'Antananarivo (GMT+0300)'), ('Indian/Chagos', 'Chagos (GMT+0600)'), ('Indian/Christmas', 'Christmas (GMT+0700)'), ('Indian/Cocos', 'Cocos (GMT+0630)'), ('Indian/Comoro', 'Comoro (GMT+0300)'), ('Indian/Kerguelen', 'Kerguelen (GMT+0500)'), ('Indian/Mahe', 'Mahe (GMT+0400)'), ('Indian/Maldives', 'Maldives (GMT+0500)'), ('Indian/Mauritius', 'Mauritius (GMT+0400)'), ('Indian/Mayotte', 'Mayotte (GMT+0300)'), ('Indian/Reunion', 'Reunion (GMT+0400)')]), ('Pacific', [('Pacific/Apia', 'Apia (GMT+1300)'), ('Pacific/Auckland', 'Auckland (GMT+1200)'), ('Pacific/Bougainville', 'Bougainville (GMT+1100)'), ('Pacific/Chatham', 'Chatham (GMT+1245)'), ('Pacific/Chuuk', 'Chuuk (GMT+1000)'), ('Pacific/Easter', 'Easter (GMT-0600)'), ('Pacific/Efate', 'Efate (GMT+1100)'), ('Pacific/Enderbury', 'Enderbury (GMT+1300)'), ('Pacific/Fakaofo', 'Fakaofo (GMT+1300)'), ('Pacific/Fiji', 'Fiji (GMT+1200)'), ('Pacific/Funafuti', 'Funafuti (GMT+1200)'), ('Pacific/Galapagos', 'Galapagos (GMT-0600)'), ('Pacific/Gambier', 'Gambier (GMT-0900)'), ('Pacific/Guadalcanal', 'Guadalcanal (GMT+1100)'), ('Pacific/Guam', 'Guam (GMT+1000)'), ('Pacific/Honolulu', 'Honolulu (GMT-1000)'), ('Pacific/Kiritimati', 'Kiritimati (GMT+1400)'), ('Pacific/Kosrae', 'Kosrae (GMT+1100)'), ('Pacific/Kwajalein', 'Kwajalein (GMT+1200)'), ('Pacific/Majuro', 'Majuro (GMT+1200)'), ('Pacific/Marquesas', 'Marquesas (GMT-0930)'), ('Pacific/Midway', 'Midway (GMT-1100)'), ('Pacific/Nauru', 'Nauru (GMT+1200)'), ('Pacific/Niue', 'Niue (GMT-1100)'), ('Pacific/Norfolk', 'Norfolk (GMT+1100)'), ('Pacific/Noumea', 'Noumea (GMT+1100)'), ('Pacific/Pago_Pago', 'Pago Pago (GMT-1100)'), ('Pacific/Palau', 'Palau (GMT+0900)'), ('Pacific/Pitcairn', 'Pitcairn (GMT-0800)'), ('Pacific/Pohnpei', 'Pohnpei (GMT+1100)'), ('Pacific/Port_Moresby', 'Port Moresby (GMT+1000)'), ('Pacific/Rarotonga', 'Rarotonga (GMT-1000)'), ('Pacific/Saipan', 'Saipan (GMT+1000)'), ('Pacific/Tahiti', 'Tahiti (GMT-1000)'), ('Pacific/Tarawa', 'Tarawa (GMT+1200)'), ('Pacific/Tongatapu', 'Tongatapu (GMT+1300)'), ('Pacific/Wake', 'Wake (GMT+1200)'), ('Pacific/Wallis', 'Wallis (GMT+1200)')]), ('US', [('US/Alaska', 'Alaska (GMT-0800)'), ('US/Arizona', 'Arizona (GMT-0700)'), ('US/Central', 'Central (GMT-0500)'), ('US/Eastern', 'Eastern (GMT-0400)'), ('US/Hawaii', 'Hawaii (GMT-1000)'), ('US/Mountain', 'Mountain (GMT-0600)'), ('US/Pacific', 'Pacific (GMT-0700)')]), ('UTC', [('UTC', 'UTC (GMT+0000)')])], default=b'US/Pacific', max_length=42, verbose_name='Timezone'),
        ),
    ]
