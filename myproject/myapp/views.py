import pandas as pd
from django import forms
from django.shortcuts import render, redirect

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select an Excel or CSV file', required=True)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                if file.name.endswith('.csv'):
                    data = pd.read_csv(file)
                elif file.name.endswith('.xls') or file.name.endswith('.xlsx'):
                    data = pd.read_excel(file)
                else:
                    return render(request, 'upload.html', {
                        'form': form,
                        'error': 'File type not supported. Please upload a CSV or Excel file.'
                    })
                
                # Display the first few rows of the data
                return render(request, 'upload.html', {
                    'form': form,
                    'data': data.head().to_html(classes='table table-striped')
                })
            except Exception as e:
                return render(request, 'upload.html', {
                    'form': form,
                    'error': f'Error processing file: {str(e)}'
                })
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def home(request):
    return redirect('upload_file')  # Redirect to the upload page
