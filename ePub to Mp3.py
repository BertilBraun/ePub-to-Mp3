
import pyttsx3
from gtts import gTTS
from bs4 import BeautifulSoup
from ebooklib import epub, ITEM_DOCUMENT

def read_ePub(path) -> str:
	
	text = ""

	for doc in epub.read_epub(path).get_items_of_type(ITEM_DOCUMENT):
		text += BeautifulSoup(doc.get_content(), features="lxml").get_text()

	return text

engine = pyttsx3.init(driverName='sapi5')

def save(path, to_save_to, voice_id):
	text = read_ePub(path)
	print("read File")

	engine.setProperty('voice', voice_id)
	engine.setProperty('rate', 300)

	print("saving File " + to_save_to)
	engine.save_to_file(text=text,filename=to_save_to)
	engine.runAndWait()
	print("saved File")

voices = engine.getProperty('voices')

paths = [
	"C:/Users/Braun/Calibre Library/Yuval Noah Harari/Homo Deus_ A Brief History of Tomorr (4)/Homo Deus_ A Brief History of T - Yuval Noah Harari.epub",
	"C:/Users/Braun/Calibre Library/Yuval Noah Harari/21 Lessons for the 21st Century (7)/21 Lessons for the 21st Century - Yuval Noah Harari.epub",
	"C:/Users/Braun/Calibre Library/Yuval Noah Harari/Sapiens_ A Brief History of Humankin (6)/Sapiens_ A Brief History of Hum - Yuval Noah Harari.epub"
]
names = [
	"Homo Deus",
	"21 Lessons for the 21st Century",
	"Sapiens"	
]

for p, n in zip(paths, names):
	save(p, n + " Male.mp3", voices[1].id)
	save(p, n + " Female.mp3", voices[2].id)
