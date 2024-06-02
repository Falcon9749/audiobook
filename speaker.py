import pyttsx3
import pdfplumber

# inicializando a engine de NLP
engine = pyttsx3.init()

# lendo o arquivo PDF
pdf = pdfplumber.open('O elefante em apuros.pdf')

# gerando lista de páginas do livro (exceto as páginas, 1, 2, 27, 28 e 29!)
paginas = pdf.pages[2:-3]

texto_livro = ''
for pagina in paginas:
   texto_livro +=  pagina.extract_text()
   
texto_final = texto_livro.replace('.', '. ').replace(',', ', ')

engine.save_to_file(texto_final, 'audiobook.mp3')
engine.runAndWait()
