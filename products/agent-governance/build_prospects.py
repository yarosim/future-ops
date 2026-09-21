import csv
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
rows = [
# Defense contractors (25)
("AeroVironment","Defense contractor","https://www.avinc.com/","Official site describes integrated defense technology and autonomous systems.","https://www.avinc.com/about/","Lead with governance for autonomous/AI-enabled tool identities and evidence across defense workflows."),
("Kratos Defense & Security Solutions","Defense contractor","https://www.kratosdefense.com/","Official site presents defense systems including unmanned systems, space, propulsion, and microwave electronics.","https://www.kratosdefense.com/","Discuss agent inventory and approval controls around engineering, program, and mission-support workflows."),
("Mercury Systems","Defense contractor","https://www.mrcy.com/","Official site positions Mercury as a mission-critical processing company serving aerospace and defense.","https://www.mrcy.com/","Frame privileged-agent controls around sensitive engineering data and mission-critical software operations."),
("V2X","Defense contractor","https://gov2x.com/","Official site describes mission solutions and operational support for government customers.","https://gov2x.com/","Offer a rapid register of agents touching program, logistics, and government-customer information."),
("Parsons","Defense contractor","https://www.parsons.com/","Official site lists defense, intelligence, security, and infrastructure markets.","https://www.parsons.com/","Connect agent audit evidence to defense/intelligence delivery and customer assurance."),
("CACI International","Defense contractor","https://www.caci.com/","Official site describes technology and expertise for national security and government modernization.","https://www.caci.com/","Focus on dedicated agent identities and traceable tool actions in national-security programs."),
("SAIC","Defense contractor","https://www.saic.com/","Official site describes mission-integrating technology services for government customers.","https://www.saic.com/","Use its public AI work as an opening for runtime permission, approval, and evidence governance."),
("Leidos","Defense contractor","https://www.leidos.com/","Official site presents technology solutions across defense, intelligence, civil, and health markets.","https://www.leidos.com/insights/artificial-intelligence","Ask how internal and customer-facing AI agents are inventoried and distinguished in logs."),
("Booz Allen Hamilton","Defense contractor","https://www.boozallen.com/","Official site describes AI, cyber, defense, and government consulting capabilities.","https://www.boozallen.com/insights/ai.html","Position the sprint as an implementation-grade control and evidence layer for agentic AI programs."),
("ManTech","Defense contractor","https://www.mantech.com/","Official site serves defense, intelligence, and federal civilian missions with technology solutions.","https://www.mantech.com/","Lead with least privilege and customer-ready evidence for agents in sensitive mission environments."),
("Amentum","Defense contractor","https://www.amentum.com/","Official site describes engineering and technology solutions for defense, intelligence, energy, and space.","https://www.amentum.com/","Audit agent access across complex program environments, owners, subcontractors, and data boundaries."),
("Peraton","Defense contractor","https://www.peraton.com/","Official site identifies Peraton as a national security company serving government missions.","https://www.peraton.com/","Tie public AI/ML capability to internal agent identity, tool permission, and recovery controls."),
("Sierra Nevada Corporation","Defense contractor","https://www.sncorp.com/","Official site describes aerospace and national-security technology solutions.","https://www.sncorp.com/","Use aerospace/mission integration complexity to discuss governed agent connectors and change evidence."),
("Anduril Industries","Defense contractor","https://www.anduril.com/","Official site develops autonomous systems and defense technology.","https://www.anduril.com/","Differentiate corporate workflow-agent governance from product safety; focus on privileged enterprise access."),
("Shield AI","Defense contractor","https://shield.ai/","Official site develops AI pilots and autonomous systems for defense.","https://shield.ai/","Propose a scoped review of non-product enterprise agents and their sensitive-data/tool boundaries."),
("Palantir Technologies","Defense contractor","https://www.palantir.com/","Official site provides software platforms used in government and commercial operations.","https://www.palantir.com/platforms/aip/","Reference AIP adoption and ask how customer/internal agent permissions, approvals, and evidence are standardized."),
("Redwire","Defense contractor","https://redwirespace.com/","Official site provides space infrastructure and technology for civil, commercial, and national-security missions.","https://redwirespace.com/","Frame governance around agents supporting engineering, supply chain, and controlled program data."),
("Rocket Lab","Defense contractor","https://www.rocketlabusa.com/","Official site provides launch and space systems to commercial and government customers.","https://www.rocketlabusa.com/space-systems/","Ask about agent write access across engineering, manufacturing, and mission-support systems."),
("BWX Technologies","Defense contractor","https://www.bwxt.com/","Official site supplies nuclear components and services for government and commercial customers.","https://www.bwxt.com/","Lead with strict identity, approval, logging, and sensitive-data boundaries in high-consequence operations."),
("Curtiss-Wright","Defense contractor","https://www.curtisswright.com/","Official site serves aerospace and defense and commercial power/process markets.","https://www.curtisswright.com/","Offer a cross-business-unit agent inventory and permission baseline for distributed operations."),
("HII","Defense contractor","https://hii.com/","Official site describes shipbuilding and all-domain technologies for national security.","https://hii.com/","Connect all-domain digital work to scoped identities and human approval for consequential automation."),
("Leonardo DRS","Defense contractor","https://www.leonardodrs.com/","Official site supplies defense products and technologies to military customers.","https://www.leonardodrs.com/","Focus on traceability and least privilege for agents touching engineering, contracts, and suppliers."),
("KBR","Defense contractor","https://www.kbr.com/","Official site provides science, technology, and engineering solutions including government services.","https://www.kbr.com/","Position a sprint around agent ownership and customer-evidence readiness in government programs."),
("Cubic","Defense contractor","https://www.cubic.com/","Official site offers transportation and mission/communications solutions, including defense training technology.","https://www.cubic.com/industries/defense","Use connected training/mission operations as context for tool-call governance and recovery design."),
("Astrion","Defense contractor","https://astrion.us/","Official site provides engineering and mission support for defense and federal customers.","https://astrion.us/","Offer a right-sized agent registry and permission audit suited to program-based federal delivery."),
# MSPs (15)
("Ntiva","MSP","https://www.ntiva.com/","Official site offers managed IT, cybersecurity, and governance/risk/compliance services.","https://www.ntiva.com/governance-risk-compliance","Propose a white-label agent-governance module for government-contractor and regulated clients."),
("Integris","MSP","https://integrisit.com/","Official site offers managed IT plus managed cybersecurity and compliance services.","https://integrisit.com/services/cybersecurity/","Position an agent privilege audit as a new assessment and recurring evidence service for clients."),
("VC3","MSP","https://www.vc3.com/","Official site offers managed IT, cybersecurity, and Compliance as a Service.","https://www.vc3.com/services/cybersecurity/compliance-as-a-service","Suggest adding agent inventory, identities, approvals, and logs to its CaaS delivery."),
("Dataprise","MSP","https://www.dataprise.com/","Official site offers managed IT and managed cybersecurity with compliance support.","https://www.dataprise.com/services/managed-cybersecurity/","Pitch a repeatable agent-governance assessment feeding vCISO and managed-security reporting."),
("Executech","MSP","https://executech.com/","Official site provides managed IT, cybersecurity, and compliance services.","https://executech.com/security-and-compliance-for-organizations/","Align the sprint with its continuous, evidence-based security/compliance positioning."),
("Thrive","MSP","https://thrivenextgen.com/","Official site presents managed IT, cloud, cybersecurity, and compliance services.","https://thrivenextgen.com/cybersecurity/","Offer a packaged governance overlay for client AI agents across cloud and security operations."),
("Coretelligent","MSP","https://coretelligent.com/","Official site provides managed IT, cybersecurity, and compliance services for regulated organizations.","https://coretelligent.com/","Use regulated-client focus to introduce defensible agent permissions and evidence reviews."),
("Magna5","MSP","https://www.magna5.com/","Official site offers managed IT and cybersecurity services.","https://www.magna5.com/cybersecurity/","Pitch an assessment-to-managed-service path for clients deploying Copilot and workflow agents."),
("Electric","MSP","https://www.electric.ai/","Official site provides IT management and support for businesses.","https://www.electric.ai/","Focus on governance for AI-enabled IT workflows that can modify accounts, devices, and SaaS."),
("Xvand","MSP","https://www.xvand.com/","Official site provides managed IT and cybersecurity services.","https://www.xvand.com/","Offer a small-business-friendly agent privilege audit as a client-facing add-on."),
("OSIbeyond","MSP","https://www.osibeyond.com/","Official site provides managed IT, cybersecurity, and CMMC-focused services.","https://www.osibeyond.com/","Lead with CUI/FCI boundaries and AI-agent evidence for defense industrial base clients."),
("Summit 7","MSP","https://www.summit7.us/","Official site focuses on cybersecurity and compliance for the defense industrial base.","https://www.summit7.us/cmmc","Propose an agent-governance control pack adjacent to Microsoft/CMMC client programs."),
("CyberSheath","MSP","https://cybersheath.com/","Official site provides managed cybersecurity and CMMC services for the defense industrial base.","https://cybersheath.com/cmmc/","Add AI-agent inventory and permission evidence to CMMC-oriented managed security engagements."),
("Kelser Corporation","MSP","https://www.kelsercorp.com/","Official site provides managed IT and cybersecurity services.","https://www.kelsercorp.com/","Introduce a governed-agent readiness review for regulated small and midsize clients."),
("Intelligent Technical Solutions","MSP","https://www.itsasap.com/","Official site offers managed IT, cybersecurity, cloud, and compliance services.","https://www.itsasap.com/","Package the 15-minute scorecard into client discovery and upsell recurring governance."),
# Regulated B2B (10)
("nCino","Regulated B2B","https://www.ncino.com/","Official site markets an AI-enabled platform purpose-built for financial institutions.","https://www.ncino.com/","Directly ask how AI-agent identities, actions, approvals, and audit evidence are governed across banking workflows."),
("Q2 Holdings","Regulated B2B","https://www.q2.com/","Official site provides digital-banking solutions and describes building AI for financial institutions.","https://www.q2.com/","Frame agent governance as trust infrastructure for bank employees, account holders, and fintech integrations."),
("Alkami Technology","Regulated B2B","https://www.alkami.com/","Official site provides a digital sales and service platform to U.S. banks and credit unions.","https://www.alkami.com/about-alkami/","Lead with controlled agent access to account-holder data and traceable next-best-action workflows."),
("Guidewire Software","Regulated B2B","https://www.guidewire.com/","Official site provides a platform for property and casualty insurers.","https://www.guidewire.com/","Discuss agent permission tiers for claims, policy, billing, and customer-data workflows."),
("Veeva Systems","Regulated B2B","https://www.veeva.com/","Official site provides software, AI, data, and consulting for regulated life sciences.","https://www.veeva.com/","Focus on evidence, approval, and change governance for AI touching clinical, quality, regulatory, and commercial processes."),
("Tyler Technologies","Regulated B2B","https://www.tylertech.com/","Official site provides software and technology services to the public sector.","https://www.tylertech.com/solutions/artificial-intelligence","Use public-sector AI as context for attributable actions, human review, and data-boundary controls."),
("R1 RCM","Regulated B2B","https://www.r1rcm.com/","Official site provides technology-driven revenue-cycle management to healthcare organizations.","https://www.r1rcm.com/technology/","Lead with agent controls around PHI, billing actions, approvals, and rollback."),
("Definitive Healthcare","Regulated B2B","https://www.definitivehc.com/","Official site provides healthcare commercial intelligence and data products.","https://www.definitivehc.com/","Offer governance for research/sales agents that can access licensed healthcare data and CRM systems."),
("BlackLine","Regulated B2B","https://www.blackline.com/","Official site provides finance and accounting automation software.","https://www.blackline.com/solutions/intercompany/","Discuss approval, segregation of duties, audit logs, and recovery for agents affecting financial records."),
("Procore Technologies","Regulated B2B","https://www.procore.com/","Official site provides construction management software connecting project stakeholders and data.","https://www.procore.com/ai","Use its AI positioning to discuss bounded agent writes across project, financial, and document workflows."),
]

out=Path(__file__).with_name('prospect-list-2026-07-20.csv')
headers=['company','segment','website','public rationale','public source URL','personalization angle','verification status']
result=[]
for company,seg,web,rationale,src,angle in rows:
    try:
        req=Request(src,headers={'User-Agent':'Mozilla/5.0 (compatible; YaRoResearch/1.0)'})
        r=urlopen(req,timeout=15)
        code=r.status
        final=r.url
        status=f"Checked 2026-07-20: HTTP {code}"
        if final.rstrip('/') != src.rstrip('/'):
            status += f"; redirected to {final}"
        r.close()
    except HTTPError as e:
        status=f"Uncertain — checked 2026-07-20: HTTP {e.code} (may block automated requests)"
    except Exception as e:
        status=f"Uncertain — URL not confirmed during 2026-07-20 check ({type(e).__name__})"
    result.append((company,seg,web,rationale,src,angle,status))
with out.open('w',newline='',encoding='utf-8-sig') as f:
    csv.writer(f).writerow(headers); csv.writer(f).writerows(result)
print(out)
from collections import Counter
print(Counter(x[1] for x in result))
print(Counter('confirmed' if 'HTTP 200' in x[-1] else 'other' for x in result))
