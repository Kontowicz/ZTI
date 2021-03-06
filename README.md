### Temat
[OKE2018 CHALLENGE – ESWC 2018: Task4-Knowledge Extraction](https://project-hobbit.eu/challenges/oke2018-challenge-eswc-2018/tasks/)

Zadanie polega na wyodrębnieniu z dokumentów określonych bytów 
należących do jednej z klas (Task 1) oraz określenia relacji (Task 3) między nimi.

### Podział prac
Zadanie zostało rozdzielone między członków zespołu, aby każdy z modułów mógł być realizowany oddzielnie 
i niezależnie od innych, mimo że duża część pracy musiała być omawiana wspólnie lub wykonywana wspólnie ze względu na jej trudność:

##### Piotr Kontowicz - wczytywanie danych oraz parsowanie
Stworzenie modułu [`parse.py`](parse.py) odpowiedzialnego za przetworzenie plików `.ttl` w celu wyodrębnienia odpowiednich informacji. Zaproponowanie rozwiązania wykorzystywanego do szukania relacji pomiędzy bytami polegającego na sprawdzaniu dwóch sąsiadujących z sobą bytów oraz zależnie od tego sprawdzanie, czy w zdaniu występują słowa kluczowe wskazujące na wystąpienie między nimi relacji. Zaproponowano tutaj implementację wyszukiwania podobieńst kategorii opartą na synonimach, gdzie zostały one wstępnie ręcznie zaadnotowane w celu sprawdzenia działania i wpływu na wyniki ['dummy.py '](dummy.py).

##### Cezary Waligóra, Łukasz Żegalski - przetwarzanie języka naturalnego 
Stworzenie modułu [`entities_recognition_tester.py `](entities_recognition_tester.py) zawierającego w sobie implementację trzech rozwiązań dotyczących `NLP`, w celu 
sprawdzenia sposobu wykrywania bytów w zdaniu przez każdą z metod. Umożliwiło to wybór najbardziej adekwatnej metody, w celu uzyskania najlepszych wyników. Przeanalizowanie i próby wykorzystania wbudowanych funkcji `Spacy` do wyznaczenia słów, między którymi występują relacje poprzez analizowanie poddrzewa danego słowa oraz zależności najbliższego wspólnego przodka. Stworzenie dokumentacji na GitHub.

##### Bartosz Ptak, Mikołaj Walkowiak - komunikacja z DBpedią
Stworzenie modułu [`sparql_resource_property_getter.py`](sparql_resource_property_getter.py) zawierającego implementację funkcji niezbędnych do odpytywania DBpedi za pomocą `SPARQ` wykorzystywanych do wyszukiwania typów obiektów wykrytych przez `Spacy` bądź zamianę typów na odpowiadające im, bądź pokrewne z wykorzystaniem słownika [`dicts.py`](dicts.py). Moduł [`word_word_relation.py`](word_word_relation.py) posiada implementację funkcji wykorzystywanej do wyznaczania relacji między danymi słowami. Stworzenie modułów [`test_all.py`](test_all.py) oraz [`formatuj.py`](formatuj.py) odpowiadających odpowiednio za przeprowadzenie poprawności wykrywania bytów i relacji przez stworzony przez nas system (porównywanie otrzymanych trójek i ,,ground truth'' dla danego zdania) , oraz za wypisanie wyników predykcji naszego systemu, w odpowiedniej postaci - jakiej występują w plikach `.ttl` i są wymagane przez konkurs.

### Wykorzystane biblioteki:
* `nltk` - biblioteka zawierająca narzędzia do przetwarzania tekstu naturalnego, głównie skorzystano z: tokenizacji tekstu (`word_tokenize`), usuwania ,,stop words'' (`stopwords`), wyznaczenia rdzenia słowa (`PorterStemmer`) oraz interfejsu synonimów wordnet (`wordnet.synsets`)
* `SPARQLWrapper` - służąca do wykonywania zapytań SPARQ do bazy dbpedii oraz do formatowania rezultatu do formatu JSON 
* `spacy` - z którego korzystaliśmy z modelu językowego (`en_core_web_sm`), który służył do wyodrębnienia bytów z tekstu oraz określenia jego kategorii; użyto modułu `displacy` do wizualizacj zależności między słowami
* `string` - do manipulacji na ciagach znaków
* `itertools` - narzędzie do iteracji po kontenerach
* `re` - wyrażenia regularne

### Etap 1: 
  Polega na parsowaniu plików `.ttl` z wykorzystaniem wyrażeń regularnych. Ma za zadanie wyodrębnić z nich zdania [`parse_task_1_2`](https://github.com/Kontowicz/ZTI/blob/5b612d3f691ecb108a9573719f36bc209640c7f4/parse.py#L4), na których będzie operował cały system oraz poprawne odpowiedzi [`parse_odp`](https://github.com/Kontowicz/ZTI/blob/db2f2e96de258d8eb708d4504cc1546dfa1aab9f/parse.py#L28) wykorzystywane do analizowania poprawności systemu. Największym problemem był fakt, iż pliki `.ttl` nie miały jednej wspólnej struktury (np. zamiast nazwy obiektu, był link do niego). Skutkowało to niekiedy błędami w wyodrębnianiu istotnych informacji. 

### Etap 2: 
  Główną częścią etapu jest wyodrębnienie ze zdań bytów, dla których będzie się określać relacje. Po przetestowaniu trzech rozwiązań: `nltk`, `StanfordNERTagger`, `Spacy` wybrany został moduł `Spacy`, który najlepiej radził sobie z wyodrębnieniem obiektów składających się z więcej niż jednego słowa takich jak: Imię Nazwisko czy nazwy instytucji. Funkcja  [`process_using_spacy`](https://github.com/Kontowicz/ZTI/blob/5b612d3f691ecb108a9573719f36bc209640c7f4/entities_recognition_tester.py#L44) analizuje pojedyncze zdanie, zwracając listę krotek zawierających wykryty byt oraz klasę, do której przynależy. 

### Etap 3: 
  Polega na określeniu relacji między bytami wykorzystując wiedzę zawartą w DBpedi oraz typy bytów określone przez spacy.
  Etapy działania funkcji [`get_relation`](https://github.com/Kontowicz/ZTI/blob/5b612d3f691ecb108a9573719f36bc209640c7f4/word_word_relation.py#L14):
 1. wykonanie permutacji wszystkich bytów w zdaniu   
 2. usunięcie znaków interpunkcyjnych
 3. usunięcie stop words ze zdania
 4. sprawdzenie czy typ obiektu nie należy do ignorelist
 5. pobranie nowego typu obiektu z DPpedi jeśli występuje i zamiana dla danego słowa
 6. jeśli nie odnaleziona w DB skorzystać z typu spacy i zmapować 
 7. pobranie ze słownika relacji na podstawie typów obiektów (klucze)
 8. sprawdzenie czy w zdaniu występują morfologiczne słowa dla słowa danego obiektu, jeśli tak to dodaj (obiekt, obiekt, relacja) do listy

### Etap 4:
a. na podstawie jednego pliku moze zostać wygenerowny plik wyjściowy w odpowiednim formacie, wymaganym przez organizatorów konkursu
b. na podstawie wielu plików można przeprawadzić testy skuteczności działania systemu

### Testy:
Na końcu został wykonany test poprawności dla danego systemu polegający na określeniu dobrze oraz źle wykrytych relacji w stosunku do   wszystkich. Największym problem polegał na małych różnicach między słowami wykrytymi a poprawnymi odpowiedziami (the united states != united states, barack hussein obama != barack obama). Skutkowało to zaliczeniem analizy danego zdania jako niepoprawne, kolejnym przypadkiem skutkującym niepoprawną analizą   były sytuacje, gdzie w zdaniu występowały informację o osobie, kraju oraz mieście. Relacja występująca w zdaniu łączyła osobę z           miastem bądź z krajem zaś relacja wykryta przez system odwrotnie co skutkowało zaliczeniem danej analizy jako niepoprawnej, mimo że     była ona mniej, bądź bardziej szczegółowa  w stosunku do poprawnej odpowiedzi co skutkuje tym, że testy poprawności mogą być zaniżone.
 
