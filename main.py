import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy_garden.mapview import MapView, MapMarker, MapSource
from plyer import gps
from math import radians, cos, sin, asin, sqrt

kivy.require("2.1.0")


class GPSBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.gps_started = False
        self.last_lat = None
        self.last_lon = None
        self.total_area = 0.0
        self.track_points = []

        # Mapa satelital (centro inicial aproximado)
        self.map = MapView(
            zoom=16,
            lat=-36.233,
            lon=-61.120,
            map_source=MapSource(
                url="https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                attribution="© Google"
            ),
        )
        self.add_widget(self.map)

        # Botonera inferior
        btns = BoxLayout(size_hint_y=None, height="50dp")
        self.btn_start = Button(text="Iniciar", background_color=(0, 1, 0, 1))
        self.btn_stop = Button(text="Detener", background_color=(1, 0, 0, 1))
        self.btn_center = Button(text="Centrar", background_color=(0, 0, 1, 1))

        btns.add_widget(self.btn_start)
        btns.add_widget(self.btn_stop)
        btns.add_widget(self.btn_center)
        self.add_widget(btns)

        self.btn_start.bind(on_press=self.start_gps)
        self.btn_stop.bind(on_press=self.stop_gps)
        self.btn_center.bind(on_press=self.center_map)

        # Configurar GPS (plyer)
        try:
            gps.configure(on_location=self.on_location, on_status=self.on_status)
        except NotImplementedError:
            print("GPS no disponible en este dispositivo.")

    def start_gps(self, *args):
        if not self.gps_started:
            try:
                # minTime en ms, minDistance en metros
                gps.start(minTime=1000, minDistance=1)
                self.gps_started = True
                print("GPS iniciado")
            except Exception as e:
                print(f"Error iniciando GPS: {e}")

    def stop_gps(self, *args):
        if self.gps_started:
            try:
                gps.stop()
            except Exception as e:
                print(f"Error deteniendo GPS: {e}")
            self.gps_started = False
            print("GPS detenido")

    def center_map(self, *args):
        if self.last_lat is not None and self.last_lon is not None:
            self.map.center_on(self.last_lat, self.last_lon)

    def on_location(self, **kwargs):
        lat = kwargs.get("lat")
        lon = kwargs.get("lon")
        if lat is None or lon is None:
            return

        print(f"Nueva ubicación: {lat}, {lon}")
        self.last_lat, self.last_lon = lat, lon

        # Marcador en la posición actual
        marker = MapMarker(lat=lat, lon=lon)
        self.map.add_marker(marker)

        # Guardar punto para cálculo de distancia/superficie
        self.track_points.append((lat, lon))
        if len(self.track_points) > 1:
            self.total_area = self.calculate_area()
            print(f"Hectáreas (ancho 20 m): {self.total_area:.2f}")

    def on_status(self, stype, status):
        print(f"Estado GPS: {stype} = {status}")

    def calculate_area(self):
        """
        Calcula área muy aproximada:
        - Suma de distancias entre puntos consecutivos
        - Multiplicado por un ancho fijo (20 m)
        - Pasado a hectáreas
        """
        total_dist = 0.0
        for i in range(1, len(self.track_points)):
            lat1, lon1 = self.track_points[i - 1]
            lat2, lon2 = self.track_points[i]
            total_dist += self.haversine(lat1, lon1, lat2, lon2)

        ancho_trabajo = 20.0  # metros (podemos hacerlo configurable después)
        area_m2 = total_dist * ancho_trabajo
        return area_m2 / 10000.0  # hectáreas

    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        """
        Distancia en metros entre dos coordenadas GPS.
        """
        R = 6371000.0
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        )
        c = 2 * asin(sqrt(a))
        return R * c


class ElMarianoApp(App):
    def build(self):
        return GPSBox()


if __name__ == "__main__":
    ElMarianoApp().run()
