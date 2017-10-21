# movistar_M3u (Español)
Código Python para generar automáticamente un fichero .m3u con los canales de Movistar+ en IPTV

- V0.1: Sólo genera archivo .m3u para clientes del País Vasco

**Importante**

- **Sólo válido en España y para clientes de Movistar+ vía IPTV**
- **Se recomienda conexión Ethernet**
- **_Sólo se verán canales contratados_**

## Pasos:
1. Descargar desde https://github.com/LuisPalacios/iptv2hts/tree/master/movistartv2xmltv los siguientes archivos:
   - get_xmls.py
   - tva.py
2. Descargar desde https://github.com/igorrecioh/movistar_M3u/ este archivo:
   - pruebas.py
3. Guardar esos 3 archivos en la misma carpeta
## Uso:
1. `sudo python get_xmls.py 239.0.2.168`
2. Espera hasta que termine el proceso
3. `sudo python pruebas.py`
4. Hecho! Tendrás en la misma carpeta un archivo llamado TVM_Eus.m3u

# movistar_M3u (English version)
Python code to automatically generate .m3u file with Movistar+ Spain IPTV channels

- V0.1: .m3u file generated includes channels for Basque Country 

**Importante**

- **Only available for Movistar+ IPTV clients in Spain**
- **Ethernet connection recommended**
- **_Only purchased channels will be available_**

## Steps:
1. Download from https://github.com/LuisPalacios/iptv2hts/tree/master/movistartv2xmltv these files:
   - get_xmls.py
   - tva.py
2. Download from https://github.com/igorrecioh/movistar_M3u/ this file:
   - pruebas.py
3. Save those 3 files in same folder
## Usage:
1. `sudo python get_xmls.py 239.0.2.168`
2. Wait until process finishes
3. `sudo python pruebas.py`
4. Done! You will get in same folder a file named TVM_Eus.m3u.
