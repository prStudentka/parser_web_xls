from app.views import (
                     get_user_params,
                     decorate_greetings_user,
                     send_message_out,
                     printed_result
                    )
from app.parser import include_parser
from app.writer_xls import save_xls


def main() -> None:
    decorate_greetings_user()
    querry: str = get_user_params()
    if querry:
        result: tuple | None = include_parser(querry)
        if result is not None:
            result = save_xls(result)
        printed_result(result)
    else:
        send_message_out()
        exit(0)


if __name__ == '__main__':
    main()
