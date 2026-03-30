Voor deze code is een specifieke mappen sturctuur nodig op een usb-stick. Deze usb-stick moet in de D-port en in de usb-stick moet een mapje project zitten. 
In het mapje project moeten geindiceerde mapjes zitten voor de metingen; 0 = de nulmeten en 1 > is voor de verdere metingen. 
In deze mapjes moet een letter voor een grid staan; A voor de eerste grid, B voor de 2de grid exc. Deze code is gelimiteerd tot 26 grids.

Hieruit volgt dat de directories in de code er alsvolgd uitzien:
"D:\project\{map}\{grid[0]}\meting_{grid[1]}.wav"
map = de aangegeven meting gevraagd als input
grid = de letter en daaraan de hoeveelste meting op deze grid gevraagd als input

Voor eigen gebruik van de code zullen de directories voor de excel documenten aangepast moeten wordeen.

voor gebruik van de code kan de hele code in 1 keer gerunt worden. Hierbij zal eerst gevraagd worden voor welke meting gedaan wordt.
Hierna zal de code vragen voor de grid. Hierbij is het belangrijk dat de code hierbij vraagt naar de grid EN de hoeveelste meting die gedaan wordt in de grid.
mochten files hier al voor bestaan zal gevraagd worden of ze overgeschreven mogen worden. Druk hierbij op enter om de files te overschrijven.
Wanneer de code is rerunt zal het het resultaat in een excel zetten voor verder gebruik en daarbij wat checks printen om de resultaten te kunnen verifieren na de meting.
