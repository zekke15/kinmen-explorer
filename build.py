from pathlib import Path
import json,html
root=Path(__file__).resolve().parents[1]
places=json.loads((root/'content/places.json').read_text(encoding='utf-8'))
esc=lambda s:html.escape(str(s),quote=True)
def card(p,prefix=''):
 search=' '.join([p['name'],p['english'],p['town'],p['category'],p['summary'],p['intro']])
 return f'<a class="card" data-place="{esc(p["id"])}" data-kind="{esc(p["category"])}" data-search="{esc(search)}" href="{prefix}places/{esc(p["id"])}.html"><img src="{prefix}assets/{esc(p["art"])}.svg" alt="{esc(p["name"])}主題意象插畫" loading="lazy"><div class="tagline"><span>{esc(p["category"])}</span><span>{esc(p["town"])}</span></div><h3>{esc(p["name"])}</h3><p>{esc(p["summary"])}</p><div class="card-bottom"><span>{esc(p["english"])}</span><b>認識景點 ↗</b></div></a>'
def render(t,values):
 for k,v in values.items():t=t.replace('{{'+k+'}}',v)
 return t
filters=''.join(f'<button type="button" data-category="{x}" aria-pressed="{str(i==0).lower()}">{x}</button>' for i,x in enumerate(['全部景點','聚落建築','戰地歷史','自然風景','街區漫步']))
t=(root/'templates/index.html').read_text(encoding='utf-8')
(root/'dist/index.html').write_text(render(t,{'total':str(len(places)).zfill(2),'filters':filters,'cards':''.join(card(p) for p in places)}),encoding='utf-8')
(root/'dist/places').mkdir(exist_ok=True)
t=(root/'templates/detail.html').read_text(encoding='utf-8')
for i,p in enumerate(places):
 vals={k:esc(v) for k,v in p.items() if isinstance(v,str)}
 vals['highlights']=''.join('<li>'+esc(x)+'</li>' for x in p['highlights'])
 vals['related']=''.join(card(places[(i+n)%len(places)],'../') for n in range(1,min(4,len(places))))
 (root/'dist/places'/(p['id']+'.html')).write_text(render(t,vals),encoding='utf-8')
print('Built homepage and',len(places),'detail pages')
