import re
text = "Contactez moi sur onsrajhi7@gmail.com ou sur +21688888"
#extraire email
email = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print("email founded" , email)