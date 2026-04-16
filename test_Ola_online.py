import streamlit as st

# Konfiguracja strony pod urządzenia mobilne
st.set_page_config(page_title="Test na style uczenia się", layout="centered")

# Bardziej agresywny CSS do zawijania długich tekstów
st.markdown(
    """
    <style>
    /* Zawijanie tekstu w wybranych polach (tagach) */
    span[data-baseweb="tag"] {
        white-space: normal !important;
        height: auto !important;
        padding-top: 5px !important;
        padding-bottom: 5px !important;
    }
    /* Zawijanie tekstu wewnątrz tagów */
    span[data-baseweb="tag"] > span {
        white-space: normal !important;
        display: block !important;
    }
    /* Zawijanie tekstu na liście rozwijanej opcji */
    div[role="option"] {
        white-space: normal !important;
        line-height: 1.4 !important;
    }
    /* Poprawa widoczności etykiet wewnątrz selektora */
    div[data-baseweb="select"] div {
        white-space: normal !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
            ("gdy nauczyciel pozwala ci zapisywać informacje lub sporządzać rysunki, dotykać przedmiotów, pisać na klawiaturze lub robić coś rękami", "D"),
            ("gdy nauczyciel pozwala ci robić projekty, symulacje, eksperymenty, grać w gry lub angażować się w ruch", "K"),
            ("gdy nauczyciel daje ci coś do czytania, pokazuje ilustracje, wykresy, mapy lub szkice", "W"),
            ("gdy nauczyciel wyjaśnia wszystko mówiąc, pozwala dyskutować i zadawać pytania", "S")
        ]
    },
    {
        "q": "5. Gdy uczysz czegoś innych, co zwykle robisz?",
        "options": [
            ("objaśniasz wszystko werbalnie bez wykorzystania żadnych materiałów graficznych", "S"),
            ("rysujesz coś, piszesz lub w inny sposób używasz rąk do wyjaśniania", "D"),
            ("demonstrujesz coś, robiąc to lub każesz uczniom robić to wspólnie z tobą", "K"),
            ("dajesz im coś do oglądania, na przykład przedmiot, ilustrację lub wykres", "W")
        ]
    },
    {
        "q": "6. Jaki rodzaj książek czytasz najchętniej?",
        "options": [
            ("książki zawierające informacje faktograficzne, historyczne lub dużo dialogów", "S"),
            ("krótkie książki z wartką akcją lub pomagające doskonalić hobby i sport", "K"),
            ("książki o uczuciach i emocjach bohaterów oraz poradniki o relacjach", "D"),
            ("książki, które zawierają opisy pomagające ci zobaczyć to, co się dzieje", "W")
        ]
    },
    {
        "q": "7. Którą z poniższych czynności wykonujesz najchętniej w czasie wolnym?",
        "options": [
            ("czytasz książkę lub przeglądasz czasopismo", "W"),
            ("słuchasz muzyki, radia lub sam muzykujesz", "S"),
            ("piszesz, rysujesz lub robisz coś rękami", "D"),
            ("uprawiasz sport, budujesz coś lub grasz w grę wymagającą ruchu", "K")
        ]
    },
    {
        "q": "8. Które ze stwierdzeń najlepiej charakteryzuje sposób, w jaki czytasz lub uczysz się?",
        "options": [
            ("musisz czuć się wygodnie; dekoncentrują cię negatywne uczucia innych", "D"),
            ("musisz czuć się wygodnie; dekoncentruje cię ruch innych osób w pomieszczeniu", "K"),
            ("potrafisz się uczyć przy muzyce i dźwiękach, umiesz się od nich odseparować", "W"),
            ("nie potrafisz się uczyć przy muzyce i dźwiękach, nie umiesz się od nich odseparować", "S")
        ]
    },
    {
        "q": "9. Gdy z kimś rozmawiasz, gdzie kierujesz wzrok?",
        "options": [
            ("spoglądasz krótko na rozmówcę, po czym wzrok wędruje na prawo i lewo", "S"),
            ("patrzysz na twarz rozmówcy i chcesz, by on patrzył na twoją", "W"),
            ("spoglądasz krótko na rozmówcę, po czym patrzysz w dół lub w bok", "D"),
            ("rzadko spoglądasz na rozmówcę, patrzysz głównie w dół lub reagujesz na ruch", "K")
        ]
    },
    {
        "q": "10. Które z poniższych stwierdzeń najlepiej do ciebie pasuje?",
        "options": [
            ("trudno ci wysiedzieć nieruchomo, potrzebujesz dużo ruchu", "K"),
            ("zwracasz uwagę na kolory, kształty i wzory w miejscach, w których jesteś", "W"),
            ("nie znosisz ciszy i nucisz lub włączasz radio, by mieć bodźce słuchowe", "S"),
            ("jesteś wrażliwy na uczucia innych i potrzebujesz akceptacji, by pracować", "D")
        ]
    },
    {
        "q": "11. Które z poniższych stwierdzeń najlepiej do ciebie pasuje?",
        "options": [
            ("płaczesz podczas wzruszających scen w kinie lub książce", "D"),
            ("niepokoi cię zła wymowa u innych lub dźwięk kapiącego kranu", "S"),
            ("zauważasz nieład w ubiorze lub włosach u innych i chcesz to naprawić", "W"),
            ("niepokoisz się i czujesz nieprzyjemnie, gdy musisz siedzieć nieruchomo", "K")
        ]
    },
    {
        "q": "12. Co wywołuje u ciebie największy niepokój?",
        "options": [
            ("miejsce, w którym jest za cicho", "S"),
            ("miejsce, w którym nie czujesz się dobrze fizycznie lub emocjonalnie", "D"),
            ("miejsce, w którym nie wolno nic robić lub jest za mało miejsca na ruch", "K"),
            ("miejsce, w którym panuje bałagan i nieład", "W")
        ]
    },
    {
        "q": "13. Czego najbardziej nie lubisz, podczas gdy ktoś cię uczy?",
        "options": [
            ("patrzenia i słuchania w bezruchu", "K"),
            ("niemożności rysowania, dotykania wszystkiego lub robienia notatek", "D"),
            ("słuchania wykładu, na którym nie wykorzystuje się pomocy wizualnych", "W"),
            ("czytania po cichu bez żadnych werbalnych wyjaśnień lub dyskusji", "S")
        ]
    },
    {
        "q": "14. Jakie wspomnienia z szczęśliwego momentu utkwiły ci w pamięci?",
        "options": [
            ("to, co słyszałeś: dialogi, rozmowy i dźwięki wokół ciebie", "S"),
            ("to, co widziałeś: wygląd ludzi, miejsc czy przedmiotów", "W"),
            ("to, co robiłeś: ruchy ciała i twoje dokonania", "K"),
            ("wrażenia dotykowe oraz to, jak czułeś się fizycznie i emocjonalnie", "D")
        ]
    },
    {
        "q": "15. Jakie wspomnienia z urlopu lub wycieczki utkwiły ci w pamięci?",
        "options": [
            ("to, co robiłeś: ruchy ciała i twoje dokonania", "K"),
            ("wrażenia dotykowe oraz to, jak czułeś się fizycznie i emocjonalnie", "D"),
            ("to, co słyszałeś: dialogi, rozmowy i dźwięki wokół ciebie", "S"),
            ("to, co widziałeś: wygląd ludzi, miejsc czy przedmiotów", "W")
        ]
    },
    {
        "q": "16. W którym z opisanych miejsc czułbyś się najlepiej?",
        "options": [
            ("miejsce do czytania, oglądania obrazów, map i rozwiązywania zagadek wizualnych", "W"),
            ("miejsce do rzemiosła, rzeźbienia, budowania modeli i prac ręcznych", "D"),
            ("miejsce do słuchania muzyki, śpiewu, głośnych gier słownych i dyskusji", "S"),
            ("miejsce do uprawiania sportu, eksperymentów i gier ruchowych", "K")
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
            key=f"question_{i}"
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
st.caption("Test do wersji cyfrowej przygotowany przez Aleksandrę Kopystyńską (pedagog specjalny) przy pomocy Gemini")
