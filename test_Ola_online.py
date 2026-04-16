import streamlit as st

# Konfiguracja strony pod urządzenia mobilne
st.set_page_config(page_title="Test na style uczenia się", layout="centered")

st.title("🧠 Test na style uczenia się")
st.info("Wskazówka: Może się zdarzyć, że na jedno pytanie udzielisz kilku odpowiedzi. W takim przypadku zaznacz wszystkie pasujące opcje[cite: 110, 212].")

# Pełna baza pytań i mapowanie odpowiedzi na style (W, S, D, K)
# Opracowano na podstawie treści dokumentu 
pytania_data = [
    {
        "q": "1. Gdy spotykasz nieznaną ci osobę, na co zwracasz uwagę w pierwszej kolejności? [cite: 111]",
        "options": [
            ("co w stosunku do niej czujesz [cite: 112]", "D"),
            ("jak wygląda i jak jest ubrana [cite: 113]", "W"),
            ("w jaki sposób i co mówi, jaki ma głos [cite: 114]", "S"),
            ("w jaki sposób się zachowuje i co robi [cite: 115]", "K")
        ]
    },
    {
        "q": "2. Co najczęściej zostaje ci w pamięci po kilku dniach od spotkania nieznanej ci wcześniej osoby? [cite: 116]",
        "options": [
            ("to, co robiliście razem, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz [cite: 117]", "K"),
            ("jej imię/nazwisko [cite: 118]", "S"),
            ("to, co czułeś, będąc w jej towarzystwie, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz [cite: 119]", "D"),
            ("jej twarz [cite: 120]", "W")
        ]
    },
    {
        "q": "3. Gdy wchodzisz do nieznanego ci pomieszczenia, na co zwracasz przede wszystkim uwagę? [cite: 121]",
        "options": [
            ("na jego wygląd [cite: 122]", "W"),
            ("na to, jak dobrze emocjonalnie i fizycznie się w nim czujesz [cite: 123]", "D"),
            ("na to, co się w nim dzieje i co ty mógłbyś w nim robić [cite: 124]", "K"),
            ("na dźwięki i rozmowy, jakie się w nim toczą [cite: 125]", "S")
        ]
    },
    {
        "q": "4. Gdy uczysz się czegoś nowego, w jaki sposób robisz to najchętniej? [cite: 126]",
        "options": [
            ("zapisywanie informacji, rysunki, dotykanie przedmiotów, pisanie na klawiaturze [cite: 127]", "D"),
            ("projekty, symulacje, eksperymenty, gry, angażowanie się w ruch [cite: 128]", "K"),
            ("czytanie, oglądanie ilustracji, wykresów, map, szkiców [cite: 129]", "W"),
            ("wyjaśnienia słowne, wykład, dyskusja i zadawanie pytań [cite: 130]", "S")
        ]
    },
    {
        "q": "5. Gdy uczysz czegoś innych, co zwykle robisz? [cite: 131]",
        "options": [
            ("objaśniasz wszystko werbalnie bez materiałów graficznych [cite: 132]", "S"),
            ("rysujesz coś, piszesz lub używasz rąk do wyjaśniania [cite: 133]", "D"),
            ("demonstrujesz coś robiąc to lub każesz uczniom robić to z tobą [cite: 134]", "K"),
            ("dajesz im coś do oglądania (przedmiot, ilustrację, wykres) [cite: 135]", "W")
        ]
    },
    {
        "q": "6. Jaki rodzaj książek czytasz najchętniej? [cite: 136]",
        "options": [
            ("informacje faktograficzne, historyczne lub dużo dialogów [cite: 137]", "S"),
            ("krótkie książki z wartką akcją lub poradniki hobby/sport [cite: 138]", "K"),
            ("o uczuciach i emocjach bohaterów, poradniki o związkach [cite: 139]", "D"),
            ("książki z opisami pomagającymi zobaczyć to, co się dzieje [cite: 140]", "W")
        ]
    },
    {
        "q": "7. Którą z poniższych czynności wykonujesz najchętniej w czasie wolnym? [cite: 141]",
        "options": [
            ("czytasz książkę lub przeglądasz czasopismo [cite: 142]", "W"),
            ("słuchasz audiobooków, radia, muzyki lub sam muzykujesz [cite: 143]", "S"),
            ("piszesz, rysujesz lub robisz coś rękami [cite: 144]", "D"),
            ("uprawiasz sport, budujesz coś lub grasz w gry ruchowe [cite: 145]", "K")
        ]
    },
    {
        "q": "8. Jak najlepiej charakteryzujesz swój sposób nauki? [cite: 146]",
        "options": [
            ("potrzebujesz wygody; dekoncentrują cię negatywne uczucia innych [cite: 147]", "D"),
            ("potrzebujesz wygody; dekoncentruje cię ruch innych osób [cite: 148]", "K"),
            ("umiesz się uczyć przy muzyce i rozmowach, odseparowujesz się [cite: 149]", "W"),
            ("nie umiesz się uczyć przy dźwiękach, nie odseparowujesz się od nich [cite: 150]", "S")
        ]
    },
    {
        "q": "9. Gdy z kimś rozmawiasz, gdzie kierujesz wzrok? [cite: 151]",
        "options": [
            ("wzrok wędruje na prawo i lewo po krótkim spojrzeniu [cite: 152]", "S"),
            ("patrzysz prosto na twarz rozmówcy [cite: 153]", "W"),
            ("spoglądasz w dół lub w bok po krótkim spojrzeniu na twarz [cite: 154]", "D"),
            ("rzadko spoglądasz na rozmówcę, reagujesz na każdy ruch w otoczeniu [cite: 155]", "K")
        ]
    },
    {
        "q": "10. Które stwierdzenie najlepiej do ciebie pasuje? [cite: 156]",
        "options": [
            ("trudno ci wysiedzieć nieruchomo, potrzebujesz ruchu [cite: 157]", "K"),
            ("zwracasz uwagę na kolory, kształty i wzory [cite: 158]", "W"),
            ("nie znosisz ciszy, nucisz lub włączasz radio [cite: 160]", "S"),
            ("jesteś wrażliwy na uczucia innych, potrzebujesz akceptacji [cite: 162]", "D")
        ]
    },
    {
        "q": "11. Które stwierdzenie najlepiej do ciebie pasuje? [cite: 164]",
        "options": [
            ("płaczesz podczas wzruszających scen w kinie lub książce [cite: 165]", "D"),
            ("niepokoi cię zła wymowa u innych, kapiący kran cię drażni [cite: 166]", "S"),
            ("zauważasz nieład we włosach lub niedopasowanie ubrań u innych [cite: 167]", "W"),
            ("czujesz niepokój, gdy musisz długo siedzieć nieruchomo [cite: 168]", "K")
        ]
    },
    {
        "q": "12. Co wywołuje u ciebie największy niepokój? [cite: 170]",
        "options": [
            ("miejsce, w którym jest za cicho [cite: 171]", "S"),
            ("miejsce, w którym nie czujesz się dobrze emocjonalnie [cite: 172]", "D"),
            ("brak przestrzeni na ruch lub zakaz robienia czegokolwiek [cite: 173]", "K"),
            ("miejsce, w którym panuje bałagan i nieład [cite: 174]", "W")
        ]
    },
    {
        "q": "13. Czego najbardziej nie lubisz podczas nauki? [cite: 175]",
        "options": [
            ("patrzenia i słuchania w bezruchu [cite: 176]", "K"),
            ("niemożności rysowania, dotykania rąk lub robienia notatek [cite: 177]", "D"),
            ("wykładu bez żadnych pomocy wizualnych [cite: 179]", "W"),
            ("czytania po cichu bez dyskusji i wyjaśnień [cite: 180]", "S")
        ]
    },
    {
        "q": "14. Jakie wspomnienia z szczęśliwych chwil utkwiły ci w pamięci? [cite: 181, 182]",
        "options": [
            ("dialogi, rozmowy i dźwięki wokół [cite: 183]", "S"),
            ("wygląd ludzi, miejsc i przedmiotów [cite: 184]", "W"),
            ("to, co robiłeś i ruchy twojego ciała [cite: 185]", "K"),
            ("wrażenia dotykowe i stan emocjonalny [cite: 186]", "D")
        ]
    },
    {
        "q": "15. Jakie wspomnienia z urlopu utkwiły ci w pamięci? [cite: 187, 188]",
        "options": [
            ("ruchy ciała i twoje dokonania [cite: 189]", "K"),
            ("wrażenia dotykowe na skórze i uczucia fizyczne [cite: 190]", "D"),
            ("dialogi, rozmowy i dźwięki [cite: 191]", "S"),
            ("wygląd ludzi, miejsc i przedmiotów [cite: 192]", "W")
        ]
    },
    {
        "q": "16. W którym z tych miejsc czułbyś się najlepiej? [cite: 193, 194]",
        "options": [
            ("miejsce do czytania, oglądania obrazów i zagadek wizualnych [cite: 195]", "W"),
            ("miejsce do rzemiosła, rzeźbienia i pisania na komputerze [cite: 198]", "D"),
            ("miejsce do słuchania muzyki, śpiewu i głośnych gier słownych [cite: 200]", "S"),
            ("miejsce do sportu, eksperymentów i budowania modeli [cite: 203]", "K")
        ]
    },
    {
        "q": "17. Gdybyś miał zapamiętać nowe słowo, zrobiłbyś to najlepiej: [cite: 206]",
        "options": [
            ("widząc je [cite: 207]", "W"),
            ("słysząc je [cite: 208]", "S"),
            ("zapisując je [cite: 209]", "D"),
            ("odtwarzając je w umyśle lub fizycznie [cite: 210]", "K")
        ]
    }
]

