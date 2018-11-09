#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import loto_classes


def get_obj_classes():

    gamer_card = loto_classes.CardGenerator('Ваша карта')
    cpu_card = loto_classes.CardGenerator('Карта компьютера')
    barrel = loto_classes.BarrelGenerator()
    return {
        'gamer': gamer_card,
        'cpu': cpu_card,
        'barrel': barrel
    }


def have_win(obj):

    win = True

    if obj['gamer'].is_win() and obj['cpu'].is_win():
        print('\nНИЧЬЯ!')
    elif obj['gamer'].is_win() and not obj['cpu'].is_win():
        print('\nПОЗДРАВЛЯЕМ!\nВЫ ПОБЕДИЛИ!!!')
    elif obj['cpu'].is_win() and not obj['gamer'].is_win():
        print('\nВЫ ПРОИГРАЛИ!\nКомпьютер зачеркнул все цифры на своей карте')
    else:
        win = False

    return win


def do_step(control_func):

    def print_step(obj, repeat=0):

        if not repeat:
            if have_win(obj):
                return False
            print('\nНовый бочонок {0} (осталось {1})\n'
              '{2}\n{3}'.format(obj['barrel'], obj['barrel'].length-1,
                                obj['gamer'], obj['cpu']))
        return control_func(obj)
    return print_step


@do_step
def control_step(obj, repeat=0):

    try:
        gamer_answer = input('Зачеркнуть цифру? (y/n): ')

        if obj['cpu'].is_include(obj['barrel'].current_number):
            obj['cpu'].cross_out(obj['barrel'].current_number)

        if gamer_answer == 'y':
            if obj['gamer'].is_include(obj['barrel'].current_number):
                obj['gamer'].cross_out(obj['barrel'].current_number)
                return True
            else:
                print('\nВЫ ПРОИГРАЛИ!\nЦифры '
                      '{} нет на Вашей карте'
                      ''.format(obj['barrel'].current_number))
                return False
        elif gamer_answer == 'n':
            if not obj['gamer'].is_include(obj['barrel'].current_number):
                return True
            else:
                print('\nВЫ ПРОИГРАЛИ!\nПропущена цифра '
                      '{}'.format(obj['barrel'].current_number))
                return False
        else:
            raise ValueError
    except ValueError:
        print('Введена неизвестная команда "{}"'.format(gamer_answer))
        gamer_answer = input('\nДля продолжения игры введите "y": ')
        if gamer_answer == 'y':
            return control_step(obj, 'try_again')
        else:
            print('Игра завершена...')
            return False


def game_regulations():

    with open('loto.txt', encoding='UTF-8') as file:
        print('\n'.join([x.strip() for x in file]))
    user_answer = input('Введите "y" чтобы начать игру: ')
    if user_answer == 'y':
        start_game()
    else:
        print('Выход из программы')
        return


def start_game():

    obj = get_obj_classes()

    while True:
        if not control_step(obj) is True:
            user_answer = input('\nВведите "y", чтобы начать новую игру: ')
            if user_answer == 'y':
                obj = get_obj_classes()
            else:
                print('Выход из программы')
                break


def menu():

    user_answer = input('Добро пожаловать в игру "ЛОТО"!\n'
                        '\t1. Начать играть\n'
                        '\t2. Напомнить правила\n'
                        'Введите "1" или "2" чтобы выбрать пункт: ')
    menu = {
        '1': start_game,
        '2': game_regulations
        }

    try:
        menu[user_answer]()
    except KeyError:
        print('"{}" неизвестная команда\n'
              'Выход из программы'.format(user_answer))

menu()