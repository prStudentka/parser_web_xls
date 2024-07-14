from app.view import get_user_params
from app.parser import include_parser


def main() -> None:
    querry: str = get_user_params()
    include_parser(querry.strip())


if __name__ == '__main__':
    main()
