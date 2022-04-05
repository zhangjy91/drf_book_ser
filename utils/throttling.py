from rest_framework.throttling import SimpleRateThrottle

class MyThrottle(SimpleRateThrottle):
    scope = 'test'
    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')