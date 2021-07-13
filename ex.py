def dados():
  
  arquivo = open('dados.txt', 'a')
  dict = {'Empresa': '', 'CNPJ': int, 'Status': ''}

  empresa = input("Qual o nome da empresa?: ")
  dict['Empresa'] = empresa

  while True:
    try:
      status = "Inativo"
      cnpj = int(input("Digite o CNPJ: "))
      dict['CNPJ'] = cnpj

      convertido = str(cnpj)
      if len(convertido) >= 15 or len(convertido) <= 13:
        print("CNPJ inválido")
        
      elif len(convertido) == 14:
        status = "Ativo"
        arquivo.write(f"""
  \nEmpresa: {dict['Empresa']}
  CNPJ: {dict['CNPJ']}
  Status: {status}""")
        
        break

    except ValueError:
      print("CNPJ inválido")
    

dados()