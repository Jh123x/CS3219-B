from django.http.response import HttpResponse

def get_result_json(is_successful) -> dict:
    return {
        "is_success": is_successful
    }

def wrap_response(response: str):
    resp = HttpResponse(response)
    resp.headers['Content-Type'] = "application/json"
    return resp