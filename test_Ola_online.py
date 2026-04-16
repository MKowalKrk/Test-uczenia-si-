import streamlit as st

# Konfiguracja strony pod urządzenia mobilne
st.set_page_config(page_title="Test na style uczenia się", layout="centered")

# CSS poprawiający widoczność w Dark i Light Mode
st.markdown(
    """
    <style>
    /* Stylizacja kontenera checkboxa - używamy kolorów adaptacyjnych */
    .stCheckbox {
        padding: 12px 15px;
        border-radius: 8px;
        /* rgba(128, 128, 128, 0.1) to delikatny szary, który widać na obu motywach */
        background-color: rgba(128, 128, 128, 0.1);
        margin-bottom: 8px;
        transition: background-color 0.3s;
    }
    
    /* Efekt po najechaniu - nieco mocniejsze podświetlenie */
    .stCheckbox:hover {
        background-color: rgba(128, 128, 128, 0.2);
    }

    /* Wymuszenie zawijania tekstu etykiety i poprawa interlinii */
    .stCheckbox label div[data-testid="stMarkdownContainer"] p {
        font-size: 1rem !important;
        line-height: 1.5 !important;
        word-wrap: break-word !important;
    }
    
    /* Usunięcie marginesu pod pytaniami */
    .stSubheader {
        margin-top: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 Test na style uczenia się")
st.write("Wskazówka: Może się zdarzyć, że na jedno pytanie udzielisz kilku odpowiedzi. W takim przypadku zaznacz wszystkie pasujące opcje[cite: 2].")

# Baza danych na podstawie dokumentu [cite: 3-102]
pytania_data = [
    {
        "q": "1. Gdy spotykasz nieznaną ci osobę, na co zwracasz uwagę w pierwszej kolejności? [cite: 3]",
        "options": [
            ("co w stosunku do niej czujesz, [cite: 4]", "D"),
            ("jak wygląda i jak jest ubrana, [cite: 5]", "W"),
            ("w jaki sposób i co mówi, jaki ma głos, [cite: 6]", "S"),
            ("w jaki sposób się zachowuje i co robi. [cite: 7]", "K")
        ]
    },
    {
        "q": "2. Co najczęściej zostaje ci w pamięci po kilku dniach od spotkania nieznanej ci wcześniej osoby? [cite: 8]",
        "options": [
            ("to, co robiliście razem, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz, [cite: 9]", "K"),
            ("jej imię/nazwisko, [cite: 10]", "S"),
            ("to, co czułeś, będąc w jej towarzystwie, nawet jeśli zapomniałeś jej imię/nazwisko lub twarz, [cite: 11]", "D"),
            ("jej twarz. [cite: 12]", "W")
        ]
    },
    {
        "q": "3. Gdy wchodzisz do nieznanego ci pomieszczenia, na co zwracasz przede wszystkim uwagę? [cite: 13]",
        "options": [
            ("na jego wygląd, [cite: 14]", "W"),
            ("na to, jak dobrze emocjonalnie i fizycznie się w nim czujesz, [cite: 15]", "D"),
            ("na to, co się w nim dzieje i co ty mógłbyś w nim robić, [cite: 16]", "K"),
            ("na dźwięki i rozmowy, jakie się w nim toczą. [cite: 17]", "S")
        ]
    },
    {
        "q": "4. Gdy uczysz się czegoś nowego, w jaki sposób robisz to najchętniej? [cite: 18]",
        "options": [
            ("gdy nauczyciel pozwala ci zapisywać informacje lub sporządzać rysunki, dotykać przedmiotów, pisać na klawiaturze lub robić coś rękami, [cite: 19]", "D"),
            ("gdy nauczyciel pozwala ci robić projekty, symulacje, eksperymenty, grać w gry, odgrywać role, odtwarzać rzeczywiste sytuacje z życia, dokonywać odkryć lub też angażować się w inne działania związane z ruchem, [cite: 20]", "K"),
            ("gdy nauczyciel daje ci coś do czytania na papierze lub tablicy, pokazuje ci książki, ilustracje, wykresy, mapy, szkice lub przedmioty, nie każąc ci przy tym niczego mówić, pisać, ani o niczym dyskutować, [cite: 21]", "W"),
            ("gdy nauczyciel wyjaśnia wszystko, mówiąc lub wygłaszając wykład, pozwala ci przedyskutować temat i zadawać pytania, nie każąc ci przy tym na nic patrzeć, niczego czytać, pisać ani robić. [cite: 22]", "S")
        ]
    },
    {
        "q": "5. Gdy uczysz czegoś innych, co zwykle robisz? [cite: 23]",
        "options": [
            ("objaśniasz wszystko werbalnie, nie pokazując żadnych materiałów graficznych, [cite: 24]", "S"),
            ("rysujesz coś, piszesz lub w inny sposób używasz rąk do wyjaśniania, [cite: 25]", "D"),
            ("demonstrujesz coś, robiąc to lub każesz uczniom robić to wspólnie z tobą, [cite: 26]", "K"),
            ("dajesz im coś do oglądania, na przykład jakiś przedmiot, ilustrację lub wykres, udzielając przy tym jedynie krótkiego werbalnego wyjaśnienia lub nie udzielając go wcale, dopuszczając lub nie do krótkiej dyskusji. [cite: 27]", "W")
        ]
    },
    {
        "q": "6. Jaki rodzaj książek czytasz najchętniej? [cite: 28]",
        "options": [
            ("książki zawierające informacje faktograficzne, historyczne lub dużo dialogów, [cite: 29]", "S"),
            ("krótkie książki z wartką akcją lub książki, które pomagają ci doskonalić umiejętności w sporcie, hobby czy też rozwijać jakiś talent, [cite: 30]", "K"),
            ("książki o uczuciach i emocjach bohaterów, poradniki, książki o emocjach i związkach międzyludzkich lub książki na temat tego, jak poprawić stan twojego ciała i umysłu, [cite: 31]", "D"),
            ("książki, które zawierają opisy pomagające ci zobaczyć to, co się dzieje. [cite: 32]", "W")
        ]
    },
    {
        "q": "7. Którą z poniższych czynności wykonujesz najchętniej w czasie wolnym? [cite: 33]",
        "options": [
            ("czytasz książkę lub przeglądasz czasopismo, [cite: 34]", "W"),
            ("słuchasz książki nagranej na kasetę, rozmowy w radiu, słuchasz muzyki lub sam muzykujesz, [cite: 35]", "S"),
            ("piszesz, rysujesz, piszesz na maszynie/komputerze lub robisz coś rękami, [cite: 36]", "D"),
            ("uprawiasz sport, budujesz coś lub grasz w grę wymagającą ruchu. [cite: 37]", "K")
        ]
    },
    {
        "q": "8. Które z poniższych stwierdzeń najlepiej charakteryzuje sposób, w jaki czytasz lub uczysz się? [cite: 38]",
        "options": [
            ("musisz czuć się wygodnie, rozluźniony; potrafisz pracować zarówno przy muzyce, jak i w ciszy, jednak dekoncentrują cię negatywne uczucia innych, [cite: 39]", "D"),
            ("musisz czuć się wygodnie, rozluźniony; potrafisz pracować zarówno przy muzyce, jak i w ciszy, jednak dekoncentruje cię działalność i ruchy innych osób znajdujących się w tym samym pomieszczeniu, [cite: 40]", "K"),
            ("potrafisz się uczyć, gdy słychać muzykę, inne dźwięki lub rozmowę, ponieważ umiesz się od nich odseparować, [cite: 41]", "W"),
            ("nie potrafisz się uczyć, gdy w twoim pobliżu słychać muzykę, inne dźwięki lub rozmowę, ponieważ nie umiesz się od nich odseparować. [cite: 42]", "S")
        ]
    },
    {
        "q": "9. Gdy z kimś rozmawiasz, gdzie kierujesz wzrok? [cite: 43]",
        "options": [
            ("spoglądasz jedynie krótko na rozmówcę, po czym twój wzrok wędruje na prawo i lewo, [cite: 44]", "S"),
            ("patrzysz na twarz rozmówcy, chcesz także, by ta osoba patrzyła na twoją twarz, gdy do niej mówisz, [cite: 45]", "W"),
            ("spoglądasz jedynie krótko na rozmówcę, by zobaczyć jego wyraz twarzy, po czym spoglądasz w dół lub w bok, [cite: 46]", "D"),
            ("rzadko spoglądasz na rozmówcę, patrzysz głównie w dół lub w bok, jeśli jednak pojawi się jakiś ruch lub działanie, natychmiast spoglądasz w tamtym kierunku. [cite: 47]", "K")
        ]
    },
    {
        "q": "10. Które z poniższych stwierdzeń najlepiej do ciebie pasuje? [cite: 48]",
        "options": [
            ("trudno ci wysiedzieć nieruchomo w jednym miejscu, potrzebujesz dużo ruchu, a jeśli już musisz siedzieć garbisz się, wiercisz, stukasz w podłogę butami lub często niespokojnie poruszasz nogami, [cite: 49]", "K"),
            ("zwracasz uwagę na kolory, kształty, wzory i desenie w miejscach, w których się znajdziesz; masz dobre oko do barw i kształtów, [cite: 50, 51]", "W"),
            ("nie znosisz ciszy i jeśli tam, gdzie akurat jesteś, jest za cicho, nucisz coś, podśpiewujesz lub głośno mówisz; włączasz radio, telewizor, magnetofon lub odtwarzacz CD, by w twoim otoczeniu były bodźce słuchowe, [cite: 52, 53]", "S"),
            ("jesteś wrażliwy na uczucia innych ludzi, twoje własne uczucia łatwo ulegają zranieniu; nie potrafisz się skoncentrować, gdy inni cię nie lubią, czujesz potrzebę bycia kochanym i akceptowanym, by pracować. [cite: 54, 55]", "D")
        ]
    },
    {
        "q": "11. Które z poniższych stwierdzeń najlepiej do ciebie pasuje? [cite: 56]",
        "options": [
            ("płaczesz podczas wzruszających scen w kinie lub czytając wzruszającą książkę, [cite: 57]", "D"),
            ("niepokoi cię, gdy ktoś nie potrafi dobrze się wysławiać, jesteś wrażliwy na odgłos kapiącego kranu lub odgłosy wydawane przez urządzenia gospodarstwa domowego, [cite: 58]", "S"),
            ("zwracasz uwagę na nieodpowiednie dopasowanie części garderoby danej osoby lub na to, że jej włosy są w nieładzie i często chcesz to naprawić, [cite: 59]", "W"),
            ("niepokoisz się i czujesz się nieprzyjemnie, gdy jesteś zmuszony siedzieć nieruchomo; nie potrafisz przebywać zbyt długo w jednym miejscu. [cite: 60, 61]", "K")
        ]
    },
    {
        "q": "12. Co wywołuje u ciebie największy niepokój? [cite: 62]",
        "options": [
            ("miejsce, w którym jest za cicho, [cite: 63]", "S"),
            ("miejsce, w którym nie czujesz się dobrze fizycznie lub emocjonalnie, [cite: 64]", "D"),
            ("miejsce, w którym nie wolno niczego robić lub jest za mało przestrzeni na ruch, [cite: 65]", "K"),
            ("miejsce, w którym panuje bałagan i nieład. [cite: 66]", "W")
        ]
    },
    {
        "q": "13. Czego najbardziej nie lubisz, podczas gdy ktoś cię uczy? [cite: 67]",
        "options": [
            ("patrzenia i słuchania w bezruchu, [cite: 68]", "K"),
            ("niemożności rysowania, gryzmolenia czegoś na kartce papieru, dotykania wszystkiego rękami lub sporządzania notatek, nawet jeśli nie będziesz już nigdy więcej z nich korzystał, [cite: 69, 70]", "D"),
            ("słuchania wykładu, na którym nie wykorzystuje się żadnych pomocy wizualnych, [cite: 71]", "W"),
            ("czytania po cichu, bez żadnych werbalnych wyjaśnień czy dyskusji. [cite: 72]", "S")
        ]
    },
    {
        "q": "14. Jakie wspomnienia utkwiły ci w pamięci z szczęśliwego momentu? [cite: 73, 74]",
        "options": [
            ("to, co słyszałeś, na przykład dialogi i rozmowy, to, co powiedziałeś, oraz dźwięki wokół ciebie, [cite: 75]", "S"),
            ("to, co widziałeś, na przykład wygląd ludzi, miejsc czy przedmiotów, [cite: 76]", "W"),
            ("to, co robiłeś, ruchy twojego ciała, twoje dokonania, [cite: 77]", "K"),
            ("wrażenia dotykowe na skórze i ciele, a także to, jak czułeś się fizycznie i emocjonalnie. [cite: 78]", "D")
        ]
    },
    {
        "q": "15. Jakie wspomnienia z urlopu lub wycieczki utkwiły ci w pamięci? [cite: 79, 80]",
        "options": [
            ("to, co robiłeś, ruchy twojego ciała, twoje dokonania, [cite: 81]", "K"),
            ("wrażenia dotykowe na skórze i ciele, a także to, jak czułeś się fizycznie i emocjonalnie, [cite: 82]", "D"),
            ("to, co słyszałeś, na przykład dialogi i rozmowy, to, co powiedziałeś, oraz dźwięki wokół ciebie, [cite: 83]", "S"),
            ("to, co widziałeś, na przykład wygląd ludzi, miejsc czy przedmiotów. [cite: 84]", "W")
        ]
    },
    {
        "q": "16. W którym z opisanych miejsc czułbyś się najlepiej? [cite: 85, 86]",
        "options": [
            ("miejsce, w którym możesz czytać; oglądać obrazy; rozwiązywać zagadki wizualne; grać w gry słowne; zajmować się dekorowaniem wnętrz, [cite: 87, 88, 89]", "W"),
            ("miejsce, w którym możesz rysować, malować, rzeźbić; tworzyć coś na piśmie lub pisać na komputerze; wykonywać czynności przy użyciu rąk, [cite: 90, 91]", "D"),
            ("miejsce, w którym możesz słuchać nagrań; grać na instrumencie lub śpiewać; bawić się głośno w gry słowne, rozprawiać o czymś, [cite: 92, 93, 94]", "S"),
            ("miejsce, w którym możesz uprawiać sport; odgrywać role; robić projekty ruchowe; robić eksperymenty, badać i odkrywać nowe rzeczy. [cite: 95, 96, 97]", "K")
        ]
    },
    {
        "q": "17. Gdybyś miał zapamiętać nowe słowo, zrobiłbyś to najlepiej: [cite: 98]",
        "options": [
            ("widząc je, [cite: 99]", "W"),
            ("słysząc je, [cite: 100]", "S"),
            ("zapisując je, [cite: 101]", "D"),
            ("odtwarzając to słowo w umyśle lub fizycznie. [cite: 102]", "K")
        ]
    }
]

with st.form("learning_styles_test"):
    all_responses = []
    
    for i, item in enumerate(pytania_data):
        st.subheader(item["q"])
        for label, code in item["options"]:
            # Wyświetlamy opcje jako checkboxy z adaptacyjnym tłem
            if st.checkbox(label, key=f"q_{i}_{label}"):
                all_responses.append(code)
        st.write("---")

    submit_button = st.form_submit_button("Oblicz wyniki [cite: 103]")

# Wyniki testu na podstawie punktacji [cite: 104-106]
if submit_button:
    if not all_responses:
        st.warning("Proszę zaznaczyć przynajmniej jedną odpowiedź.")
    else:
        scores = {
            "Wzrokowiec (W)": all_responses.count("W"),
            "Słuchowiec (S)": all_responses.count("S"),
            "Dotykowiec (D)": all_responses.count("D"),
            "Kinestetyk (K)": all_responses.count("K")
        }
        
        st.header("📊 Twoje Wyniki [cite: 103]")
        st.bar_chart(scores)
        
        max_score = max(scores.values())
        winners = [k for k, v in scores.items() if v == max_score]
        
        st.success(f"Twój dominujący styl uczenia się to: **{', '.join(winners)}**[cite: 105, 107]!")
        st.write("Wiesz już, jaki styl uczenia się dominuje u Ciebie. Teraz dowiedz się, co to właściwie oznacza! [cite: 108]")

# Stopka
st.markdown("---")
st.caption("Test do wersji cyfrowej przygotowany przez Aleksandrę Kopystyńską (pedagog specjalny) przy pomocy Gemini")
