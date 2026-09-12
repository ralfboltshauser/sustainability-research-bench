import json,pathlib,shutil,zipfile
P=pathlib.Path(__file__).parent
APP=pathlib.Path('/home/ralf/prj/exploration/preventable-gap-app')
d=json.load(open(P/'base-app-data.json'))
by={c['slug']:c for c in d['companies']}
for slug in ['ups','delta','duke']:
 by[slug]=json.load(open(P/(slug+'.json')))

def fmt(v):
 if v is None:return None
 if isinstance(v,list):return ' / '.join(fmt(x) or 'unknown' for x in v)
 if isinstance(v,(int,float)):return f'{v:,.4f}'.rstrip('0').rstrip('.') if isinstance(v,float) and not v.is_integer() else f'{v:,.0f}'
 return str(v)
def ev(r):
 v=r.get('value'); u=r.get('unit',''); t=r.get('type','reported'); note=r.get('note',r.get('caveat',r.get('limitation','')))
 if 'fraction' in u and (isinstance(v,(int,float)) or isinstance(v,list)):
  v=[x*100 for x in v] if isinstance(v,list) else v*100;u=u.replace('fraction','%')
 return dict(claim=r['claim'],value=fmt(v),unit=u,period=r.get('period',''),source=r.get('source',''),locator=r.get('locator',''),type=t,note=note)
def source_pairs(s):
 if isinstance(s,dict):s=list(s.values())
 out=[]
 for x in s:
  if isinstance(x,list):out.append(x)
  elif isinstance(x,dict) and x.get('url'):out.append([x.get('title','Primary source'),x['url']])
 return out
def dedup(s):
 out=[];seen=set()
 for label,url in s:
  if url not in seen:seen.add(url);out.append([label,url])
 return out
for slug in ['walmart','exxon','microsoft']:
 x=json.load(open(P/(slug+'-deep.json')));c=by[slug]
 c['evidenceRecords']=x['evidenceRecords']
 c['sources']=dedup(c['sources']+source_pairs(x['sources']))
 c['researchUrl']='/research/deep-dive/'+slug+'-deep.md'
 if slug=='microsoft':c['summary']=x['appRecordUpdates']['summary']

w=by['walmart'];w.update(status='Direct-emissions sensitivity; net gap unknown',summary='Walmart reports 4.08 million tonnes from onsite refrigerants and a 20.7% year-over-year decline. Low-impact systems are already deployed, but the remaining emissions-weighted conversion opportunity is undisclosed.',boundary='Global onsite refrigerant leakage, including refrigeration and HVAC; energy and lifecycle effects excluded',gapNote='External equal-mass comparison; not a measured Walmart reduction',benchmarkPeriod='2013–2014 paired-store study; published 2015')
w['constraints']=[
 'The deployment percentages, including zero, are assumptions. Eligible extent and new funding impact are not measured.',
 '619 U.S. facilities use ultra-low-GWP systems partly or fully. This is not 619 full conversions or a share of global refrigerant emissions.',
 'About 80% reductions reported for some projects concern installed legacy refrigerant footprint, not annual leakage or whole-store emissions.',
 'The external 191 versus 0.1 tonne comparison is only an equal-leaked-mass direct sensitivity. Walmart’s current gas mix, HVAC share and site suitability remain unknown.',
 'The older DOE study’s whole-store propane row has an unresolved unit/conversion discrepancy. Its reported net result is not used as a validated net reduction factor.',
 'Walmart already funds end-of-life replacements and specifies CO₂ refrigeration for new stores and clubs. Count only extra or earlier improvements beyond this baseline.'
]
w['steps']=['Walmart reports 4.08 million tonnes CO₂e of onsite refrigerant emissions in FY2026.','An external paired-store comparison reports 191 versus 0.1 tonnes of direct refrigerant impact at equal leaked mass; the factor is not a measured Walmart result.','Apply that factor only to the explicitly assumed emissions share. Net energy and lifecycle effects and eligible coverage remain unknown.','Keep the direct sensitivity separate from already achieved inventory reductions and funded replacements. No fund-caused savings are established.']
w['additionalMetrics']=[dict(label='Partial or full low-GWP deployment',value='619',unit='U.S. facilities',note='Reported at December 2025. Includes partial installations, varied facility types and HVAC; no emissions-weighted denominator.',source=w['sources'][0][1]),dict(label='Refrigerant inventory change',value='−20.7%',unit='year over year',note='FY2026 reported change. This is achieved inventory change, not a controlled causal estimate of a specific intervention.',source=w['sources'][0][1]),dict(label='Verified R-404A leak avoided',value='3.922',unit='tCO₂e per kg of avoided leakage',note='Physical unit calculation using the EPA 2011 GWP convention. Requires verified avoided R-404A mass and aligned GWP vintage; no Walmart eligible volume is established.',source='https://www.epa.gov/sites/production/files/documents/leakpreventionrepairguidelines.pdf')]
w['investmentEvidence']=[dict(label='Current Walmart project economics',value='Not established',note='Asset-specific replacement bids, energy impacts, refrigerant savings and committed replacement dates are needed.',source=w['sources'][0][1]),dict(label='Historical equipment premium',value='≈40%',note='2013 Hannaford case, reported in 2015. Piping and cases had a separate 10–15% premium. These percentages cannot be added and are not current Walmart quotes.',source=w['sources'][1][1]),dict(label='Additionality test',value='Earlier or extra adoption',note='Compare each project with Walmart’s already funded end-of-life schedule. Societal damage dollars cannot repay a loan.',source=w['sources'][0][1])]

