import requests
from django.shortcuts import render


def tanos_click_view(request):
    if request.method == 'POST':
        response = requests.get('https://yesno.wtf/api').json()
        answer_first = response.get('answer')

        if answer_first == 'no':
            death = True
            message_1 = 'Вы выжили!'
            message_2 = 'Вам повезло больше, чем половине живых существ...'
        else:
            death = False
            message_1 = 'Вы погибли!'
            message_2 = 'Убийственная энергия Перчатки Бесконечности добралась и до вас. Последний вдох провожает ваше рассыпающееся пеплом сознание в небытие...'
        context = {'death': death,
                   'message_1': message_1,
                   'message_2': message_2}
        return render(request, 'app_tanos_click/click.html', context)
    else:
        message_1 = 'Танос близко!'
        message_2 = 'Могучий титан поднимает руку, складывает пальцы. Раздался щелчок!'
        return render(request, 'app_tanos_click/click.html', {'death': None,
                                                               'message_1': message_1,
                                                               'message_2': message_2})
