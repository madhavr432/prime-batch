import datetime

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        self.chatroom = chatroom
        chatroom.add_user(self)
        print(f"{self.username} joined {chatroom.room_name}")

    def leave_chatroom(self):
        if self.chatroom:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.room_name}")
            self.chatroom = None

    def send_message(self, content):
        if self.chatroom:
            message = Message(self, content)
            self.chatroom.broadcast_message(message)
        else:
            print(f"{self.username} is not in a chatroom!")

class Message:
    def __init__(self, sender, content):
        self.sender = sender.username
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"[{self.timestamp.strftime('%H:%M:%S')}] {self.sender}: {self.content}"

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast_message(self, message):
        self.messages.append(message)
        for user in self.users:
            print(message)

    def view_history(self):
        print(f"--- Chat History of {self.room_name} ---")
        for msg in self.messages:
            print(msg)

chatroom = ChatRoom("OOP Chatroom")

u1 = User("Madhav")
u2 = User("Raj")

u1.join_chatroom(chatroom)
u2.join_chatroom(chatroom)

u1.send_message("Hello everyone!")
u2.send_message("Hi Madhav, welcome to the chat!")

chatroom.view_history()

u1.leave_chatroom()