# Tworzenie formularza testu
with st.form("learning_styles_test"):
    all_responses = []
    
    for i, item in enumerate(pytania_data):
        st.subheader(item["q"])
        selected = st.multiselect(
            "Wybierz odpowiedzi:",
            options=[opt[0] for opt in item["options"]],
            key=f"question_{i}",
            help="Zaznacz wszystkie pasujące opcje."
        )
        
        # Zbieranie kodów (W, S, D, K) dla wybranych odpowiedzi
        for s in selected:
            code = next(opt[1] for opt in item["options"] if opt[0] == s)
            all_responses.append(code)
        st.write("---")

    submit_button = st.form_submit_button("Zakończ test i zobacz wyniki")

# Przetwarzanie wyników po kliknięciu przycisku
if submit_button:
    if not all_responses:
        st.warning("Proszę zaznaczyć przynajmniej jedną odpowiedź przed zakończeniem.")
    else:
        # Zliczanie punktów 
        scores = {
            "Wzrokowiec (W)": all_responses.count("W"),
            "Słuchowiec (S)": all_responses.count("S"),
            "Dotykowiec (D)": all_responses.count("D"),
            "Kinestetyk (K)": all_responses.count("K")
        }
        
        st.header("📊 Twoje Wyniki")
        st.bar_chart(scores)
        
        # Znalezienie najwyższego wyniku 
        max_score = max(scores.values())
        winners = [k for k, v in scores.items() if v == max_score]
        
        st.success(f"Twój dominujący styl uczenia się to: **{', '.join(winners)}**! [cite: 213, 215]")
        
        # Krótka instrukcja co dalej [cite: 216]
        st.write("Wiesz już, jaki styl uczenia się dominuje u Ciebie. Teraz dowiedz się, co to właściwie oznacza! [cite: 216]")