from django.urls import path
from .consumers import ChatroomConsumer

# websocket_urlpatterns = [
#     path("ws/chatroom/<chatroom_name>", ChatroomConsumer.as_asgi()),
#     path("ws/chatroom/public-chat", ChatroomConsumer.as_asgi()),
#     path("messenger/ws/chatroom/public-chat", ChatroomConsumer.as_asgi()),
#
# ]


websocket_urlpatterns = [
    path(
      "ws/chatroom/<str:room_name>/",
      ChatroomConsumer.as_asgi(),
      name="ws-chatroom"
    ),
]

