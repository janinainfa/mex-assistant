<div align="center">
    <h1>Mex Assistant</h1>
</div>

Mex Assistant to prosty asystent głosowy stworzony przy użyciu Pythona i Qt5.

## Uruchamianie
Żeby Mex mógł sterować muzyką, musisz mieć zainstalowane [Playerctl](https://github.com/altdesktop/playerctl).
### Instalacja
Pobierz najnowsze wydanie z [Github Releases](https://github.com/janinainfa/mex-assistant/releases/latest). Zainstaluj je przy użyciu swojego menedżera pakietów lub w terminalu używając `sudo apt install /ścieżka/do/pliku`, np. jeśli pobrałeś plik do `~/Pobrane`, `sudo apt install ~/Pobrane/mexassistant.deb`.

### Uruchamianie z kodu źródłowego
Uruchom terminal w miejscu, gdzie zamierzasz pobrać kod i wpisz poniższe komendy
```bash
git clone https://github.com/janinainfa/mex-assistant
cd mex-assistant
pip install -r requirements.txt
python3 main.py
```
## Własne komendy
Możesz tworzyć własne komendy przy użyciu ustawień (Plik > Ustawienia) lub edytując plik konfiguracyjny, który znajduje się w folderze`~/mexassistant`.
Każda komenda ma swoją nazwę, która po powiedzeniu do asystenta ją aktywuje, oraz typ, który decyduje czy komenda jest wykonywana jako skrypt powłoki czy skrypt Pythona.
Jeśli "przypadkiem" usuniesz w ustawieniach wszystkie komendy lub chcesz je zresetować do domyślnych, usuń plik konfiguracyjny (`~/mexassistant/config.ini`), następnie uruchom program ponownie.
