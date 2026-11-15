# GrayScottModelSimulation
Simulation des Gray Scott Models in Python<br>
<br>
![image01](/images/01.png)
![image01](/images/02.png)
![image01](/images/03.png)
![image01](/images/04.png)

Das Model beschreibt das Verhalten zweier Substanzen U und V. Dabei reagiert U zu V. <br>
Das Verhalten beider Stoffe kann durch zwei Gleichungen angegeben werden, die die jeweilige Änderungsrate der Stoffe beschreibt: <br>
![equation](/images/equation.jpg)
<br>
Implementiert ist die Simulation auf zwei numpy Arrays. Jeden Simulationsschritt wird die Änderungsrate für die Substrate errechnet und auf das entsprechende Array addiert.<br>
Verschiedene Parameter können die Reaktionsgeschwindigkeit und -charakteristiken verändern: *f* gibt die Feed-Rate an, wie schnell das Substrat U sich wieder regeneriert, *k* gibt die Kill-rate an, wie schnell der entstandene Stoff V wieder verschwindet. <br>
Durch Anpassung dieser Parameter können auf ganz natürliche Weise spannende Muster entstehen. Wie oben in den Bildern gezeigt, entstehen Labyrinth-, Zebra- oder andere Muster.
