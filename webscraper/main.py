from webscraper.cli import command

VERSION = '1.16'
NAME = 'web-scraper'
PROMPT = NAME+VERSION+'/>'
PROMPT_START = 'Startitng '+NAME+VERSION


def start_command():
    prompt = command.Command()
    prompt.prompt = PROMPT
    prompt.cmdloop(PROMPT_START)

if __name__ == "__main__":
    start_command()
