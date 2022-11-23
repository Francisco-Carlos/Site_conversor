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
