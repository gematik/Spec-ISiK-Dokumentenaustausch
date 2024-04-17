### Interaktionen

Für die Ressource DocumentReference MUSS die REST-Interaktion "CREATE" implementiert werden, siehe {{pagelink:ImplementationGuide/markdown/AkteureUndInteraktionen-Interaktion-Dokumentenbereitstellung.md}}.
Für die Ressource DocumentReference MUSS die REST-Interaktion "READ" implementiert werden, siehe {{pagelink:ImplementationGuide/markdown/AkteureUndInteraktionen-Dokumentenabfrage.md}}.

Folgende Suchparameter sind für das Bestätigungsverfahren relevant, auch in Kombination:

Die in IHE-MHD geltende Einschränkung, dass Clients bei allen Suchen mindestens die Parameter `patient` oder `patient.identifier` sowie `status` verwenden müssen, gilt nicht. Siehe dazu Kapitel {{pagelink:ImplementationGuide/markdown/Kompatibilitaet.md}}

1. Der Suchparameter "_id" MUSS unterstützt werden:

    Beispiele:

    ```GET [base]/DocumentReference?_id=103270```

    Anwendungshinweise: Weitere Informationen zur Suche nach "_id" finden sich in der [FHIR-Basisspezifikation - Abschnitt "Parameters for all resources"](https://hl7.org/fhir/R4/search.html#all).

1. Der Suchparameter "status" MUSS unterstützt werden:

    Beispiele:

    ```GET [base]/DocumentReference?status=final```

    Anwendungshinweise: Weitere Informationen zur Suche nach Token-type Parametern finden sich in der [FHIR-Basisspezifikation - Abschnitt "Token Search"](https://hl7.org/fhir/R4/search.html#token).

    Dieser Suchparameter ist für die Umsetzung des IHE MHD Profils für Clients und Server verpflichend.

1. Der Suchparameter "patient" MUSS unterstützt werden:

   Beispiele:

    ```GET [base]/DocumentReference?patient=Patient/123```

    Anwendungshinweise: Weitere Informationen zur Suche nach Reference-type Parametern finden sich in der [FHIR-Basisspezifikation - Abschnitt "Reference Search"](https://www.hl7.org/fhir/R4/search.html#reference).
	
	Dieser Suchparameter ist für die Umsetzung des IHE MHD Profils für Clients und Server verpflichend.
	
1. Der Suchparameter "type" MUSS unterstützt werden:

    Beispiele:

    ```GET [base]/DocumentReference?type=http://dvmd.de/fhir/CodeSystem/kdl|AD010101```

    Anwendungshinweise: Weitere Informationen zur Suche nach Token-type Parametern finden sich in der [FHIR-Basisspezifikation - Abschnitt "Token Search"](https://hl7.org/fhir/R4/search.html#token).

    Dieser Suchparameter ist für die Umsetzung des IHE MHD Profils für Server verpflichtend.

1. Der Suchparameter "category" MUSS unterstützt werden:

    Beispiele:

    ```GET [base]/DocumentReference?category=http://ihe-d.de/CodeSystem/IHEXDSclassCode|BEF```

    Anwendungshinweise: Weitere Informationen zur Suche nach Token-type Parametern finden sich in der [FHIR-Basisspezifikation - Abschnitt "Token Search"](https://hl7.org/fhir/R4/search.html#token).

    Dieser Suchparameter ist für die Umsetzung des IHE MHD Profils für Server verpflichtend.


1. Der custom Suchparameter "creation" MUSS unterstützt werden:

    Beispiele:

    ```GET [base]/DocumentReference?creation=2021-11-05```

    Anwendungshinweise: Weitere Informationen zur Suche nach Date-type Parametern finden sich in der [FHIR-Basisspezifikation - Abschnitt "Date Search"](https://hl7.org/fhir/R4/search.html#date).
	
	Dieser Suchparameter ist nicht Bestandteil der FHIR-Kernspezifikation und wurde [von IHE im Rahmen der MHD-Spezifikation definiert](https://profiles.ihe.net/ITI/MHD/SearchParameter-DocumentReference-Creation.html).

    Dieser Suchparameter ist für die Umsetzung des IHE MHD Profils für Server verpflichtend.


1. Der Suchparameter "encounter" MUSS unterstützt werden:

   Beispiele:

    ```GET [base]/DocumentReference?encounter=Encounter/123```

    Anwendungshinweise: Weitere Informationen zur Suche nach Reference-type Parametern finden sich in der [FHIR-Basisspezifikation - Abschnitt "Reference Search"](https://www.hl7.org/fhir/R4/search.html#reference).



### Verkettete Suchparameter (Chaining und Reverse Chaining)

Auch die verketteten Suchparameter MÜSSEN unterstützt werden und sind mit entsprechenden Referenzen im CapabilityStatement unter ```CapabilityStatement.rest.resource.searchInclude``` bzw. ```CapabilityStatement.rest.resource.searchRevInclude``` angegeben. Siehe {{pagelink:ImplementationGuide/markdown/CapabilityStatement.md}}

Informationen und Beispiele zur Suche nach verketteten Parametern finden sich [im Basismodul](https://simplifier.net/guide/isik-basis-v4/UebergreifendeFestlegungen-UebergreifendeFestlegungen_Suchparameter) und in der FHIR-Basisspezifikation im [Abschnitt "Chained Parameters"](https://hl7.org/fhir/R4/search.html#chaining) und im [Abschnitt "Reverse Chaining"](https://hl7.org/fhir/R4/search.html#has).

Die verketteten Suchparameter des Profils ```DocumentReference``` hängen wie folgt mit den festgelegten {{pagelink:ImplementationGuide/markdown/UseCasesAnwendung/UseCases.md, text:Anwendungsfällen (Use Cases)}}  zusammen:


1. Der verkettete Suchparameter ```Patient:identifier``` unterstützt den Anwendungsfall:

    Um für behandlungsrelevante Dokumente eine {{pagelink:ImplementationGuide/markdown/UseCasesAnwendung/UseCases.md, text:Verwechslung}} zwischen verschiedenen Patienten vermeiden.

    Beispiele:

    ```GET [base]/DocumentReference?patient.identifier=http://mein-krankenhaus.example/fhir/sid/patienten|1032702```

    ```GET [base]/DocumentReference?patient.identifier=1032702```

    Dieser Suchparameter ist für die Umsetzung des IHE MHD Profils für Client und Server verpflichtend.