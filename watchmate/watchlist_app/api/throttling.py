from rest_framework.throttling import UserRateThrottle

class RevireCreateThrottle(UserRateThrottle):
    scope = 'review-create'

class ReviewDetailThrottle(UserRateThrottle):
    scope = 'review-detail'    