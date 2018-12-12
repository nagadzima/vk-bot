import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})
    # API-ключ созданный ранее
token = "aded41a6ef0438988be48abdb70fe3100f6102804348ead9dabc114414709bbbc60c2b3c3a5e6f79ba377"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
