from django.utils.deprecation import MiddlewareMixin
from ip_tracking.models import RequestLog

class IPLoggingMiddleware(MiddlewareMixin):
    """Middleware to log IP addresses, timestamps, and paths of incoming requests."""
    
    def process_request(self, request):
        # Get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # Get the first IP in case of multiple proxies
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Log the request details
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path
        )
        
        return None
