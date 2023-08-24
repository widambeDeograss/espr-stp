from user_management.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.


class RolesView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        print(data)
        try:
            user = User.objects.get(id=data['user_id'])
        except User.DoesNotExist:
            return Response({'message': 'User Does Not Exist'})
        if len(data['add']) > 0:
            for roles in data['add']:
                if roles['role'] in user.roles:
                    continue
                else:
                    user.roles.append(roles['role'])

        if len(data['remove']) > 0:
            for roles in data['remove']:
                if roles['role'] in user.roles:
                    user.roles.remove(roles['role'])
                else:
                    continue
        user.save()

        return Response({'save': True})


# {
#     "user_id": "1c3244aa-d47a-4e88-a484-6f1162804a01",
#     "add": [{"role": 1}, {"role": 2}, {"role": 3}, {"role": 4}],
#     "remove": [{"role": 1}]
# }
