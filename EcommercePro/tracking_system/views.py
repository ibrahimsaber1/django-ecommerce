import json
import os
import pandas as pd
from django.shortcuts import render
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

    return render(request, 'tr/home.html', {'df_html': df_html})


# -------------------------------------------------------------------
# this function to display the html form :)
# -------------------------------------------------------------------

def add_order(request):
    return render(request, 'tr/add_order.html')



@csrf_exempt
@require_http_methods(["POST"])
def postdata(request):
    try:
        # Check if the request is sending JSON data
        if request.content_type == 'application/json':
            # Parse JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
        else:
            # If not JSON, assume form data is being sent
            data = request.POST

        # Extract fields from the data
        order_id = data.get('orderID')
        order_name = data.get('orderName')
        user_name = data.get('userName')
        status = data.get('status')

        # Check if all required fields are present
        if not all([order_id, order_name, user_name, status]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        # Check if file exists, if not create it with headers
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
        else:
            df = pd.DataFrame(columns=['orderID', 'orderName', 'userName', 'status'])

        # Create a new DataFrame for the new data
        new_data = pd.DataFrame([{
            'orderID': order_id,
            'orderName': order_name,
            'userName': user_name,
            'status': status
        }])

        # Concatenate the new data to the existing DataFrame
        df = pd.concat([df, new_data], ignore_index=True)

        # Save updated DataFrame to CSV
        df.to_csv(file_path, index=False)

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Data saved successfully'}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
