from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    # Lógica a ser executada quando um usuário entra no sistema
    print(f'O usuário {user.username} entrou no sistema.')

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    # Lógica a ser executada quando um usuário sai do sistema
    print(f'O usuário {user.username} saiu do sistema.')
