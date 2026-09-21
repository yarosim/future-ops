# CMMC 2.0 Readiness Toolkit — NIST SP 800-171 Rev 2 Self-Assessment Checklist

All 110 security requirements, 14 families. For each: plain-English requirement, small-supplier implementation, evidence, common gaps. Mark status in `gap-tracker.csv`. A control only counts MET if you can show an assessor the evidence.

---

## 3.1 Access Control (22 controls)

**3.1.1 Limit system access to authorized users, processes, devices.** Every account individually assigned; no shared logins. *Evidence:* account inventory, offboarding records. *Common gap:* shared shop-floor logins; ex-employee accounts never disabled.

**3.1.2 Limit access to authorized transactions/functions.** Role-based permissions. *Evidence:* role matrix, group memberships. *Common gap:* everyone is ERP/Domain admin.

**3.1.3 Control the flow of CUI per approved authorizations.** Restrict CUI flow (firewall rules, DLP). *Evidence:* data-flow diagram, firewall exports. *Common gap:* no flow diagram; CUI scattered.

**3.1.4 Separate duties of individuals.** No one both performs and approves security actions. *Evidence:* duty-separation doc, review records. *Common gap:* single IT person no independent review — document owner oversight.

**3.1.5 Employ least privilege.** Minimum necessary access. *Evidence:* privileged account list. *Common gap:* users run as local admin.

**3.1.6 Use non-privileged accounts for non-security functions.** Two-account model. *Evidence:* paired account inventory. *Common gap:* admins read email from admin account.

**3.1.7 Prevent non-privileged execution of privileged functions; audit them.** *Evidence:* GPO exports, elevation logs. *Common gap:* users install anything.

**3.1.8 Limit unsuccessful logon attempts.** Lockout 3–5 failures everywhere CUI touches. *Evidence:* policy exports. *Common gap:* lockout on laptops not ERP/devices.

**3.1.9 Privacy/security notices (monitoring consent).** Login banner. *Evidence:* GPO legal notice. *Common gap:* only on workstations.

**3.1.10 Session lock with pattern-hiding.** 15-min screen lock. *Evidence:* GPO settings. *Common gap:* users disable it.

**3.1.11 Terminate sessions after defined conditions.** Enforced timeouts. *Evidence:* timeout configs. *Common gap:* documented not enforced.

**3.1.12 Monitor and control remote-access sessions.** Managed logged gateway. *Evidence:* remote-access policy, VPN logs. *Common gap:* exposed RDP.

**3.1.13 Cryptographic protection of CUI in transit.** TLS/VPN. *Evidence:* TLS config. *Common gap:* CUI emailed clear.

**3.1.14 Route remote access through managed control points.** Single entry. *Evidence:* network diagram, firewall rules. *Common gap:* ad-hoc remote paths.

**3.1.15 Encrypt CUI on remote-access devices.** Full-disk encryption. *Evidence:* BitLocker status. *Common gap:* unencrypted personal laptops.

**3.1.16 Implement session lock/termination controls (prove it fires).** *Evidence:* tested example. *Common gap:* GPO not applied everywhere.

**3.1.17 Refuse network requests by origin (allowlists).** *Evidence:* GPO/firewall allowlists. *Common gap:* compensate via gateway.

**3.1.18 Control WLANs for CUI.** WPA2/3-Enterprise, isolated guest. *Evidence:* wireless config. *Common gap:* shared PSK.

**3.1.19 Encrypt CUI on mobile devices.** *Evidence:* MDM/encryption report. *Common gap:* unmanaged phones.

**3.1.20 Verify/control connections to external systems.** *Evidence:* interconnection list. *Common gap:* shadow vendor connections.

**3.1.21 Limit external connections to systems storing CUI.** *Evidence:* firewall policy. *Common gap:* uncontrolled FTP.

**3.1.22 FCI/CUI disclosure controls.** *Evidence:* marking policy. *Common gap:* unmarked downloads.

## 3.2 Awareness & Training (3 controls)

**3.2.1 Ensure MGMT/admins/security trained.** *Evidence:* training certs. *Common gap:* nobody tracks it.

**3.2.2 Ensure personnel trained for security duties.** Annual awareness training. *Evidence:* training records. *Common gap:* "training" = an email.

**3.2.3 Training on recognizing/reporting threats.** *Evidence:* training, phishing test. *Common gap:* no simulation.

## 3.3 Audit & Accountability (9 controls)

**3.3.1 Create/protect audit logs.** *Evidence:* policy, sample logs. *Common gap:* default logging only.
**3.3.2 Protect audit info + correct problems.** *Evidence:* log destination (central). *Common gap:* logs on user machine.
**3.3.3 Review and analyze logs.** *Evidence:* monthly review records. *Common gap:* collected never read.
**3.3.4 Alert on audit process failure.** *Evidence:* monitoring config. *Common gap:* nothing.
**3.3.5 Correlate audit info.** *Evidence:* central log store. *Common gap:* siloed.
**3.3.6 Define audit events.** *Evidence:* audit policy doc. *Common gap:* undefined.
**3.3.7 Audit reduction/reporting.** *Evidence:* SIEM report samples. *Common gap:* raw logs only.
**3.3.8 Approved timestamps (NTP).** *Evidence:* time-source config. *Common gap:* drift.
**3.3.9 Protect audit info from unauthorized access.** *Evidence:* ACL config. *Common gap:* open log share.

