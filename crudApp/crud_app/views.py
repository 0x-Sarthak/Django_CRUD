from django.shortcuts import render, redirect

# This dictionary will simulate our "database"
data = {
    'Alice': {'age': 25, 'city': 'New York'},
    'Bob': {'age': 30, 'city': 'San Francisco'},
    'Carol': {'age': 28, 'city': 'Los Angeles'}
}

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        data[name] = {'age': age, 'city': city}
        print(data)
        return redirect('/read')
    return render(request, 'create.html')

def read(request):
    return render(request, 'read.html', {'data': data})

def update(request):
    keys = data.keys()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name in data:
            data_entry = data[name]
            age = request.POST.get('age')
            city = request.POST.get('city')
            data_entry['age'] = age
            data_entry['city'] = city
        return redirect('/read')
    return render(request, 'update.html', {'keys': keys})


def delete(request):
    keys = data.keys()
    if request.method == 'POST':
        name = request.POST.get('name')
        print("Deleting entry:", name)  # Add this line
        if name in data:
            del data[name]
            print("Entry deleted:", name)  # Add this line
        return redirect('/read')
    return render(request, 'delete.html', {'keys': keys})

