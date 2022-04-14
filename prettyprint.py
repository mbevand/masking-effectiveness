#!/usr/bin/python

import datetime, json

def sym(finding):
    if finding == 'effective': return ':heavy_check_mark:'
    elif finding == 'ineffective': return ':no_entry_sign:'
    elif finding == 'inconclusive': return ':question:'
    else: raise Exception(f'invalid value: {finding}')

def main():
    papers = json.load(open('articles.json'))
    finding_types = {}
    for p in papers:
        finding_types[p["finding"]] = 1 + finding_types.get(p["finding"], 0)
    print(
'''(List in JSON format: [articles.json](articles.json); author: Marc Bevand)

# List of all peer-reviewed studies evaluating face mask effectiveness against COVID-19
''')
    print(f'* **{len(papers)} studies in total**')
    for finding, count in finding_types.items():
        g = '' if finding == 'inconclusive' else 'generally '
        print(f'* {count} find face masks are {g}{finding} ({sym(finding)})')
    print('''
### Criteria for inclusion:

* Be a **research article** (data, methods, results). Commentaries, opinion pieces, etc, do not qualify
* Be **peer-reviewed & published** among the 26,000 titles in Scopus
* Be **explicit**. No secondhand interpretation of figures or data tables. The
  authors must explicitly state in the text whether their results suggest masking
  is effective or not.

### List:
''')
    papers = sorted(papers, reverse=True, key=lambda p: datetime.datetime.strptime(p['pub'], '%b %Y'))
    for (i, p) in enumerate(papers):
        print(f'{i + 1}. {p["url"]} ({p["pub"]})  \n  {p["title"]}  \n  {sym(p["finding"])} {p["quote"]}\n')

if __name__ == '__main__':
    main()
