aby pobrać potrzebne nam narzędzia włączamy cmd
i wpisujemy 
pip install pyqt5 - aby pobrać pyqt5
oraz pip install pyqt5designer - aby pobrać qtdesigner

![Alt text](https://github.com/JaimeUnCroissant/Zadanie-2024_25_001/blob/main/Zrzut%20ekranu%20(187).png "pobranie")

następnie wpisujemy designer aby odpalić qtdesigner
potem dodaje przycisk i label i eksportuje plik ui

następnie do pliku python importuje moduł uic oraz qtWidgets z biblioteki 
PyQt5
 tworzymy klasę application i w konstruktorze w czytujemy ui za pomocą 
loadUi podłączamy metodę increment do przycisku a końcowo pokazujemy i 
odpalamy aplikacje za pomocą show() oraz .exec() na kocu tworzymy aplikacje
którą przekazujemy jako argument do stworzenia naszej klasy application

![Alt text](https://github.com/JaimeUnCroissant/Zadanie-2024_25_001/blob/main/Zrzut%20ekranu%20(189).png "uzycie")

