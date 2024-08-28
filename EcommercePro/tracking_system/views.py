
from django.shortcuts import render
import json
import os
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.

file_path = 'orders.csv'

#endpoint home
def home(request):

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        # Create a DataFrame
        df = pd.DataFrame({
            'orderID': [1, 2, 3],
            'orderName': ['Order A', 'Order B', 'Order C'],
            'userName': ['User 1', 'User 2', 'User 3'],
            'status': ['', '', '']
        })

        # Save the DataFrame to CSV
        df.to_csv(file_path, index=False)

    # Convert DataFrame to HTML for rendering
    df_html = df.to_html(classes='table table-striped')

    return render(request, 'home.html', {'df_html': df_html})


