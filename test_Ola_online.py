import streamlit as st

# Konfiguracja strony pod urządzenia mobilne
st.set_page_config(page_title="Test na style uczenia się", layout="centered")

st.title("🧠 Test na style uczenia się")
st.info("Wskazówka: Może się zdarzyć, że na jedno pytanie udzielisz kilku odpowiedzi. W takim przypadku zaznacz wszystkie pasujące opcje.")

# Pełna baza pytań i mapowanie odpowiedzi na style (W, S, D, K)
pytania_data = [
    {
        "q": "1. Gdy spotykasz nieznaną ci osobę, na co zwracasz uwagę w pierwszej kolejności?",
        "options": [
            ("co w stosunku do niej czujesz", "D"),
            ("jak wygląda i jak jest ubrana", "W"),
            ("w jaki sposób i co mówi, jaki ma głos", "S"),
            ("w jaki sposób się zachowuje i co robi", "K")
        ]
    },
    {
        "q": "2. Co najczęściej zostaje ci w pamięci po kilku dniach od spotkania nieznanej ci wcześniej osoby?",
        "options": [
            ("to, co robiliście razem, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz", "K"),
            ("jej imię/nazwisko", "S"),
            ("to, co czułeś, będąc w jej towarzystwie, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz", "D"),
            ("jej twarz", "W")
        ]
    },
    {
        "q": "3. Gdy wchodzisz do nieznanego ci pomieszczenia, na co zwracasz przede wszystkim uwagę?",
        "options": [
            ("na jego wygląd", "W"),
            ("na to, jak dobrze emocjonalnie i fizycznie się w nim czujesz", "D"),
            ("na to, co się w nim dzieje i co ty mógłbyś w nim robić", "K"),
            ("na dźwięki i rozmowy, jakie się w nim toczą", "S")
        ]
    },
    {
        "q": "4. Gdy uczysz się czegoś nowego, w jaki sposób robisz to najchętniej?",
        "options": [
            ("zapisywanie informacji, rysunki, dotykanie przedmiotów, pisać na klawiaturze", "D"),
            ("projekty, symulacje, eksperymenty, gry, angażowanie się w ruch", "K"),
            ("czytanie, oglądanie ilustracji, wykresów, map, szkiców", "W"),
            ("wyjaśnienia słowne, wykład, dyskusja i zadawanie pytań", "S")
        ]
    },
    {
        "q": "5. Gdy uczysz czegoś innych, co zwykle robisz?",
        "options": [
            ("objaśniasz wszystko werbalnie bez materiałów graficznych", "S"),
            ("rysujesz coś, piszesz lub używasz rąk do wyjaśniania", "D"),
            ("demonstrujesz coś robiąc to lub każesz uczniom robić to z tobą", "K"),
            ("dajesz im coś do oglądania (przedmiot, ilustrację, wykres)", "W")
        ]
    },
    {
        "q": "6. Jaki rodzaj książek czytasz najchętniej?",
        "options": [
            ("informacje faktograficzne, historyczne lub dużo dialogów", "S"),
            ("krótkie książki z wartką akcją lub poradniki hobby/sport", "K"),
            ("o uczuciach i emocjach bohaterów, poradniki o związkach", "D"),
            ("książki z opisami pomagającymi zobaczyć to, co się dzieje", "W")
        ]
    },
    {
        "q": "7. Którą z poniższych czynności wykonujesz najchętniej v czasie wolnym?",
        "options": [
            ("czytasz książkę lub przeglądasz czasopismo", "W"),
            ("słuchasz audiobooków, radia, muzyki lub sam muzykujesz", "S"),
            ("piszesz, rysujesz lub robisz coś rękami", "D"),
            ("uprawiasz sport, budujesz coś lub grasz w gry ruchowe", "K")
        ]
    },
    {
        "q": "8. Jak najlepiej charakteryzujesz swój sposób nauki?",
        "options": [
            ("potrzebujesz wygody; dekoncentrują cię negatywne uczucia innych", "D"),
            ("potrzebujesz wygody; dekoncentruje cię ruch innych osób", "K"),
            ("umiesz się uczyć przy muzyce i rozmowach, odseparowujesz się", "W"),
            ("nie umiesz się uczyć przy dźwiękach, nie odseparowujesz się od nich", "S")
        ]
    },
    {
        "q": "9. Gdy z kimś rozmawiasz, gdzie kierujesz wzrok?",
        "options": [
            ("wzrok wędruje na prawo i lewo po krótkim spojrzeniu", "S"),
            ("patrzysz prosto na twarz rozmówcy", "W"),
            ("spoglądasz w dół lub w bok po krótkim spojrzeniu na twarz", "D"),
            ("rzadko spoglądasz na rozmówcę, reagujesz na każdy ruch w otoczeniu", "K")
        ]
    },
    {
        "q": "10. Które stwierdzenie najlepiej do ciebie pasuje?",
        "options": [
            ("trudno ci wysiedzieć nieruchomo, potrzebujesz ruchu", "K"),
            ("zwracasz uwagę na kolory, kształty i wzory", "W"),
            ("nie znosisz ciszy, nucisz lub włączasz radio", "S"),
            ("jesteś wrażliwy na uczucia innych, potrzebujesz akceptacji", "D")
        ]
    },
    {
        "q": "11. Które stwierdzenie najlepiej do ciebie pasuje?",
        "options": [
            ("płaczesz podczas wzruszających scen v kinie lub książce", "D"),
            ("niepokoi cię zła wymowa u innych, kapiący kran cię drażni", "S"),
            ("zauważasz nieład we włosach lub niedopasowanie ubrań u innych", "W"),
            ("czujesz niepokój, gdy musisz długo siedzieć nieruchomo", "K")
        ]
    },
    {
        "q": "12. Co wywołuje u ciebie największy niepokój?",
        "options": [
            ("miejsce, w którym jest za cicho", "S"),
            ("miejsce, w którym nie czujesz się dobrze emocjonalnie", "D"),
            ("brak przestrzeni na ruch lub zakaz robienia czegokolwiek", "K"),
            ("miejsce, w którym panuje bałagan i nieład", "W")
        ]
    },
    {
        "q": "13. Czego najbardziej nie lubisz podczas nauki?",
        "options": [
            ("patrzenia i słuchania w bezruchu", "K"),
            ("niemożności rysowania, dotykania rąk lub robienia notatek", "D"),
            ("wykładu bez żadnych pomocy wizualnych", "W"),
            ("czytania po cichu bez dyskusji i wyjaśnień", "S")
        ]
    },
    {
        "q": "14. Jakie wspomnienia z szczęśliwych chwil utkwiły ci w pamięci?",
        "options": [
            ("dialogi, rozmowy i dźwięki wokół", "S"),
            ("wygląd ludzi, miejsc i przedmiotów", "W"),
            ("to, co robiłeś i ruchy twojego ciała", "K"),
            ("wrażenia dotykowe i stan emocjonalny", "D")
        ]
    },
    {
        "q": "15. Jakie wspomnienia z urlopu utkwiły ci w pamięci?",
        "options": [
            ("ruchy ciała i twoje dokonania", "K"),
            ("wrażenia dotykowe na skórze i uczucia fizyczne", "D"),
            ("dialogi, rozmowy i dźwięki", "S"),
            ("wygląd ludzi, miejsc i przedmiotów", "W")
        ]
    },
    {
        "q": "16. W którym z tych miejsc czułbyś się najlepiej?",
        "options": [
            ("miejsce do czytania, oglądania obrazów i zagadek wizualnych", "W"),
            ("miejsce do rzemiosła, rzeźbienia i pisania na komputerze", "D"),
            ("miejsce do słuchania muzyki, śpiewu i głośnych gier słownych", "S"),
            ("miejsce do sportu, eksperymentów i budowania modeli", "K")
        ]
    },
    {
        "q": "17. Gdybyś miał zapamiętać nowe słowo, zrobiłbyś to najlepiej:",
        "options": [
            ("widząc je", "W"),
            ("słysząc je", "S"),
            ("zapisując je", "D"),
            ("odtwarzając je w umyśle lub fizycznie", "K")
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
        
        for s in selected:
            code = next(opt[1] for opt in item["options"] if opt[0] == s)
            all_responses.append(code)
        st.write("---")

    submit_button = st.form_submit_button("Zakończ test i zobacz wyniki")

# Wyniki i stopka
if submit_button:
    if not all_responses:
        st.warning("Proszę zaznaczyć przynajmniej jedną odpowiedź przed zakończeniem.")
    else:
        scores = {
            "Wzrokowiec (W)": all_responses.count("W"),
            "Słuchowiec (S)": all_responses.count("S"),
            "Dotykowiec (D)": all_responses.count("D"),
            "Kinestetyk (K)": all_responses.count("K")
        }
        
        st.header("📊 Twoje Wyniki")
        st.bar_chart(scores)
        
        max_score = max(scores.values())
        winners = [k for k, v in scores.items() if v == max_score]
        
        st.success(f"Twój dominujący styl uczenia się to: **{', '.join(winners)}**!")
        st.write("Wiesz już, jaki styl uczenia się dominuje u Ciebie. Teraz dowiedz się, co to właściwie oznacza!")

# Informacja o autorstwie wersji cyfrowej
st.markdown("---")
st.caption("Test do wersji cyfrowej przygotowany przez Aleksandrę Kopystyńską przy pomocy Gemini")