import json
from sqlalchemy import insert
from app.models.surah import Surah
from app.models.verse import Verse
from app.models.topic import Topic, verse_topic
# from app.models.versetopic import VerseTopic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

with open('../scrapper/results/quran-ayah.json', encoding="utf8") as f:
    quran = json.load(f)
with open('../scrapper/results/surah.json', encoding="utf8") as f:
    qsurah = json.load(f)
with open('../scrapper/results/en.asad.json', encoding="utf8") as f:
    en_ayah = json.load(f)
with open('../scrapper/results/v2-topics-quran.json', encoding="utf8") as f:
    vtopics = json.load(f)

surah = {}
surahname = {}
verses = {}
verse_id = 1
for verse in quran['data']:
    l_surah = verse['surah']
    if l_surah['id'] not in verses:
        verses[l_surah['id']] = {
            verse['ayah']: {
                'id': verse_id,
                'juz': verse['juz'],
                'ayah': verse['ayah'],
                'arabic': verse['arabic'],
                'latin': verse['latin'],
                'id_translation': verse['translation'],
            }
        }
    else:
        verses[l_surah['id']][verse['ayah']] = {
            'id': verse_id,
            'juz': verse['juz'],
            'ayah': verse['ayah'],
            'arabic': verse['arabic'],
            'latin': verse['latin'],
            'id_translation': verse['translation'],
        }
    surah[l_surah['id']] = l_surah
    sname = l_surah['transliteration'].replace("'",'')
    sname = sname.replace('‘','')
    sname = sname.replace('-','')
    surahname[sname] = l_surah['id']
    verse_id += 1

for verse in qsurah['data']:
    surah[verse['number']]['enTranslate'] = verse['englishNameTranslation']

for s in en_ayah['data']['surahs']:
    for verse in s['ayahs']:
        verses[s['number']][verse['numberInSurah']]['en_translate'] = verse['text'].strip('"')
# print(surah)
# print(surahname)
topicsrqt = {}
iv = 1
for t in vtopics:
    surah_number = 0
    sname = t['surah'].replace("'",'')
    sname = sname.replace("-",'')

    # print(verses[31])
    # exit()
    if sname in surahname:
        surah_number = surahname[sname]
    # print(f"{sname}, {surah_number}, {t['surah']}")
    if t['topic'] in topicsrqt:
        for ayat in t['ayat']:
            topicsrqt[t['topic']]['verse_ids'].append(verses[surah_number][ayat]['id'])
        continue
    else:
        rs = []
        for ayat in t['ayat']:
            rs.append(verses[surah_number][ayat]['id'])
        topicsrqt[t['topic']] = {
            'topic' : t['topic'],
            # 'topicID': t['topicID'],
            'topicID': '',
            'surah_number': surah_number,
            'id': iv,
            'verse_ids': rs
        }
        iv += 1

# print(vtopics)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
dbuser = os.environ.get("DB_USER")
dbpass = os.environ.get("DB_PASS")
dbname = os.environ.get("DB_NAME")
dbhost = os.environ.get("DB_HOST")
DATABASE_URL = f"postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()
# print(topicsrqt)

objects = [

]
for k,i in surah.items():
    objects.append(
        Surah(id=i['id'],arabic=i['arabic'], latin=i['latin'], revelation_type=i['location'],
              number_of_verse=i['num_ayah'], id_translation=i['translation'], en_translation=i['enTranslate'])
    )
session.bulk_save_objects(objects)
session.commit()

sql_verses = []

# print(verses[2])
for k,surah in verses.items():
    for n, verse in surah.items():
        sql_verses.append(
            Verse(
                id=verse['id'], surah_id=k, verse_number=verse['ayah'],
                juz=verse['juz'], arabic=verse['arabic'], latin=verse['latin'],
                id_translation=verse['id_translation'], en_translation= verse['en_translate'],
            )
        )

session.bulk_save_objects(sql_verses)
session.commit()

print(topicsrqt)
sql_topic = []
sql_verse_topic = []
tov_id = 1
for k, t in topicsrqt.items():
    sql_topic.append(
        Topic(
            id=t['id'], en_title = t['topic'], id_title = t['topicID']
        ))
    for to_v in t['verse_ids']:
        sql_verse_topic.append(
            verse_topic.insert().values(topic_id=t['id'], verse_id=to_v)
        )
        tov_id+=1

session.bulk_save_objects(sql_topic)
for x in sql_verse_topic:
    session.execute(x)
session.commit()