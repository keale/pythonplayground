import socket
import struct
import time

def receive_integers(host='localhost', port=6340):
    """
    Stellt eine TCP-Verbindung zu dem angegebenen Host und Port her
    und liest eine Folge von 32-Bit Integer-Werten. Nach einem Verbindungsabbruch
    versucht das Skript erneut zu verbinden.
    
    :param host: Hostname oder IP-Adresse zum Verbinden (Standard: 'localhost')
    :param port: Portnummer zum Verbinden (Standard: 6340)
    """
    BUFFER_SIZE = 4  # Anzahl der Bytes, die auf einmal gelesen werden
    INT32_SIZE = 4      # Größe eines 32-Bit Integer-Werts in Bytes
    RECONNECT_DELAY = 1  # Wartezeit (in Sekunden) vor einem Reconnect-Versuch

    while True:  # Endlos-Schleife für die Verbindung
        try:
            print(f"Versuche, Verbindung zu {host}:{port} herzustellen...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                print(f"Verbunden zu {host}:{port}")

                data_buffer = b''  # Puffer zum Speichern unvollständiger Daten

                while True:
                    # Empfange Daten vom Socket
                    data = sock.recv(BUFFER_SIZE)
                    if not data:
                        print("Verbindung geschlossen vom Server.")
                        break

                    data_buffer += data

                    # Verarbeite alle vollständigen Integer-Werte im Puffer
                    while len(data_buffer) >= INT32_SIZE:
                        # Extrahiere die ersten 4 Bytes
                        int_bytes = data_buffer[:INT32_SIZE]
                        data_buffer = data_buffer[INT32_SIZE:]

                        # Unpacken der Bytes in einen 32-Bit Integer-Wert
                        # Annahme: Netzwerk-Byte-Reihenfolge (Big Endian).
                        int_value = struct.unpack('!i', int_bytes)[0]
                        print(f"Empfangener 32-Bit Integer-Wert: {int_value}")

        except ConnectionRefusedError:
            print(f"Verbindung zu {host}:{port} wurde verweigert.")
        except socket.error as e:
            print(f"Socket-Fehler: {e}")
        except struct.error as e:
            print(f"Fehler beim Entpacken der Daten: {e}")
        except KeyboardInterrupt:
            print("\nVerbindung beendet vom Benutzer.")
            break
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

        # Warte vor einem erneuten Verbindungsversuch
        print(f"Erneuter Verbindungsversuch in {RECONNECT_DELAY} Sekunden...")
        time.sleep(RECONNECT_DELAY)

if __name__ == "__main__":
    receive_integers()
