<h1 align="center">Site de conversão</h1>
<p align='center'>Site para converter CSV em Excel e Excel em CSV</p>
<p aling="center"> <img src="https://img.shields.io/static/v1?label=Python&message=3.10&color=7159c1&style=for-the-badge&logo=ghost"/>
<img src="https://img.shields.io/static/v1?label=Pandas&message=1.5.2&color=7159c1&style=for-the-badge&logo=ghost"/> </p>

<p align="center">
 <a href="#Sobre">Sobre </a> --
 <a href="#Funcionamento">Como fuciona </a>  --
 <a href="#Imagens">Imagens </a>  --
 <a href="#Codigos">Codigos </a>  --
 <a href="#tecnologia">Tecnologia </a> --
</p>
<h4 align="center"> 
	 Python 🚀 Concluido...  
</h4>

<h2 align="center" id="Sobre">Sobre</h2>
<p> O projeto e simples o foco dele e fazer com que as pessoas, precisarem converter os arquivos em texto puro ou em Excel
e nao tiver nem um modo de fazer isso utilizando programas pode usar o site que e rapido e eficiente. </p>



<h2 align="center" id="#Funcionamento"> Funcionamento </h2>
<p> E simples você escolhe o arquivo que para converter escolhe a extenção que ele vai sair, utilizando o pandas ele vai converter
depois desse processo vai ser feito o dawload do arquivo com o formato desejado.

<h2 align="center" id="Imagens"> Imagens</h2>

![Index Seth Pandas](https://user-images.githubusercontent.com/30003984/203645191-1286c598-d474-4c87-aeec-8627141af6c2.png)


<h2 align="center" id="Codigos"> Codigo </h2>
*** <p>Formulario</p> ***

```from django import forms

tipo_de_planilhas = (
    ('1', 'CSV'),
    ('2', 'EXCEL'),
)


class UploadFileForm(forms.Form):
    file = forms.FileField()
    options = forms.ChoiceField(choices=tipo_de_planilhas)
    widgets = {
        file: forms.FileInput(),
        options: forms.SelectMultiple(),
    }
```

***<p>Views</p>***

```
import csv
import io

import xlrd
from django.shortcuts import render
import pandas as pd
from io import BytesIO



from django.http import HttpResponseRedirect, HttpResponse
from .form import UploadFileForm

# Create your views here.

def index(request):
    form = UploadFileForm()
    return render(request,'index.html',{'form':form})

def pandas(request):
    if request.method == 'POST':
        form = UploadFileForm( request.POST ,request.FILES)
        if form.is_valid():
            pad = request.FILES['file']
            tip = request.POST['options']

            if tip == '1':
                test = pd.read_excel(pad)
                test.to_csv('arquivo.csv',encoding='utf-8', index=True)
                response = HttpResponse( content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename=Arquivo.csv'
                col = csv.writer(response)
                col.writerow(test.columns)
                for index, row in test.iterrows():
                    col.writerow(row)
                return response
            elif tip == '2':
                #baixar
                df = pd.read_csv(pad)
                with BytesIO() as b:
                    writer = pd.ExcelWriter(b, engine='xlsxwriter')
                    df.to_excel(writer,sheet_name='Planilha', index=False)
                    writer.save()
                    filename = 'Arquivo.xls'
                    response = HttpResponse(
                        b.getvalue(),
                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    )
                    response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
    else:
        form = UploadFileForm()
    return render(request,'index.html',{'form':form})

```

### As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pandas](https://pandas.pydata.org/)
