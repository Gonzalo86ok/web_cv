from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CVForm  # Importa el formulario que crearemos en el siguiente paso

# Create your views here.

def crear_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario y crea el CV
            # Puedes guardar los datos en la base de datos o generar un PDF, por ejemplo
            # Luego, redirige a una página de éxito o muestra el CV creado
            # Por ahora, solo redireccionaremos a la página principal
            return redirect('pagina_principal')
    else:
        form = CVForm()

    return render(request, 'crear_cv.html', {'form': form})
