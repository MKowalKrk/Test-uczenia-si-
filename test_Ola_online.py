import streamlit as st

# Konfiguracja strony pod urządzenia mobilne
st.set_page_config(page_title="Test na style uczenia się", layout="centered")

# CSS do zawijania długich tekstów w multiselect
st.markdown(
    """
    <style>
    /* Zawijanie tekstu w wybranych elementach (tagach) */
    .stMultiSelect [data-baseweb="tag"] {
        white-space: normal !important;
        height: auto !important;
    }
    /* Zawijanie tekstu na liście rozwijanej opcji */
    div[role="listbox"] ul li div {
        white-space: normal !important;
    }
    /* Poprawa widoczności etykiet opcji */
    .stMultiSelect div[data-baseweb="select"] > div {
        white-space: normal !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Test na style uczenia się: dzień otwarty 18.04.2026")
st.info("Wskazówka: Może się zdarzyć, że na jedno pytanie udzielisz kilku odpowiedzi[cite: 2]. W takim przypadku zaznacz wszystkie pasujące opcje.")

# Pełna baza pytań i mapowanie odpowiedzi na style (W, S, D, K)
# Treść pytań pochodzi z dokumentu "Test na style uczenia się" [cite: 1, 3]
pytania_data = [
    {
        "q": "1. Gdy spotykasz nieznaną ci osobę, na co zwracasz uwagę w pierwszej kolejności? [cite: 3]",
        "options": [
            ("co w stosunku do niej czujesz [cite: 4]", "D"),
            ("jak wygląda i jak jest ubrana [cite: 5]", "W"),
            ("w jaki sposób i co mówi, jaki ma głos [cite: 6]", "S"),
            ("w jaki sposób się zachowuje i co robi [cite: 7]", "K")
        ]
    },
    {
        "q": "2. Co najczęściej zostaje ci w pamięci po kilku dniach od spotkania nieznanej ci wcześniej osoby? [cite: 8]",
        "options": [
            ("to, co robiliście razem, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz [cite: 9]", "K"),
            ("jej imię/nazwisko [cite: 10]", "S"),
            ("to, co czułeś, będąc w jej towarzystwie, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz [cite: 11]", "D"),
            ("jej twarz [cite: 12]", "W")
        ]
    },
    {
        "q": "3. Gdy wchodzisz do nieznanego ci pomieszczenia, na co zwracasz przede wszystkim uwagę? [cite: 13]",
        "options": [
            ("na jego wygląd [cite: 14]", "W"),
            ("na to, jak dobrze emocjonalnie i fizycznie się w nim czujesz [cite: 15]", "D"),
            ("na to, co się w nim dzieje i co ty mógłbyś w nim robić [cite: 16]", "K"),
            ("na dźwięki i rozmowy, jakie się w nim toczą [cite: 17]", "S")
        ]
    },
    {
        "q": "4. Gdy uczysz się czegoś nowego, w jaki sposób robisz to najchętniej? [cite: 18]",
        "options": [
            ("gdy nauczyciel pozwala ci zapisywać informacje, robić rysunki, dotykać przedmiotów lub pisać na klawiaturze [cite: 19]", "D"),
            ("gdy nauczyciel pozwala ci robić projekty, eksperymenty, grać w gry lub angażować się w ruch [cite: 20]", "K"),
            ("gdy nauczyciel daje ci coś do czytania, pokazuje ilustracje, wykresy, mapy lub szkice [cite: 21]", "W"),
            ("gdy nauczyciel wyjaśnia wszystko mówiąc, pozwala dyskutować i zadawać pytania [cite: 22]", "S")
        ]
    },
    {
        "q": "5. Gdy uczysz czegoś innych, co zwykle robisz? [cite: 23]",
        "options": [
            ("objaśniasz wszystko werbalnie, nie pokazując żadnych materiałów graficznych [cite: 24]", "S"),
            ("rysujesz coś, piszesz lub w inny sposób używasz rąk do wyjaśniania [cite: 25]", "D"),
            ("demonstrujesz coś, robiąc to lub każesz uczniom robić to wspólnie z tobą [cite: 26]", "K"),
            ("dajesz im coś do oglądania, na przykład przedmiot, ilustrację lub wykres [cite: 27]", "W")
        ]
    },
    {
        "q": "6. Jaki rodzaj książek czytasz najchętniej? [cite: 28]",
        "options": [
            ("książki zawierające informacje faktograficzne, historyczne lub dużo dialogów [cite: 29]", "S"),
            ("krótkie książki z wartką akcją lub pomagające doskonalić hobby i sport [cite: 30]", "K"),
            ("książki o uczuciach i emocjach bohaterów oraz poradniki o relacjach [cite: 31]", "D"),
            ("książki, które zawierają opisy pomagające ci zobaczyć to, co się dzieje [cite: 32]", "W")
        ]
    },
    {
        "q": "7. Którą z poniższych czynności wykonujesz najchętniej w czasie wolnym? [cite: 33]",
        "options": [
            ("czytasz książkę lub przeglądasz czasopismo [cite: 34]", "W"),
            ("słuchasz muzyki, radia lub sam muzykujesz [cite: 35]", "S"),
            ("piszesz, rysujesz lub robisz coś rękami [cite: 36]", "D"),
            ("uprawiasz sport, budujesz coś lub grasz w grę wymagającą ruchu [cite: 37]", "K")
        ]
    },
    {
        "q": "8. Które ze stwierdzeń najlepiej charakteryzuje sposób, w jaki czytasz lub uczysz się? [cite: 38]",
        "options": [
            ("musisz czuć się wygodnie; dekoncentrują cię negatywne uczucia innych [cite: 39]", "D"),
            ("musisz czuć się wygodnie; dekoncentruje cię ruch innych osób w pomieszczeniu [cite: 40]", "K"),
            ("potrafisz się uczyć przy muzyce i dźwiękach, umiesz się od nich odseparować [cite: 41]", "W"),
            ("nie potrafisz się uczyć przy muzyce i dźwiękach, nie umiesz się od nich odseparować [cite: 42]", "S")
        ]
    },
    {
        "q": "9. Gdy z kimś rozmawiasz, gdzie kierujesz wzrok? [cite: 43]",
        "options": [
            ("spoglądasz krótko na rozmówcę, po czym wzrok wędruje na prawo i lewo [cite: 44]", "S"),
            ("patrzysz na twarz rozmówcy i chcesz, by on patrzył na twoją [cite: 45]", "W"),
            ("spoglądasz krótko na rozmówcę, po czym patrzysz w dół lub w bok [cite: 46]", "D"),
            ("rzadko spoglądasz na rozmówcę, patrzysz głównie w dół lub reagujesz na ruch [cite: 47]", "K")
        ]
    },
    {
        "q": "10. Które z poniższych stwierdzeń najlepiej do ciebie pasuje? [cite: 48]",
        "options": [
            ("trudno ci wysiedzieć nieruchomo, potrzebujesz dużo ruchu [cite: 49]", "K"),
            ("zwracasz uwagę na kolory, kształty i wzory w miejscach, w których jesteś [cite: 50, 51]", "W"),
            ("nie znosisz ciszy i nucisz lub włączasz radio, by mieć bodźce słuchowe [cite: 52, 53]", "S"),
            ("jesteś wrażliwy na uczucia innych i potrzebujesz akceptacji, by pracować [cite: 54, 55]", "D")
        ]
    },
    {
        "q": "11. Które z poniższych stwierdzeń najlepiej do ciebie pasuje? [cite: 56]",
        "options": [
            ("płaczesz podczas wzruszających scen w kinie lub książce [cite: 57]", "D"),
            ("niepokoi cię zła wymowa u innych lub dźwięk kapiącego kranu [cite: 58]", "S"),
            ("zauważasz nieład w ubiorze lub włosach u innych i chcesz to naprawić [cite: 59]", "W"),
            ("niepokoisz się i czujesz nieprzyjemnie, gdy musisz siedzieć nieruchomo [cite: 60, 61]", "K")
        ]
    },
    {
        "q": "12. Co wywołuje u ciebie największy niepokój? [cite: 62]",
        "options": [
            ("miejsce, w którym jest za cicho [cite: 63]", "S"),
            ("miejsce, w którym nie czujesz się dobrze fizycznie lub emocjonalnie [cite: 64]", "D"),
            ("miejsce, w którym nie wolno nic robić lub jest za mało miejsca na ruch [cite: 65]", "K"),
            ("miejsce, w którym panuje bałagan i nieład [cite: 66]", "W")
        ]
    },
    {
        "q": "13. Czego najbardziej nie lubisz, podczas gdy ktoś cię uczy? [cite: 67]",
        "options": [
            ("patrzenia i słuchania w bezruchu [cite: 68]", "K"),
            ("niemożności rysowania, dotykania wszystkiego lub robienia notatek [cite: 69, 70]", "D"),
            ("słuchania wykładu, na którym nie wykorzystuje się pomocy wizualnych [cite: 71]", "W"),
            ("czytania po cichu bez żadnych werbalnych wyjaśnień lub dyskusji [cite: 72]", "S")
        ]
    },
    {
        "q": "14. Jakie wspomnienia z szczęśliwego momentu utkwiły ci w pamięci? [cite: 73, 74]",
        "options": [
            ("to, co słyszałeś: dialogi, rozmowy i dźwięki wokół ciebie [cite: 75]", "S"),
            ("to, co widziałeś: wygląd ludzi, miejsc czy przedmiotów [cite: 76]", "W"),
            ("to, co robiłeś: ruchy ciała i twoje dokonania [cite: 77]", "K"),
            ("wrażenia dotykowe oraz to, jak czułeś się fizycznie i emocjonalnie [cite: 78]", "D")
        ]
    },
    {
        "q": "15. Jakie wspomnienia z urlopu lub wycieczki utkwiły ci w pamięci? [cite: 79, 80]",
        "options": [
            ("to, co robiłeś: ruchy ciała i twoje dokonania [cite: 81]", "K"),
            ("wrażenia dotykowe oraz to, jak czułeś się fizycznie i emocjonalnie [cite: 82]", "D"),
            ("to, co słyszałeś: dialogi, rozmowy i dźwięki wokół ciebie [cite: 83]", "S"),
            ("to, co widziałeś: wygląd ludzi, miejsc czy przedmiotów [cite: 84]", "W")
        ]
    },
    {
        "q": "16. W którym z opisanych miejsc czułbyś się najlepiej? [cite: 85, 86]",
        "options": [
            ("miejsce do czytania, oglądania obrazów, map i rozwiązywania zagadek wizualnych [cite: 87, 88, 89]", "W"),
            ("miejsce do rzemiosła, rzeźbienia, budowania modeli i prac ręcznych [cite: 90, 91]", "D"),
            ("miejsce do słuchania muzyki, śpiewu, głośnych gier słownych i dyskusji [cite: 92, 93, 94]", "S"),
            ("miejsce do uprawiania sportu, eksperymentów i gier ruchowych [cite: 95, 96, 97]", "K")
        ]
    },
    {
        "q": "17. Gdybyś miał zapamiętać nowe słowo, zrobiłbyś to najlepiej: [cite: 98]",
        "options": [
            ("widząc je [cite: 99]", "W"),
            ("słysząc je [cite: 100]", "S"),
            ("zapisując je [cite: 101]", "D"),
            ("odtwarzając je w umyśle lub fizycznie [cite: 102]", "K")
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
# Obliczanie wyników odbywa się poprzez zliczanie odpowiedzi w kategoriach W, S, D, K [cite: 103, 104, 105, 106]
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
        
        st.success(f"Twój dominujący styl uczenia się to: **{', '.join(winners)}**! [cite: 107]")
        st.write("Wiesz już, jaki styl uczenia się dominuje u Ciebie. Teraz dowiedz się, co to właściwie oznacza! [cite: 108]")

# Informacja o autorstwie wersji cyfrowej
st.markdown("---")
st.caption("Test do wersji cyfrowej przygotowany przez Aleksandrę Kopystyńską (pedagog specjalny) przy pomocy Gemini")
