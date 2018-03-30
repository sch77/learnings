

dummy_file = open("c:\dummy.txt");

print(callable(file))

codeInString = "import string\ncity = \"34Bangalore\" \nmod_city = string.translate(city,None,\"0123456789\")\nprint(mod_city)"
result = compile(codeInString,"scratch","exec")
exec(result)