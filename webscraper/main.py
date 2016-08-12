from webscraper.cli import command

VERSION = '1.0'
NAME = 'web-scraper'
PROMPT = NAME+VERSION+'/>'
PROMPT_START = 'Startitng'+NAME+VERSION


prompt = command.Command()
prompt.prompt = PROMPT
prompt.cmdloop(PROMPT_START)