x=by['exxon'];ex=json.load(open(P/'exxon-deep.json'))
x['gapNote']='Tank-source sensitivity; untreated eligible share unknown';x['benchmarkPeriod']='EPA method 2023; page updated 2026'
x['constraints'] += ['Emission-factor updates increased some 2025 estimated fugitive emissions; monitoring coverage is not a fully reconciled measured inventory.','The company describes independent assurance of its 2025 inventory as underway. OGMP Gold Standard Pathway recognition must not be treated as completed verification.','Zero additional benefit is possible if suitable sources are already controlled or conversions would occur without this fund.']
x['additionalMetrics']=[dict(label='Estimated tank/storage source pool',value='≈6,800',unit='tonnes CH₄ / year',note='Derived from rounded 2025 source shares. This is not an inventory of untreated, suitable tanks.',source=x['evidenceRecords'][0]['source']),dict(label='Additional eligible tank share',value=None,unit='fraction of source',note='Not disclosed. Physical feasibility, prior controls and existing commitments must be established before assigning a fund effect.',source=x['evidenceRecords'][0]['source']),dict(label='Inventory assurance status',value='Underway',unit='2025 inventory',note='As described on the company’s metrics page when researched. Monitoring does not imply every source is measured and reconciled.',source='https://corporate.exxonmobil.com/publications/metrics-and-data')]
x['investmentEvidence']=[dict(label='Historical 100 Mcf/day VRU installation',value='$55,524',note='Archived EPA illustration, not a current Exxon quote. Underlying cost-dollar year is unverified; actual site and connection costs can be higher.',source=ex['investmentEvidence']['source']),dict(label='Historical annual operating cost',value='$10,103 / year',note='Same historical equipment case. Operating costs may already include electricity; do not count it twice.',source=ex['investmentEvidence']['source']),dict(label='Illustrative simple payback',value='≈1.32 years at $3/Mcf',note='Assumes 50 Mcf/day feed, 95% recovery and those historical costs. Excludes omitted site costs, taxes and finance. Not a prospective Exxon return.',source=ex['investmentEvidence']['source'])]

m=by['microsoft'];ms=json.load(open(P/'microsoft-deep.json'));m['benchmarkPeriod']='2025 lifecycle study; 2021 U.S. grid assumptions';m['gapNote']='Study-matched service; eligible fleet unknown'
msources=ms['appRecordUpdates']['sources']
metric_sources=[m['sources'][0][1],m['sources'][0][1],'https://blogs.microsoft.com/blog/2026/06/24/inside-microsofts-two-decade-push-to-cut-water-intensity-while-scaling-for-growth/','https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/','https://www.nature.com/articles/s41586-025-08832-3','https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/','https://local.microsoft.com/blog/testing-underway-to-understand-noise-at-our-mount-pleasant-datacenter/']
m['additionalMetrics']=[dict(label=a['label'],value=fmt(a['value']),unit=a['unit'],note=f"{a['period']} · {a['status']}. {a['detail']}",source=s) for a,s in zip(ms['appRecordUpdates']['additionalMetrics'],metric_sources)]
m['investmentEvidence']=[dict(label='Existing deployment',value='Fairwater operating since April 2026',note='Company-reported commissioning strengthens availability evidence. Existing deployments and Phoenix efficiency gains are not remaining fund-additional opportunity.',source='https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3'),dict(label='Incremental cooling retrofit economics',value='Not disclosed',note='Need an eligible cohort, cooling-only water baseline, IT service, weather, extra power, tariffs, replacement dates and actual bids before underwriting.',source=metric_sources[3])]
m['constraints'] += ['Phoenix’s reported 23% WUE improvement is achieved intensity progress, not 23% of company water saved.','The greater-than-125,000 m³/site/year design claim concerns projected withdrawal avoidance. No matching measured annual consumption saving is established; dry cooling can increase power use.']