## 3.4 Configuration Management (9 controls)

**3.4.1 Establish configuration settings (baseline).** *Evidence:* baseline doc. *Common gap:* none.
**3.4.2 Enforce security config settings.** *Evidence:* GPO/Intune. *Common gap:* documented not enforced.
**3.4.3 Track/monitor/control config changes.** *Evidence:* change records. *Common gap:* ad hoc.
**3.4.4 Analyze security impact of changes.** *Evidence:* change tickets. *Common gap:* none.
**3.4.5 Define/limit ports/protocols/services.** *Evidence:* port inventory. *Common gap:* defaults.
**3.4.6 Restrict/remove unnecessary programs.** *Evidence:* approved software list. *Common gap:* bloatware.
**3.4.7 Control/monitor user-installed software.** *Evidence:* install policy. *Common gap:* users install freely.
**3.4.8 Deny-by-exception software policy.** *Evidence:* blacklist. *Common gap:* none.
**3.4.9 Monitor security-relevant COTS/GOTS config.** *Evidence:* config reviews. *Common gap:* never revisited.

## 3.5 Identification & Authentication (11 controls)

**3.5.1 Identify users/processes/devices.** *Evidence:* account inventory. *Common gap:* anonymous/service accounts.
**3.5.2 Authenticate uniquely (MFA on remote).** *Evidence:* MFA settings. *Common gap:* MFA only email.
**3.5.3 MFA for privileged/network access.** *Evidence:* MFA report. *Common gap:* none on VPN/admin.
**3.5.4 Replay-resistant auth.** *Evidence:* protocol settings (Kerberos/TLS1.2+). *Common gap:* legacy auth.
**3.5.5 Prevent reuse of identifiers.** *Evidence:* lifecycle process. *Common gap:* recycled accounts.
**3.5.6 Disable identifiers after inactivity.** *Evidence:* policy. *Common gap:* dormant accounts.
**3.5.7 Password complexity minimum.** *Evidence:* GPO export. *Common gap:* weak passwords.
**3.5.8 Prohibit password reuse.** *Evidence:* history. *Common gap:* reuse.
**3.5.9 Temporary passwords changed on first login.** *Evidence:* default config. *Common gap:* never forced.
**3.5.10 Store/transmit cryptographically-protected passwords.** *Evidence:* vault, script scan. *Common gap:* scripts/sticky notes.
**3.5.11 Obscure auth feedback.** *Evidence:* masking. *Common gap:* rare.

## 3.6 Incident Response (3 controls)

**3.6.1 Establish IR capability.** *Evidence:* IR plan. *Common gap:* none.
**3.6.2 Track/document/correct incidents.** *Evidence:* incident log. *Common gap:* verbal only.
**3.6.3 Test IR processes.** *Evidence:* annual test. *Common gap:* never tested.

## 3.7 Maintenance (6 controls)

**3.7.1 Perform maintenance (patching).** *Evidence:* maintenance records. *Common gap:* inconsistent.
**3.7.2 Supervise/spare equipment/logistics.** *Evidence:* spares list. *Common gap:* unknown spares.
**3.7.3 Maintenance personnel approved access.** *Evidence:* vendor policy. *Common gap:* MSP free rein.
**3.7.4 MFA for remote maintenance.** *Evidence:* tool config. *Common gap:* RMM no MFA.
**3.7.5 Supervise/protect non-local maintenance.** *Evidence:* session logging. *Common gap:* unsupervised.
**3.7.6 Sanitize removed CUI components.** *Evidence:* NIST 800-88 records. *Common gap:* drives leave unwiped.

## 3.8 Media Protection (9 controls)

**3.8.1 Mark CUI media.** *Evidence:* labeling. *Common gap:* unmarked.
**3.8.2 Restrict access to CUI media.** *Evidence:* storage access. *Common gap:* open drawers.
**3.8.3 Log removal of media.** *Evidence:* media log. *Common gap:* no tracking.
**3.8.4 Protect media in transport.** *Evidence:* shipping policy. *Common gap:* plain USB mailed.
**3.8.5 Control accountability for stored media.** *Evidence:* inventory. *Common gap:* unknown location.
**3.8.6 Cryptographic protection at rest.** *Evidence:* encryption report. *Common gap:* unencrypted USBs.
**3.8.7 Remove CUI before disposal (NIST 800-88).** *Evidence:* disposal certs. *Common gap:* tossed whole.
**3.8.8 Sanitize before external release.** *Evidence:* verification. *Common gap:* returned unwiped.
**3.8.9 Control media access in exit facilities.** *Evidence:* physical controls. *Common gap:* low risk.

