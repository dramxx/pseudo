import sys
import colorama
import pyfiglet

colorama.init()


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print("Usage: pseudo [-roman] [-styles] <text>")
        print("       pseudo -roman hello")
        print("       pseudo -styles")
        return

    if args[0] == "-styles":
        fonts = sorted(pyfiglet.FigletFont.getFonts())
        for i, font in enumerate(fonts, 1):
            print(f"{i}. {font}")
        return

    font = "roman"
    text_args = []

    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("-roman", "--roman"):
            font = "roman"
        elif arg.startswith("-"):
            print(f"Unknown flag: {arg}")
            print("Usage: pseudo [-roman] [-styles] <text>")
            return
        else:
            text_args.append(arg)
        i += 1

    if not text_args:
        print("Usage: pseudo [-roman] [-styles] <text>")
        return

    text = " ".join(text_args)
    result = pyfiglet.figlet_format(text, font=font, width=9999)
    print(result)


if __name__ == "__main__":
    main()
