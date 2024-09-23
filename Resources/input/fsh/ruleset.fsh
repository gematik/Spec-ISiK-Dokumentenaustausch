RuleSet: Meta
* ^version = "4.0.1"
* ^status = #active
* ^experimental = false
* ^publisher = "gematik GmbH"
* ^date = "2024-09-23"

RuleSet: Meta-Inst
* status = #active
* publisher = "gematik GmbH"
* date = "2024-09-23"

RuleSet: Meta-CapabilityStatement
* status = #active
* experimental = false
* version = "4.0.1"
* publisher = "gematik GmbH"
* date = "2024-09-23"
* implementationGuide = "https://gematik.de/fhir/isik/ImplementationGuide/ISiK-Dokumentenaustausch"
* url = "https://gematik.de/fhir/isik/CapabilityStatement/ISiKCapabilityStatementDokumentenaustauschServer"

RuleSet: Expectation (expectation)
* extension.url = $capabilitystatement-expectation
* extension.valueCode = {expectation}