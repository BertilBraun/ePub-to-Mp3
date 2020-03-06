import pyttsx3
from gtts import gTTS
from bs4 import BeautifulSoup
from ebooklib import epub, ITEM_DOCUMENT
from multiprocessing import Pool, cpu_count

def read_ePub(path) -> str:
	
	text = ""

	for doc in epub.read_epub(path).get_items_of_type(ITEM_DOCUMENT):
		text += BeautifulSoup(doc.get_content(), features="lxml").get_text()

	return text

engine = pyttsx3.init(driverName='sapi5')

def save(data):
	text = read_ePub(data[0])
	print("read File")

	engine.setProperty('voice', data[2])
	engine.setProperty('rate', 300)

	print("saving File " + data[1])
	engine.save_to_file(text=text,filename=data[1])
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

if __name__ == '__main__': 
	p = Pool(cpu_count())

	p.map(save, ([p, n + " Male.mp3", voices[1].id] for p, n in zip(paths, names)))
