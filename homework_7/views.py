from django.http import HttpRequest, HttpResponse


def greeting(request: HttpRequest) -> HttpResponse:
    # http://127.0.0.1:8000/home/?name=Alex  -->> Hello, Alex
    # http://127.0.0.1:8000/home/            -->> Hello, Guest
    name = request.GET.get("name", 'Guest')
    return HttpResponse(
        f"""
        <h1>{f"Hello, {name}"}</h1>
        """
    )


