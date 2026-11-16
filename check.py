from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,re
r=Path(__file__).resolve().parents[1];d=r/'dist';data=json.loads((r/'content/places.json').read_text())
assert len({x['id'] for x in data})==len(data)
for x in data:
 assert re.fullmatch('[a-z]+(?:-[a-z]+)*',x['id'])
 assert len(x['highlights'])==3 and len(x['summary'])<=55
 assert x['category'] in ['聚落建築','戰地歷史','自然風景','街區漫步']
 assert x['source'].startswith('https://kinmen.travel/')
class P(HTMLParser):
 def __init__(self,text):super().__init__();self.links=[];self.ids=set();self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  self.links.extend(a[k] for k in ['href','src'] if k in a)
for f in d.rglob('*.html'):
 t=f.read_text();assert '{{' not in t
 for link in P(t).links:
  u=urlsplit(link)
  if u.scheme:continue
  dest=(f.parent/u.path).resolve() if u.path else f
  assert dest.is_file(),str(dest)
  if u.fragment and dest.suffix=='.html':assert u.fragment in P(dest.read_text()).ids
print('PASS: unique IDs, categories, content, sources, all local links and anchors')
