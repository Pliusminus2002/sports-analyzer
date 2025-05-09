
# Sports Analyzer

**Projekto pavadinimas:** Sports Analyzer  
**Autorius:** Vaidilė Dubickaitė  
**Studijos:** Dirbtinio intelekto sistemos 
**Dalykas:** Objektinio programavimo pagrindai  
**Data:** 2025 m.

---

## Projekto aprašymas

**Sports Analyzer** yra interaktyvi, vartotojui patogi sporto analizės svetainė, skirta palyginti skirtingų komandų statistinius duomenis ir prognozuoti rungtynių baigtį. Projektas apima tris sporto šakas: **krepšinį**, **futbolą** ir **tinklinį**.

### Funkcijos:
- Komandų bei žaidėjų duomenų vizualizavimas (pagal pasirinktą sporto šaką).
- Dinaminis komandų palyginimas su laimėjimo tikimybių apskaičiavimu.
- Realių duomenų panaudojimas iš JSON failo.
- Objektiu programavimu grįsta backend logika (OOP).
- Automatiniai vienetiniai testai funkcionalumo patikrai.

Projektas sukurtas naudojant Python (Flask), HTML, CSS, JavaScript, o vartotojo sąsaja pritaikyta šiuolaikiniam naudojimui.

---

## Naudojamos technologijos

| Kalba / Įrankis      | Naudojimas |
|----------------------|------------|
| Python + Flask       | Backend / API |
| HTML, CSS, JS        | Vartotojo sąsaja |
| JSON                 | Duomenų saugojimas |
| Unittest             | Vienetiniai testai |
| Git, GitHub          | Versijų kontrolė |

---

## Projekto struktūra

```bash
sports-analyzer/
├── app/
│   ├── static/                # CSS, JS, paveikslėliai
│   ├── templates/app/         # HTML šablonai pagal sporto šakas
│   ├── models.py              # Žaidėjų ir komandų klasės
│   ├── utils.py               # Pagalbinės funkcijos
│   ├── routes.py              # Flask maršrutai ir puslapiai
│   └── data.json              # Komandų ir žaidėjų duomenys
├── tests/
│   └── test_models.py         # Vienetiniai testai
├── run.py                    # Projekto paleidimas
├── requirements.txt          # Naudojamos bibliotekos
└── README.md                 # Aprašymas (šis failas)
```

---

## Paleidimo instrukcijos

1. **Klonuoti projektą iš GitHub:**
```bash
git clone https://github.com/tavovardas/sports-analyzer.git
cd sports-analyzer
```
2. **(Pasirinktinai) aktyvuoti virtualią aplinką:**
```bash
python -m venv venv
source venv/bin/activate  # Linux / MacOS
venv\Scripts\activate     # Windows
```
3. **Įdiegti priklausomybes:**
```bash
pip install -r requirements.txt
```
4. **Paleisti projektą:**
```bash
python run.py
```
Tada naršyklėje atidaryti: `http://localhost:5000`

---

## Funkcionalumas

- Pagrindiniame puslapyje rodomos judančios sporto kamuolių animacijos (JS + CSS).
- Galima pasirinkti sporto šaką (krepšinis / futbolas / tinklinis).
- Pateikiamos komandų žaidėjų lentelės su vidutiniais rodikliais.
- Komandų palyginimas su tikimybe (%) kuri komanda laimės, apskaičiuota pagal algoritmą.

---

## Objektiu programavimu grįsta architektūra (OOP)

| Principas       | Realizacija |
|------------------|-------------|
| **Encapsulation** | Klasės `Player` ir `Team` turi savo metodus ir valdo duomenis lokaliai. |
| **Inheritance**   | Lengvai galima paveldėti bendras savybes į `BasketballPlayer`, `FootballPlayer`. |
| **Abstraction**   | `calculate_strength()` metodas slepia sudėtingumą nuo naudotojo. |
| **Polymorphism**  | Skirtingų sportų analizė vyksta skirtingai, bet tuo pačiu interfeisu. |

---

## Testavimas

Naudojamas **`unittest`** paketas:

```bash
python -m unittest discover tests
```

Tikrinama:
- Ar žaidėjai teisingai atpažįstami kaip sveiki / traumuoti.
- Komandų stiprumo skaičiavimas.
- Ar `PlayerFactory` sukuria tinkamą objektą.

---

## Internetinė demonstracija

Projekto demonstracija pasiekiama adresu:  
🔗 [https://sports-analyzer.onrender.com](https://sports-analyzer.onrender.com)

---

## Autorius

**Vaidilė Dubickaitė**  
Vilnius Tech, 2025
