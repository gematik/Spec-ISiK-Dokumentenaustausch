# Decision Log

Version: 3.0.5

* Problem: Durch die Entfernung von Anforderungen die Abfragen von Patienten- und Encounter-Ressourcen betreffend wäre die Herstellung von Dokumentenkontexten zu besagten Ressourcen in der Regel nicht mehr möglich.
* Lösung: Rollback der Änderung - wodurch die entsprechenden Suchparameter wieder in die Spezifikation aufgenommen werden.
* **Hintergrund**: 
Während der Überlegung zum Entfernen der Suchparamter waren zwei Architekturen angenommen worden:
- Architektur A - Integrierte Umgebung: Wir haben ein patientenführendes System (Basis -Server), das alleinig ISiK-Patienteninstanzen (und Encounter) verwaltet
- Architektur B  - geteilte Patienten (und -Encounter) Verwaltung: Basis-Server und DMS persistieren voneinander unabhängig ISiK-Patienten-Instanzen

Nachträglich erscheint Architektur A als nicht der Realität in KH-Umgebungen entsprechend - womöglich auch nicht als wünschenswert da eine Autonomie der Datenhaltung der verschiedenen Systeme auch bei Ausfällen ein Sicherheits-Feature darstellt.

Es stimmt daher NICHT, dass das DMS selbst keine Abfrage auf eine Patienten-Instanz erfüllen muss - sondern lediglich in der Lage sein SOLL/MUSS (dies nicht geprüft) die "referentielle Integrität" zu prüfen (ggf. noch zu forwarden) durch eine Anfrage an den Basis-Server.
Es muss dagegen angenommen werden, dass ein DMS auch immer Patienter- und Encounter-Abfragen (zumindest zur Herstellung der Ressourcen-Kontexte) ermöglichen muss. 
----
Version: 3.0.1

Datum: 11.12.2023

* Problem: Für das Modul Dokumentenaustausch sind die Abhängigkeit der referenzierten Ressourcen Encounter und Patient zum ISIK Basismodul nicht klar herausgearbeitet. Aus diesem Grund müssen die DMS-Systeme sämtliche Interaktionen, die auf diesen Ressourcen definiert sind auch umsetzen, um eine Bestätigung zu erlangen. 
  * Option A (ggf. mit Nennung der Risiken): Anforderungen zur Nutzung der Ressourcen aus ISIK Basismodul präzisieren und Testfallkataloge anpassen
  * Option B (ggf. mit Nennung der Risiken): Keine Änderung, damit bleiben offene Fragen zur Nutzung von Basismodul Ressourcen unklar
  * Entscheidung: Option A - umgesetzt hier: Anforderungen zur Nutzung der Ressourcen aus ISIK Basismodul wird präzisiert. Es werden entsprechende Interaktionen aus dem CapabilityStatement entfernt und ein generischer Text zur Klärung der Verwendung von Profilen und Interaktionen aus der Basis in diesem Modul wird hinzugefügt. Aus den Testfallkataloge werden Interaktionstests mit diesen Ressourcen, so wie sie in dem Testfallkatalog für Basismodul enthalten sind, entfernt. Stattdessen wird nur die Deferenzierbarkeit und Konformität der Ressourcen zu entsprechenden ISiK-Baisprofilen geprüft. 
  * Begründung: Die Profile des Moduls Dokumentenaustausch sollen im Sinne der Interoperabilität auch außerhalb des unmittelbaren Krankenhaus und ISiK-Umfeldes nutzbar sein. Dort wird z.B. womöglich ein vom ISIK-Profil abweichendes Patienten-Profil genutzt und dies soll weiterhin möglich sein. Auf eine explizite Referenz zu den ISiK-Profile mittels Reference(ISiKPatient) wurde daher verzichtet. Stattdessen wird in der Profilbeschreibung festgelegt, dass die ISiK-Profile nur *im Krankenhausumfeld* verpflichtend zu nutzen sind.
