import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
re.search(patron, texto).group()