mi_texto = '"Taller"' #Al usar comillas de diferente tipo no interfieren
mi_texto2 = "de \"Python\"" # El \ hace que se ignore el caracter siguiente para que no cierre comillas

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

texto_unido = mi_texto + "\n " + mi_texto2 #Salta de linea
print(texto_unido)

texto_unido = mi_texto + "\t " + mi_texto2 #Tabula
print(texto_unido)

texto_unido = mi_texto + "\r " + mi_texto2 #Borra lo anterior
print(texto_unido)