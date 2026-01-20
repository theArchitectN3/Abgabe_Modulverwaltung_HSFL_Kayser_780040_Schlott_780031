# init_db.py
from app.database import SessionLocal, engine
from app.domain import models
from datetime import datetime, timedelta
import random

# --- 1. Reset Database ---
print("Resetting database...")
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

def create_data():
    print("Inserting comprehensive HS Flensburg real-world data...")

    # ==========================================
    # 1. STAFF
    # ==========================================
    
    president = models.User(username="christoph.jansen", full_name="Dr. Christoph Jansen (President)", role="Dean")
    
    comm_1 = models.User(username="antje.labes", full_name="Prof. Dr. Antje Labes (Comm)", role="Commission")
    comm_2 = models.User(username="bosco.lehr", full_name="Prof. Dr. Bosco Lehr (Comm)", role="Commission")
    comm_3 = models.User(username="michael.teichmann", full_name="Prof. Dr. Michael Teichmann (Comm)", role="Commission")

    coord_winf = models.User(username="coord_winf", full_name="Coord. Business Informatics", role="Coordinator")
    coord_maritime = models.User(username="coord_maritime", full_name="Coord. Maritime & Logistics", role="Coordinator")
    coord_bio = models.User(username="coord_bio", full_name="Coord. Biotech", role="Coordinator")
    coord_bwl = models.User(username="coord_bwl", full_name="Coord. Business Admin", role="Coordinator")

    # Lecturers
    lec_petersen = models.User(username="kai.petersen", full_name="Prof. Dr. Kai Petersen", role="Lecturer")
    lec_gerken = models.User(username="jan.gerken", full_name="Prof. Dr. Jan Gerken", role="Lecturer")
    lec_oelze = models.User(username="nelly.oelze", full_name="Prof. Dr. Nelly Oelze", role="Lecturer")
    lec_welland = models.User(username="ulrich.welland", full_name="Prof. Dr. Ulrich Welland", role="Lecturer")
    lec_kuemper = models.User(username="thorsten.kuemper", full_name="Prof. Dr. Thorsten Kümper", role="Lecturer")
    lec_brandenburg = models.User(username="marcus.brandenburg", full_name="Prof. Dr. Marcus Brandenburg", role="Lecturer")
    lec_severin = models.User(username="thomas.severin", full_name="Prof. Dr. Thomas Severin", role="Lecturer")
    lec_tausch = models.User(username="lasse.tausch", full_name="Prof. Dr. Lasse Tausch-Nebel", role="Lecturer")
    lec_schmidt = models.User(username="thomas.schmidt", full_name="Prof. Dr. Thomas Schmidt", role="Lecturer")
    lec_erichsen = models.User(username="indra.erichsen", full_name="Prof. Dr. Indra Erichsen", role="Lecturer")
    lec_geffert = models.User(username="roger.geffert", full_name="Prof. Dr. Roger Geffert", role="Lecturer")
    lec_cordts = models.User(username="soenke.cordts", full_name="Prof. Dr. Sönke Cordts", role="Lecturer")
    lec_heybock = models.User(username="hasso.heybock", full_name="Prof. Dr. Hasso Heybrock", role="Lecturer")
    lec_rusnjak = models.User(username="andreas.rusnjak", full_name="Prof. Dr. Andreas Rusnjak", role="Lecturer")

    lec_ziegler = models.User(username="pawel.ziegler", full_name="Prof. Pawel Ziegler", role="Lecturer")
    lec_limant = models.User(username="sander.limant", full_name="Prof. Sander Limant", role="Lecturer")
    lec_luebben = models.User(username="ralf.luebben", full_name="Prof. Dr. Ralf Luebben", role="Lecturer")
    lec_werninger = models.User(username="claus.werninger", full_name="Prof. Dr. Claus Werninger", role="Lecturer")
    lec_tuschy = models.User(username="ilja.tuschy", full_name="Prof. Dr. Ilja Tuschy", role="Lecturer")
    lec_leisse = models.User(username="ingmar.leisse", full_name="Prof. Dr. Ingmar Leiße", role="Lecturer")
    lec_clausen = models.User(username="brigitte.clausen", full_name="Prof. Dr. Brigitte Clausen", role="Lecturer")

    lec_labes = models.User(username="antje.labes_lec", full_name="Prof. Dr. Antje Labes", role="Lecturer")
    lec_anicolai = models.User(username="andreas.nicolai", full_name="Prof. Dr. Andreas Nicolai", role="Lecturer")
    lec_bnicolai = models.User(username="birte.nicolai", full_name="Prof. Dr. Birte Nicolai", role="Lecturer")
    lec_vest = models.User(username="anja.vest", full_name="Prof. Dr. Anja Vest", role="Lecturer")
    lec_uellendahl = models.User(username="hinrich.uellendahl", full_name="Prof. Dr. Hinrich Uellendahl", role="Lecturer")
    lec_langmaack = models.User(username="thies.langmaack", full_name="Prof. Dr. Thies Langmaack", role="Lecturer")
    lec_kyed = models.User(username="mads.kyed", full_name="Prof. Dr. Mads Kyed", role="Lecturer")
    lec_rohrlack = models.User(username="kirsten.rohrlack", full_name="Prof. Dr. Kirsten Rohrlack", role="Lecturer")
    lec_vith = models.User(username="wiktoria.vith", full_name="Prof. Dr. Wiktoria Vith", role="Lecturer")
    lec_subic = models.User(username="nico.subic", full_name="Prof. Nico Subic", role="Lecturer")
    lec_erdmann = models.User(username="frederik.erdmann", full_name="Prof. Frederik Erdmann", role="Lecturer")

    staff_users = [
        president, comm_1, comm_2, comm_3, 
        coord_winf, coord_maritime, coord_bio, coord_bwl,
        lec_petersen, lec_gerken, lec_oelze, lec_welland, lec_kuemper, lec_brandenburg, 
        lec_severin, lec_tausch, lec_schmidt, lec_erichsen, lec_geffert, lec_cordts, lec_heybock, lec_rusnjak,
        lec_ziegler, lec_limant, lec_luebben, lec_werninger, lec_tuschy, lec_leisse, lec_clausen,
        lec_labes, lec_anicolai, lec_bnicolai, lec_vest, lec_uellendahl, lec_langmaack, 
        lec_kyed, lec_rohrlack, lec_vith, lec_subic, lec_erdmann
    ]
    db.add_all(staff_users)
    db.commit()

    lec_map = {
        "petersen": lec_petersen, "gerken": lec_gerken, "oelze": lec_oelze, "welland": lec_welland,
        "kuemper": lec_kuemper, "brandenburg": lec_brandenburg, "severin": lec_severin, "tausch": lec_tausch,
        "schmidt": lec_schmidt, "erichsen": lec_erichsen, "geffert": lec_geffert, "cordts": lec_cordts,
        "heybock": lec_heybock, "rusnjak": lec_rusnjak,
        "ziegler": lec_ziegler, "limant": lec_limant, "luebben": lec_luebben, "werninger": lec_werninger,
        "tuschy": lec_tuschy, "leisse": lec_leisse, "clausen": lec_clausen,
        "labes": lec_labes, "anicolai": lec_anicolai, "bnicolai": lec_bnicolai, "vest": lec_vest,
        "uellendahl": lec_uellendahl, "langmaack": lec_langmaack, "kyed": lec_kyed, "rohrlack": lec_rohrlack,
        "vith": lec_vith, "subic": lec_subic, "erdmann": lec_erdmann
    }

    # ==========================================
    # 2. STUDY PROGRAMS & SPOs
    # ==========================================
    
    # WINF
    prog_winf = models.StudyProgram(name="B.Sc. Business Informatics")
    db.add(prog_winf)
    db.commit() 
    db.refresh(prog_winf)
    
    spo_winf = models.StudyRegulation(version="SPO 2024", valid_from="2024-09-01", program_id=prog_winf.id)
    db.add(spo_winf)
    db.commit()
    db.refresh(spo_winf)

    # Maritime
    prog_mar = models.StudyProgram(name="B.Sc. Seeverkehr, Nautik und Logistik")
    db.add(prog_mar)
    db.commit()
    db.refresh(prog_mar)

    spo_mar = models.StudyRegulation(version="SPO 2023", valid_from="2023-06-26", program_id=prog_mar.id)
    db.add(spo_mar)
    db.commit()
    db.refresh(spo_mar)

    # BWL
    prog_bwl = models.StudyProgram(name="B.A. Betriebswirtschaft")
    db.add(prog_bwl)
    db.commit()
    db.refresh(prog_bwl)

    spo_bwl = models.StudyRegulation(version="SPO 2025", valid_from="2025-06-18", program_id=prog_bwl.id)
    db.add(spo_bwl)
    db.commit()
    db.refresh(spo_bwl)

    # Bio
    prog_bio = models.StudyProgram(name="B.Sc. Biotechnologie-Lebensmitteltechnologie")
    db.add(prog_bio)
    db.commit()
    db.refresh(prog_bio)

    spo_bio = models.StudyRegulation(version="SPO 2024", valid_from="2024-07-10", program_id=prog_bio.id)
    db.add(spo_bio)
    db.commit()
    db.refresh(spo_bio)

    # ==========================================
    # 3. STUDENTS
    # ==========================================
    first_names = [
        "Lukas", "Julia", "Finn", "Laura", "Jan", "Sarah", "Niklas", "Anna", "Tom", "Lisa", 
        "Max", "Lena", "Tim", "Marie", "Felix", "Sophie", "Jonas", "Nele", "Ben", "Lea",
        "Noah", "Emma", "Paul", "Hannah", "Luis", "Mia", "Leon", "Emilia", "Elias", "Lina",
        "Matteo", "Sophia", "Luca", "Mila", "Theo", "Ella", "Emil", "Clara", "Henry", "Charlotte",
        "Anton", "Amelie", "Jakob", "Luise", "Moritz", "Johanna", "Leo", "Mathilda", "Alexander", "Lilli",
        "David", "Maja", "Maximilian", "Ida", "Oskar", "Frieda", "Phillip", "Pia", "Henri", "Leni",
        "Samuel", "Zoe", "Hannes", "Paula", "Mads", "Lotte", "Milan", "Romy", "Jonathan", "Mara"
    ]
    last_names = [
        "Mueller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
        "Koch", "Richter", "Klein", "Wolf", "Schroeder", "Neumann", "Schwarz", "Zimmermann", "Braun", "Hartmann",
        "Krueger", "Hofmann", "Lange", "Schmitt", "Werner", "Schmitz", "Krause", "Meier", "Lehmann", "Schmid",
        "Schulze", "Maier", "Koehler", "Herrmann", "Koenig", "Walter", "Mayer", "Huber", "Kaiser", "Fuchs",
        "Peters", "Lang", "Scholz", "Moeller", "Weiss", "Jung", "Hahn", "Schubert", "Vogel", "Friedrich",
        "Keller", "Gunther", "Frank", "Berger", "Winkler", "Roth", "Beck", "Lorenz", "Baumann", "Franke",
        "Albrecht", "Ludwig", "Bauer", "Nowak", "Simon", "Moeller", "Otto", "Pohl", "Bohm", "Kramer"
    ]
    
    students = []
    program_ids = [prog_winf.id, prog_bwl.id, prog_mar.id, prog_bio.id]
    
    for i in range(70):
        fname = first_names[i % len(first_names)]
        lname = last_names[i % len(last_names)]
        username = f"{fname.lower()}.{lname.lower()}"
        
        count = 1
        base_user = username
        while any(s.username == username for s in students):
            username = f"{base_user}{count}"
            count += 1
            
        pid = program_ids[i % len(program_ids)]
        
        # Max semesters depend on program
        max_sem = 6
        if pid == prog_bio.id: max_sem = 7
        if pid == prog_mar.id: max_sem = 8
        
        rand_semester = random.randint(1, max_sem)

        s = models.User(
            username=username, 
            full_name=f"{fname} {lname}", 
            role="Student",
            study_program_id=pid,
            current_semester=rand_semester
        )
        students.append(s)
    
    db.add_all(students)
    db.commit()

    # ==========================================
    # 4. MODULES (STANDARD CURRICULUM)
    # ==========================================
    modules_data = [
        # --- WIRTSCHAFTSINFORMATIK (6 Semester) ---
        {"c": "WI-101", "t": "Digitale Wirtschaft", "e": 5, "s": 1, "r": spo_winf.id, "p": "severin"},
        {"c": "WI-102", "t": "Programming Basics", "e": 5, "s": 1, "r": spo_winf.id, "p": "cordts"},
        {"c": "WI-103", "t": "Rechnerarchitekturen / Betriebssysteme", "e": 5, "s": 1, "r": spo_winf.id, "p": "luebben"},
        {"c": "WI-104", "t": "Allgemeine Betriebswirtschaftslehre", "e": 5, "s": 1, "r": spo_winf.id, "p": "tausch"},
        {"c": "WI-105", "t": "Mathematik", "e": 5, "s": 1, "r": spo_winf.id, "p": "welland"},
        {"c": "WI-106", "t": "Rechnungswesen 1", "e": 5, "s": 1, "r": spo_winf.id, "p": "tausch"},
        
        {"c": "WI-201", "t": "Business Process Management", "e": 5, "s": 2, "r": spo_winf.id, "p": "schmidt"},
        {"c": "WI-202", "t": "Programming User Interfaces", "e": 5, "s": 2, "r": spo_winf.id, "p": "cordts"},
        {"c": "WI-203", "t": "Netzwerke", "e": 5, "s": 2, "r": spo_winf.id, "p": "luebben"},
        {"c": "WI-204", "t": "Produktions- & Materialwirtschaft", "e": 5, "s": 2, "r": spo_winf.id, "p": "brandenburg"},
        {"c": "WI-205", "t": "Grundlagen der Statistik", "e": 5, "s": 2, "r": spo_winf.id, "p": "severin"},
        {"c": "WI-206", "t": "Rechnungswesen 2", "e": 5, "s": 2, "r": spo_winf.id, "p": "kuemper"},
        
        {"c": "WI-301", "t": "ERP-Systeme", "e": 5, "s": 3, "r": spo_winf.id, "p": "schmidt"},
        {"c": "WI-302", "t": "Software Engineering", "e": 5, "s": 3, "r": spo_winf.id, "p": "petersen"},
        {"c": "WI-303", "t": "Datenbanksysteme", "e": 5, "s": 3, "r": spo_winf.id, "p": "gerken"},
        {"c": "WI-304", "t": "Advanced Programming", "e": 5, "s": 3, "r": spo_winf.id, "p": "cordts"},
        {"c": "WI-305", "t": "Statistische Analyseverfahren", "e": 5, "s": 3, "r": spo_winf.id, "p": "severin"},
        {"c": "WI-306", "t": "Volkswirtschaftslehre", "e": 5, "s": 3, "r": spo_winf.id, "p": "tausch"},

        {"c": "WI-401", "t": "Data Science", "e": 5, "s": 4, "r": spo_winf.id, "p": "gerken"},
        {"c": "WI-402", "t": "Web Engineering", "e": 5, "s": 4, "r": spo_winf.id, "p": "petersen"},
        {"c": "WI-403", "t": "Research Methods", "e": 5, "s": 4, "r": spo_winf.id, "p": "petersen"},
        {"c": "WI-404", "t": "Wahlpflichtfach 1", "e": 5, "s": 4, "r": spo_winf.id, "p": "gerken"},
        {"c": "WI-405", "t": "Datenmanagement & Big Data", "e": 5, "s": 4, "r": spo_winf.id, "p": "gerken"},
        {"c": "WI-406", "t": "Investition & Finanzierung", "e": 5, "s": 4, "r": spo_winf.id, "p": "erichsen"},

        {"c": "WI-501", "t": "Business Model Transformation", "e": 5, "s": 5, "r": spo_winf.id, "p": "rusnjak"},
        {"c": "WI-502", "t": "Software-Projekt", "e": 5, "s": 5, "r": spo_winf.id, "p": "petersen"},
        {"c": "WI-503", "t": "IT-Recht", "e": 5, "s": 5, "r": spo_winf.id, "p": "heybock"},
        {"c": "WI-504", "t": "Wahlpflichtfach 2", "e": 5, "s": 5, "r": spo_winf.id, "p": "petersen"},
        {"c": "WI-505", "t": "Einfuehrung KI", "e": 5, "s": 5, "r": spo_winf.id, "p": "gerken"},
        {"c": "WI-506", "t": "Marketing", "e": 5, "s": 5, "r": spo_winf.id, "p": "oelze"},

        {"c": "WI-601", "t": "Berufspraktisches Projekt", "e": 18, "s": 6, "r": spo_winf.id, "p": "rusnjak"},
        {"c": "WI-602", "t": "Bachelorthesis & Kolloquium", "e": 12, "s": 6, "r": spo_winf.id, "p": "petersen"},

        # --- BETRIEBSWIRTSCHAFT (6 Semester) ---
        {"c": "BW-101", "t": "Mathematik fuer Wirtschaftswissenschaften", "e": 5, "s": 1, "r": spo_bwl.id, "p": "welland"},
        {"c": "BW-102", "t": "Allgemeine Betriebswirtschaftslehre", "e": 5, "s": 1, "r": spo_bwl.id, "p": "tausch"},
        {"c": "BW-103", "t": "Rechnungswesen 1", "e": 5, "s": 1, "r": spo_bwl.id, "p": "tausch"},
        {"c": "BW-104", "t": "Digitale Wirtschaft", "e": 5, "s": 1, "r": spo_bwl.id, "p": "rusnjak"},
        {"c": "BW-105", "t": "Volkswirtschaftslehre", "e": 5, "s": 1, "r": spo_bwl.id, "p": "tausch"},
        {"c": "BW-106", "t": "Methodenkompetenz", "e": 5, "s": 1, "r": spo_bwl.id, "p": "rohrlack"},

        {"c": "BW-201", "t": "Statistik fuer Wirtschaftswissenschaften", "e": 5, "s": 2, "r": spo_bwl.id, "p": "severin"},
        {"c": "BW-202", "t": "Produktions- und Materialwirtschaft", "e": 5, "s": 2, "r": spo_bwl.id, "p": "brandenburg"},
        {"c": "BW-203", "t": "Rechnungswesen 2", "e": 5, "s": 2, "r": spo_bwl.id, "p": "kuemper"},
        {"c": "BW-204", "t": "Betriebliche Informationsverarbeitung", "e": 5, "s": 2, "r": spo_bwl.id, "p": "cordts"},
        {"c": "BW-205", "t": "Wirtschaftsprivatrecht", "e": 5, "s": 2, "r": spo_bwl.id, "p": "geffert"},
        {"c": "BW-206", "t": "Leading and Presenting in Teams", "e": 5, "s": 2, "r": spo_bwl.id, "p": "rohrlack"},

        {"c": "BW-301", "t": "Grundlagen Investition & Finanzierung", "e": 5, "s": 3, "r": spo_bwl.id, "p": "erichsen"},
        {"c": "BW-302", "t": "Marketing", "e": 5, "s": 3, "r": spo_bwl.id, "p": "oelze"},
        {"c": "BW-303", "t": "Rechnungswesen 3", "e": 5, "s": 3, "r": spo_bwl.id, "p": "tausch"},
        {"c": "BW-304", "t": "Grundlagen Human Resource Management", "e": 5, "s": 3, "r": spo_bwl.id, "p": "rohrlack"},
        {"c": "BW-305", "t": "Wissenschaftliches Arbeiten", "e": 5, "s": 3, "r": spo_bwl.id, "p": "severin"},
        {"c": "BW-306", "t": "Professional Profiles & Systemic Intelligence", "e": 5, "s": 3, "r": spo_bwl.id, "p": "rohrlack"},

        {"c": "BW-401", "t": "Schwerpunktmodule", "e": 15, "s": 4, "r": spo_bwl.id, "p": "brandenburg"},
        {"c": "BW-402", "t": "Ergaenzungsmodule", "e": 10, "s": 4, "r": spo_bwl.id, "p": "erichsen"},
        {"c": "BW-403", "t": "Elective", "e": 5, "s": 4, "r": spo_bwl.id, "p": "geffert"},

        {"c": "BW-501", "t": "Schwerpunktmodule 2", "e": 15, "s": 5, "r": spo_bwl.id, "p": "brandenburg"},
        {"c": "BW-502", "t": "Ergaenzungsmodule 2", "e": 10, "s": 5, "r": spo_bwl.id, "p": "erichsen"},
        {"c": "BW-503", "t": "General Management", "e": 5, "s": 5, "r": spo_bwl.id, "p": "oelze"},

        {"c": "BW-601", "t": "Berufspraktisches Projekt", "e": 18, "s": 6, "r": spo_bwl.id, "p": "rohrlack"},
        {"c": "BW-602", "t": "Bachelorthesis", "e": 12, "s": 6, "r": spo_bwl.id, "p": "tausch"},

        # --- SEEVERKEHR, NAUTIK (8 Semester) ---
        {"c": "NAV-101", "t": "Bordpraktikum 1", "e": 30, "s": 1, "r": spo_mar.id, "p": "limant"},
        
        {"c": "NAV-201", "t": "Mathematik 1", "e": 5, "s": 2, "r": spo_mar.id, "p": "kyed"},
        {"c": "NAV-202", "t": "Informatik", "e": 4, "s": 2, "r": spo_mar.id, "p": "subic"},
        {"c": "NAV-203", "t": "Mechanik", "e": 5, "s": 2, "r": spo_mar.id, "p": "tuschy"},
        {"c": "NAV-204", "t": "Elektrotechnik", "e": 5, "s": 2, "r": spo_mar.id, "p": "leisse"},
        {"c": "NAV-205", "t": "Werkstoffkunde", "e": 3, "s": 2, "r": spo_mar.id, "p": "werninger"},
        {"c": "NAV-206", "t": "Thermodynamik", "e": 3, "s": 2, "r": spo_mar.id, "p": "tuschy"},
        {"c": "NAV-207", "t": "Grundlagen BWL", "e": 3, "s": 2, "r": spo_mar.id, "p": "tausch"},
        {"c": "NAV-208", "t": "Englisch 1", "e": 2, "s": 2, "r": spo_mar.id, "p": "vith"},

        {"c": "NAV-301", "t": "Mathematik 2", "e": 5, "s": 3, "r": spo_mar.id, "p": "kyed"},
        {"c": "NAV-302", "t": "Grundlagen Schiffbau", "e": 3, "s": 3, "r": spo_mar.id, "p": "ziegler"},
        {"c": "NAV-303", "t": "Navigation 1", "e": 7, "s": 3, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-304", "t": "Seeverkehrswirtschaft", "e": 2, "s": 3, "r": spo_mar.id, "p": "erdmann"},
        {"c": "NAV-305", "t": "Grundlagen Logistik", "e": 4, "s": 3, "r": spo_mar.id, "p": "brandenburg"},
        {"c": "NAV-306", "t": "Stroemungslehre", "e": 3, "s": 3, "r": spo_mar.id, "p": "tuschy"},
        {"c": "NAV-307", "t": "Wissenschaftliches Arbeiten", "e": 2, "s": 3, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-308", "t": "Wirtschaftsenglisch", "e": 2, "s": 3, "r": spo_mar.id, "p": "vith"},
        {"c": "NAV-309", "t": "Grundlagen Recht", "e": 2, "s": 3, "r": spo_mar.id, "p": "heybock"},

        {"c": "NAV-401", "t": "Schifffahrtsrecht", "e": 2, "s": 4, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-402", "t": "Stabilitaet", "e": 4, "s": 4, "r": spo_mar.id, "p": "ziegler"},
        {"c": "NAV-403", "t": "Navigation 2", "e": 2, "s": 4, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-404", "t": "Schiffsbetriebstechnik", "e": 2, "s": 4, "r": spo_mar.id, "p": "leisse"},
        {"c": "NAV-405", "t": "Gefahrstoffe", "e": 2, "s": 4, "r": spo_mar.id, "p": "erdmann"},
        {"c": "NAV-406", "t": "Gefahrgueter (IMDG)", "e": 2, "s": 4, "r": spo_mar.id, "p": "erdmann"},
        {"c": "NAV-407", "t": "Personalfuehrung / ISPS", "e": 5, "s": 4, "r": spo_mar.id, "p": "rohrlack"},
        {"c": "NAV-408", "t": "Gesundheitspflege", "e": 7, "s": 4, "r": spo_mar.id, "p": "vith"},
        {"c": "NAV-409", "t": "Meteorologie", "e": 4, "s": 4, "r": spo_mar.id, "p": "limant"},

        {"c": "NAV-501", "t": "Verwaltung & Umweltschutz", "e": 5, "s": 5, "r": spo_mar.id, "p": "erdmann"},
        {"c": "NAV-502", "t": "Seehandelsrecht", "e": 5, "s": 5, "r": spo_mar.id, "p": "heybock"},
        {"c": "NAV-503", "t": "Ladungssicherung", "e": 5, "s": 5, "r": spo_mar.id, "p": "ziegler"},
        {"c": "NAV-504", "t": "Systemueberwachung", "e": 2, "s": 5, "r": spo_mar.id, "p": "leisse"},
        {"c": "NAV-505", "t": "Internationale Logistik", "e": 2, "s": 5, "r": spo_mar.id, "p": "brandenburg"},
        {"c": "NAV-506", "t": "Navigation 3", "e": 8, "s": 5, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-507", "t": "Radarsimulation", "e": 3, "s": 5, "r": spo_mar.id, "p": "limant"},

        {"c": "NAV-601", "t": "Telekommunikation", "e": 4, "s": 6, "r": spo_mar.id, "p": "luebben"},
        {"c": "NAV-602", "t": "Bridge Procedures", "e": 7, "s": 6, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-603", "t": "Maritime Communications", "e": 4, "s": 6, "r": spo_mar.id, "p": "vith"},
        {"c": "NAV-604", "t": "Notfallmanagement", "e": 5, "s": 6, "r": spo_mar.id, "p": "erdmann"},
        {"c": "NAV-605", "t": "Hafenwirtschaft", "e": 5, "s": 6, "r": spo_mar.id, "p": "brandenburg"},
        {"c": "NAV-606", "t": "Supply Chain Management", "e": 5, "s": 6, "r": spo_mar.id, "p": "brandenburg"},

        {"c": "NAV-701", "t": "Bordpraktikum 2", "e": 30, "s": 7, "r": spo_mar.id, "p": "limant"},

        {"c": "NAV-801", "t": "Offshore Operations", "e": 3, "s": 8, "r": spo_mar.id, "p": "ziegler"},
        {"c": "NAV-802", "t": "Schiffssicherheit", "e": 2, "s": 8, "r": spo_mar.id, "p": "erdmann"},
        {"c": "NAV-803", "t": "Manoevrieren", "e": 4, "s": 8, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-804", "t": "Schiffsfuehrungssimulation", "e": 6, "s": 8, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-805", "t": "Wissenschaftliches Projekt", "e": 3, "s": 8, "r": spo_mar.id, "p": "limant"},
        {"c": "NAV-806", "t": "Bachelor Thesis", "e": 12, "s": 8, "r": spo_mar.id, "p": "limant"},

        # --- BIOTECHNOLOGIE (7 Semester) ---
        {"c": "BIO-101", "t": "Einfuehrung Bio-, Lebensmittel- und Verfahrenstechnik", "e": 10, "s": 1, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-102", "t": "Mathematik 1", "e": 5, "s": 1, "r": spo_bio.id, "p": "vest"},
        {"c": "BIO-103", "t": "Chemie", "e": 5, "s": 1, "r": spo_bio.id, "p": "uellendahl"},
        {"c": "BIO-104", "t": "Mechanik 1", "e": 5, "s": 1, "r": spo_bio.id, "p": "werninger"},
        {"c": "BIO-105", "t": "Werkstofftechnik", "e": 5, "s": 1, "r": spo_bio.id, "p": "werninger"},

        {"c": "BIO-201", "t": "Naturwissenschaftliche Grundlagen", "e": 5, "s": 2, "r": spo_bio.id, "p": "vest"},
        {"c": "BIO-202", "t": "Mikrobiologie", "e": 5, "s": 2, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-203", "t": "Mathematik 2", "e": 5, "s": 2, "r": spo_bio.id, "p": "vest"},
        {"c": "BIO-204", "t": "Physik", "e": 5, "s": 2, "r": spo_bio.id, "p": "vest"},
        {"c": "BIO-205", "t": "Informatik", "e": 5, "s": 2, "r": spo_bio.id, "p": "subic"},
        {"c": "BIO-206", "t": "Thermodynamik", "e": 5, "s": 2, "r": spo_bio.id, "p": "langmaack"},

        {"c": "BIO-301", "t": "Waerme- und Stoffuebertragung", "e": 5, "s": 3, "r": spo_bio.id, "p": "langmaack"},
        {"c": "BIO-302", "t": "Stroemungslehre", "e": 5, "s": 3, "r": spo_bio.id, "p": "langmaack"},
        {"c": "BIO-303", "t": "Mathematik 3", "e": 5, "s": 3, "r": spo_bio.id, "p": "vest"},
        {"c": "BIO-304", "t": "Lebensmittelanalytik", "e": 5, "s": 3, "r": spo_bio.id, "p": "bnicolai"},
        {"c": "BIO-305", "t": "Lebensmittelmikrobiologie", "e": 5, "s": 3, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-306", "t": "Bioverfahrenstechnik 1", "e": 5, "s": 3, "r": spo_bio.id, "p": "anicolai"},

        {"c": "BIO-401", "t": "Mess-, Steuer- und Regelungstechnik", "e": 5, "s": 4, "r": spo_bio.id, "p": "leisse"},
        {"c": "BIO-402", "t": "Konstruktion / CAE", "e": 5, "s": 4, "r": spo_bio.id, "p": "werninger"},
        {"c": "BIO-403", "t": "Betriebswirtschaftslehre / Recht", "e": 5, "s": 4, "r": spo_bio.id, "p": "tausch"},
        {"c": "BIO-404", "t": "Produkttechnologie pflanzlich", "e": 5, "s": 4, "r": spo_bio.id, "p": "anicolai"},
        {"c": "BIO-405", "t": "Analytische Biochemie", "e": 5, "s": 4, "r": spo_bio.id, "p": "bnicolai"},
        {"c": "BIO-406", "t": "Bioverfahrenstechnik 2", "e": 5, "s": 4, "r": spo_bio.id, "p": "anicolai"},

        {"c": "BIO-501", "t": "Technisches Wahlpflichtfach 1", "e": 5, "s": 5, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-502", "t": "Prozess- und Anlagetechnik 1", "e": 5, "s": 5, "r": spo_bio.id, "p": "langmaack"},
        {"c": "BIO-503", "t": "Produkttechnologie tierisch", "e": 5, "s": 5, "r": spo_bio.id, "p": "anicolai"},
        {"c": "BIO-504", "t": "Qualitaetsmanagement", "e": 5, "s": 5, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-505", "t": "Modellbildung Simulation BLT", "e": 5, "s": 5, "r": spo_bio.id, "p": "vest"},
        {"c": "BIO-506", "t": "Mechanische Verfahrenstechnik", "e": 5, "s": 5, "r": spo_bio.id, "p": "langmaack"},

        {"c": "BIO-601", "t": "Technisches Wahlpflichtfach 2", "e": 5, "s": 6, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-602", "t": "Nicht-technisches Wahlpflichtfach", "e": 5, "s": 6, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-603", "t": "Molekularbiologie", "e": 5, "s": 6, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-604", "t": "Produktentwicklung & Sensorik", "e": 5, "s": 6, "r": spo_bio.id, "p": "anicolai"},
        {"c": "BIO-605", "t": "Verpackungstechnik", "e": 5, "s": 6, "r": spo_bio.id, "p": "langmaack"},
        {"c": "BIO-606", "t": "Bioverfahrenstechnik 3", "e": 5, "s": 6, "r": spo_bio.id, "p": "anicolai"},

        {"c": "BIO-701", "t": "Berufspraktikum", "e": 18, "s": 7, "r": spo_bio.id, "p": "labes"},
        {"c": "BIO-702", "t": "Bachelor Thesis", "e": 12, "s": 7, "r": spo_bio.id, "p": "labes"},
    ]

    for m in modules_data:
        lecturer_obj = lec_map.get(m.get('p'))
        lec_id = lecturer_obj.id if lecturer_obj else None
        lec_name = lecturer_obj.full_name if lecturer_obj else "Unknown Lecturer"

        mod = models.Module(
            code=m["c"],
            title=m["t"],
            ects=m["e"],
            semester=m["s"],
            status="RELEASED",
            regulation_id=m["r"],
            description=f"Module {m['t']} in Semester {m['s']} taught by {lec_name}",
            lecturer_id=lec_id
        )
        db.add(mod)
    db.commit()

    # ==========================================
    # 5. HISTORICAL / DUMMY DATA FOR CHARTS
    # ==========================================
    
    # 1. Rejected by Coordinator (WINF)
    m1 = models.Module(code="WI-901", title="Crypto Finance", ects=5, semester=5, status="CHANGES_REQUIRED", regulation_id=spo_winf.id, lecturer_id=lec_rusnjak.id, description="Dummy")
    db.add(m1)
    db.commit()
    # History
    h1_1 = models.HistoryEntry(module_id=m1.id, timestamp=(datetime.now()-timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submitted", decision=True, reviewer_role="Author")
    h1_2 = models.HistoryEntry(module_id=m1.id, timestamp=(datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"), comment="Too risky content.", decision=False, reviewer_role="Program Coordinator")
    db.add_all([h1_1, h1_2])

    # 2. Rejected by Commission (Maritime)
    m2 = models.Module(code="NAV-902", title="Deep Sea Mining", ects=5, semester=6, status="CHANGES_REQUIRED", regulation_id=spo_mar.id, lecturer_id=lec_limant.id, description="Dummy")
    db.add(m2)
    db.commit()
    h2_1 = models.HistoryEntry(module_id=m2.id, timestamp=(datetime.now()-timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submit", decision=True, reviewer_role="Author")
    h2_2 = models.HistoryEntry(module_id=m2.id, timestamp=(datetime.now()-timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"), comment="Approved", decision=True, reviewer_role="Program Coordinator")
    h2_3 = models.HistoryEntry(module_id=m2.id, timestamp=(datetime.now()-timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ethical concerns.", decision=False, reviewer_role="Study Commission")
    db.add_all([h2_1, h2_2, h2_3])

    # 3. Pending at Dean (BWL)
    m3 = models.Module(code="BW-903", title="Advanced Controlling", ects=5, semester=4, status="REVIEW_DEAN", regulation_id=spo_bwl.id, lecturer_id=lec_kuemper.id, description="Dummy")
    db.add(m3)
    db.commit()
    h3_1 = models.HistoryEntry(module_id=m3.id, timestamp=(datetime.now()-timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submit", decision=True, reviewer_role="Author")
    h3_2 = models.HistoryEntry(module_id=m3.id, timestamp=(datetime.now()-timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Program Coordinator")
    h3_3 = models.HistoryEntry(module_id=m3.id, timestamp=(datetime.now()-timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Study Commission")
    db.add_all([h3_1, h3_2, h3_3])

    # 4. Pending at Commission (Bio)
    m4 = models.Module(code="BIO-904", title="Synthetic Biology", ects=5, semester=6, status="REVIEW_COMMISSION", regulation_id=spo_bio.id, lecturer_id=lec_labes.id, description="Dummy")
    db.add(m4)
    db.commit()
    h4_1 = models.HistoryEntry(module_id=m4.id, timestamp=(datetime.now()-timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submit", decision=True, reviewer_role="Author")
    h4_2 = models.HistoryEntry(module_id=m4.id, timestamp=(datetime.now()-timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Program Coordinator")
    db.add_all([h4_1, h4_2])

    # 5. Rejected by Dean (WINF) - Old entry (60 days ago)
    m5 = models.Module(code="WI-905", title="Legacy Cobol", ects=5, semester=5, status="CHANGES_REQUIRED", regulation_id=spo_winf.id, lecturer_id=lec_petersen.id, description="Dummy")
    db.add(m5)
    db.commit()
    h5_1 = models.HistoryEntry(module_id=m5.id, timestamp=(datetime.now()-timedelta(days=65)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submit", decision=True, reviewer_role="Author")
    h5_2 = models.HistoryEntry(module_id=m5.id, timestamp=(datetime.now()-timedelta(days=62)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Program Coordinator")
    h5_3 = models.HistoryEntry(module_id=m5.id, timestamp=(datetime.now()-timedelta(days=61)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Study Commission")
    h5_4 = models.HistoryEntry(module_id=m5.id, timestamp=(datetime.now()-timedelta(days=60)).strftime("%Y-%m-%d %H:%M:%S"), comment="Not relevant anymore.", decision=False, reviewer_role="Dean")
    db.add_all([h5_1, h5_2, h5_3, h5_4])

    # 6. Released recently
    m6 = models.Module(code="WI-906", title="Green IT", ects=5, semester=5, status="RELEASED", regulation_id=spo_winf.id, lecturer_id=lec_gerken.id, description="Dummy")
    db.add(m6)
    db.commit()
    h6_1 = models.HistoryEntry(module_id=m6.id, timestamp=(datetime.now()-timedelta(days=15)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submit", decision=True, reviewer_role="Author")
    h6_2 = models.HistoryEntry(module_id=m6.id, timestamp=(datetime.now()-timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Program Coordinator")
    h6_3 = models.HistoryEntry(module_id=m6.id, timestamp=(datetime.now()-timedelta(days=12)).strftime("%Y-%m-%d %H:%M:%S"), comment="Ok", decision=True, reviewer_role="Study Commission")
    h6_4 = models.HistoryEntry(module_id=m6.id, timestamp=(datetime.now()-timedelta(days=10)).strftime("%Y-%m-%d %H:%M:%S"), comment="Great addition.", decision=True, reviewer_role="Dean")
    db.add_all([h6_1, h6_2, h6_3, h6_4])

    # 7. Another Rejected by Coordinator (BWL)
    m7 = models.Module(code="BW-907", title="Speculation 101", ects=5, semester=2, status="CHANGES_REQUIRED", regulation_id=spo_bwl.id, lecturer_id=lec_severin.id, description="Dummy")
    db.add(m7)
    db.commit()
    h7_1 = models.HistoryEntry(module_id=m7.id, timestamp=(datetime.now()-timedelta(days=8)).strftime("%Y-%m-%d %H:%M:%S"), comment="Submit", decision=True, reviewer_role="Author")
    h7_2 = models.HistoryEntry(module_id=m7.id, timestamp=(datetime.now()-timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"), comment="Too theoretical.", decision=False, reviewer_role="Program Coordinator")
    db.add_all([h7_1, h7_2])

    db.commit()
    print("✅ SUCCESS: Database populated with standard curriculum AND historical demo data!")
    db.close()

if __name__ == "__main__":
    create_data()