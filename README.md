### Temat
[OKE2018 CHALLENGE – ESWC 2018: Task4-Knowledge Extraction](https://project-hobbit.eu/challenges/oke2018-challenge-eswc-2018/tasks/)

Zadanie polega na wyodrębnieniu z dokumentów określonych bytów 
należących do jednej z klas (Task 1) oraz określenia relacji (Task 3) między nimi.

### Podział prac
Zadanie zostało rozdzielone między członków zespołu, aby każdy z modułów mógł być realizowany oddzielnie 
i niezależnie od innych:
  1) Piotr Kontowicz - wczytywanie danych oraz parsowanie
  2) Cezary Waligóra, Łukasz Żegalski - przetwarzanie języka naturalnego 
  3) Bartosz Ptak, Mikołaj Walkowiak - komunikacja z DBpedią

### Wykorzystane biblioteki:
* `nltk`
* `string`
* `itertools`
* `SPARQLWrapper`
* `spacy`
* `re`

### Etap 1: 
  Polega na parsowaniu plików `.ttl` z wykorzystaniem wyrażeń regularnych ma za zadanie wyodrębnić z nich zdania (`parse_task_1_2`), na których będzie operował cały system oraz poprawne odpowiedzi (`parse_odp`) wykorzystywane do analizowania poprawności systemu. Największym problemem był fakt, iż pliki `.ttl` nie miały jednej wspólnej struktury. Skutkowało to niekiedy błędami w wyodrębnianiu istotnych informacji. 

### Etap 2: 
  Główną częścią etapu jest wyodrębnienie ze zdań bytów, dla których będzie się określać relację. Po przetestowaniu trzech rozwiązań: `nltk`, `StanfordNERTagger`, `Spacy` wybrany został moduł `Spacy`, który najlepiej radził sobie z wyodrębnieniem obiektów składających się z więcej niż jednego słowa takich jak: Imię Nazwisko czy nazwy instytucji. Funkcja  `process_using_spacy` analizuje pojedyncze zdanie, zwracając listę krotek zawierających wykryty byt oraz klasę, do której przynależy. 

### Etap 3: 
  Polega na określeniu relacji między bytami wykorzystując wiedzę zawartą w DBpedi oraz typy bytów określone przez spacy.
  Etapy działania funkcji (get_relation):
 1. wykonanie permutacji wszystkich bytów w zdaniu   
 2. usunięcie znaków interpunkcyjnych
 3. usunięcie stop words ze zdania
 4. sprawdzenie czy typ obiektu nie należy do ignorelist
 5. pobranie nowego typu obiektu z DPpedi jeśli występuje i zamiana dla danego słowa
 6. jeśli nie odnaleziona w DB skorzystań z typu spacy i zamapować 
 7. pobranie ze słownika relacji na podstawie typów obiektów(klucze)
 8. sprawdzenie czy w zdaniu występują morfologiczne słowa dla słowa danego obiektu, jeśli tak to dodaj (obiekt, obiekt, relacja) do listy

### Testy:
  Na końcu została wykonany test poprawności dla danego systemu polegający na określeniu dobrze oraz źle wykrytych relacji w stosunku do wszystkich.
  Największym problem polegał na małych różnicach między słowami wykrytymi a poprawnymi odpowiedziami (the united states = united states),
  skutkowało to zaliczeniem analizy danego zdania jako niepoprawne, kolejnym przypadkiem skutkującym niepoprawną analizą były sytuacje 
  gdzie w zdaniu występowały informację o osobie, kraju oraz mieście. Relacja występująca w zdaniu łączyła osobę z miastem bądź z krajem zaś
  relacja wykryta przez system odwrotnie co skutkowało zaliczeniem danej analizy jako nie poprawnej mimo że była ona mniej bądź bardziej szczegółowa
  w stosunku do poprawnej co skutkuje tym że testy poprawności mogą być zaniżone.
 
