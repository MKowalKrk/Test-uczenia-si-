import streamlit as st

# Konfiguracja strony pod urządzenia mobilne
st.set_page_config(page_title="Test na style uczenia się", layout="centered")

# CSS dla poprawy wyglądu na telefonach
st.markdown(
    """
    <style>
    .stCheckbox {
        padding: 10px;
        border-radius: 5px;
        background-color: #f0f2f6;
        margin-bottom: 5px;
    }
    .stCheckbox:hover {
        background-color: #e0e4eb;
    }
    label {
        font-size: 1rem !important;
        line-height: 1.4 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Test na style uczenia się")
st.write("Wskazówka: Może się zdarzyć, że na jedno pytanie udzielisz kilku odpowiedzi. W takim przypadku zaznacz wszystkie pasujące opcje.")

# Pełna baza danych z Twojego dokumentu
pytania_data = [
    {
        "q": "1. Gdy spotykasz nieznaną ci osobę, na co zwracasz uwagę w pierwszej kolejności?",
        "options": [
            ("co w stosunku do niej czujesz,", "D"),
            ("jak wygląda i jak jest ubrana,", "W"),
            ("w jaki sposób i co mówi, jaki ma głos,", "S"),
            ("w jaki sposób się zachowuje i co robi.", "K")
        ]
    },
    {
        "q": "2. Co najczęściej zostaje ci w pamięci po kilku dniach od spotkania nieznanej ci wcześniej osoby?",
        "options": [
            ("to, co robiliście razem, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz,", "K"),
            ("jej imię/nazwisko,", "S"),
            ("to, co czułeś, będąc w jej towarzystwie, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz,", "D"),
            ("jej twarz.", "W")
        ]
    },
    {
        "q": "3. Gdy wchodzisz do nieznanego ci pomieszczenia, na co zwracasz przede wszystkim uwagę?",
        "options": [
            ("na jego wygląd,", "W"),
            ("na to, jak dobrze emocjonalnie i fizycznie się w nim czujesz,", "D"),
            ("na to, co się w nim dzieje i co ty mógłbyś w nim robić,", "K"),
            ("na dźwięki i rozmowy, jakie się w nim toczą.", "S")
        ]
    },
    {
        "q": "4. Gdy uczysz się czegoś nowego, w jaki sposób robisz to najchętniej?",
        "options": [
            ("gdy nauczyciel pozwala ci zapisywać informacje lub sporządzać rysunki, dotykać przedmiotów, pisać na klawiaturze lub robić coś rękami,", "D"),
            ("gdy nauczyciel pozwala ci robić projekty, symulacje, eksperymenty, grać w gry, odgrywać role, odtwarzać rzeczywiste sytuacje z życia, dokonywać odkryć lub też angażować się w inne działania związane z ruchem,", "K"),
            ("gdy nauczyciel daje ci coś do czytania na papierze lub tablicy, pokazuje ci książki, ilustracje, wykresy, mapy, szkice lub przedmioty, nie każąc ci przy tym niczego mówić, pisać, ani o niczym dyskutować,", "W"),
            ("gdy nauczyciel wyjaśnia wszystko, mówiąc lub wygłaszając wykład, pozwala ci przedyskutować temat i zadawać pytania, nie każąc ci przy tym na nic patrzeć, niczego czytać, pisać ani robić.", "S")
        ]
    },
    {
        "q": "5. Gdy uczysz czegoś innych, co zwykle robisz?",
        "options": [
            ("objaśniasz wszystko werbalnie, nie pokazując żadnych materiałów graficznych,", "S"),
            ("rysujesz coś, piszesz lub w inny sposób używasz rąk do wyjaśniania,", "D"),
            ("demonstrujesz coś, robiąc to lub każesz uczniom robić to wspólnie z tobą,", "K"),
            ("dajesz im coś do oglądania, na przykład jakiś przedmiot, ilustrację lub wykres, udzielając przy tym jedynie krótkiego werbalnego wyjaśnienia lub nie udzielając go wcale, dopuszczając lub nie do krótkiej dyskusji.", "W")
        ]
    },
    {
        "q": "6. Jaki rodzaj książek czytasz najchętniej?",
        "options": [
            ("książki zawierające informacje faktograficzne, historyczne lub dużo dialogów,", "S"),
            ("krótkie książki z wartką akcją lub książki, które pomagają ci doskonalić umiejętności w sporcie, hobby czy też rozwijać jakiś talent,", "K"),
            ("książki o uczuciach i emocjach bohaterów, poradniki, książki o emocjach i związkach międzyludzkich lub książki na temat tego, jak poprawić stan twojego ciała i umysłu,", "D"),
            ("książki, które zawierają opisy pomagające ci zobaczyć to, co się dzieje.", "W")
        ]
    },
    {
        "q": "7. Którą z poniższych czynności wykonujesz najchętniej w czasie wolnym?",
        "options": [
            ("czytasz książkę lub przeglądasz czasopismo,", "W"),
            ("słuchasz książki nagranej na kasetę, rozmowy w radiu, słuchasz muzyki lub sam muzykujesz,", "S"),
            ("piszesz, rysujesz, piszesz na maszynie/komputerze lub robisz coś rękami,", "D"),
            ("uprawiasz sport, budujesz coś lub grasz w grę wymagającą ruchu.", "K")
        ]
    },
    {
        "q": "8. Które z poniższych stwierdzeń najlepiej charakteryzuje sposób, w jaki czytasz lub uczysz się?",
        "options": [
            ("musisz czuć się wygodnie, rozluźniony; potrafisz pracować zarówno przy muzyce, jak i w ciszy, jednak dekoncentrują cię negatywne uczucia innych,", "D"),
            ("musisz czuć się wygodnie, rozluźniony; potrafisz pracować zarówno przy muzyce, jak i w ciszy, jednak dekoncentruje cię działalność i ruchy innych osób znajdujących się w tym samym pomieszczeniu,", "K"),
            ("potrafisz się uczyć, gdy słychać muzykę, inne dźwięki lub rozmowę, ponieważ umiesz się od nich odseparować,", "W"),
            ("nie potrafisz się uczyć, gdy w twoim pobliżu słychać muzykę, inne dźwięki lub rozmowę, ponieważ nie umiesz się od nich odseparować.", "S")
        ]
    },
    {
        "q": "9. Gdy z kimś rozmawiasz, gdzie kierujesz wzrok?",
        "options": [
            ("spoglądasz jedynie krótko na rozmówcę, po czym twój wzrok wędruje na prawo i lewo,", "S"),
            ("patrzysz na twarz rozmówcy, chcesz także, by ta osoba patrzyła na twoją twarz, gdy do niej mówisz,", "W"),
            ("spoglądasz jedynie krótko na rozmówcę, by zobaczyć jego wyraz twarzy, po czym spoglądasz w dół lub w bok,", "D"),
            ("rzadko spoglądasz na rozmówcę, patrzysz głównie w dół lub w bok, jeśli jednak pojawi się jakiś ruch lub działanie, natychmiast spoglądasz w tamtym kierunku.", "K")
        ]
    },
    {
        "q": "10. Które z poniższych stwierdzeń najlepiej do ciebie pasuje?",
        "options": [
            ("trudno ci wysiedzieć nieruchomo w jednym miejscu, potrzebujesz dużo ruchu, a jeśli już musisz siedzieć garbisz się, wiercisz, stukasz w podłogę butami lub często niespokojnie poruszasz nogami,", "K"),
            ("zwracasz uwagę na kolory, kształty, wzory i desenie w miejscach, w których się znajdziesz; masz dobre oko do barw i kształtów,", "W"),
            ("nie znosisz ciszy i nucisz coś, podśpiewujesz lub głośno mówisz; włączasz radio, telewizor lub odtwarzacz, by mieć bodźce słuchowe,", "S"),
            ("jesteś wrażliwy na uczucia innych ludzi, twoje własne uczucia łatwo ulegają zranieniu; potrzebujesz bycia akceptowanym, by pracować.", "D")
        ]
    },
    {
        "q": "11. Które z poniższych stwierdzeń najlepiej do ciebie pasuje?",
        "options": [
            ("płaczesz podczas wzruszających scen w kinie lub czytając wzruszającą książkę,", "D"),
            ("niepokoi cię, gdy ktoś nie potrafi dobrze się wysławiać, jesteś wrażliwy na odgłos kapiącego kranu lub odgłosy urządzeń domowych,", "S"),
            ("zwracasz uwagę na nieodpowiednie dopasowanie części garderoby danej osoby lub na to, że jej włosy są w nieładzie,", "W"),
            ("niepokoisz się i czujesz się nieprzyjemnie, gdy jesteś zmuszony siedzieć nieruchomo; nie potrafisz przebywać zbyt długo w jednym miejscu.", "K")
        ]
    },
    {
        "q": "12. Co wywołuje u ciebie największy niepokój?",
        "options": [
            ("miejsce, w którym jest za cicho,", "S"),
            ("miejsce, w którym nie czujesz się dobrze fizycznie lub emocjonalnie,", "D"),
            ("miejsce, w którym nie wolno niczego robić lub jest za mało przestrzeni na ruch,", "K"),
            ("miejsce, w którym panuje bałagan i nieład.", "W")
        ]
    },
    {
        "q": "13. Czego najbardziej nie lubisz, podczas gdy ktoś cię uczy?",
        "options": [
            ("patrzenia i słuchania w bezruchu,", "K"),
            ("niemożności rysowania, dotykania wszystkiego rękami lub sporządzania notatek,", "D"),
            ("słuchania wykładu, na którym nie wykorzystuje się żadnych pomocy wizualnych,", "W"),
            ("czytania po cichu, bez żadnych werbalnych wyjaśnień czy dyskusji.", "S")
        ]
    },
    {
        "q": "14. Jakie wspomnienia z szczęśliwego momentu utkwiły ci w pamięci?",
        "options": [
            ("to, co słyszałeś, na przykład dialogi i rozmowy, to, co powiedziałeś, oraz dźwięki wokół ciebie,", "S"),
            ("to, co widziałeś, na przykład wygląd ludzi, miejsc czy przedmiotów,", "W"),
            ("to, co robiłeś, ruchy twojego ciała, twoje dokonania,", "K"),
            ("wrażenia dotykowe na skórze i ciele, a także to, jak czułeś się fizycznie i emocjonalnie.", "D")
        ]
    },
    {
        "q": "15. Jakie wspomnienia z urlopu lub wycieczki utkwiły ci w pamięci?",
        "options": [
            ("to, co robiłeś, ruchy twojego ciała, twoje dokonania,", "K"),
            ("wrażenia dotykowe na skórze i ciele, a także to, jak czułeś się fizycznie i emocjonalnie,", "D"),
            ("to, co słyszałeś, na przykład dialogi i rozmowy, to, co powiedziałeś, oraz dźwięki wokół ciebie,", "S"),
            ("to, co widziałeś, na przykład wygląd ludzi, miejsc czy przedmiotów.", "W")
        ]
    },
    {
        "q": "16. W którym z niżej opisanych miejsc czułbyś się najlepiej?",
        "options": [
            ("miejsce, w którym możesz czytać; oglądać obrazy; rozwiązywać zagadek wizualne; grać w gry słowne; zajmować się dekorowaniem,", "W"),
            ("miejsce, w którym możesz rysować, malować, rzeźbić; tworzyć coś na piśmie; wykonywać czynności przy użyciu rąk,", "D"),
            ("miejsce, w którym możesz słuchać nagrań, talk shows; grać na instrumencie lub śpiewać; bawić się głośno w gry słowne,", "S"),
            ("miejsce, w którym możesz uprawiać sport; odgrywać role; robić projekty ruchowe i eksperymenty; budować coś.", "K")
        ]
    },
    {
        "q": "17. Gdybyś miał zapamiętać nowe słowo, zrobiłbyś to najlepiej:",
        "options": [
            ("widząc je,", "W"),
            ("słysząc je,", "S"),
            ("zapisując je,", "D"),
            ("odtwarzając to słowo w umyśle lub fizycznie.", "K")
        ]
    }
]

with st.form("test_form"):
    all_responses = []
    for i, item in enumerate(pytania_data):
        st.subheader(item["q"])
        for label, code in item["options"]:
            # Używamy checkboxów zamiast multiselect, aby tekst nigdy nie był ucinany
            if st.checkbox(label, key=f"q_{i}_{label}"):
                all_responses.append(code)
        st.write("---")
    
    submit = st.form_submit_button("Oblicz wyniki")

if submit:
    if not all_responses:
        st.error("Proszę zaznaczyć przynajmniej jedną odpowiedź.")
    else:
        scores = {
            "Wzrokowiec (W)": all_responses.count("W"),
            "Słuchowiec (S)": all_responses.count("S"),
            "Dotykowiec (D)": all_responses.count("D"),
            "Kinestetyk (K)": all_responses.count("K")
        }
        
        st.header("📊 Twoje Wyniki")
        st.bar_chart(scores)
        
        max_val = max(scores.values())
        dominance = [k for k, v in scores.items() if v == max_val]
        
        st.success(f"Twój dominujący styl uczenia się to: **{', '.join(dominance)}**")
        st.write("Teraz dowiedz się, co to właściwie oznacza!")

st.markdown("---")
st.caption("Test do wersji cyfrowej przygotowany przez Aleksandrę Kopystyńską (pedagog specjalny) przy pomocy Gemini")