## 3.9 Personnel Security (2 controls)

**3.9.1 Screen personnel (background checks).** *Evidence:* screening records. *Common gap:* none documented.
**3.9.2 Terminate access on personnel actions.** *Evidence:* offboarding checklist. *Common gap:* delayed removal.

## 3.10 Physical Protection (6 controls)

**3.10.1 Limit physical access to CUI systems.** *Evidence:* access list. *Common gap:* open closet server.
**3.10.2 Visitor provisions/controls.** *Evidence:* sign-in log. *Common gap:* none.
**3.10.3 Control/monitor physical access (logs).** *Evidence:* review records. *Common gap:* never reviewed.
**3.10.4 Escort visitors.** *Evidence:* policy. *Common gap:* visitors wander.
**3.10.5 Manage access devices (keys/badges).** *Evidence:* key log. *Common gap:* mystery keys.
**3.10.6 Safeguards for CUI at work/remote.** *Evidence:* remote-work policy. *Common gap:* none.

## 3.11 Risk Assessment (3 controls)

**3.11.1 Periodic risk assessment.** *Evidence:* risk report. *Common gap:* never.
**3.11.2 Vulnerability scanning.** *Evidence:* scan reports. *Common gap:* none.
**3.11.3 Remediate vulnerabilities per risk.** *Evidence:* remediation log. *Common gap:* never fixed.

## 3.12 Security Assessment (12 controls)

**3.12.1 Periodically assess security controls.** *Evidence:* assessment records. *Common gap:* none documented.
**3.12.2 Develop/document POA&M.** *Evidence:* POA&M. *Common gap:* no tracking.
**3.12.3 Monitor controls ongoing.** *Evidence:* dashboard/report. *Common gap:* point-in-time.
**3.12.4 Develop/validate plan for inadequate controls.** *Evidence:* test report. *Common gap:* no fix plan.

## 3.13 System & Communications Protection (16 controls)

**3.13.1 Boundary protections.** *Evidence:* firewall, DMZ diagram. *Common gap:* flat network.
**3.13.2 Partition into defined components.** *Evidence:* VLAN config. *Common gap:* single LAN.
**3.13.3 Communications control (logical separation).** *Evidence:* segmentation. *Common gap:* CUI + guest same LAN.
**3.13.4 Deny-by-default network.** *Evidence:* default-deny rules. *Common gap:* permissive.
**3.13.5 Subnetworks for public systems (DMZ).** *Evidence:* DMZ config. *Common gap:* none.
**3.13.6 Prevent public-subnet hopping.** *Evidence:* path rules. *Common gap:* double-hop.
**3.13.7 Session authenticity.** *Evidence:* TLS. *Common gap:* plaintext mgmt.
**3.13.8 FIPS-validated crypto.** *Evidence:* FIPS config. *Common gap:* non-FIPS.
**3.13.9 Prohibit remote activation of collaborative devices.** *Evidence:* config. *Common gap:* unmonitored gear.
**3.13.10 Secure CUI transmission.** *Evidence:* TLS/SFTP. *Common gap:* plaintext.
**3.13.11 Encrypt command/control traffic.** *Evidence:* SSH/RDP-TLS. *Common gap:* Telnet admin.
**3.13.12 Encrypt CUI at rest.** *Evidence:* encryption report. *Common gap:* unencrypted backups.
**3.13.13 Approved random generators.** *Evidence:* platform default. *Common gap:* met via platform.
**3.13.14 Protect CUI on shared resources.** *Evidence:* sanitization. *Common gap:* VM/disk reuse.
**3.13.15 Collaborate externally to protect CUI (agreements).** *Evidence:* agreements. *Common gap:* verbal only.
**3.13.16 PKI maps identity to keys.** *Evidence:* CA config. *Common gap:* self-signed everywhere.

## 3.14 System & Information Integrity (7 controls)

**3.14.1 Identify/report/remediate flaws (patch mgmt).** *Evidence:* patch records. *Common gap:* patch when broken.
**3.14.2 Protection from malicious code (EDR/AV).** *Evidence:* AV/EDR reports. *Common gap:* unmanaged Defender.
**3.14.3 Monitor integrity alerts.** *Evidence:* alert config. *Common gap:* no monitoring.
**3.14.4 Update malicious-code protection.** *Evidence:* update logs. *Common gap:* auto-update off.
**3.14.5 Periodic scans / real-time monitoring.** *Evidence:* scan history. *Common gap:* never scanned.
**3.14.6 Monitor suspicious behavior (EDR).** *Evidence:* EDR alerts. *Common gap:* "didn't need it."
**3.14.7 Integrate malicious-code protection.** *Evidence:* mgmt console report. *Common gap:* inconsistent AV.

**Total: 110 controls, 14 families — NIST SP 800-171 Rev 2.**

---
*This toolkit is a self-assessment aid, not a substitute for a formal C3PAO assessment or legal advice.*