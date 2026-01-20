# Modulverwaltung HS Flensburg - Software Engineering Projekt

Dieses Projekt implementiert eine webbasierte Modulverwaltungssoftware basierend auf den Prinzipien der Clean Architecture. Sie ermöglicht den vollständigen Lebenszyklus eines Moduls von der Erstellung durch Dozenten über die Prüfung durch Gremien bis zur Veröffentlichung.

**Autoren:** Nick Kayser, Mats Schlott  
**Datum:** 20.01.2026

## 🚀 Features & Highlights

*   **Clean Architecture:** Strikte Trennung von Domain, Application, Infrastructure und UI Layer.
*   **Workflow Engine:** Implementierter Zustandsautomat (Draft -> Review Coordinator -> Review Commission -> Review Dean -> Released).
*   **Rollenspezifische Dashboards:**
    *   **Studierende:** Einsicht in Studienverlauf, simuliertes Notenkonto & Workload-Analyse (Charts).
    *   **Lehrende:** Verwaltung eigener Module (Entwürfe vs. Veröffentlicht).
    *   **Gremien (Koordinator/Kommission/Dekan):** "Inbox"-Workflow für Genehmigungen, Audit-Logs und Statistiken.
*   **Echte Datenbasis:** Das System initialisiert sich mit realen Modulen und Dozenten der HS Flensburg (Wirtschaftsinformatik, BWL, Nautik, Bio).

## 🛠 Tech Stack

*   **Backend:** Python, FastAPI, SQLAlchemy
*   **Frontend:** Jinja2 Templates, Bootstrap 5, Chart.js
*   **Datenbank:** SQLite (automatische Initialisierung)

## 📦 Installation & Start

1.  **Abhängigkeiten installieren:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Anwendung starten:**
    ```bash
    python main.py
    ```
    *Das System setzt die Datenbank bei jedem Neustart zurück und befüllt sie mit Demo-Daten.*

3.  **Browser öffnen:**
    *   URL: [http://127.0.0.1:8080](http://127.0.0.1:8080)

## 🧪 Test-Szenarien für die Demo

Nutzen Sie den Rollen-Umschalter oben rechts (`Role: ...`), um das System zu erkunden.

1.  **Szenario "Student":** 
    *   Wählen Sie Rolle `Student` und einen Studenten (z.B. "Lukas Müller") aus dem Dropdown.
    *   Beobachten Sie das **personalisierte Dashboard** mit Notenspiegel und Semester-Workload.
    *   Wechseln Sie den Studenten, um andere Daten zu sehen.

2.  **Szenario "Workflow":**
    *   Wählen Sie Rolle `Lecturer` -> "Prof. Dr. Kai Petersen".
    *   Erstellen Sie ein neues Modul ("Create Module").
    *   Reichen Sie es ein ("Submit for Review").
    *   Wechseln Sie zur Rolle `Coordinator`. Das Modul erscheint in der Inbox.
    *   Genehmigen Sie das Modul durch die Instanzen bis zum `Dean`.

3.  **Szenario "Analytics":**
    *   Die Dashboards von `Coordinator` und `Dean` bieten statistische Auswertungen (Chart.js) über den Modulstatus.
    *   Nutzen Sie den **Zeitfilter** (oben rechts im Chart), um historische Daten zu filtern.