u=by['ups'];u['scope1Note']='tCO₂e · main GRI total; segment table differs by 0.001 Mt';u['benchmarkPeriod']='2014 Frito-Lay operations; NREL report 2016';u['gapNote']='External delivery fleet; historical local electricity mix'
u['additionalMetrics']=[dict(label='Grid sensitivity in the same study',value='32.3%',unit='operating GHG reduction',note='Historical U.S. national electricity case versus the 46.4% local-grid case. Not a forecast range, UPS measurement or full vehicle lifecycle result.',source=u['sources'][1][1]),dict(label='Ground diesel emissions',value='1.624 million',unit='tCO₂e · 2025',note='Reported inventory, not a baseline of eligible urban delivery routes.',source=u['sources'][0][1]),dict(label='Existing electric vehicles',value='More than 580',unit='vehicles',note='Company 2025 overview. These already deployed vehicles cannot be counted as new conversions.',source=u['sources'][2][1])]
u['investmentEvidence']=[dict(label='Historical incremental vehicle cost',value='$86,791',note='NREL 2016 report p.19, historical Smith Newton example. Not a current UPS quote; $60,000 New York voucher was a separate location-specific incentive.',source=u['sources'][1][1]),dict(label='Current project repayment',value='Not established',note='Measure diesel and maintenance savings against electricity, demand charges, charger cost, downtime and financing. Confirm payload, range and replacement schedule.',source=u['sources'][1][1])]

k=by['duke'];k['scope1Note']='tCO₂e · approximate sum of rounded Scope 1 rows';k['benchmarkPeriod']='EPA 2006 technical guidance; AR6 GWP';k['gapNote']='50% recovery case; other lifecycle effects excluded'
k['additionalMetrics']=[dict(label=a['name'],value=fmt(a['value']),unit=a['unit'],note=f"{a['period']}. {a['interpretation']}",source=a['source']) for a in k['additionalMetrics']]+[dict(label='Higher technical recovery case',value='81.7%',unit='of qualifying baseline methane climate burden',note='90% recovery case, after burning recovered methane; compressor and other lifecycle effects excluded. Not a Duke fleet savings estimate.',source=k['sources'][1][1])]
k['investmentEvidence']=[dict(label='Historical recovery project cost',value='$68,100',note='Southern Natural Gas, not Duke. EPA describes 1998 activity on a 2006 cost basis. Historical illustration only.',source=k['sources'][1][1]),dict(label='Historical net savings',value='$159,900',note='Same case assumes 32,550 Mcf recovered and $7/Mcf gas. It does not establish current Duke project economics or ownership of retained gas value.',source=k['sources'][1][1]),dict(label='Current Duke repayment',value='Not established',note='Confirm specific events, recovery costs, gas ownership, tariff treatment and allocation of savings before lending.',source=k['sources'][1][1])]

z=by['delta'];z['scope1Note']='tCO₂e · airline operational control; Monroe refinery excluded';z['benchmarkPeriod']='2021 gate-electrification lifecycle study';z['gapNote']='Low study case; not a guaranteed minimum'
z['constraints'].append('The original author’s dissertation supplies the detailed methods. Study cost and operating assumptions still require current, asset-specific validation.')
z['additionalMetrics']=[dict(label='Study case range',value='63–97%',unit='gate lifecycle reduction',note='Across study cases, not a confidence interval or guaranteed performance floor. Main card uses the low case.',source=z['sources'][2][1]),dict(label='Operational fuel savings already achieved',value='59 million',unit='US gallons · 2025',note='Company counterfactual estimate, excluding fleet renewal. Do not relabel achieved savings as a new remaining opportunity.',source=z['sources'][3][1]),dict(label='SAF procurement',value='23.4 million',unit='US gallons · 2025',note='Includes physical supply and certificates. It is not verified physical-only SAF burn. Compare carefully with the 4.269 billion gallon fuel pool.',source=z['sources'][3][1]),dict(label='APU runtime sensitivity',value='11,700',unit='tonnes direct CO₂ / systemwide minute / year',note='Derived from Delta’s 1.2 million gallon sensitivity × EPA 9.75 kg CO₂/gallon. Remaining reducible minutes are unknown; replacement electricity and other effects must be subtracted. Not combined with the lifecycle percentage.',source='https://news.delta.com/media/image/64251')]
z['investmentEvidence']=[dict(label='Historical study average payback',value='1–2 years',note='Study payback is relative to 100% APU use, unlike the partly electrified baseline for the 63–97% emissions comparison. Historical study assumptions are not current Delta project economics.',source=z['sources'][-1][1]),dict(label='Airport–airline repayment structure',value='Needs a contract',note='Infrastructure owner and airline may differ. Assign fuel savings, electricity bills and maintenance costs explicitly; exclude already committed projects.',source=z['sources'][4][1])]

