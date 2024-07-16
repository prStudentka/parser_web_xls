from typing import Dict, List
from web_parser.app.messages import LEXICON


__LastMessage: Dict[str, str] = {
    'ok':  LEXICON['save_ok'],
    'bad': LEXICON['save_bad'],
}


def decorate_greetings_user() -> None:
    '''Decorate greeting user

    Function drawing decor and insert greeting
    and tell about the app
    '''

    decor:  str = ' * '
    amount: int = 20
    decor_line: str = decor * amount
    text: List[str] = LEXICON['greetings'].split('\n')
    max_line: int = len(decor_line)
    print(decor_line, decor)
    for line in text:
        length: int = len(line)
        new_length: int = max_line - length - len(decor) - 1
        new_line: str = f'{line}{new_length * " "}'
        print(decor, new_line, decor)
    print(decor_line, decor)
    print()


def get_user_params() -> str:
    ''' Inputting users data

    :return: str - querry for parsing

    This function get user querry for filtering
    and find text for using the parsing
    '''

    querry: str = input(LEXICON['message'])
    return querry.strip().lower()


def send_message_out() -> None:
    ''' Send negative message for user

    This function print message if user press Enter
    and querry empty
    '''

    text_system: str = '--- ATTENTION ---'
    print()
    print()
    print(text_system)
    print()
    print(LEXICON['message_out'])
    print()
    print('-' * len(text_system))


def printed_result(result: tuple | None) -> None:
    ''' Message about result parsing

    :param result: tuple | None - None for Bad result.
    result have OK or Bad message.

    This function printing message for user about
    result parsing
    '''

    print()
    if result is None:
        print(LEXICON['result_bad'])
    else:
        print(__LastMessage[result[0].lower()])
        print(result[1])
        print('---- end ----')
