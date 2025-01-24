# Release Notes

Im Rahmen der ISiK-Veröffentlichungen wird das [Semantic Versioning](https://semver.org/lang/de/) verwendet.

Die erste Ziffer X bezeichnet ein Major-Release und regelt die Gültigkeit von Releases. Die dritte Ziffer Y (Release x.0.y) bezeichnet eine technische Korrektur und versioniert kleinere Änderungen (Packages) während eines Jahres, z. B. 1.0.1.

Offene Punkte und bekannte Probleme siehe [GitHub Issues](https://github.com/gematik/ISiK-Dokumentenaustausch/issues?q=is%3Aissue+is%3Aopen+label%3A%22offene+Punkte+Ballot%22)



Version: 3.0.5

Datum: tbd

* `fix` `test modifying` Rollback der Entfernung von Patienten- und Encounter-Interaktionen (veranlasste Änderung in TC 3.0.1) - in diesem Zusammenhang wird auch der Suchparameter "subject" von SHALL auf MAY gesetzt https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/226

----

Version: 3.0.4

Datum: 25.11.2024

* Achtung: Einige IHE ValueSets sind sowohl in der referenzierten Version des de.basisprofil.r4 packages, als auch in de.ihe-d.terminology enthalten. Hier gelten immer die ValueSets aus dem IHE package.
* Hinzufügen von Dependencies für IHE ValueSets https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/193 & https://github.com/gematik/spec-ISiK-Dokumentenaustausch/commit/8d89dd1000e5cada0451b31eb93116835499f1c3

---

Version: 3.0.3

Datum: 07.05.2024

* fix IHEXDStypeCode Canonical-URL https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/187/commits/33b3832adfd65ba6496d419c92870d6f30d4ffe1
* add patternCoding by @f-peverali in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/190
* Fix der XDS Slices für .type und .category https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/189
* Update Basismodul-Dependency to Patch-Wildcard 3.0.x
* Add dependency to IHE package

----
Version: 3.0.2

Datum: 27.03.2024

* Hinweis hinzugefügt wie aus einer UUID eine OID generiert werden kann #172 by @alexzautke in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/172
* Hinweis zum Umgang mit Dokumentenupdates hinzugefügt
  * Fix/versionierung von dokumenten #177 by @alexzautke in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/177
* Hinweis zur base64-Kodierung von FHIR-nativen Dokumenten hinzugefügt
  * Hinweis zur Kodierung von FHIR Bundles hinzugefügt #178 by @alexzautke in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/178
* Hinweis zur Verwendung des ‘UNK’-Codes im KDL-Mapping hinzugefügt (#179): https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/179
* Klarstellung, dass keine Vorgaben für "Managing Return Content" bestehen by @alexzautke in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/183
* Beispiel Encounter geändert zu Abteilungskontakt (kohärent mit Basis): https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/184/files
* Update Basis dependency to 3.0.4

**Full Changelog**: https://github.com/gematik/spec-ISiK-Dokumentenaustausch/compare/v3.0.1...v.3.0.2

----
Version: 3.0.1

Datum: 05.01.2024

* Update Dependency zu Basismodul (Technical Correction 3.0.1)
* Nutzung der ISiKBinary präzisiert und im CapabilityStatement entsprechend korrigiert: add CpS statement and reference regarding ISIK binary PTDATA-605 by @f-peverali in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/157
* Anforderungen zur Nutzung der Ressourcen aus ISIK Basismodul präzisiert: Feature/ptdata 773 anforderungen anpassen basis ressourcen by @f-peverali in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/163
* rm all interaction on Encounter + Patient  in CpS by @f-peverali in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/165


----
Version: 3.0.0

Datum: 01.07.2023

* Mit dem Release der Stufe 3.0.0 werden die unten gelisteten Änderungen normativ festgesetzt.

----
Version: 3.0.0-rc4

Datum: 31.05.2023

* Dokumentenmetadaten (DocumentReference): Kardinalität korrigiert zur Harmonisierung mit MHD
  * update cardinality #139 by @f-peverali in https://github.com/gematik/spec-ISiK-Dokumentenaustausch/pull/143


Version: 3.0.0-rc3

Datum: 04.04.2023

* Update der Dependency auf Basismodul 3.0.0-rc2

---
Version: 3.0.0-rc2

Datum: 31.01.2023
- Status-Korrektur: "draft"
- Dependency update auf ISiK Basis-Version 2.0.4
- weitere Änderungen an Implementierungsleitfaden (informativ)
---
Version: 3.0.0-rc1

Datum: 04.01.2023
- Interaktion Dokumentenbereitstellung: Ersetzen der Operation $submit-document mit IHE ITI-105
- Interaktion Metadaten erzeugen: Ersetzen der Operation $generate-metadata mit IHE ITI-106
- Profil ISiKDokumentenMetadaten:
  - Kardinalität von DocumentReference.content.attachment.data und .url gelockert, um ITI-105 bedienen zu können
  - Kommentare zu Inkompatibilitäten angepasst auf die Änderungen in IHE MHD Version 4.2.0
- Akteure und Interaktionen: Anpassung der Dokumentation and die IHE Nomenklaturen
- Update MHD Dependency -> 4.2.0
- Update KDL Dependency -> 2022.1.2
- Beispieldaten an Änderungen in den Interaktionen angepasst
----
Version: 2.0.1

Datum: 31.10.2022

- Update Basismodul Dependency -> 2.0.2

----
Version: 2.0.0

Datum: 30.06.2022

- Initialer Release

----
