import sys
from config_parser import Configuration, ConfigParser


def main() -> None:
    if len(sys.argv) != 2:
        print("Use python a_maze_ing.py [config.txt]", file=sys.stderr)
        exit(1)

    configuration: Configuration = ConfigParser.parse_config(sys.argv[1])
    print(configuration)


if __name__ == "__main__":
    main()