n=by['nucor'];n['benchmarkPeriod']='Supplier-reported Seattle installation, 2017';n['gapNote']='Already achieved at Seattle; replication unverified'
n['evidenceRecords']=[dict(claim='Company direct emissions',value=n['scope1'],unit='tCO₂e',period='2025',source=n['sources'][0][1],locator='p.37',type='reported'),dict(claim='Seattle furnace electricity reduction',value=5,unit='%',period='2017 case',source=n['sources'][1][1],locator='Seattle installation case',type='supplier-reported achieved process improvement',note='Already achieved at this asset. No remaining unoptimized company cohort identified.')]
n['investmentEvidence']=[dict(label='Remaining eligible furnace project economics',value='Not established',note='The demonstrated Seattle improvement is already implemented. Find comparable still-unoptimized assets and verify metered savings and capital cost.',source=n['sources'][1][1])]
n['additionalMetrics']=[]
j=by['jpmorgan'];j['evidenceRecords']=[dict(claim='Operational Scope 1 emissions',value=j['scope1'],unit='tCO₂e',period='2024',source=j['sources'][0][1],locator='Operational emissions inventory',type='reported'),dict(claim='Eligible borrower-asset reduction',value=None,unit='tCO₂e',period='Not established',source=j['sources'][0][1],locator='Operational inventory does not identify borrower projects',type='unknown',note='Operational inventory is not financed emissions. Need named borrower assets, physical counterfactuals and additional financing effect.')];j['additionalMetrics']=[];j['investmentEvidence']=[dict(label='Borrower-asset repayment',value='Not established',note='A lower portfolio footprint can arise from selling exposures without changing physical emissions. Underwrite project cashflows and causal improvements separately.',source=j['sources'][0][1])]

for slug,c in by.items():
 if slug in ['ups','duke','delta']:c['researchUrl']='/research/deep-dive/'+slug+'.md'
 c['evidenceRecords']=[ev(r) for r in c.get('evidenceRecords',[])]
 if not any('scope 1' in r['claim'].lower() or 'direct emissions' in r['claim'].lower() for r in c['evidenceRecords']):
  c['evidenceRecords'].insert(0,ev(dict(claim='Company direct Scope 1 inventory',value=c['scope1'],unit='tCO₂e',period=c['period'],source=c['sources'][0][1],locator='Company inventory; see original source',type='reported')))
 c['sources']=dedup(c['sources'])
 if c['kind']=='normalized':c['rowNote']=f"{round(c['baseline']*c['reductionRate']):,} t / 1,000 qualifying baseline t"
 if slug in ['ups','duke','delta']:
  c['indexEvidence']={'status':'Corroborated in S&P 500 tracker holdings, September 10, 2026','source':'https://www.ishares.com/us/products/239726/ishares-core-s-p-500-etf/latest-holdings.csv'}
d['companies']=list(by.values());d['researchVersion']='Expanded evidence audit · 12 September 2026';d['evidenceCount']=sum(len(c['evidenceRecords']) for c in d['companies']);d['sourceCount']=len({s[1] for c in d['companies'] for s in c['sources']})
(APP/'app/data.json').write_text(json.dumps(d,indent=2,ensure_ascii=False))
(P/'expanded-app-data.json').write_text(json.dumps(d,indent=2,ensure_ascii=False))
for f in P.glob('*.md'):shutil.copyfile(f,APP/'public/research/deep-dive'/f.name)
print('Companies:',len(d['companies']),'Evidence records:',d['evidenceCount'],'Source URLs:',d['sourceCount'])
