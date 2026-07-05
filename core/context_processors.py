from .models import CompanyInfo

def company_context(request):
    return {
        'company_info': CompanyInfo.objects.first()
    }
